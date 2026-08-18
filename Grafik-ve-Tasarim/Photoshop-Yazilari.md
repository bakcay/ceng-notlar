# Photoshop Yazilari

## Temmuz 2001

## **PHOTOSHOP VE WEB GRAFİKLERİ******

*Bu ayki konularımızı tek cümle ile özetleyecek olursak; "web grafiklerine yönelik çalışmalarımızın yönetilmesi, isteğe uygun hale getirilmesi için gerekli araçların/ayarların anlatımı ve uygulaması" demek doğru olur. Dökümanlarımızın boyutlarını küçültmek, büyütmek; paspartu oluşturmak; işe yaramaz bölümleri atmak, geri almak gibi işlevler Photoshop'un olmazsa olmazlarındandır. Her Photoshop kullanıcısı tarafından program ne amaçla kullanılıyor olursa olsun bilinmesi gerekir. Ayrıca Photoshop 6'da tamamen değiştirilmiş araçları terfi edenlerin kullanabilmesi için tanıyacağız.*

IMAGE
Photoshop 6 ile "Image" altındaki "Adjust" menüsüne "Gradient Map" adlı yeni bir komut eklendiğini görüyoruz. Gradient, bildiğiniz üzere bir rengin diğer bir renge dönüşmesi esnasında oluşan renk geçişine deniyordu. Gradient Tool (kısayol tuşu "G") seçilmiş alanları veya katmanları renk geçişleri ile boyamamızı sağlayan bir araçtı. Vektörel bir araçtır. Illustrator'un başrol oyuncularındandır. Kısaca gradient'i hatırladıktan sonra bir de resimlerdeki palet mantığını hatırlayalım ve her iki konuyu birleştirip "Gradient Map" komutunu tanımlayalım.
16-24-32-48-64 bit renk derinliğine sahip grafik formatları henüz yokken maksimum 256 renkli grafikler üretip kullanabiliyorduk PC'lerimizde... 16 renkli ve 256 renkli grafikler çizerken renk paletimiz sınırlıydı, ancak kullanacağımız renkleri seçerdik. Fotoğraflarımızı ise bilgisayar ortamına aktarırken renk sayısı 256'ya düşürülürdü ve bu da doğal olarak renk kaybına neden olurdu. Birlikte aşağıdaki örneğimizi inceleyelim ve uzun zamandır kullanmadığımız, belki bazılarının hiç tanışmadığı paletimizi inceleyelim.
Şekildeki paletimizden herhangi bir rengi palet üzerinde değiştirirsek resim içindeki tüm o renkler otomatik olarak değişecektir. Aşağıdaki resimde bunun örneğini görebilirsiniz. Bu işlem 256 renkten yüksek renk derinliğine sahip grafik dosyalarında uygulanamıyor çünkü 256 renk üstü grafiklerin paleti sanal bir palettir. Ancak bu işlemin benzerini Image > Adjust > Replace Color seçeneği ile yapabildiğimizi hatırlarsınız.
Gradient Map'ın işlevine gelecek olursak; program, grafik dosyanızın renk derinliği ne olursa olsun sanal bir palet yaratır, bu paletteki renkleri açıktan koyuya doğru sıralar, ve gradient renk geçiş işlemini paletteki renklere uygular. Böylece grafiğimiz gradient'in sahip olduğu renklere bürünür. Bu komut gelmeden önce de bu işlemi yapabiliyorduk çeşitli yollar ile. Grafiğimizi "desaturate" komutu ile siyah-beyaz hale getirip "hue and saturation" ile renk verebiliyorduk. Ancak bu işlemde koyu bölgelerin az etkilenmesi nedeni ile istenilen etki elde edilemiyordu.
Bir diğer yöntem renk sayısını 256'ya düşürüp palet renklerini varolan seçeneklerden seçerek değiştirmek... Bu belki rastladığınız, bildiğiniz bir uygulama. Grafiğimizi "desaturate" komutu ile siyah-beyaz hale getiriyoruz, renk sayısını Image > Mode > Indexed Color ile 256'ya indiriyoruz. Image > Mode > Color Table penceresini açıp "table" bölmünde çıkan seçenekleri deneyerek ihtiyacımıza en uygun olanı kullanıyoruz. Hatta "black body" seçeneği seçerek alevler ve patlama efektleri oluşturabiliriz. Bu uygulamayı da yeri gelmişken yapalım:
o 400x400 renk derinliğine sahip bir döküman açalım. Fırça rengi bölümünde zemin rengini beyaz, fırça ucu rengini koyu gri yapalım. Filter > Render > Clouds seçeneği ile gri-beyaz bulutlar yaratalım.
o 2 kere Filter > Render > Difference Clouds komutunu uygulayalım ki bulutlarımız açık renk ama sık dokulu olsun.

o Image > Mode > RGB seçili değil ise seçelim. Image > Adjust > Desaturate siyah-beyaz hale getirelim. Görüntüde bir değişim olmayacaktır ama bu komut ile sanal paletimiz düzenlenir.

o Image > Mode > Indexed Color ile grafiğimizin renk sayısını 256'ya indirip reel bir palet sahibi olmasını sağlayalım. Hemen ardından Image > Mode > Color Table penceresini açıp "table" bölümünden "Black Body" seçeneğini seçelim. Image > Mode > RGB Color ile tekrar RGB'ye çevirip çalışmamızı izleyelim.
Bu uygulamada zemini kaplayan bir grafik ile değil de duman benzeri bir obje ile çalışsaydık, dumanımız bir aleve dönüşebilirdi. Palet üzerinde değişiklikler ile yapılan uygulamalardan biriydi bu.
Image menüsünün "adjust" ve "mode" seçeneklerini iki yazı önce anlatmıştık. Yeni eklenen komutu da öğrendikten sonra geriye kalanlara geçelim...

DUPLICATE
Bir döküman üzerinde çalışırken geri dönülmez bir işlemi uygulayacağız... Hemen "duplicate" komutu ile dökümanın bir kopyasını çıkarıyoruz ve işlemi onun üzerinde gerçekleştiriyoruz. Bir diğer amaç da farklı iki işlemi aynı grafiğe uygulayıp karşılaştırmaktır. "Duplicate" ile bir grafiğin kopyasını aldığınızda yeni açılan grafikte history bilgisi bulunmaz; yeni "load" edilmiş gibidir. Komutu uygularken açılan penceredeki "Duplicate Merged Layers Only" seçeneği seçili olursa sonuç grafiğin tüm katmanlarını şeffaflık bilgisini korunarak birleştirilir, tek katman olarak sunulur.
IMAGE SIZE
Dökümanımızın en ve boyunun ölçüsünü değiştirdiğimiz komuttur.

o Pixel Dimensions: Boyutları değiştirmek için gerekli ölçüleri bu kutuda giriyoruz. En üstte yazan rakam dökümanın hafızada kapladığı miktarı KB/MB/GB cinsinden verir. Rakamlarda değişiklik yaptığımızda normalde varolan değerin yanına parantez içinde başka bir değer eklenir. İlk değer verilen ayarlara göre hafızada kapladığı yer; parantez içindeki ise değişim olmadan önceki kapladığı yerdir. Aynı zamanda PSD dosyası olarak kaydettiğimizde dosyanın kaplayacağı yer olarak da düşünebiliriz. Adobe'un yardım dosyasındaki açıklamaya göre Photoshop 6 maksimum 30,000X30,000 boyutlarında ve maksimum 2GB'lik dökümanlar yaratmaya izin veriyor.

o Width: Dökümanın pixel cinsinden genişliğini girdiğimiz yerdir. Sağ tarafında bulunan pulldown menü ile girilecek rakamın birimi seçilir. İstersek 1024 gibi kesin bir ölçü gireriz "pixel" birimini seçip, istersek %20 gibi bir değer gireriz "percent" birimini seçerek. "Percent" ile değer girdiğimizde dökümanın önceki boyutu alınır, girdiğiniz değerle çarpılıp yüze bölünür. Klasik bir yüzde hesabı diyebiliriz.

o Height: Yükseklik / Boy anlamındadır. Özellikleri aynı "width" gibidir.

"Width" ve "Heigth" en sağında zincire benzer bir sembol bulunmaktadır. Bu sembol aşağıdaki "Constrain Proportions" ayar kutusu ile yönetilir. Şekilden tahmin edebileceğimiz gibi gösterdiği ayarlar birbirine bağlı (linked) anlamına gelir. Yani bir ayarı değiştirince belirli bir orana göre bağlı olan diğer ayar değişir.

o Document Size: Bu bölümde gireceğimiz en ve boy ölçüsü percent (yüzde), inch (inç), cm, points (pixel), picas ve column birimlerinde olabiliyor. Ayrıca çözünürlüğü de "Resolution" bölümünden belirleyebiliyoruz.

o Constrain Proportions: Eğer bu özellik seçili ise en ve boy ölçülerini birbirine bağlar. Birinin değişimi dökümanın en-boy oranına göre diğerinin değişmesine neden olur. Örneğin 800x600 boyutlarında bir grafik üzerinde çalışmaktayız ve genişliği 200 yapmak istiyoruz. 800/600 = 1,333333 eder. Bu grafiğimizin en-boy oranıdır. Aspect Ratio'da denir. Boyut değişikliği için komutu seçtiğimizde "Constrain Proportions" seçeneğini seçip genişliği 200 yazdığımızda 1,3333 oranına göre yüksekliğin 150 olması gerektiği otomatik hesaplanır.

