# En Cok Kullanilan Modem Komutlari

## **EN ÇOK KULLANILAN MODEM KOMTLARI**

** ‘ AT ’ **; bu komutu modeme gönderdiğinizde ekrana ‘OK’ çıkması gerekmektedir.Aksi halde modem – program – bilgisayar üçlüsü arasında bir iletişim bozukluğu var demektir.

**AT < ENTER > **şeklinde kullanılır ve modem komutlarından bazıları bu ‘AT’ komutuna eklenerek kullanılmalıdır.

** ‘ A ’ **; modemin telefon hattınızı açmasını ve bir cevap sinyali göndermesini sağlar . Modem başka bir modem tarafından arandığında bağlantıyı kurmak için , telefon çalarken bu komutun verilmesi gerekir.

**ATA < ENTER > **şeklinde kullanılır.

** ‘ A/ ’** ; modeme verdiğiniz son komutu tekrar eder.Sürekli kullanılan bir komut yada devamlı aranan bir telefon numarası olabilir , zamandan tasarruf etmek için bu komut kullanılır.

**A/ < ENTER > ** şeklinde kullanılır.

** ‘ %C ’ **; iletilen bilgilerin sıkıştırılmasını sağlar.Daha önce sıkıştırılmamış dosyaların transfer zamanlarını en aza indirir.Daha önce sıkıştırılmış dosyalar için kullanılırsa , transfer zamanında azalma beklerken tam tersi ile karşılaşabilirsiniz.Bu komut , ‘ \\N ’ komutunun aldığı değerlerden etkilenmektedir.Bu seçenekler ;

0 = bilgi sıkıştırma aktif

1 = bilgi sıkıştırma pasif

**AT%C \[ seçenek \] < ENTER > ** şeklinde kullanılır.

** ‘ &C ’ ** ; bağlantı durumunun belirtilmesinde kullanılır . Bazı iletişim yazılımları , modem bağlantı kurmadan önce bağlantı durumunun açık olmasını isterler. Gelişmiş iletişim yazılımları ise , bu opsiyonu bağlantı kurulduğunda açarak , kullanıcıya haber verir.Seçenekler ;

0 = bağlantı durumu her zaman açık

1 = sadece bağlantı kurulduğunda açık

**AT&C < ENTER > **şeklinde kullanılır.

‘ **D ’ **; telefon numarası çevirmek için kullanılır.Modem kullanımı , telefon hattı üzerinden telefon numarası çevrilerek , başka modemleri arama şeklinde gerçekleşir.Seçenekler ;

P— çevirmeli telefon modu

T— ton sesli telefon modu

R— aradıktan sonra cevap ver modu

W – ikinci bir çevir sinyali bekle

S – hafızadaki numarayı çevir

**, ** numara çevirirken bekleme yap

**; ** komut moduna geri dön

**/ ** 0.125 sn bekle

**ATD \[ seçenek \] \[ seçenek \] \[ telefon numarası \] < ENTER > **şeklinde kullanılır.

** ‘ &D ’ **; modemin DTR sinyalini kontrol eder ve bu sinyalin değişiminde modemin ne yapacağını belirler.Modem , DTR seçeneğini devamlı açık tutacak şekilde programlanabilir.Bir çok iletişim yazılımı , modemlerin hattı kapatmaları için bu komutu kullanır.( %D2 ) Seçenekler;

0 = DTR her zaman açık

1 = DTR kapandığı zaman modem komut moduna geçer , otomatik cevap verme kapalıdır.

2 = DTR kapandığı zaman modem telefon hattını kapatır., komut moduna geçer ve otomatik cevap verme kapalıdır.

3 = 2 ile aynı , fakat en sonunda modemin kendini sıfırlamasını sağlar( ATZ )

**AT&D < ENTER > **şeklinde kullanılır.

** ‘ E ’** ;terminal programından modeme gönderilen bilgileri geriye terminale göndermeyi sağlar.Bazı terminal programları yazdıklarınızı ekranda göstermeyebilir.O zaman bu fonksiyonunuzu açık tutulmalıdır.Seçenekler ;

0 = fonksiyon kapalı

1 = fonksiyon açık

**ATE \[ seçenek \] < ENTER > **şeklinde kullanılır.

** ‘ &F ’** ; bu komut modemin tüm ayarlarını fabrika ayarlarına döndürür.Bazı durumlarda modem ayarları ile oynanmış olabilir, o zaman en başa dönebilmek için bu komut kullanılmalıdır.

**AT&F < ENTER > ** şeklinde kullanılır.

** ‘ &G ’ **; koruyucu ton ayarlamasını yapar.Ülkeler arası ayarlamalarda kullanımı gerekli olabilir.İngiltere ile yapılan görüşmelerde 1800 Hz’ lik bir koruyucu ton sesi gerekmektedir.Bazı Avrupa ülkelerinde ise bu değer 550 Hz olmaktadır.ABD , Kanada ve Türkiye’ de koruyucu ton uygulaması yoktur.Seçenekler ,

0 = kapalı

1 = 550 Hz

2 = 1800 Hz

**AT&G <ENTER > **şeklide kullanılır.

** ‘ \\ G ’** ; akış kontrolü ( XON / XOFF ) seçimi yapar.v.42 ve MNP kullanılmayan durumlarda modem ile bilgisayar arasında bir akış protokolü kullanmak , bilgi kaybını önlemek açısından yararlı olur.v.42 ve MNP kendi akış kontrol metotlarını kullandıkları için böyle bir durum söz konusu olduğu zaman bu komut dikkate alınmaz.Seçenekler ;

0 = kapalı

1 = açık

**AT \\ G \[ seçenek \]< ENTER > ** şeklinde kullanılır.

**‘ H ’** ; modemin telefonu açıp kapatma görevini yapar.Bağlantıyı sona erdirmek için ( bağlantı halinde iken ) ya da telefonu meşgul durumuna almak için ( bağlantı halinde değilken ) kullanılır.Seçenekler ;

0 = bağlantıyı sona erdir.

1 = telefonu meşgul durumuna al

**ATH \[ seçenek \] <ENTER > **şeklinde kullanılır.

**‘ I ’** ; modemin hızını ( bps ) , ROM değerini ve kayıt numarasını gösterir.Seçenekler;

0 = hızını gösterir

1 (3) = ROM testini yapar

4 (6) = ürün kayıt numarasını gösterir

**ATI \[ seçenek \] <ENTER > **şeklinde kullanılır.

**‘ Z ’ **; o ana kadar ki tüm değerleri sıfırlar ve başlangıç değerine döndürür.

**ATZ <ENTER > **şeklinde kullanılır.

**‘ L ’** ; modemin sesini ayarlar.Seçenekler ;

0 = en düşük

3 = en yüksek

**ATL \[ seçenek \] < ENTER > **şeklinde kullanılır.

s

---
*Kaynak: `EN COK KULLANILAN MODEM KOMUTLARI/EN COK KULLANILAN MODEM KOMUTLARI.doc` — ESENGÜL KARABULUT — 2004*
