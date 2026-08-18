# PLC Sistemlerinin İncelenmesi

**PLC Sistemlerin İncelenmesi**

** ‘**Programmable Logic Kontroller’sözcüklerinin kısaltılmasından oluşan PLC yi proglamnabilen mantık denetleyicisi olarak tanımlayabiliriz.Kontrol sistemlerinde çok yaygın bir kullanımı olan PLC elektromekanik donanımlara oranla; düşük maliyet dayanıklılık küçük fiziksel boyut,çeşitli sistemlere bağlanabilirlik,yeniden proglanabilme ve esneklik gibi avantajlar sağlar.

** **Elektromekaniksel kontrol sistemlerinde kontrol eden elemanlar ile kontrol edilen elemanlar arasında (algılayıcı kontaklar ile seleneoid lamba vs. elemanlar).Programa göre yapılan bir iletken bağlantı mevcuttur.PLC sisteminde ise prıgram tanımı(senaryo) yapıldıktan sonra kontrol sistemi donanımsal olarak kurulur.Bu senaryo bir proglamyıcı(P6 700 vb)yardımı ile doğrudan PLC nin belleğine yazılır.Bu senaryoya göre algılayıcı kontaklarından gelen girişler(Inputs) taranır.Uygun mantıksal işlerin sonucunda(and or ...) işlemci elemanların(valve bobin vb...)enerjilenmesi için gerekil çıkışlar(Outputs) üretilir.

PLC aşaığıdaki birimlerden oluşur:

1)Giriş/çıkış (Input/Output) bağlantı modülleri.

2)Merkezi işlem birimi(CPU)

3)Bellek(Memory)

4)Sinyal taşıma sistemi(Bus system)

5)Güç kaynağı(Power Supply)

6)Proglama dilleri..

PLC en basit şekilde;sinyal vericileri,kontrol ünitesi ve dış ortamdaki işlemcilerden oluşur (Bkz.şekil –1)

Sinyal vericileri dış ortadaki işlemciler

PLC sistemi bütünüyle aşağıdaki blok diyagramdaki gibi tasarlanmıştır.

Sinyal

Dış ortamdaki işlemciler

Allen Bradley PLC system

Giriş Çıkış (İnput / Outputs ) Birimleri : CPU birimini dış ortamdaki algılayıcılar ile ( input ) işlemcilere ( Output ) bağlayan birimlerdir. Dış ortamdaki algılayıcılardan bazıları şunlardır:

1-) sınırlama anahtarları (Limit Switches)

2-) Basma anahtarları (push – buttons)

3-) basınç anahtarları (pressure Switches)

4-) Seviye anahtarları ( Level switches)

5-) Basınç uyarıcıları

6-) Dönüştürücüler ( Transdücers )

7-) Seçici anahtarları (selectör Switches)

PLC ‘nin çıkış (output) sinyallerine göre çalışan dış ortamdaki bazıları ise şunlardır:

1-) Selenoid valfler

2-) Röleler Kontaktörler

3-) Lambalar

4-) Göstergeler (Led Display )

5-) Motor sürücüleri

Şekil 2 de görüldüğü gibi inputlar sinyal vericilerden ve kotlayıcıdan sinyalleri alır ve PLC ‘deki merkezi ünitenin çevirebileceği hale getirir. Merkezi ünite programı içeren kısımdır. Her olası input sinyalinde merkezi ünite output sinyalini belirler. Outputlar merkezi üniteden gelen output sinyallerini makinenin yukarıda belirtilen işlemcilerine iletir.

İnputlar vericilerden sinyalleri alır ve merkezi ünite ile iletişim sağlamak için onların voltajlarını ayarlar. Yani merkezi üniteye giden sinyallerin lojik konumlarını belirler. ( 1 veya 0 )

Her input aktif hale geldiğinde yanan bir Led’e sahiptir. İinputlar 24-48 v arasında aktif haldedir. Aktif bir inputun merkezi üniteye gönderdiği lojik konum “1” dir.