o Resample Image: Dökümanın en ve boyunu büyütürken program bazı pixelleri yoktan var etmesi gerekir. Bu vâretme sırasında kullandığı algoritmanın hızı ve oluşacak kaliteyi pencerenin alt bölümündeki bu ayarlar ile belirleyebiliriz. "Bicubic" en yavaş ama en kaliteli; "Nearest Neighbour" en hızlı ama en kalitesiz yöntemdir. Eğer "Resample Image" seçeneği seçili değilse program boyut değişimi esnasında gerçekçiliği korumak için özel bir yöntem kullanmaz.
Not: Adobe Photoshop 6'da bu iş için bir de sihirbaz bulunuyor. "Help" menüsünden "Resize Image" olarak bulabilirsiniz.

CANVAS SIZE
Canvas'ın türkçe karşılığı tuvaldir. Photo-shop'da, çalıştığımız dökümanın boyutlarını değiştirmeyi sağlar. Ancak "Image Size" komutundan farklı olarak çalışma içerisindeki grafiğin ölçülerini değiştirmez. Grafiği sabit tutarak dışardan ekstra alan eklemeyi veya eksiltmeyi sağlar diyebiliriz.

o Current Size: Değişim uygulanmadan önceki en boy ve hafızada işgal ettiği yer bu bölümde görüntülenir.

o New Size: Grafiğin sahip olmasını istediğiniz yeni en-boy ölçülerini bu bölümde giriyoruz. Bu ölçüler önceki en-boy değerlerinden büyük de olabilir küçük de... Eğer küçük değer girilecekse, Photoshop, grafiğin bir bölümünü yitireceğimizi anlatan bir uyarı verir. Yine "New Size" satırındaki rakamdan dosyanın yeni halinin hafızada ne kadar yer kaplayacağını görebiliriz.

o Anchor: Grafiğimizin boyutunu değiştirirken varolan çalışmayı, yeni boyutların hangi bölümüne yerleştireceğimizi ayarladığımız bölümdür. Aşağıdaki resimleri inceleyerek daha iyi anlayabiliriz.

ROTATE CANVAS
Kısaca tuvalimizi döndürmeye yaradığını söyleyebiliriz. Transform > Rotate'den farklı olarak dökümanımızın en ve boy ölçüleri değişir; katmana veya seçili alana değil, tüm dökümana etki eder.
180?: Dökümanı 180 derece çevirir.
90? CW: Dökümanı "clockwise" yani saat yönünde 90 derece çevirir.
90? CCW: Dökümanı "counterclockwise" yani saat yönünün tersinde 90 derece çevirir.

o Arbitrary: Dökümanı sizin belirleyebileceğiniz bir açıda saat yönünde veya saat yönünün tersinde çevirebilir.
o Flip Horizontal: Dökümanın sağı soluna gelecek şekilde yansımasını alır.
o Flip Vertical: Dökümanın üstü altına gelecek şekilde yansımasını alır.
CROP
Seçili bir alanı alıp dökümanın geri kalanını atar. "Tools" paletindeki "Crop Tool" ile aynı işlemi yapar. Bu komutu önceki yazımızda ayrıntılı olarak anlatmıştık.

TRIM
Bir çeşit crop komutudur. İşlemi biraz daha otomatikleştirip, yükümüzü azaltıyor. Komutu seçtiğimizde grafiğimizi inceliyor ve boyalı/çizili olan (şeffaf olmayan) bölgeyi içine alabilecek minimum boyutta bir dikdörtgen oluşturup crop komutunu uyguluyor.
Daha basit bir anlatımla; koskoca bir dökümanın ortasına bir şekil çizip trim komutunu uygularsanız sadece şekli alıp geri kalanı çöpe atıyor. Örnek resmi inceleyerek daha iyi anlayabiliriz.
REVEAL ALL
Crop aracı ile gizlenen bölgeleri geri getirmek için yaratılmış bir komuttur.
HISTOGRAM
Grafiğimizde hangi tonlardaki pixellerin kaçar tane varolduğunu merak edersek veya belirli bir değerde tonların hakim olduğu çalışmalar yapacaksak bu göstergeyi izlemeliyiz. Limunosity (siyahtan beyaza), red (siyahtan kırmızıya), green (siyahtan yeşile), blue (siyahtan maviye) renk diyaglamlarından birini seçerek tonlara yığılan pixel miktarlarını görebilirsiniz. Örneğin aşağıdaki örnekte aynı resmin iki farklı tonla oluşturulmuşu ve histogramları var. Bir resim açık gri tonlar ile, bir resim koyu gri tonlar ile... Histogramları inceleyiniz...
TRAP
CMYK modunda, basım işleri için Photoshop kullananlar basım esnasında renklerdeki küçük dağılmaları engellemek için bu komutu kullanırlar. RGB modda iken bu komutu deneyemeyiz. CMYK'ya geçmeniz gereklidir, deneme yapmak isteyenlere duyurulur. Aşağıdaki örnek resmi de inceleyebilirsiniz.
OBJE SEÇİMİ VE EXTRACT
Bazen grafikler veya fotoğraflar içerisindeki objeleri başka çalışmalarımızda kullanmamız gerekir. Kendi fotoğrafınızdaki zemini değiştirmek için; sitesini yaptığınız bir firmanın logosunu başka bir grafikten bir diğerine alabilmek için ve bunlar gibi... Bu kes-çıkar işlemi için dört yöntem var:
o Kesmek istediğimiz resme "navigator" veya "zoom tool" ile iyice yaklaşıp "Polygon Lasso Tool" ile objenin kenarlarından çizeriz. Şekil tamamlandıktan sonra oluşan seçim alanı bize objemizi istediğimiz dökümana veya katmana copy/paste yapma şansını verir. Ancak bu yöntem ile saç ve benzeri detaylı alanlarda çalışmak; bol bol eğrilerden, elipslerden veya dairelerden oluşan cisimleri kesmek zahmetlidir.
o Bir önceki yöntemdeki gibi ancak bu defa "Path" araçlarını kullanarak objenin etrafından çizebiliriz. Path'in eğri oluşturmaya olanak tanıyan özelliği bize büyük rahatlık sağlar ancak kullanımı zordur, istediğiniz eğriyi elde edebilmek için path çiziminde deneyimli olmanız gerekir. Path tamamlandıktan sonra farenin sağ tuşuna tıklanır ve açılan menüden "Make Selection" seçilir. Böylece obje kesmeye hazır olur. Ancak bu yöntemde de saç gibi ayrıntılı ve uçlara doğru incelip bazı bölgelerde şeffafmış gibi görünen objelerin kesimi zordur, başarılsa bile gerçekçi olmaz.
o Eğer zemin rengi ile objenin rengi birbirinden çok farklı ve aynı rengin tonlarında ise Select > Color Range komutu başarılı olabilir. Fotoğrafınız; piknik alanı, kafe, cadde gibi renk cümbüşü ortamlarda değil de tek renkli bir perdenin önünde çekilmiş olmalıdır. Komutu seçeriz, zemin rengini grafiğimizin içerisinden seçip tolerans ayarlarını yaparız. Fuzzy ayarı ne kadar yüksek ise komut seçtiğimiz rengin o kadar farklı tonunu dahil eder; ne kadar düşük ise o kadar az renk sayısında ve küçük bölgelerde seçim yapar. Komut onaylandıktan sonra seçim aracımızın belirli bir bölgeyi seçtiğini görebiliriz. Ancak bu komut diğerlerinden farklı işler. Tıkladığımız noktadan dışa doğru açılmayıp tüm dökümandaki renkleri analiz eder ve seçer. Örneğin mavi perde önünde çekilmiş bir vesikalık fotoğrafınızın zeminini seçmek için bu komutu kullanan mavi gözlü arkadaşlar farkedecektirler ki gözleri de seçime dahil ediliyor. Göz ile mavi perde arasında uzaklık ne olursa olsun, arada cisim olsun olmasın benzer tonlar seçime dahil edilir. Gerçi bu durumdan da sıyrılabilir dikkatli okuyucularımız. Önceki aylarda ALT tuşu ve seçim araçlarından birini birlikte kullanacak olursak seçim silmiş olacağımızı anlatmıştık. Seçime dahil olan göz bölgesine gelip ALT tuşu ile her gözün olduğu yere birer elips seçim uygulayacak olursak gözler seçimden çıkarılmış olur. ALT tuşu ile ALT-GR tuşunun karıştırışmaması gerektiğini tekrar hatırlayalım.

o Son yöntemimiz ise Photoshop 5'den itibaren imdadımıza koşan ve büyük zaman kayıplarından bizi kurtaran "Extract" komutu...
Image menüsünde bulabileceğimiz bu komutu seçince ek bir pencere açılıyor. Solda çizim elemanları olan, orta bölümün çizime ayrıldığı, sağda yine farklı bir menüsü olan korkutucu bir pencere bu... Ama kullanımı çok basit.

Önce Edge Highlighter Tool (kısayol tuşu "B") ile objemizin kenarlarını "üstünkörü" çiziyoruz. Ardından Fill Tool (kısayol tuşu "G") ile kalacak olan objemizin içini boyuyoruz.
Boyadığımız fırçanın boyutu, rengi ve benzeri önemsiz özellikler sağdaki menüden ayarlanabiliniyor. Eğer "Edge Highlighter Tool" ile boyadığımız bölgelerde aslında cisimde varolmayan ama ışığın meydana getirdiği yoğun aydınlanmalar var ise "Smart Highlighting" seçeneğini seçiyoruz; böylece program cismin aslında nasıl olduğunu bir nebze daha iyi anlıyor. İşlem tamamlanınca "Preview" tuşu ile ön izlemesi yapılabiliyor veya "OK" tuşu ile hemen uygulanabiliyor. Bu aracı tüm grafiğe uygulayabildiğimiz gibi belirli bir seçili alana da uygulayabiliyoruz. Büyük kolaylık...
LIQUIFY
PowerGOO isimli bir surat deforme etme programı vardı hatırlar mısınız bilmiyorum. Kulak, göz, burun, kaş vb. büyütme-küçültme gibi işlemleri yapmak suretiyle komik yüzler elde ederdik. Adobe, bu programı kıskanmış olacak ki hemen bir benzerini Photoshop 6'ya dahil etmiş. 9 farklı araç ile ilginç efektler oluşturabiliyoruz. Özellikle insan yüzlerinde denemelisiniz...

a. Warp Tool: Faremizin sol tuşuna basılı tuttuğumuz sürece, hareket ettiğimiz yönde, fırçanın dahilindeki pixelleri sürükler.
b. Twirl Clockwise Tool: Faremizin sol tuşuna basılı tuttuğumuz ve hareket ettirdiğimiz sürece fırça dahilindeki pixelleri saat yönünde döndürür, girdap oluşturur.
c. Twirl Counterclockwise Tool: Bir önceki komut ile aynıdır ancak saat yönünün tersine girdap oluşturur.

d. Pucker Tool: Faremizin sol tuşuna basılı tuttuğumuz ve hareket ettirdiğimiz sürece fırça dahilindeki pixelleri dışarıdan içeriye doğru toplar.

e. Bloat Tool: Faremizin sol tuşuna basılı tuttuğumuz ve hareket ettirdiğimiz sürece fırça dahilindeki pixelleri içeriden dışarıya doğru dağıtır.
f. Shift Pixels Tool: Faremizin sol tuşuna basılı tuttuğumuz sürece, hareket ettirdiğimiz yönde, fırçanın dahilindeki pixelleri karıştırarak sürükler. Alt tuşu ile birlikte kullanılırsa yapılan fare hareketinin zıttını baz alarak işlemi gerçekleştirir.

g. Reflection Tool: Faremizin sol tuşuna basılı tuttuğumuz sürece uygulanan bölgenin yansımasını alır. Alt tuşu yine yön vektörünü tersine çevirir.
h. Reconstruct Tool: Undo / History aracı gibidir. Faremizin sol tuşuna basılı tuttuğumuz ve hareket ettirdiğimiz sürece fırça dahilindeki önceden uygulanmış deformasyonları düzeltir.

i. Freeze Tool: Kalkan oluşturmayı sağlayan bir araçtır. Bu araç ile işaretlenen bölgeler yukarıdaki araçlar tarafından deformasyona uğratılamazlar. Koruma sağlar. Ancak fırçanın yoğunluğuna göre kalkanın gücü değişir. Mask mantığını bilenler rahatça anlayabilecektirler.
j. Thaw Tool: "Freeze Tool" ile oluşturulan kalkanı yokeder.

a. Tool Options: Bu bölümde fırça ucunun boyutu (brush size) ve aracın etki yoğunluğu (brush pressure) belirlenir. Fırça ucu 1 pixel ile 150 pixel arasında, yoğunluk ise 1 ile 100 arasında değişebilir.

b. Reconstruction: "Mode" menüsünden seçilen etkiyi "Reconstruct" tuşuna tıklayarak uygulayabiliriz.

MODE
o Revert: Tüm deformasyonları eski haline getirir.
o Rigid: Kalkansız bölgelerde gizli iskelet üzerindeki araçlar ile oluşturulan deformasyonların açılarını özel bir algoritma ile düzenler. Deneyip verdiği etkiyi görmekte fayda var.
o Stiff: Bir önceki araç gibidir. Ancak oluşturduğu görüntü zayıf bir manyetik alana benzer.
o Smooth: Oluşturulan deformasyonların kalkanlı bölgelere bitişik olan bölümlerini yumuşatır.
o Loose: "Smooth" etkisinin daha şiddetli bir versiyonudur.
o Displace: Kalkanla korunmayan bölgeleri başka bir konuma taşır.
o Amplitwist: Bir önceki araca açı ve büyüklük unsurlarının eklenmiş hâlidir.
o Affine: Bir önceki araca skew (eğim) deformasyonunun eklenmiş hâlidir.
İpucu: Deformasyonları ESC tuşu ile iptal edebilirsiniz. Tüm grafiğe uygulanmış deformasyonları geri almak için ise "Revert" tuşuna tıklamanız yeterlidir.

c. Freeze Area: Kalkanımızı yönettiğimiz bölümdür. Channel ile kalkanın neye göre belirleneceği; Invert ile kalkansız bölgelerin kalkan sahibi olması, kalkanlıların kalkanlarını kaybetmeleri; "Thaw All" ile tüm kalkanların silinmesi sağlanır.

d. View Options: Kullanılan deforme unsurlarının görüntülenme biçimlerini bu bölümden ayarlarız.
o Show Frozen Areas: Çalışma sırasında kalkanlı bölgelerin görüntülenip görüntülenmemesi bu ayar ile belirlenir.
o Show Image: Çalışma sırasında ana grafiğimizin gizlenip gizlenmeyeceği bu ayar ile belirlenir.
o Show Mesh: Grafiğimize uygulanan deformasyonları sanal bir iskelet ise görülebilir hale getirebiliriz. Bu iskeletin çalışma sırasında görüntülenip görüntülenmemesi bu ayar ile belirlenir.
o Mesh Size: Sanal iskeletimizin polygon boyutlarını bu ayar ile belirleriz.
o Mesh Color: İskelet rengimizi buradan seçebiliriz.
o Freeze Color: Kalkanlı bölgeler şeffaf bir renk ile işaretlenir. Bu rengi buradan seçebiliriz.
o İpucu: Deformasyonu uygularken "OK" tuşuna "Shift" tuşuna basılı iken tıklarsanız deformasyonlar hafızaya alınır. Başka bir katmana veya başka bir bölgeye aynı deformasyonları uygulamak için "Shift" tuşuna basılı iken "Liquify" komutunu seçmeniz yeterlidir. Deformasyonları kaydetmek neden yok diyenlere...

TYPE TOOL
En çok kullandığımız elemanlardan biri olan yazı aracımıza Photoshop 6'da yeni ayarlar eklendi; terfi edenleri düşünerek bunları tanıtmak farz oldu...

o Kullanımı: Aracımızı seçtikten sonra faremizin sol tuşu ile grafiğimize tıklıyoruz ve yazımızı yazıyoruz. Yazıyı taşımak için harfleri girdiğimiz bölgeden uzaklaşmamız yeterli. Faremizin imleci hemen taşıma aracı sembolüne dönüşüyor; sol tuşa basılı tutarak taşıyabiliyoruz. Yazımızı tamamlayınca yukarıdaki onay tuşuna tıklamamız işlemi sonlandırıyor. Metinde değişiklik yapmamız gerekirse, harflerin üzerine geliyoruz ve bir kere tıklıyoruz. Faremizin sol tuşunu bırakmayıp tıpkı diğer programlardaki metin değişikliği işlemlerinde olduğu gibi harfleri seçip silebiliyoruz/değiştirebiliyoruz. Herhangi bir değişiklikten sonra yukarıdaki onay tuşuna tıklamayı unutmayalım.
Bir diğer yenilik ise Illustator, InDesign, PageMaker gibi vektörel programlarda bulunan, Photoshop'a yeni transfer olmuş bir kullanım biçimi. Type aracını kullanmak için grafiğimize tıklayıp sol fare tuşunu basılı tutarak bir dörtgen çiziyoruz.
Ne yazarsak yazalım artık bu dikdörtgenin sınırlarını aşamaz. Dikdörtgenin dışına gelince imlecimizin çeşitli ok işaretlerine dönüştüğü ve tıklandığında yazımızın açısının değiştiğini farketmişsinizdir. Bu dikdörtgeni bir kolon olarak da düşünebilirsiniz. Diyelim ki bir afiş hazırlıyorsunuz ve 5-6 paragraftan oluşan bir yazı içerecek... Bu yazıyı 3 kolona bölmek istediniz... İşte bu yeniliğin amacı bu. Kutunun köşelerindeki küçük kutucukları tıklayıp çekiştirerek kutunun boyutunu değiştirebiliriz. Ancak sağ alttaki kutunun farklı olduğunu; içinde bir artı işareti taşıdığını farketmişsinizdir. Bunun Photoshop'taki anlamı yazımızın kutu içine sığmadığı, bir grup karakterin görüntülenemediğidir. Ancak sadece bir belirteç... Diğer vektörel programlardaki gibi bir görevi yok.