İnputlar 8 input modelinde toplanır. Bu modüller kartın içinde saklıdır. Ve bu yolla birkaç modül bir üniteye yarleştirilebilir.

Not: modüllerde dış voltajlar ve sinyaller , iç sinyaller ile PLC sistem arasındakine uygulanır. Bu yanlış bir sinyalin (220v) bütün PLC sistemine değil küçük bir modülüne zarar vereceği anlamına gelir.

Merkezi Ünite

Merkezi ünite PLC sisteminin kontrol merkezidir ve makineyi kontrol eden programı içerir. Merkezi ünite ; hafıza modülü , merkezi işletme modülü , taşıma modülü ve sistem güç modülünden oluşur.

Merkezi işletme modülü (CPU) giriş arabirimleri yardımı ile veri (Data) alır. Bunları belleğindeki programa göre işler ve kontrol edilmek istenen cihaza , çıkış arabirimi üzerinden veri yollar. Bu işlem sürekli olarak tekrarlanır ve buna tarama ( scanning ) denir. CPU ‘nun yaptığı bazı işlemler şunlardır. :

1-) Mantıksal işlemler ( lojik operations )

2-) sayma işlemleri (counting )

3-) zamanlama işlemleri ( timing )

4-) bilgi transfer işlemleri ( data transfering )

5-) Bilgi kaşılaştırma tranferi ( comparison )

6-) matematiksel işlemler ( aritmetik )

7-) açısal işlemler ( angle valve )

8-) Regülatör Kontrolü benzeri işlemlerdir.

Programda yapılan işlemler komutlardan oluşur :

Röle tip komutlar :

İnceleme komutları inputların durumunu anlar. Her input talimatı bir inputa bağlıdır ki adresi o kumuta saklıdır.

İki tip inceleme komutu vardır :

Examine on - \]\[ - : Bu komutun inputu lojik 1 ise doğrudur , eğer input aktif ise

Examine off - \]\[ - : Bu komutun inputu lojik 0 ise doğrudur.

A B

+ -

C D

İnputlar Outputlar

12012 02110

12013 02112

A kontağı kapalı iken B lambası , C kontağı açık iken de D lambası yanar.

Eğer kilitli bir output ile açık bir output aynı zamanda aktif hale gelirse , programda son yerleşen komut outputun konumunu belirler

Not: güç kaybı durumunda bütün aftif output kilit talimatları geçici olarak aktifliğini kaybeder. Güç geldiğinde basamak parçalarına bakmaksızın hepsi lojik 1 konumuna gelir.

Zamanlama komutları :

Zamanlama komutları açmayı ve kapamayı geciktirmek için kullanılır. Dört tip zaman komutu vardır. TON , TOF . RTO ve RTR. TON ve RTO açma geciktirmesi ,TOF kapama geciktirmesi ve RTR RTD komutlarını silmek için kullanılır.

Gecikme “time base” ve “preset value ( PR) “ değerleri ile belirlenir.

Time base 1.0s,0.1s,0.01s olabilir.

Pr değeri 1-999 arası olabilir.

Bu gecikmenin 0.01s ile 999s arasında olduğunu gösterir.(16dak ve 34 s)

Ek olarak AC değeri (accumulated value) komut tarafından gösterilir. AC değeri gecikmenin ne kadar değiştiğini gösterir.

Kontrol Ünitesi

Angle Encoder (Kodlayıcı)

Girişler (İnputs)

Merkez ünite

Çıkışlar (outputs)

Programlama ünitesi

Cascade recorder

12012

12013

Merkezi ünite

02110

02112

---
*Kaynak: `PLC SİSTEMLERİNİN İNCELENMESİ/ekitap-Anonim-Elektronik_PLC_Sistemlerinin_Incelenmesi.doc` — Titan — 2001*