AYARLARI
o Option Bar
İçi dolu "T" harfi standart yazı aracımızdır. Vektöreldir. İçi boş "T" harfi, yazımızı seçili alan olarak yazar. İçi boştur. İstenildiği gibi boyanır, efekt uygulanır. Vektörel değildir.
Soldaki ikon yazımızı soldan sağa, sağdaki ise yukarıdan aşağıya yazmak içindir.
Yazının fontunu ve stilini (normal, kalın, eğik, kalın ve eğik) seçtiğimiz bölümdür.
Yazının harf büyüklüğünü 6 ile 72 pt değerleri arasında belirlediğimiz bölümdür. Eğer istersek kutuya kendi istediğimiz bir değeri de yazabiliriz.
Yazının anti-alias derecesini bu menü ile belirleyebiliriz. None, keskin kenarlı; Smooth ise en yumuşak hatlı yazıyı yaratan ayardır.

CHARACTER PENCERESİ
Yazı aracı seçili iken "Palettes" tuşuna tıklarsanız o araçla ilgili ek ayar pencereleri açılır. Ayrıca "Character" penceresini "Window" menüsündeki "Show Character" ile ekrana getirip, "Hide Character" ile gizleyebiliriz.
a. Pencere içinde bulunmayan, ek birtakım ayarlar içeren bir menüdür.
b. Kullanılan font belirlenir.
c. Font stili belirlenir. (normal, kalın, eğik, eğik ve kalın)
d. Harf boyutu belirlenir. (Punto)
e. Satırların birbirlerine olan uzaklıkları belirlenir.
f. İki karakter arasındaki mesafe belirlenir.
g. Tüm yazının veya seçtiğimiz karakterlerin aralarındaki uzaklık belirlenir.
h. Karakter boyu belirlenir.
i. Karakter eni belirlenir.
j. Seçili karakterlerin satır çizgisine olan uzaklıkları değiştirilir.
k. Karakterlerin rengi belirlenir.
o İpucu: Bazı fontlar yapıları gereği bold (kalın) ve italic (eğik) stilleri içermezler. Bu gibi fontlarda bu stilleri kullanabilmemiz için Photoshop Type Tool içerisinde "Faux Bold" ve "Faux Italic" komutları bulunurdu. Ancak Photoshop 6'da böyle bir komutun olmadığını farketmiş olabilirsiniz. Vazgeçilmez birer kolaylık olan bu ayarlar "Character" penceresini gösteren resimde "a" ile işaretlenmiş menüde gizlenmiştirler. Yine bu menüyü kullanarak altı çizili (underlined), ortası çizili (strikethrough), üs (superscript) ve indis (subscript) gibi stilleri yazılarımıza kolayca uygulayabiliriz.

PARAGRAPH PENCERESİ
Yazılarımızı kutular içinde yazdığımızda bir takım yerleşim ayarları yapmamız gerekebiliyor. Bunlar sağa veya sola yaslamak, boşluklar (margin) bırakmak, ilk satırı bir miktar içeriden başlatmak gibi ayarlar...
a. Pencere içerisinde bulunmayan, ek bir takım ayarlar içeren bir menüdür.
b. Yazıları sağa, sola yaslar veya ortalar.
c. Paragrafı sağ ve sola hizalar (justify) son satırı isteğimize uygun konumlandırır.
d. İlk satır son satır farketmeksizin justify uygular.
e. Paragrafın solunda bırakılacak boşluğu belirler.
f. Paragrafın sağında bırakılacak boşluğu belirler.
g. İlk satırı içeriden başlatmak için gerekli ölçüdür.
h. Paragrafın üzerinde bırakılacak boşluğu belirler.
i. Paragrafın altında bırakılacak boşluğu belirler.
j. Ve son olarak; bu seçenek satır sonuna gelmiş kelimeleri tire ile bölüp bölmeyeceğimizi ayarlar. (Sadece Photoshop'un desteklediği dillerdeki kelimeleri bölebilir. Türkçe henüz desteklenmiyor. Ancak Adobe Photoshop CE'de Türkçe desteğinin geleceği duyuruldu.)

ADOBE PHOTOSHOP 6 CE
TÜRKÇE Mİ KONUŞACAK?
Bu yazıyı yazdığım sıralarda Adobe ürünlerinin türkçeleşeceği haberi geldi. Bugün itibariyle Adobe henüz bir açıklamada bulunmuş değil. Rivayetlere göre; Türkçe'nin, Orta Avrupa (CE) dilleri arasında olduğu kabul edilmiş olup yeni çıkacak CE sürümünde Türkçe desteğine yer verilecekmiş. Programın tamamı Türkçe olacağı gibi paragraflardaki satır sonu kesmeleri de Türkçe Dil Bilgisi kurallarına göre çalışır hale gelecekmiş. Firma, 2001 sonuna kadar tüm ürünlerini Türkçeleştirmiş olacağını söylüyor. Yakın zaman içerisinde, belki de siz bu dergiyi henüz satın almadan Adobe Photoshop 6 CE'nin deneme sürümü ücretsiz olarak dağıtılacakmış.
Her ne kadar eski topraklar için önemsiz olsa da büyük bir kesim Türkçe konuşan Photoshop istiyordu... Türkiye'de Photoshop kullanan kişiler çok olmasına rağmen lisanslı program sayısının azlığı Türkçe Photoshop çıkması ihtimâlini düşünmemize olanak vermiyordu. Biz de sizler gibi, gelişmeleri merakla izleyeceğiz.
Bu aylık benden bu kadar. Unutmayınız ki emek harcamadan istediklerinizi elde etmeniz imkansız. Bol bol çalışma yapın; rastladığınız grafiklerin, öğrendiğimiz hangi tekniklerle yapılmış olduklarına kafa yorun; takıldıklarınızı sorun... Gelecek ay yeni bir dersle birlikte olmak üzere, iyi çalışmalar.

## Haziran 2001

## **PHOTOSHOP 6.0 İLE TANIŞALIM******

Merhaba; birkaç aylık ayrılıktan sonra tekrar Photoshop bölümüyle birlikteyiz. En son yazıyı yazdığım zamanlarda Adobe Photoshop 6'ın beta sürümünü yeni elimize alabilmiş, inceliyorduk. Birkaç güzel özelliğin haberini vermiştik. Program piyasaya sürüleli uzun zaman oldu ve bir çoğumuz birer tane edinip kullanmaya başladık bile. Bu yazıda Adobe Photoshop 6 'ın yeniliklerini, getirdiği avantajları ve dejavantajları inceleyeceğiz. Bundan sonraki çalışmaları ben 5.0, 5.5 ve 6.0 sürümlerini kullanan arkadaşların takip edebileceği biçimde anlatacağım malum ekonomik nedenlerle terfi edememiş olabilecekleri düşünerek... Her konuda olduğu gibi sürümler arasındaki farklardan doğan sorunlarda da e-posta yoluyla danışmaktan çekinmeyin.

ADOBE PHOTOSHOP 6 İLE GELEN YENİLİKLER
Adobe Photoshop 6 diğer yeni sürümlerden farklı olarak büyük değişimleri beraberinde getirdi. Belki Adobe Illustator'a olan ilgiyi ateşlemek için olacak ki firma, vektörel çizim yapısını geliştirdi, yenilikler ekledi. Her iki programı da kullananlar kaba bir tabirle iki programın sentezi ile karşılaştıklarını söylediler ilk olarak Photoshop 6 için. Artık vektörel yapı daha gelişmiş durumda. Ayrıntılar:

Arayüzdeki Değişiklikler:
o The Option Bar (Özellikler Çubuğu): "Option Box" olarak bildiğimiz ayar kutusu artık bir satır halinde menünün altına yerleşti.
o The Palette Well (Palet Kuyusu): Option Bar 'ın sağ tarafına ilk bakışta ne işe yarayacağını kestiremediğimiz koyu gri bir kutu eklendi. Sağ üst bölümde bulunan bu kutu; Navigator, Info, Color, Layers, History, Actions ve bunlar gibi ekranın sağında çıkan ve taşınabilir olan kutuları saklayabileceğimiz bir alan. Varlığından rahatsızlık duyduğunuz ama sık kullandığınız için gizleyemediğiniz pencereleri bu bölüm içine sürükleyip onları ikonize hale getiriyoruz. Kullanımı ise artık üst menüdeki gibi tıkla, seç, kaybolsun şeklinde...

o Confirmation (Onay) İkonları: Uygulanmasından önce onay gerektiren araçlarda "onayla" ve "iptal et" anlamına gelen iki ikon özellikler çubuğunun yanına eklendi.
o Araçlardaki farklılıklar:
1. Crop Tool (Kes-al Aracı) ayrı bir ikon olarak araçlar arasında yerini aldı.
2. Web grafikleri oluştururken ImageReady'de kullandığımız iki araç Photoshop 'a transfer oldu. Bu araçlar, resimleri bölmeyi sağlayan "Slice Tool" ve bölünmüş parçaları seçmeyi sağlayan "Slice Select Tool".
3. Kare, dikdörtgen, çokgen, elips, kenarları yuvarlatılmış dikdörtgen gibi geometrik şekilleri kolayca oluşturabileceğiniz "Shape Tools" eklendi.
4. "Pencil Tool" ile "Paint Brush Tool"; "Paint Bucket Tool" ile "Gradient Tool"; "Line Tool" ile Shape Tools (dikdörtgen, beşgen, elips ve isteğe bağlı üretme aracı) aynı ikon grubu içine alındı.
5. İki yeni Selection Tool (Seçim Aracı) eklendi. Bunlar, Illustrator 'ın baş rol oyuncuları olan "Path Component Selection Tool" ve "Direct Selection Tool".
6. Measure Tool (Ölçüm Aracı), Eyedropper (Renk Seçici) 'den ayrıldı..

o Preferences (Ayarlar): Ayarlar komutu Edit Menüsü içine taşındı. Ayrıca "Reset Tool" ve "Reset All Tools" adlı iki yeni komut eklendi. Bu komutlar ayarları, yerleri değiştirilmiş araçları başlangıç haline döndürüyor.
o "Filter Fade" komutu Filter Menüsünden alınıp Edit Menüsüne taşındı. Ayrıca Present Manager (yüklediğiniz fırça, renk grupları, renk geçişleri, stiller, desenler, vb. Ekstraların yönetimini yapabileceğiniz komut) ve Color Settings seçenekleri de Edit menüsüne taşınanlar arasında.

o File Menüsüne aslında çok önceleri eklenmiş olması gereken Open Recent (son kullandığınız dökümanlar arasından birini yükle) ve Close All (tüm açık dökümanları kapat) komutları eklendi.

Layers (Katman) ve Layers
Penceresindeki değişiklikler:
o Layer Sayısı: Sadece bir kere çalışmama engel olan 99 layer'dan fazlasına izin yok kuralı artık 8.000 katmandan fazlasına izin yok diyor.

o Layer Sets: Artık katmanlar konularına göre veya kullanıldıkları yerlere göre setlere ayrılabiliniyor. Örneğin çalışmanızda üç farklı button bulunuyor ve üçü de 5 layerdan oluşuyor. Bu buttonları beşer layer'dan oluşan üç set halinde gruplarsak hem layer penceresindeki onbeş katman sayısı üçe inecek hem de buttonları hareket ettirmemiz, yönetmemiz daha kolay olacak. Katmanları ilişkilendirmekten (link) farklı; çok daha yararlı bir yeni özellik. Ayrıca her set kendine ait bir şeffaflık tipi ve miktarı içeriyor. Bu bilgi içerdiği katmaların şeffaflık tip ve miktarlarından farklıdır. Bu ilginç yeni özellik çok büyük kolaylıkları beraberinde getirmesi nedeniyle önemli.
o Effect ON/OFF: "Drop Shadow", "Glow" gibi efektlerin uygulandığı pencerede her efektin soluna yerleştirilen bir checkbox ile uygula veya uygulamayı iptal et komutunu hızlıca verebiliyoruz. Bu özellik animated gif'ler yaratırken veya rollover menü seçenekleri oluştururken işimize yarayacak. Photoshop 5.5 'de bu kolaylığı elde etmek için efekti raster moda geçirip (render işlemi uygulayıp / yeni katman haline getirip) çözmeye çalışıyorduk. Ancak bu eski yöntem, efektimizin ayarlarını kaybetmemize neden oluyordu... Yeni özelliğimiz sayesinde bu zorluktan kurtulmuş olduk.
o Mask Set: Aynı layer set mantığında olduğu gibi maskelerimizi de setler halinde yönetebiliyoruz. Bu kolaylığın yanında bir objeye birden fazla maske uygulama şansına sahip oluyoruz. Eğer maskeler hakkında daha fazla bilgi almak istiyorsanız Photoshop bölümümüzü takip ediniz.

o Content (Adjustment/Fill) Layers: Bu yeni katman çeşidi grafiğimize çeşitli renk etkilerini katmanlar aracılığıyla uygulamamız için geliştirilmiş. Önceki sürümlerde Photoshop dökümanını tek katmana indiripte uyguladığımız etkileri bu özellikle kolayca elde edebiliyoruz. Böylece katmanlarımızın sayısını ve özelliklerini korumuş oluyoruz.

Vektör Yazı ve Katman Tipleri:
o Type Tool (Metin/Yazı Aracı - Kısayol tuşu "T") yapısı Illustrator 'ın yapısına büründü. Artık yazı yazmak için grafiğin üzerinde bir yere "Type Tool" ile tıklıyoruz ve yazımızı yazıyoruz. Ekstra bir pencere açılmıyor, size ayarlar sorulmuyor. Tüm ayarlar Option Bar içerisinde herhangi bir an kolayca değiştirilebiliniyor. Character ve Paragraph adında iki yeni pencere de bu araç için çeşitli yeni ayarları içeriyor.

o Farklı Renkler: "Type Tool" ile oluşturduğumuz yazımızın artık istersek her bir harfini farklı renklerde yapabiliyoruz.

o Warp Text: Bir diğer mucizevi yenilik vektörel bir çizim elemanı olan Text Warp (Metin eğme/bükme) denilen araç. Bu eleman, yazımıza; eğme, bükme, dalgalandırma gibi çeşitli uzay deformasyonları uygulamamızı sağlıyor. Illustrator kullananlar bu deformasyonları Path Type Tool (Rota Yazı Aracı) ile deformasyon eğrisini çizerek yapabiliyordu. Photoshop kullanıcıları ise transform ve filter/distort ile bu etkileri elde etmek için çabalıyordu. Artık istenen deformasyon 15 seçenek arasından seçilip kolayca uygulanabiliyor veya Illustrator 'dan yeni transfer edilen Path Type Tool ile kolayca çizilebiliniyor.
o Converting to Outlines: Bir diğer Illustrator kaynaklı komut olan "Coverting To Outlines / Shape", yazılarımızı ya kapalı şekillere ya da vektörel olan Pathler'e çevirmemizi sağlıyor. Bu sayede harfler üzerinde değişiklikler, deformasyonlar yapılabiliyoruz.

o Rasterize the Type: Önceki sürümlerden "Render Layer" olarak bildiğimiz komut... Vektörel type katmanını bitmap katmana çeviriyor.

Vektör Şekiller ve Maskeler:
o Vector Shapes: Dikdörtgen, köşeleri yuvarlatılmış diktörtgen, elips, çokgen gibi çeşitli şekilleri vektörel olarak yaratmamızı sağlayan yeni araçlar, Tools penceresine eklendi.
o Selecting Shapes: Yaratılan bu şekillerin tamamını veya bir bölümünü seçme şansı tanıyan iki yeni araç eklendi. (Path Component Selection Tool, Direct Selection Tool)

o Vector Layer Masks: Photoshop 'un maske özelliği Photoshop 6 'ya kadar sadece bitmap elemanlardan oluşuyordu. Şimdi ise ister bitmap ister vektörel maskeler oluşturabilirsiniz. Üstelik ikisini aynı katman üzerinde...

Automation:
o Picture Package: Bir kaynak resmi, dökümanınıza istediğiniz sıklıkta ve sayıda döşemeyi sağlayan yeni bir araç...
o Web Photo Gallery: Bir dizin içerisindeki grafiklerinizi, sizin belirlediğiniz renklerde, boyutta, templatelerde kolayca bir web foto-galerisi haline getiren bir araç...
o Batch Processing: Bir dizin içerisindeki grafiklerimizin tamamına önceden kaydettiğimiz bir "Action"ı uygulamamızı sağlar. Örneğin dizin içerisindeki tüm grafikleri 640x480 boyutuna indirmek istiyoruz; bu durumda boyut değiştiren bir "Action" oluşturuyoruz ve bu seçenek ile tamamına uygululayabiliyoruz.

o Create Droplets: Droplets, küçük programcıklardır. "Create Droplets" komutu, Action scriptlerini "EXE" dosyaları haline getirir ve üzerinde bir grafik dosyası sürüklenip bırakıldığında belirtilen action'ın görevini yapar. Dropletlerimizi çeşitli Photoshop kaynak sitelerinde paylaşabilir, diğer kullanıcıların yolladıklarının arasından işimize yarayabilecek çok çeşitli kolaylık programları edinebiliriz.

Yeni Save (Kayıt) Özellikleri:
o Save a Copy: Grafiklerimizi GIF, JPG, TGA, TIFF gibi tek katman destekleyen grafik formatlarında kaydetmek için kullanılan "Save a Copy" seçeneği artık "Save As..." seçeneği altında bir checkbox ile kullanılabiliniyor. "Save a Copy" komutunu CTRL-SHIFT-S kısayolunu kullanarak çağırmaya alışan kullanıcılar düşünülmüş; bu kombinasyon ile komuta ulaştığınızda checkbox seçili olarak ekrana geliyor.
o Save With Backwards Compatibility: Edit / Preferences / Saving Files seçeneği altına eklenen bu satır kaydedilen PSD dosyalarının önceki Photoshop sürümleri tarafından açılması için eklenmiş yeni bir ayar.

o Layered PDF Files: Adobe'un Photoshop kullanarak PDF (Portable Document Format) dosyaları yaratanlara bir jesti... Artık dosyaları PDF formatında kaydettiğinizde tekrar üzerlerinde çalışabilmek için katman bilgilerini koruyor. Bu format hakkında bilgi almak için http://www.adobe.com/products/acrobat/adobepdf.html adresini kullanabilirsiniz.

o Layered TIFF Files: Photoshop'un bu yeni özelliği TIFF dosya formatına katman bilgisinin de eklenmesinden ibaret. Ancak bu yöntem ile üretilen TIFF dosyaları bu yeni formatı desteklemeyen programlar tarafından görüntülenemiyor.

o Color Profiles: Artık her PSD dökümanının kendine ait bir renk profili olabiliyor.

16 Bit Grafiklere Doping:
16 bit renk derinliğine sahip dökümanlar yaratmak zorunda olanlar için önceden kullanılamayan bazı araçlar kullanılabilinir hale getirildi. Bunlar; Crop, Rotate Canvas, Image Size, Canvas Size gibi değişiklik araçları; Auto Contrast, Levels, Curves, Color Balance, Hue/Saturation, Channel Mixer, Gradient Map gibi tonâl yardımcılar; Clone Stamp, History Brush, Gradient tools gibi çizim araçları... Ayrıca Gaussian Blur, Add Noise, Median, Unsharp Mask, High Pass, Dust and Scratches, and Solarize filtreleri de artık kullanılabiliniyor.

Slicing (Parçalama):
o Slice Tools (Parça Araçları): Sadece ImageReady 'de bulunan Slice (Parçalama) ve Select Slice (Parça Seçme) araçları, web grafiklerinin büyük yardımcıları, Photoshop'a eklendi.

o Auto Save (Oto-kayıt): ImageReady ve Photoshop programları arasında gezinirken üzerinde çalıştığınız dökümanın otomatik olarak kaydedilmesini sağlayan yeni bir ayar. Edit / Preferences / General / Auto Update Documents seçeneği...

o Layer Based Slicing (Katman Tabanlı Parçalama): Bu yeni özellik, katman tabanlı parçalar oluşturmamızı sağlıyor. Böylece grafiklerdeki değişiklikler parçalara eşzamanlı yansıyor ve büyük zaman kayıplarınının önüne geçmiş oluyor.

Cropping (Kesme):
o Karartma: Araçlar arasına eklenen "Crop"u kullanırken seçili alanın dışında kalan bölge crop işleminden sonra yok olacak bölgeyi vurgulamak için kararıyor.

o Delete (Sil) veya. Hide (Gizle): Grafiğinizin bir bölümünü crop komutu ile aldığınızı düşünelim. Kesilip atılan bölüm artık isteğe bağlı olarak korunuyor veya silinip gidiyor. Korunması, katmanı kaydırdığınız/taşıdığınız zaman boşlukla karşılaşmamamız için gerekli. Silinmesi ise dosya boyutunu küçük tutmanız gerektiği zamanlarda önemli. Photoshop 6 'da "Crop Aracını" kullanırken "Option Bar" üzerinde Delete (Sil) ve Hide (Gizle) yöntemlerinden birini seçebiliriz. Eğer dökümanımız sadece "Background" katmanından oluşuyorsa bu iki yöntemden birini seçmek mümkün değildir; program, "Delete" seçeneği seçili gibi davranır.
o Trim: Trim, yeni eklenmiş bir crop türü... İşlemi biraz daha otomatikleştirip, sizin yükünüzü azaltıyor. Komutu seçtiğinizde grafiğinizi inceliyor ve boyalı/çizili olan (şeffaf olmayan) bölgeyi içine alabilecek minimum boyutta bir dikdörtgen oluşturup crop komutunu uyguluyor. Daha basit bir anlatımla; koskoca bir dökümanın ortasına bir şekil çizip trim komutunu uygularsanız sadece şekli alıp geri kalanı çöpe atıyor.

o Reveal All: Crop komutu gizlenen bölgeleri geri getirmek için yaratılmış bir komuttur. Crop'un tam tersi diyebiliriz...

Liquify:
Emin olmamakla birlikte eğer ingilizcedeki "liquid" isminden "liquify" fiili olarak türetildiğini düşürsek "akışkanlaştırılmış" anlamına gelmektedir. Grafiğinize dokuz farklı araç ile sıvıya benzer etkiler / deformasyonlar uygulayabiliyorsunuz. Başlı başına bir terfi nedeni olabilir bazıları için...

Color Management
(Renk Yönetimi):
o Color Settings (Renk Ayarları): Renk ayarları tek başlık (Edit / Color Settings) altında toplandı. Her seçeneğe diyalog kutusunun altında belirecek şekilde açıklamalar eklendi.

o Document Specific Working Spaces: Photoshop 6 'da, açık olan her döküman için renk profili ayarları ayrıdır. Her bir dökümana farklı profiller verilebilinir.

o Advanced Options: Artık dökümanlarınıza bir renk profili uygulamak için Image / Mode Assign Profile veya Image / Mode / Convert to Profile seçeneklerini kullanarak convert etmenize (dönüştürmenize) gerek yok. Herhangi bir değişim yapmadan sadece görünümüne etki edecektir.

o Embedding profiles: Dökümanınıza renk profili iliştirme, "Save As..." komutunun altında "Embed Color Profiles" olarak yerleştirildi.
Annotations (Notlar / Post-itler):
o Notes (Notlar): Photoshop 6 'nın bir diğer yeni özelliği ise grafiklerinize çeşitli notlar bırakabilmemiz. Özellikle bir grafik üzerinde birden fazla kişinin çalıştığı durumlarda artık gizli type layerlar kullanmadan diğer kişilere notlar bırakabilirsiniz. Ancak sadece PSD ve PDF formatlarında not bilgisi dosya ile saklanır.
o Audio Annotations (Sesli Notlar): Bir önceki özellikten farklı olarak "Audio Annotations" sesli mesajları dökümanlarınıza eklemenizi sağlar. Her iki not yönteminde de unutulmaması gereken tek nokta bu notların sadece Photoshop 6 tarafından görüntülenebildiğidir / dinlenebildiğidir.
o Importing Annotations: Bir PDF dosyası içine eklediğiniz notları çalıştığınız dökümana çağırmaya (import) yarayan bir özelliği de eklemeyi unutmamışlar. Nedense sadece PDF'den notları import edebiliyor; bu da ilginç bir durum.

ImageReady:
o Preview State: Araçların alt bölümüne yeni birtakım ikonların eklendiğini farketmişsinizdir. Bunlardan biri, üzerinde parmaktan çıkan noktalar olan ikon seçili olduğu sürece dökümanınızdaki rollover menü elemanlarını test edebilirsiniz. Tarayıcınıza geçmeden bu test işlemini sağlaması büyük zaman kazancı...

o Animating Type: Photoshop 6 'daki Type Warp elemanını ImageReady 'de yazılara hareket kazandırmak ve ilginç animasyonlar oluşturmak için kullanabilirsiniz. Dalgalanan, bükülen, dönen yazılar gibi...

ADOBE PHOTOSHOP 6 VE
İLK RESMİ GÜNCELLEMESİ 6.0.1
Firmanın açıkladıklarına göre bazı belirgin değişiklikler:
o Painting Tool (kısayol tuşu "B") için fırça seçim sistemi geliştirilmiş. Bunlar:
o Fırça boyutunu seçtikten hemen sonra grafiğiniz üzerinde çizime devam ettiğinizce seçme penceresi yokoluyor.
o Seçmek istediğiniz fırça ucuna çift tıkladığınızda seçim penceresi yokoluyor.
o Seçili fırça boyutu daima option bar'da görünen fırçadır.
o Her fırça ucunun boyutu rakamla belirtilmektedir.
o İlk fırça ucunu ve son fırça ucunu kolayca seçmeyi sağlayan kısayol tuşları ">" ve "<" artık yüklenmiş ekstra fırçaları da hesaba katarak çalışıyor.
o Vektörel çalışmalarda büyük kolaylık sağlayan "Image clipping paths" artık 6.0.1 'in ürettiği EPS ve TIFF dosyalarında QuarkXPress yazılımının okuyabileceği şekilde kaydediliyor.
o ImageReady, artık animasyonları ve önizlemeleri düşük hafızada dahi sorunsuzca çalıştırıyor.
o "Open Recent" seçeneği altındaki dosyalar bulunamadığı zaman yaşanan yavaşlamalar engellendi.
o "Batch file naming" (otomatik dosya isimlendirme) artık sorunsuzca çalışıyor.
o "Export Paths to Illustrator" komutu ile üretilen dökümanlardaki path boyutu artık korunuyor.
o Move, Marquee, Lasso Tool gibi basit komutlar Open, Save ve Print gibi komutların ardından kullanıldığında artık hata mesajı alınmıyor. (Büyük bir sorundu.)
o "Color Range" özelliğinde tek renk seçme artık sorunsuzca çalışıyor.
o Help (Yardım) artık pek çok farklı web tarayıcısı ile uyumlu çalışıyor.
o Tüm Windows İşletim Sistemlerinde program hafızayı etkin kullanabiliyor; Photoshop kullanılırken ağda veya internet bağlantısında hafıza yetersizliğinden kaynaklanan kesilmeler engellendi. (Şimdiye kadar rastladığım en önemli sorun buydu sanıyorum. Başlı başına bir terfi nedenidir.)
o Seçim alanının kenarlarının görüntülenmesi veya gizlenmesi için CTRL-H kısayolunu artık iki kere kullanmak gerekmiyor.

Photoshop 6.0 için üretilmiş bu ilk resmi güncellemeyi yüklemek için http://
www.adobe.com/products/photoshop/update.html?code=awe\_171000 adresini kullanabilirsiniz. PC sürümü yaklaşık 6.5 MB.

BITMAP VE VEKTÖR TEKNOLOJİSİ
Bitmap (raster) ve vektör birer dosya formatı olarak doğdular. İki format farklı programlar tarafından yaratılmakta. Bitmap grafikleri Adobe Photoshop, Macromedia Fireworks, Corel Photo-Paint, Jasc Paint Shop Pro, Micrografx Picture Publisher, Ulead PhotoImpact, MS Paint gibi programlar ile; vektörel grafikleri ise Adobe Illustrator, Adobe ImageStyler, Adobe LiveMotion (hareketli), Macromedia Freehand, Macromedia Flash (hareketli), CorelDRAW, Xara, gibi programlar ile üretebiliyoruz. Ancak son zamanlarda çıkan programlar veya eski programların yeni sürümleri mümkün olduğunca diğer format ile uyumlu hazırlanıyor. Örneğin Photoshop bitmap tabanlı bir program olmasına rağmen vektörel çizim elemanı olan path'leri bünyesine dahil etmişti uzun zaman önce. Ayrıca Adobe lllustator ve Micromedia FreeHand ile uyumlu ve rahat bir şekilde çalışabiliyor. Bu durum bitmap ve vektörü birbirinden "ayrı formatlar" olmaktan çıkarıp "farklı çizim yöntemleri" haline getirdi diyebiliriz. Gereksiz uğraşılara girmemek, zaman kaybetmemek için yapacağımız çalışmaya en uygun yöntemi seçebilmeliyiz. Hemen tanışalım:

Bitmap (Raster) Grafikler:
Bu grafik formatını anlatırken üzerinde duracağımız önemli unsurlar grafiğimizin "pixel" cinsinde genişliği ve yüksekliği; renk derinliği... Eğer en ve boy ölçülerini inch veya cm cinsinde kullanacak olursak resolution (çözünürlük) büyük önem kazanır. Çünkü bir cm içerisindeki pixel sayısı çözünürlüğe göre değişir. Bizim kullandığımız çözünürlükler genellikle 72 veya 96 dpi (dot per inch / bir inche düşen pixel adedi) dir. Genişlik ve yüksekliği pixel olarak belirledikten sonra program, her pixele farklı bir renk bilgisi verir. Her pixel için şeffaf mı (boş) boyalı mı (dolu), dolu ise dolduran rengin RGB ve CMYK değeri saklanır. (NOT: Şeffaflığı destekleyen formatlar sadece GIF ve PNG'dir. Bunun yanında TGA, PSD ve benzeri formatlar, alpha channel denilen şeffaflık bilgisini dosyanın bir bölümüne yerleştirebilir. Ancak bunlar sadece kaydedildikleri veya uyumlu olarak hazırlanmış programlarca okunabilir.) Siz bir düz çizgi çizerken aslında çizgi yaratmıyor, var olan pixellerin renklerini çizgi gibi görünecek şekilde boyuyorsunuz. Şekilde 10x10luk bitmap bir grafiğin anatomisini görebilirsiniz:

Bitmap Grafiklerin İyi
ve Kötü Özellikleri:
o Genellikle büyük dosya boyutlarına sahiptirler.
o En ve/veya boyları azaltığında bir miktar pixel boşa gider. Resize komutu ile küçültme yapılırsa kalitesiz, kirli görüntüler oluşabilir, Resample komutu ile küçültülürse kaybolan pixellerin verdiği kötü görüntüleri engellemek için kalan pixellerde düzenleme yapılarak doğallık korunmaya çalışılır. Aynı teknik büyütme için de geçerlidir. Bu nedenle boyut değişikliklerinden istenen sonuçlar alınmayabilinir.
o Şeffaflık, görüntüde sorunsuzdur ancak grafiğin üzerinde çalışılırken vektörün getirdiği avantajları getirmez.
o Diğer bitmap formatlarına çevirimi kolaydır.
o Vektör grafiklerden çok daha kompleks görüntüler içerebilir. Örneğin fotoğraflar, kamera ile alınmış görüntüler, tarama ile elde edilen grafikler birer bitmap'tir.
o Hareketlendirip, eğip, büküp animasyon hanilne getirmek zordur.
o Çalışma alanı, üzerinde çalışılan cisim ve bunlar gibi birimler sadece kare ve dikdörtgen gibi düzgün dörtgenlerden oluşabilir. Bu durumun yaratacağı olumsuzluğu anlamak için aşağıdaki örneği inceleyelim:
Katman desteği vermeyen programlarda bir yuvarlağı hareket ettirirken aslında yuvarlağı içine almış en küçük kare hareket ettirilir. Bu nedenle yuvarlak ile kare arasındaki bölge doludur aslında boş olması beklenirken.

Vektör (Vektörel) Grafikler:
Bitmap'in aksine pixel bilgisi içermez. Çeşitli matematiksel ifadelerle üretilmiş çizgiler, eğriler, metinlerden oluşur. Obje tabanlıdır. Bir sin(x) eğrisi 100x100 boyutunda da 1000x1000 boyutunda da aynı şekilde ve aynı çizgi kalınlığında (siz aksini belirtmedikçe) olacağı için boyuttan ve çözünürlükten bağımsızdır. Bitmap çalışma mantığından çok farklı olarak vektörel çizimde bir cismin içinin dolu olup olmadığı, dış kontürünün var olup olmadığı, varsa çizgi kalınlığı ve türü önemlidir...

Vekörel Grafiklerin İyi
ve Kötü Özellikleri:
o Dosyalar çok az yer kaplarlar.
o İstenildiği gibi boyutlarında değişiklik yapılabilinir, kaliteyi etkilemez. Aşağıdaki mağara adamı resmine dikkatlice bakın; vektörel çizilmiş bu çalışma hem bitmap'e çevrilip zoom yapılıyor hem de vektörel halde iken zoom yapılıyor. Kuşkusuz vektörel hal daha kaliteli. Ne kadar yaklaşırsanız yaklaşın, kalite düşmeyecektir.
o Mağara adamı örneğinde olduğu gibi vektörel çizimler bir fotoğrafın sahip olduğu kompleksliği taşıyamaz. Karikatürize çizimler için biçilmiş kaftandır.
o Çizgi türleri, kalınlıkları, renkleri; yüzey türleri, renkleri birkaç tıklama ile kolaylıkla değiştirilebilinir.
o Background yoktur.
o Çalışma alanı sınırsız en ve boya sahiptir, yeni bir döküman açarken belirttiğiniz ölçüler sadece sizin çalışmanızı kolaylaştırmak için sanal, yardımcı çizgiler oluşturmayı sağlar.
o Kolayca şekil değiştirebilir, kolayca animasyonlar yapılabilinir.
o Grafik içerisindeki metinler, kullanılan fontların sistemde yüklü olmasını isteyen formatlarda fontun yüklü olmadığı sistemlerde olduğundan farklı görüntülenir. (Sadece eski formatlar için geçerli)
o Çalışma alanı, üzerinde çalışılan cisim ve bunlar gibi birimler istenildiği kadar köşeli, istenildiği kadar eğri olabilir. Cisim dışında kalan bölgeler her zaman şeffaftır.

DOSYA UZANTILARI
Vektörel grafik dosyası uzantıları; AI Adobe Illustrator, CDR CorelDRAW, CMX Corel Exchange, CGM Computer Graphics Metafile, DRW Micrografx Draw, DXF AutoCAD, EPS Encapsulated PostScript, TXT ASCII Text, WMF Windows Metafile...
Bitmap grafik dosyası uzantıları; BMP, GIF, JPEG, JPG, PNG, PICT (Macintosh), PCX, TIFF, PSD Adobe Photoshop...

FORMATLAR ARASINDA GEÇİŞLER
Farklı çizimleri farklı teknikleri kullanarak oluşturabiliriz. Örneğin Photoshop'da bir çalışma yapıyoruz ve bir karikatürize kalp resmine ihtiyacımız var. Kalp, eğri kenarları nedeniyle vektörel yöntemlerle kolayca oluşturulabilinir. İster Photoshop 'un Path araçlarını kullanarak çizeriz ister vektörel tabanlı bir program ile oluşturup Photoshop içine çağırırız. Dışarıdan çağırmak için copy/paste yöntemini veya EPS / AI dosya ile taşıma yöntemini kullanabiliriz. Kaliteyi maksimum koruyabilmek için bir vektörel grafiği EPS veya AI formatında kaydedip Photoshop'da açmak en iyisidir. Copy/Paste yönteminde eğrilerin ekstremum noktalarında anti-ailasing yumuşak görünüm özelliğinin yitirildiği görülmüştür. Çağırma işleminin yanında bir vektörel grafiği bitmap'e çevirmek için GIF, JPG, TGA, TIFF gibi formatlarda save (kayıt) etmek yeterlidir. Ancak bitmap grafikleri vektörel formata dönüştürmek oldukça zordur. Pixellerin oluşturduğu kenarların saptanıp matematiksel formüllere dökülmesi, renk yapısının çözümlenmesi gerekmektedir. Bugün itibariyle bilinen programlar içerisinde sadece Corel Draw paketindeki TRACE aracı bu işlemi yapabiliyor. Ancak karmaşık ayarlar ve sağlıklı bir sonuca ulaşabilmek için yapılan onlarca deneme baş ağrıtıyor...

GELECEK AYA KADAR
NE YAPSAK?
Bu ay Photoshop 6'ya terfide zorlanmamanız için yenilikleri inceledik. Eğer sizde programı edindiyseniz, yavaş yavaş eski sürümü rafa kaldırıp yenisine korkusuzca girişin... Yazıyı bir de programın başında okuyun, yenilikleri iyice öğrenin. İlerleyen derslerde komutları teker teker öğreneceğiz, komutların varlıklarından haberdar olup üzerlerinde birkaç deneme yapmış olursanız öğrenme süreciniz kısalabilir. "Bitmap ve Vektör" konusuna gelecek olursak; temiz bir döküman açın, 2 yeni katman yaratın, katmanlardan birine "Line Tool" ile kalın ve büyük bir çizgi çizin, diğerine "Type Tool" ile kocaman bir "I" harfi yazın. Çizgimiz rasterized (yani bitmap) bir elemanı temsil etmekte, harfimiz vektörel bir çizim elemanını temsil etmekte. Bu iki elemanı sırayla eğin, bükün, efektler uygulayın, büyütün, küçültün, yakınlaşın, uzaklaşın, bildiğiniz herşeyi üzerlerinde deneyip tepkilerini görün. Böylece bitmap ve vektör mantığını iyice öğrenin.
Bu aylık benden bu kadar. Unutmayınız ki emek harcamadan istediklerinizi elde etmeniz imkansız. Bol bol çalışma yapın; rastladığınız grafiklerin, öğrendiğimiz hangi tekniklerle yapılmış olduklarına kafa yorun; takıldıklarınızı sorun... Gelecek ay yine sıradışı ve eşsiz bir dersle birlikte olmak üzere, iyi çalışmalar.

## Mayıs 2001

## **PHOTOSHOP**

*Photoshop'daki Hesap Makinesini Kullanın ***

Photoshoperlar'ın bu muhteşem yazılımda kullanmamayı alışkanlık haline getirdikleri işlemlerden birisi de Calculations tablosu. Halbuki bu tablo, 2.5 versiyonundan bu yana harikalar oluşturmanızı sağlıyor.

Photoshop'un standart layer efektlerini kullanarak bir yazıya (Resim1) deki gibi kabartma efekti uygulayabilirsiniz. Hemen akabinde bir zemin layer'ının altına alıp, (Resim2) Alt tuşu ile iki layer arasındaki çizgiye tıklayarak, zemini, kabartma yapısını bozmadan, harfin içine gömebilirsiniz. (Resim3) Ne yazık ki, bunu herkes yapabilir.

Eğer farklılaşmak istiyorsanız, Photoshop'un hesap makinesinin tuşlarına dokunmalısınız.

BEN HUMBARACI'YIM :-)

Malumunuz, Ortaçağ'da kuşatılan kalenin çevresinden tüneller kazıp, tam surların altında kanalları patlatanlara Humbaracı deniyor. Evet sevgili Photoshop halkı, ben kanalcıyım. Birçokları, artık layer'lar ile her şeyin yapılabildiğini ve kanallara gerek olmadığını söylüyor. Yazıyı okuyup yuttuktan sonra bu konuda daha sağlıklı karar vereceğinize eminim. Şimdi örnek çalışmaya başlayalım mı?

Text aracıyla yazınızı oluşturun, sonra Control tuşuyla layer'ın üzerine tıklayıp (Resim4), seçili alan haline getirin. Ardından Channels paletine geçin ve kanal olarak kaydedin (Resim5) Alpha 1 adıyla oluşan kanalı, palet altındaki sayfa ikonu üzerine sürükleyip çoğaltın ve bu kanala Gaussian Blur uygulayın. (Fiziğe önemli katkıları olan Karl Frederick Zeuss Gauss adına ithaf edilen bu filtreyi ben, 200 piksel yüksekliğindeki çalışmamda, 7 piksel değeriyle kullandım.)

Hemen akabinde Levels tablosundaki Output Levels değerini, 128'e getirin. (Resim6) Hala Alpha 2 kanalındasınız ve son olarak, Filter/ Other/ Offset filtresini, (Resim7) deki gibi kullanın. Ohh be, bitti...

Alpha 2'yi çoğaltıyorsunuz (ismi otomatik olarak Alpha 3 olacaktır) ve tekrar Offset filtresine gidip, bir öncekinin iki katı ve negatif değerde kullanıyorsunuz (örneğe göre -6 horizontal, -6 vertical) (Resim 8)

Şimdi geçin hesap makinesine. Image/ Calculations ile tabloyu getirin. (Resim 9) daki gibi Source kanallarını belirleyin. Geçişme metodunu Difference yapın ve tabloyu okeyleyin.

Calculations tablosunun oluşturduğu Alpha 4 kanalında efekt henüz belirgin değildir. Levels tablosunu Control-L ile çağırıp, (Resim10) daki gibi beyaz üçgeni, histogram çubuklarının başına kaydırın. (Resim 11) deki gibi sonuca ulaşmalısınız.

Alpha 4 kanalındayken, Select/ Load Selection ile Alpha 1 kanalını, tablodaki Invert seçeneğini işaretleyerek yükleyin. Yazının etrafı seçilecektir, % 100 siyah renk ile doldurun. (Resim12) 12. resim karşınızda mı? Bu etki, harfin koyu bölgelerini tanımlamaktadır. Kanalda beyaz gördüğünüz bölgeler, harfin karanlık kısımlarını oluşturacaktır. Seçilmişliği gidermeyi unutmayın.

Çoğaltın Alpha 4'ü. Alpha 5'i Image/ Adjust/ Invert ile dişiye çevirin. (Dişi, bizim masaüstü yayıncılıktaki stüdyo terminolojisinden geliyor.) Tekrar Alpha 1'i Load Selection ile Invert işaretleyerek yükleyin ve siyah renk doldurun. Levels tablosunu çağırıp, bu sefer siyah üçgeni, sağa doğru, (Resim 13) deki etkiye ulaşıncaya kadar sürükleyin. Böylece harfin açık kısımlarını, ışık patlamasının olduğu bölgeleri ürettiniz. Seçilmişliği giderin ve hala kafanız karışmadıysa, bir sonraki adımla devam :-)

RGB birleşik kanalına geçin. Dokümana bir zemin çağırın veya oluşturun. Zemin layerında iken önce Alpha 1 kanalını Load Selection ile yükleyin. Harf alanındaki pikselleri, (Resim 14) deki gibi bir evlek açın (Evlek, çok küçük bir ölçü birimi :-). Seçilmişliği giderin.

Bu sefer Alpha 4'ü, yani koyu renk bölge için hazırladığınız kanalı, Load Selection ile çağırın. İster Levels, ister Curves kanalıyla, seçili alandaki pikselleri koyulaştırın. (Resim 15) Işık patlamaları, tam parlak olmadığı için henüz tam olamadı. Seçilmişliği giderin ve Alpha 5'i çağırın. Bu sefer seçili alandaki piksellerin rengini açın. Finalde, Alpha 1 kanalını çağırın ve yazının etrafını uygun bir renk ile doldurun. (Resim 16)

Evet, 16. resim ile efekt tamamlandı. Ama bir de 17. resme bakın. Çok farklı değil. 17. resimde, birçok detay var, ışık zenginliği birdenbire tüm etkiyi değiştirmiş. (Resim 17)

Gelecek sayılarda, illustrasyon sanatının temeli olan ışık/gölge/kontrastlık etkileşimiyle, çalışmalarınızı güzelleştirmeyi öğreneksiniz. Şimdilik 17'ye bakmakla idare edin :-)

(Sabri Varol, PC Magazine dergisinin freelancee yazarlarındandır. Geleneksel ve online yayıncılık, görsel efektler konusunda Medyasoft Eğitim Merkezi'nde kurslar vermektedir. (www.medyasoft.com.tr) Kendisine svarol@sabrivarol.com ile ulaşabilirsiniz.)

---
*Kaynak: `PHOTOSHOP YAZILARI/Pcmagazine Photoshop Yazıları.doc` — KhanCiCEK — 2000*
