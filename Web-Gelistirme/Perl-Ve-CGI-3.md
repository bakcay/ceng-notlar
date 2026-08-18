# Perl Ve CGI

## **PERL ile CGI**

## **PERL**

Perl(Practical Extraction Report Language), kelimelerinden türemiştir.Perl bir “yorumlayıcı” dildir.Yani,yazdığımız programları derlemek zorunda kalmıyoruz,sadece yazıyoruz ve çağırıyoruz.Web sunucusu bizim adımıza çalıştırıyor.Bir script metin halinde yazılan Perl kodudur.Perl yorumlayıcısı sadece bu metni alır ve çalıştırır,ilave işlemlere gerek yoktur.

Perl scriptlerinizi ya kendi lokal makinamızda (Notepad,Simpletext vb.editör programlarıyla) ya da UNIX sunucusu üzerinde hazırlayabiliriz.

Öncelikle Perl ile program yazmadan önce Perl'ü internetten temin etmemiz gerekir.Perl kullandığımız işletim sistemleri için değişik adreslerden temin edilebilir.

Gerekli program internetten temin edildikten sonra Perl programlarımızı çalıştırmak için **<dosya adı>.pl **şeklinde kaydettikten sonra MS-DOS penceresini açar ve herhangi bir dizinde

** c:\\>perl <dosya adı>.pl**

komutunu vererek programımızı çalıştırırız.

** **Perl ile yazılan tüm scriptlerde her dosyanın ilk satırında aşağıdaki gibi bir deyimin olması gerekir.Bu satır,sunucuya bu dosyanın bir Perl scripti olduğunu ve de Perl yorumlayıcısının yerini söyler.

**#!/usr/bin/perl**

Bu satırdan sonra,Perl kodunu yazmaya başlayabiliriz.Perl deyimleri (;) ile sonlanır.Döngüler(for,while…..) ve şartlı dallanma yapılarında(if) (;) kullanılmaz.

## **PERL'DE DEĞİŞKENLER**

Bir değişken, daha sonra kullanılmak üzere bir değeri geçici olarak saklayan bellek bölgesidir.Perl'de 3 tür değişken vardır: Skaler değişkenler(scalars),diziler(arrays) ve özel tablolar(hashes).

## **Skaler Değişkenler(Scalars)**

Bir skaler değişken tek bir skaler değer içerir.Perl'de skaler değişkenler ön ek olarak bir $-dolar işareti ile başlarlar.Değişken isimleri rakamla başlayamaz,boşluk ve ekstra(standart dışı) karakterler içeremezler.Bir harfle başlamak zorundadırlar,daha sonra rakam bulundurabilirler.En fazla 32 karakter uzunluğunda olabilirler.Perl'de skaler değişkenler için sayısal,string ya da mantıksal diye bir ayrım söz konusu değildir.Örneğin;

$isim="Fatih Taşçı";

$yas=27;

Değişkenlerde çift tırnak içine alınanlar "yorumlanırlar",tek tırnak içine alınanlar yorumlanmazlar,olduğu gibi ekrana yazdırılırlar.

Perl'de değişkenleri kullanmadan önce deklare etmek zorunda değiliz.İstediğimiz anda bir değişkeni tanımlamaksızın kullanabiliriz.Perl'de değişkenler anında tip değiştirebilirler.

Bir değişkene klavyeden değer atamak için aşağıdaki deyim kullanılır.Burada klavyeden girilenler $isim değişkenine aktarılmaktadır.

$isim=<STDIN>;

İsmimizi yazdıktan sonra genellikle Enter'a basarız.Salt girilen veriyi elde etmek için Enter karakterini değişkenden ayıklamak gerekir.Bunun için aşağıdaki deyim kullanılır:

chomp($isim);

print deyimi ile de mesajları,değişkenleri ve sabitleri ekrana yazdırırız.Satır başı yapmak için C'de olduğu gibi,"\\n" kullanırız.

## **Diziler(Arrays)**

Bir dizi değişkeni,birden çok değeri içeren bir listedir.Bir skaler değişkende tek bir değer saklanırken bir dizi değişkende birden çok değer tutulabilir.Perl'de dizi değişkenler ön ek olarak bir @ işareti ile başlarlar.Örneğin;

@renkler=("kirmizi","yesil","mavi");

Perl'de dizi indisleri 0'dan başlar.Örneğin,@renkler dizisinin ilk elemanını belirtmek için $renkler\[0\] şeklinde bir notasyon kullanılır.

Perl'de # işareti ile başlayan satırlar açıklama satırı kabul edilir.

**Dizi Fonksiyonları**

** **Perl'de dizilere eleman eklemek,eleman silmek,iki diziyi birleştirmek,dizideki elemanların sıralarını kaydırmak vb. işlemleri gerçekleştirmek için birtakım hazır fonksiyonlar vardır.Bunlara dizi fonksiyonları denilmektedir.

@renkler=(“kirmizi”,”yesil”,”mavi”,”mor”,”sari”);

$renk=pop(@renkler); # dizideki son elemanı,”sari”yı verir.

$renk=shift(@renkler); # dizideki ilk elemanı,”kirmizi”yı verir.

Pop ve shift,diziden elemanları silmek,yok etmek için kullanılır.Diziye eleman eklemek için push fonksiyonu kullanılır.

push(@renkler,”turuncu”); # @renkler dizisinin sonuna “turuncu” eklenir.

Dizilerle ilgili çok kullanılan bazı fonksiyonlar şunlardır:

sort(@renkler) # Dizideki elemanları alfabetik olarak sıralar.

reverse(@renkler) # Dizideki elemanları tersinden yer değiştirir.

$#renkler # renkler dizisinin uzunluğu (eleman sayısı-1)

join(“,”,@renkler) # Dizideki elemanları aralarına virgül koyarak bir string olarak birleştirir.

## **Özel-Tablolar(Hashes)**

Özel-tablolar,dizilerin özel bir hali olup her bir eleman;”anahtar-değer” şeklindeki ikililerden oluşur.Perl’de özel-tablo isimleri %-yüzde işareti ile başlarlar.Örneğin;

%HASH\_LISTE=("Ahmet"=>24,

"Veli"=>30,

"Ayşe"=>23,

"Orhan"=>18);

Özel-tablolar ,CGI programlamada özellikle bir form’dan gelen verileri ayrıştırmak için oldukça kullanışlıdırlar.Örneğin,$FORM{‘soyad’} şeklindeki bir kullanım ile kullanıcının form’daki ‘soyad’ alanına girdiği bilgiyi öğrenmekteyiz.

**Özel-Tablo Fonksiyonları**

** **Özel-tablolarla çalışırken sık kullanılan fonksiyonlar aşağıda verilmiştir:

delete $tablo{"anahtar"} # belirtilen anahtar/değer ikilisini tablodan

siler ve silinen değeri geri döndürür.

exist $tablo{$key} # belirtilen anahtar tabloda mevcut ise true

döndürür.

keys %tablo # tablonun anahtarlarını bir liste olarak verir.

values %tablo # tablonun degerlerini bir liste olarak verir.

scalar %tablo # tabloda eleman varsa,boş değilse true

verir.

## **DÖNGÜLER**

## **If Döngüsü**

** **Bir if deyiminin genel yapısı şöyledir:

If(test1) {

test1 sonucu ‘true’ iken çalışacak deyimler…

}

elsif(test2) {

test2 sonucu ‘true’ iken çalışacak deyimler…

}

else {

test2 sonucu ‘false’ iken çalışacak deyimler…

}

else ve elsif blokları seçimliktir;gerektiğinde kullanılır,gerekmediği zaman kullanılmaz.

Perl’de test ettiğimiz değişkenin string veya sayı olmasına göre farklı karşılaştırma operatörleri kullanılır.Karşılaştırma operatörleri aşağıdaki tabloda görülmektedir:

**Test Sayılar için String’ler için******

$x eşittir $y $x==$y $x eq $y

$x eşit değildir $y $x!=$y $x ne $y

$x büyüktür $y $x>$y $x gt $y

$x büyük eşittir $y $x>=$y $x ge $y

$x küçüktür $y $x<$y $x lt $y

$x küçük eşittir $y $x<=$y $x le $y

## **Foreach Döngüsü**

** **Örneğin;

foreach $eleman(%HASH)

{

print $eleman;

}

#Ekrana HASH tipinde listenin anahtarlarını yazar.

## **While Döngüsü**

** **While döngüsü verilen şart geçerli olduğu sürece blok içindeki komutları çalıştırır.Yapısı şöyledir:

while(şart)

{

deyimler......

}

## **Do-While Döngüsü******

Önce döngü bir kez çalışır,sonra verilen şart sağlanıyorsa çalışmaya devam eder.Yapısı şöyledir:

do

{

deyimler.......

}

while(şart);

## **For Döngüsü**

** **Perl,C dilindekine benzer bir for döngüsüne sahiptir.Yapısı şöyledir:

for(başlangıç;şart;artım)

{

deyimler........

}

## **ALT PROGRAMLAR**

** **Diğer dillerden metot,fonksiyon ya da prosedür olarak tanıdığımız kod birimleri,Perl dilinde subrutin(alt program) olarak isimlendirilirler.Subrutinleri programın herhangi bir yerinde tanımlayarak,programımızın içinde kullanabiliriz.

Subrutin kullanmak yazdığımız kodları düzenli bir yapıya kavuşturur.En önemlisi bir kere yazdığımız kodu programın çeşitli yerlerinde subrutin ismini yazarak kullanabiliriz.Perl’de bir altprogramı çağırmak için birkaç alternatif bulunmaktadır:

&subname;

&subname(args);

subname;

subname(args);

subname();

Altprogramın önüne konulan & işaretini kullanmak seçimliktir.Genel olarak bir altprogramın yapısı şöyledir:

Sub altprogramadı {

kodlar….

return ($deger); veya exit($deger);

}

## **VERİ DOSYALARI**

## **Dosyaların Açılması**

** **Dosyalarla çalışırken ilk önce onlara aşağıdaki deyim ile bir belirteç(filehandle) atanır ve okuma-yazma işlemleri bu belirteç üzerinden gerçekleştirilir.

open(BELİRTEÇ,”dosya\_adi”);

Dosya adının önünde mod belirteci olarak “>” ya da “>>” olabilir.Bunların anlamları,dosya çıktı modunda(dosya yeniden oluşturulacak) ya da ekleme modunda açılacak demektir.

Dosyalarla çalışırken dosyanın gerçekten açılıp açılmadığını kontrol etmek lazımdır.Örneğin;

open(OUTPUT,”>output.txt”) or dienice(“Dosya açilamadi.”);

Burada dienice,dosya açılamadığı takdirde kullanıcıya bir hata mesajı veren ve CGI dan çıkan bir altprogramdır.

## **Dosyaların Kilitlenmesi**

Aynı dosyadan okuma-yazma yapan iki farklı script aynı anda işlem yapmaya çalışırlarsa veri dosyası silinebilir ve tüm verilerinizi kaybedebilirsiniz.Bunu önlemek için:

**flock(BELIRTEÇ,mod)** fonksiyonu kullanılır.Bu sayede dosyayı sadece bizim işlem yapabileceğimiz hale getirerek kilitleriz.

flock fonksiyonu,bir diğer proses dosyaya yazma işleri yaparken bizi bekletir,eğer bizde yazma işlemi yapacaksak kayıt işaretçisini dosyanın sonuna konumlandırmamız gerekir.Bunun içinde;

**seek(BELIRTEÇ,öteleme,yer) **fonksiyonunu kullanırız.

Öteleme,işaretçinin yer’e göre göreceli olarak kaç satır hareket edeceğini gösteren sayıdır.Yer parametresinin değerleri şunlardan biridir:

0 dosyanın başı

1 şu anki konum

2 dosyanın sonu

## **Dosyaların Kapatılması**

** **Bir dosyaya yazma işlemimiz bittiyse değişikliklerin kaydedilmesi için dosyayı kapatmamız gerekir:

close (BELIRTEÇ);

## **Dosyaların Okunması**

** **Dosyayı okumak için kullanmamız gereken komutlar:

open(INF,”anket.dat”) or dienice(Dosya açilmadi);

$a=<INF>; #dosyadan tek bir satır oku ve $a değişkeninde sakla

@b=<INF>; #dosyanın tamamını oku ve @b dizisinde sakla

close(INF);

## **STRING’LER**

## **Stringlerin Karşılaştırılması **

Perl’de küçük büyük harfler dönüşümleri için lc ve uc hazır fonksiyonları kullanılabilir.

$country=lc($country); #küçük harfe(lowercase) çevirir.

$country=uc($country);** **#büyük harfe(uppercase) çevirir.

## **Stringlerde Bul-Değiştir İşlemleri **

** **index fonksiyonu,str2’nin str1 içindeki pozisyonunu verir.

$pos=index(str1,str2,\[baslamayeri\])

baslamayeri seçimliktir. Eğer baslamayeri kullanılırsa str2’nin,str1 içerisinde belirtilen konumdan sonraki bulunduğu yer döndürülür.

İndisleme 0’dan başlar.str2,str1 içinde yoksa geriye -1 döndürür.index fonksiyonu küçük büyük harf duyarlıdır.Eğer arama işini sondan başlatacaksak rindex fonksiyonu kullanılır.Bu durumda indisleme sondan itibaren 0’dan başlar.

Verilen bir stringin belli bir kısmını elde etmek veya değiştirmek için substr fonksiyonu kullanılır.Yapısı şöyledir:

$str=substr(string,baslamayeri,uzunluk)

## **Stringlerin Formatlı Yazdırılması**

** **Perl’de stringleri ekrana formatlı yazdırmak için standart bir yöntem kullanılmaktadır: printf ve sprintf.Bu iki fonksiyonun kullanımı C’dekiler ile birebir aynıdır:

printf(“format stringi”,degiskenler listesi);

$mystr=sprintf(“format stringi”,degiskenler listesi);

format stringi,normal metin(mesaj) ve %-direktifleri içerir.Değişken listesinde yer alan elemanlar,birebir karşılık gelecek şekilde %-direktifleri ile eşleştirilerek,bu direktif ile istenilen formatta ekrana yazdırılırlar.

%-direktifinin genel formu şöyledir;

%mx veya %m.nx

Burada m ve n,keyfi sayılardır ve genişlik belirtirler.m,genellikle alanın minimum genişliğini,n ise reel sayılarda ondalık kısmın genişliğini,diğer alanlarda ise alanın maksimum genişliğini belirtmektedir.x ise c(karakter),i(tamsayı),s(string).... gibi tiplerdir.

## **DÜZENLİ(REGÜLER) TERİMLER**

** **Perl ve diğer dillerde regüler terimler olarak isimlendirilen harf ve kelime gruplarıyla bir metni taramamız mümkündür.

## **Regüler Terimlerin Kullanılması**

** **Regüler terimler bir dosyanın içinde geçen kelime ve kelime gruplarını bulmak için kullanılır.Örneğin;

$var="Bugün hava çok güzel.Arkadaşlarla sinemaya gideceğiz.";

if($var=~/çok/)

{

print "Çok kelimesi kullanılıyor";

}

Burada if döngüsünü kullanarak,çok kelimesinin string içinde kullanılıp kullanılmadığını kontrol ediyoruz./çok/ burada kullanılan regüler terimdir.Regüler terimler iki / / işareti arasında yer alır.

Bazen de içinde aradığımız regüler terimin bulunmadığı bir dosyayı taramak isteyebiliriz.Bunun için NOT (!) operatörü kullanılır.

Tarama yaparken büyük/küçük harf ayırımı yapmak istemiyorsak;

$var=~/Cok/i

şeklinde i opsiyonunu kullanırız.Tüm satırlarda tarama yapmak için m opsiyonunu kullanabiliriz.S opsiyonunu kullanarak,satır içinde bulunan regüler terimi başka bir kelimeyle değiştirmemiz mümkündür.

G opsiyonu ile cümle içinde birden fazla bulunan regüler terimi aynı anda değiştirebiliriz.Örneğin;

$var=~s/cok/cok cok/g

ifadesi cümle içindeki tüm "cok" kelimeleri yerine "cok cok" kelimelerini yerleştirir.

## **Regüler Terimlerde Kullanılan Özel İşaretler**

| **Sembol** | **Anlamı** |
| --- | --- |
| .(nokta) | Yeni satır(satırbaşı) hariç herhangi bir karakter |
| \[a-z\] | a'dan z'ye kadar bir küçük harf |
| \[^a-f\] | a'dan f'ye kadar harf grubu dışındaki herhangi bir küçük harf |
| \[abc\] | a,b ya da c |
| \\d | Herhangi bir rakam(0-9) |
| \\D | Herhangi bir rakam olmayan(0-9 disinda) |
| \\w | Harfle başlayan herhangi bir kelime |
| \\W | Harfle başlamayan herhangi bir kelime |
| \\s | İki kelime arasındaki boşluk |
| \\n | Yeni satır |
| \\r | Yeni satır yapmadan satır başı |
| \\t | Tab karakteri |
| \\0 | NULL karakter |
| \\b | Sadece kelime olanlar(kelime sınırı)(sadece \[\] dışında) |
| \\B | Kelime sınırı değil |
| ^ | Satır veya string başı |
| $ | Satır veya string sonu |
| X? | 0 veya 1 adet x; x,yukarıdakilerden herhangi biri |
| X\* | 0 veya çok adet x |
| X{m,n} | En az m adet, en çok n adet x |
| X+ | 1 veya çok adet x |
| (des1\|des2) | des1 veya des2’den herhangi biri |
| (des) | Sonradan kullanmak üzere desen’le eşleşen’leri saklama($1,$2,…$9) |

## **Here Dökümanları**

Perl programlarımıza Here dökümanı çerçevesinde print() fonsiyonunu kullanmadan text pasajları ekleyebiliriz.Here dökümanları kullanılarak,CGI programlarına HTML sayfa kodları eklenir.

Here dökümanları <<operatörü ve Here ismiyle başlar.İstenilen pasaj eklendikten sonra,Here ismi tekrar yazılarak,Here döküman çerçevesinin kapatılması gerekmektedir.

## **ARAMA VE SIRALAMA **

** **Bir dosya içerisinde bir verinin aranması için birçok yöntem mevcuttur.Ya dosyayı tamamen okuttuktan sonra bir döngü ile okunanları tarayıp aradığımız kelimelerin olup olmadığına bakarız ya da Perl’in grep fonksiyonunu kullanarak bir liste üzerinde olan arama işlemini tek hamlede gerçekleştiririz.

## **Arama**

** **Arama yapmak için kullandiğımız grep fonksiyonunun yapısı şöyledir:

@sonuc=grep(/desen/,@liste\_adi);

/desen/, aradığınız kelimeleri içeren bir düzenli ifadedir.Bu,yalın 1-2 kelime olabileceği gibi kompleks bir düzenli ifadede olabilir.

## **Sıralama**

Perl bize listeler üzerinde alfabetik olarak sıralama yapan basit bir sort fonksiyonu sunar.Ancak sort fonksiyonu sayılar üzerinde çalışırken sayıları string gibi ele alarak farklı sonuçlar vermektedir.Ancak sort fonksiyonu aşağıdaki gibi çağrılırsa bu sorun ortadan kalkar.

sort subname @liste

Belirtilen subname,sıralanacak listedeki herbir çift için ayrı ayrı çağırılır.Değerler,$a ile ilk eleman,$b ile ikinci eleman olarak altprograma gönderilir.Altprogram geri dönüş değeri olarak,eğer $a,$b’den küçük ise -1,eşit ise 0 ve büyük ise +1 döndürmelidir.Bu altprogram şöyledir:

sub sayisal {

return $a < = > $b;

}

## **REFERANSLAR(POINTERS)**

** **Referansları kullanarak,herhangi bir değişken adres alanı üzerinde işlem yapabiliriz.Böylece referansın tipine göre,referans üzerinde yapacağımız değişiklikler,değişkenin sahip olduğu değeri etkileyecektir.

Perl dilinde iki tip referans vardır:

## **1)Sembolik Referanslar**

** **Sembolik referanslar bir başka değişkenin ismini kullanarak,bu değişkenin değeri üzerinde işlem yapabilir.Sembolik referanslar genel anlamda kendileri ve referanse ettikleri değerler değişken oldukları için,referanse edilen değerlere ulaşmak için $$ işaretlerini kullanmamız gerekir.

## **2)Gerçek Referanslar**

** **Sembolik referansların aksine gerçek referanslar beraberlerinde bir referans sayacı taşırlar.Örneğin;

Bir subrutin içinde bir değişken tanımladığımızı düşünelim.Bu değişken subrutin içinde bulunduğumuz sürece geçerliliğini koruyacaktır.Ana program içinde kullanmamız mümkün olmayacaktır.Eğer değişkenin değerini ana program içinde kullanmak istiyorsak gerçek bir referans kullanarak değişken referanse edilebilr ve bu değişkenin değerini silinmekten kurtarabiliriz.Ancak ana programda bu değişkeni kullanarak sahip olduğu değere ulaşamayız.Yalnızca referans ismini kullanarak bu değişkenin değerine ulaşabiliriz.

/$değişken yazarak herhangi bir değişkene referanse edebiliriz.Referans bir değişkenin sahip olduğu hafıza alanı adresini içerir.Referanse edilmiş değişken silinmiş olsa bile,hafıza alanı adresine sahip olduğumuz için referans üzerinden bu bilgiye ulaşabiliriz.

## **Require Komutu**

Require komutu ile başka dosya içinde bulunan bir kodu kendi programımıza eklememiz mümkündür.

## **İsim-Alanı**

** **Require komutu ile dışarıdan eklenen kod ana programın bir parçası olarak görülür.Bundan ötürü ana programda kullandığımız değişkenler, dışarıdan eklenen kodunda içinde bulunabileceği için zarara uğrayabilirler.Değişkenlerin geçerliliklerini koruduğu bölgeye,kod içinde isim-alanı adı verilir.Dışarıdan eklediğimiz kodun içinde bulunan değişkenler de,kodun içinde diğer değişkenlerle aynı isim-alanını paylaştıkları için,ortaya istenmedik durumlar çıkabilir.Bunun için isim-alanlarını birbirinden ayıracak bir mekanizmaya ihtiyacımız var.

## **Paketler**

Bir paket başlı başına bir isim-alanı oluşturur.Bir paket içinde yer alan tüm değişken ve subrutinler sadece paket içinde,paket ismi olmadan kullanılabilir.Paket dışına çıkıldığı zaman,paket ismini kullanarak,paket ismiyle tanımladığımız isim-alanı içindeki değişken ve subrutinlere ulaşabiliriz.Böylece paket isimlerini kullanarak,isim-alanlarını birbirinden ayırmış oluruz.

## **Package Direktifi**

** **Bir paketi,package isim;direktifini kullanarak tanımlayabiliriz.Bu direktiften sonra normal kod yazılır.Örneğin;

package ornek;

$var=123;

$isim=”fatih”;

1;

Ana programda,require “paketismi.pl”; kullanarak bu paketi programımıza ekleyebiliriz.Paket kullanılarak tanımlanmış isim-alanlarına $paketismi::$değişken şeklinde ulaşabiliriz.

## **Modüller**

** **Perl modülü bir .pm dosyası içinde yer alan bir pakettir.Use direktifini kullanarak ana programa dahil edilirler.

## **CGI**

## **CGI NEDİR?**

CGI,”Common Gateway Interface”(Ortak Geçit Arayüzü) kelimelerinin kısaltılmışıdır.CGI terim olarak,bir web sunucusu üzerinden;verileri veritabanlarından, dökümanlardan ve diğer programlardan okuma ve verileri hazırlayıp yine web üzerinden web tarayıcılara sunma metodudur.Yani kısaca **CGI, web tabanlı programlama yöntemidir.**Web tabanlı programlamayı ana hatlarıyla ikiye ayırabiliriz:

Sunucu(server) tarafında programlama ve istemci(client) tarafında programlama.(ya da her ikisi aynı anda olabilir)İstemci tarafında programlama için Java,JavaScript veya VBScript iyi birer seçim olabilir.Sunucu tarafında programlama için en uygun seçenek CGI’dır.(Hem UNIX hem de WinNT platformları için).Bir CGI programı kısıtlama olmaksızın istenilen herhangi bir programlama dili ile yazılabilir.Ancak,**Perl **en popüler CGI programlama dilidir,çünkü bu amaçla tasarlanmıştır.

Eğer web sayfaları tasarlamak istiyorsak sayfamızı kaç kişinin ziyaret ettiğini öğrenmek,ziyaretçilerin bize mesaj bırakmalarını yada bir sipariş geçmelerini sağlamak ve buna benzer şeyler isteyebiliriz.CGI,tüm bunları ve daha fazlasını yapmak için bize birtakım imkanlar sunar.

## **CGI ORTAM DEĞİŞKENLERİ**

Ortam değişkenleri, çalıştırdığımız her CGI programına web tarayıcı ve web sunucusu tarafından gönderilen birtakım gizli bilgilerdir.CGI bunları ayrıştırır,yorumlar ve kendisine bu şekilde gönderilen verileri kullanır.Perl’de ortam değişkenleri ve değerleri %ENV adlı bir özel tabloda tutulurlar.Bazı ortam değişkenleri aşağıda verilmiştir:

**Ortam Değişkeni İçerdiği Bilgi**

DOCUMENT\_ROOT Web sunucusunun göreceli kök dizini

HTTP\_COOKIE Ziyaretçiye ait çerez(eğer varsa)

HTTP\_HOST Sunucunun adı

HTTP\_REFERER Scriptimizin çağrıldığı sayfanın URL adresi

HTTP\_USER\_AGENT Ziyaretçinin tarayıcısının türü

HTTPS Script güvenli bir sunucu üzerinden çağrılıyorsa “on” değerini alır

PATH Sunucuya ait sistem yolu

QUERY\_STRING GET ile sorgulama stringi

REMOTE\_ADDR Ziyaretçinin IP adresi

REMOTE\_HOST Ziyaretçinin bilgisayarının DNS adı

REMOTE\_PORT Ziyaretçinin web sunucuya bağlandığı port

numarası

REMOTE\_USER Ziyaretçinin kullanıcı adı

REQUEST\_METOD GET veya POST ya da diğerleri

REQUEST\_URI İstekte bulunulan dökümanın veya CGI

scriptinin göreceli yolu

SERVER\_FILENAME Şu anki çalışan scriptin tam yolu

SERVER\_ADMIN Webmaster’ın e-posta adresi

SERVER\_NAME Sunucunun kayıtlı DNS adı

SERVER\_PORT Sunucunun takip ettiği port numarası

SERVER\_SOFTWARE Kullandığımız HTTP sunucu yazılımının adı

Her CGI programı için tüm ortam değişkenlerinin kullanılması zorunlu değildir.

## **FORM’LARLA ÇALIŞMAK**

** **Web sayfalarının en güzel imkanlarından biri,kullanıcıların sayfa üzerinde çeşitli bilgiler girerek bunları web sunuculara gönderebilmesidir.Örneğin,ticari amaçlı bir sayfa tasarlıyorsak,bu sayfa üzerine bir sipariş formu yerleştirebilir ve siparişlerin bu form aracılığıyla bize ulaşmasını sağlayabiliriz.Ya da bir veritabanımız varsa ve bunu bir web sayfası aracılığıyla hizmete sunuyorsak,oluşturacağımız bir arama form’u ile kullanıcıların bu veritabanı üzerinde sorgulamalar yapmasını sağlayabiliriz.

Form üzerinde çeşitli seçenekler yerleştirerek kullanıcıların seçenek butonları veya işaretleme kutucukları aracılığıyla bu seçenekleri seçmelerini sağlayabiliriz.

Form’larda aşağıdaki elemanları kullanabiliriz:

**1.**Bilgi giriş alanları (textbox)

**2.**Şifre giriş alanları (password)

**3.**Seçenek butonları (radio)

**4.**İşaretleme kutucukları (checkbox)

**5.**Çok satırlı bilgi giriş alanları (textarea)

**6.**Tekli ya da çoklu seçim yapılabilen listeler (select-option)

**7.**Dosya arama pencereleri (file)

**8.**Sıfırlama (reset) ve gönderme (submit) butonları

**9.**Gizli alanlar (hidden)

Web sayfaları üzerinde form’lar oluşturmak için FORM tag’ı kullanılır.İç içe formlar oluşturulamaz.Bir HTML dökümanı içerisinde birden fazla form kullanılabilir.FORM tag’ının sintaksı şöyledir:

<FORM action=”script.cgi” method=”POST|GET” ENCTYPE=”encryptype”>

……………………

</FORM>

Eğer method belirtilmezse varsayılanı GET’dir.Bu iki metod arasındaki fark şudur:GET ile bazı kısıtlamalar söz konusudur.POST daha güçlüdür ve veri güvenliği için kullanılması şarttır.

## **Basit Bir Sorgulama Formu**

** **Bir HTML formundan bir CGI’ya veri gönderilirken GET ve POST metodları yaygın olarak kullanılmaktadır.GET metodunda,formdan girilen veriler URL’nin bir uzantısı olarak gönderilirler ve QUERY\_STRING adlı ortam değişkeninde tutulurlar.POST metodunda ise veriler,veri blokları(stream) halinde gönderilir ve standart girdi kanalından (stdin) okunurlar.

QUERY\_STRING ortam değişkenine değer atamak için birtakım farklı yollar vardır.Bunlardan ilki bir CGI programını çağırırken URL adresinin sonuna ?-soru işareti ile başlayan eklemeler yapmaktır.URL de ?-soru işaretinden sonra yer alan kısım QUERY\_STRING ortam değişkenine aktarılmış olacaktır.Aynı şey GET metodunu kullanan bir formdan bir CGI’ya veri postalandığında da söz konusudur.GET metodunu kullanan bir form oluşturalım:

<form action=”env.cgi” method=”GET”>

Çalıştığınız bölümü giriniz:

<input type=”text” name=”bolum” size=20><p>

</form>

**NOT:**Bu örnekte “submit-gönder” butonu kullanılmamıştır.GET metodunu kullanan ve tek bir girdi alanı içeren formlarda Enter’a basmakla veri hemen CGI’ya gönderilir.Birden çok girdi alanı içeren formlarda “submit-gönder” kullanmak zorunludur.

bolum=matematik+muh+prg

Burada sol taraftaki değer,formumuzdakı alanın adıdır.Sağ taraftaki değer ise bizim metin kutusuna yazdığımız bilgidir.Buradan da görülmektedir ki boşluk karakterleri +(artı) ile;noktalama işaretleri ve diğer ekstra karakterler %HH şeklinde gönderilmektedirler.Diğer karakterler ise aynen gönderilmektedirler.Eğer form üzerinde birden çok ‘alan’ kullanmışsak her alan-değer çifti birbirlerinden & işareti ile ayrılırlar.

Uzun ve karmaşık veriler göndermek için POST metodu daha uygundur.GET metodu esas itibarıyla kısa,tek alanlı sorgulamalar için,özellikle de veri tabanı sorgulamaları için elverişlidir.

Şimdi birden fazla alan kullanımına örnek verelim:

<form action="env.cgi" method="GET">

Adınızı giriniz:

<input type="text" name="ad" value=”Fatih” size=20><br>

Soyadınızı giriniz:

<input type="text" name="soyad" value=”Taşçı” size=20><p>

<input type="submit" value="gönder">

<input type="reset" value="sil">

</form>

Bu form,girilen verileri env.cgi scriptine şu şekilde gönderecektir:

$ENV{‘QUERY\_STRING’}<- ad=Fatih&soyad=Ta%DE%DF%DC

## **İşaretleme Kutucukları(Checkbox)**

Kullanıcıya seçeneklerden birini veya birkaçını seçebilmesi için formumuza işaretleme kutucukları koyabiliriz.Eğer işaretleme kutucuklarıyla girilen verileri e-posta olarak almak istersek herbirine farklı bir isim(name) vermeliyiz.Şu örneği inceleyelim:

<html>

<body>

<form action="colors.cgi" method="POST">

<input type="checkbox" name=”kirmizi” value=1>Kirmizi<br>

<input type="checkbox" name=”yesil” value=1>Yesil<br>

<input type="submit" value="gönder">

</form> </body> </html>

Bu örnekte kullanıcı,bir ya da daha çok rengi seçebilir.Kullanıcının kutucuğu işaretlemesi durumunda karşı tarafa value ile belirtilen değer (bu örnekte 1) gönderilir.

## **Seçenek Butonları(Radio)**

Seçenek butonları,form içerisinde aynı alan ve farklı value değerleriyle kullanılarak birkaç seçenek arasından kullanıcının sadece bir tanesini seçebilmesini sağlamak için kullanılır.Yine bir örnek verelim:

<input type="radio" name=”color” value=”Kirmizi”>Kirmizi<br>

<input type="radio" name=”color” value=”Yesil”>Yesil<br>

## **Menülerle Çalışmak(Select-option)**

** **Select alanları,kullanım olarak seçenek butonları ile aynıdır,ancak alanlar HTML sayfasında aşağı-çekmeli(pull-down) menüler şeklinde görünürler.Kullanımına şöyle bir örnek verebiliriz:

<SELECT multiple size=10 name=”color”>

<OPTION selected value=”Kirmizi”>Kirmizi</OPTION>

<OPTION selected value=”Yesil”>Yesil</OPTION>

</SELECT>

## **CGI PROGRAMLARININ ÇALIŞTIRILMASI**

** **Programlarımızın Windows NT altında çalışabilmesi için bazı ayarların yapılması gerekmektedir.Öncelikle Windows Option Pack içinde yer alan Internet Information Server(IIS)’ı kurmamız gerekir.Bunun ardından bilgisayarımıza ActivePerl programını kurarız.ActivePerl,Perl derleyicisinin IIS ile beraber çalışabilmesi için gerekli ayarları otomatik yapar.

Kurma işlemlerinin ardından IIS web server’ın Internet Service Manager programını çalıştırarak web server’ın yönetim paneline ulaşırız.

CGI programlarını çalıştırabilmek için c:\\inetpub\\wwwroot dizini altında cgi-bin isminde bir dizin açarız.Programımızı bu dizin altına yerleştiririz.Daha sonra programımızı browser’dan http://localhost/cgi-bin/<programadi>.pl yazarak çalıştırabiliriz.

## **CGI PROGRAM UYGULAMASI**

## **Ziyaretçi Defteri:**

** **Web sayfalarında gördüğümüz ziyaretçi defterlerini yapmanın bir yolu da CGI programları kullanmaktır.Biz de bir ziyaretçi defteri örneği yapacağız.Şimdi kodumuzu açıklamalarıyla yazıyoruz:

**#!/usr/bin/perl**

**print”Content-type:text/html”,”\\n\\n”;******

Server’dan gelen bilgileri değerlendirebilmesi için browser,gelen bilgilerin tipini tespit edebilmelidir.Server ve Client arasında bilgi alışverişi HTTP Header olarak isimlendirilen bu birimler aracılığıyla olur.Content-type,gelen bilgilerin HTML cinsinden olduğunu belirler.Browser üzerinde yapabilmek için yukarıdaki satır yer almalıdır.

**$metod=$ENV{‘REQUEST\_METHOD’};**

**$veri=$ENV{‘QUERY\_STRİNG’};**

**$dizin=”/usr/local/httpd/htdocs”;**

**$dosya=”/ziyaretçi.html”;**

**$path=$dizin.$dosya;**

** **Ziyaretçilerin yaptıkları kayıtları dosyalamak için bir HTML dosyasına ihtiyacımız olacak.$dizin değişkeninde,bu dosyanın sistem üzerinde hangi dizin içinde yer aldığı tespit ediliyor.

Ziyaretçi.html dosyasına $dosya değişkeni üzerinden ulaşabiliriz.$path ise $dizin ve $dosya bileşiminden oluşan ve dosyanın sistem üzerinde yerini tespit eden yolu içeriyor.

Programın ne zaman ziyaretçi defterine kayıt yapılmada kullanılan HTML arayüzünü göstermesi gerektiğini bilmesi gerekiyor.Bunun gerçekleşebilmesi için programa,?ekle şeklinde parametre gönderiyoruz.

GET metodunu ziyaretçi defterine kayıt yapmada kullanılan HTML arayüzünü ve ziyaretçi defterine yapılan kayıtları göstermede kullanacağız.Ziyaretçi defterine kayıt yapmak için POST metodunu kullanacağız.Program başlangıcında REQUEST\_METHOD çevre değişkenini sorgulayarak,hangi metodun kullanıldığını ve kullanılan metoda göre ne yapmamız gerektiğini tespit edebiliriz.Eğer GET metodu kullanılmışsa,o zaman sadece kayıt yapma ve kayıt gösterme işlemleri söz konusu olabilir.Method POST ise,o zaman kayıt yapacağız demektir ve if döngüsünü kullanarak programın gerekli yerine ulaşabiliriz.

**if($metod eq “GET”)**

** {**

** if($veri eq “ekle”)**

** {**

** **ilk if döngüsü,kullanılan metodun GET olup olmadığını sorgular.Eğer GET kullanılmışsa,QUERY\_STRING ve $veri değişkenleri içinde yer alan değer ya ekle ya da göster olacaktır.

İkinci if döngüsü içinde $veri değişkenini sorgulayarak,hangi işlemin yapılması gerektiğini tespit ediyoruz.Eğer $veri=”ekle” ise o zaman program ** ****http://localhost/cgi-bin/ziyaretçi.pl?ekle** şeklinde çalıştırılmıştır ve kullanıcı ziyaretçi defterine kayıt yapmak için HTML arayüzünü görmek istemektedir.

**$kayit\_zamani=&zaman();**

** print<<HTML;**

**<HTML>**

**<BODY>**

**<CENTER><H2>Ziyaretçi Defteri</H2></CENTER>**

**Web sayfamızı ziyaret ettiğiniz için teşekkür ederiz.Lütfen ziyaretçi defterimize kaydınızı bırakınız.**

**<P>$kayit\_zamani</P>**

**<HR>**

**<FORM METHOD=”POST”>**

**<PRE>**

**<EM>İsim: <INPUT TYPE=”text” NAME=”isim” SIZE=40>**

**<EM>E-mail: <INPUT TYPE=”text” NAME=”email” SIZE=40>**

**<EM>URL: <INPUT TYPE=”text” NAME=”url” SIZE=40>**

**</PRE>**

**<P>**

**<EM>Lütfen eklemek istediklerinizi yazınız:<EM><BR>**

**<TEXTAREA ROWS=5 COLS=40 NAME=”yazilan”></TEXTAREA><P>**

**<INPUT TYPE=”submit” VALUE=”EKLE”>**

**<INPUT TYPE=”reset” VALUE=”SİL”>**

**<P>**

**</FORM>**

**<HR>**

**</BODY>**

**</HTML>**

**HTML**

**}**

** **Karşımıza çıkan HTML arayüzündeki formu doldurup,EKLE düğmesine bastıktan sonra,veriler,<FORM>tag’ında yer aldığı gibi POST metodu ile programa gönderilir.Daha öncede belirttiğimiz gibi,POST metodu kullanıldığı için,programımız ,ziyaretçi defterine kayıt yapılmak istendiğini anlar ve programın gerekli yerine geçer.

**elsif($veri eq “goster”)**

** {**

** if(open(DEFTER,”<”.$path))**

** {**

** **Program http://localhost/ziyaretçi.pl?goster parametresiyle çağrıldıysa,ziyaretçi.html içinde yer alan kayıtlar ekrana yazılacaktır.Öncelikle okumak amacıyla ziyaretçi.html dosyasını açıyoruz.

**while(<DEFTER>)**

**{**

** print;**

**}**

** close(DEFTER);**

**}**

** **Dosyayı açtıktan sonra,DEFTER anahtarını kullanarak while döngüsüyle tüm satırları ekrana yazıyoruz.

**else**

**{**

** print”ziyaretçi.html dosyasını açamadım!!!!!”;**

**}**

Eğer ziyaretçi.html dosyası açılamazsa,yukarıda yer alan hata mesajı ekrana yazılır.

**}**

**else**

**{**

**print<<MENU**

**<HTML>**

**<HEAD><TITLE>Menü</TITLE></HEAD>**

**<BODY>**

**<H1>Menü</H1>**

**<P>**

**<HR>**

**<A HREF=”/cgi-bin/ziyaretçi.pl?ekle”>Deftere kayıt yap</A><BR>**

**<A HREF=”/cgi-bin/ziyaretçi.pl?goster”>Kayitlari göster</A><BR>**

**</BODY>**

**</HTML>**

**MENU**

**}**

Program http://localhost/cgi-bin/ziyaretçi.pl şeklinde herhangi bir parametre verilmeden çalıştırıldığı zaman,ekrana bir menü yazar.Bu menü üzerinden deftere kayıt yapılabilir ve yapılan kayıtlar gösterilebilir.

**}**

**elsif($metod eq “POST”)**

**{**

** if(open(DEFTER,”>>”.$path))**

**{**

** **GET metoduyla ilgili program bölümlerini yazdıktan sonra,sırada POST metodu için gerekli program bölümlerinin yazılması var.

Öncelikle $metod değişkenini sorguluyoruz.Eğer kullanılan metod POST ise o zaman kayıt yapmak için hazırladığımız HTML arayüzü kullanılarak,programa veri girişi yapılmıştır.İlk işimiz ziyaretçi.html dosyasını ekleme yapmak için açmaktır.Yapacağımız eklemeler dosyanın en sonuna eklenecektir.

Web sitemiz üzerinde yer alan sayfalara aynı anda birden fazla insan bağlanabilir.Birden fazla kullanıcının aynı anda ziyaretçi defterine kayıt yapmak istemesi sorun yaratabilir.

Bunu önlemek için açılan bir dosyaya açık olduğu sürece başka bir kullanıcı tarafından kayıt yapılmasını önlemek için kilitlememiz gerekiyor.Bu işlemi daha önce öğrendiğimiz flock komutuyla yaparız.

**flock(DEFTER,2);**

** **Fonksiyon içinde kullandığımız 2 rakamı,dosyayı kilitler.Dosyayı tekrar açmak için 8 rakamını kullanacağız.

**$kayit\_zamani=&zaman();**

**&girilen\_bilgileri\_isle(\*FORM);**

HTML arayüzü aracılığıyla yapılan kaydı gözden geçirmek aracılığıyla,&girilen\_bilgileri\_isle() subrutinini kullanıyoruz.Burada önemli olan \*FORM referansıdır.

&girilen\_bilgileri\_isle() subrutini içinde,ziyaretçi defterine eklemek istediğimiz bilgiler yer almaktadır.Herhangi bir şekilde bu bilgilere,subrutinden çıkıp sonra tekrar ulaşmamız gerekiyor.Bunu FORM isminde bir referans kullanarak yapıyoruz.&girilen\_bilgileri\_isle() subrutini içinde HASH tipi bir liste tanımlayacağız.Kayıt için gerekli tüm bilgiler bu liste içine yerleştirilecek.Bir referanstan yaralanarak bu listenin adresini,form referansı içine yerleştireceğiz.Böylece subrutinden çıktıktan sonra,kayıt için gerekli bilgilerin yer aldığı liste silinse bile,bu listenin hafıza adresi FORM içinde olacağı için,bilgilere form referansı üzerinden ulaşmamız mümkün olacaktır.&girilen\_bilgileri\_isle() subrutinini programımızın en sonunda ele alacağız.

**$FORM{‘isim’}=”Anonim Kişi” if !$FORM{‘isim’};**

**$FORM{‘email’}=”Anonim” if!$FORM{‘email’};**

** **&girilen\_bilgileri\_isle() subrutininden gelen bilgilere artık FORM değişkeni üzerinden ulaşabiliriz.Eğer kullanıcı kayıt esnasında bir isim girmediyse,yukarıda yer alan satırla,isim Anonim Kişi olarak değiştirilir.Diğer bir deyişle,kullanıcının isim girip girmediği kontrol ediliyor.Aynı işlemi email kutusu için tekrarlıyoruz.$FORM içinde kullanılan ‘isim’ HTML arayüzünde kullanılan isim kutusunun ismidir.Kutu isimlerini kullanarak,kutulara girilen verilere ulaşıyoruz.

Ziyaretçi kayıt yaparken,ENTER tuşuna basarak,yeni satıra atlayacak ve yazısına devam edecektir.Ziyaretçi.html dosyasına bu ENTER’lar \\n olarak işlenir.Ziyaretçi.html dosyasını bu şekilde görüntülemek istediğimizde,browser (Netscape/explorer) \\n işaretini tanımadığı için yazılanların hepsini uzun bir satır üzerinde görürüz.Herhangi bir şekilde bu \\n işaretlerini,HTML dilinde yeni satır anlamına gelen <BR> ile değiştirmemiz gerekiyor.Bunu aşağıdaki satır yapıyor.

**$FORM{‘yazılan’}=~s/\\n<BR>/g;**

HTML arayüzünde bulunan ‘yazılan’ isimli kutuyu girilen veri içindeki tüm \\n(ENTER) karakterler <BR> olacak şekilde değiştirilir.

Şimdi ziyaretçi.html dosyasına gerekli kaydı yapalım.

**print DEFTER<<EKLE;**

** <P>**

** <B>$kayit\_zamani:</B>**

** Yaziyi birakan:<EM>$FORM{‘isim’}</EM><BR>**

** Email:<EM>$FORM{‘email’}</EM><BR>**

** <P>**

** $FORM{‘yazilan’}**

**EKLE**

** if($FORM{‘url’})**

** {**

** print DEFTER<<URL\_EKLE;**

** <P>**

** $FORM{‘isim’},URL adresi:**

**<A HREF=”$FORM{‘url’}”>$FORM{‘url’}</A>**

**URL\_EKLE**

** }**

if döngüsüyle,kullanıcının bir URL adresi girilip girilmediği kontrol ediliyor.Eğer ‘url’ isimli kutuya URL adresi girilmediyse,ziyaretçi.html dosyasına URL adresi eklenmiyor.

**print DEFTER”<P><HR>”;**

** **Her kaydın altına bir çizgi çekilerek,kayıtlar birbirinden ayrılır.

**flock(DEFTER,8);**

**close(DEFTER);**

** **Kayıt işlemi sona erdikten sonra,flock() fonksiyonunu kullanarak,kilidi açıyoruz ve bunun ardından close() fonksiyonu ile dosyayı kapatıyoruz.

Ziyaretçi kaydı yapıldıktan sonra,ekrana bir teşekkür mesajı yazıyoruz.

**print<<TESEKKURLER**

**Ziyaretçi defterimize kayıt yaptığınız için teşekkür ederim.**

**<A HREF=”/cgi-bin/ziyaretçi.pl”>Geriye</A>**

**TESEKKURLER**

** }**

**else**

** {**

**print”ziyaretçi.html dosyasını yazmak üzere açamadım”;**

** }**

**}**

**else**

**{**

**print”Kullandığınız metot geçerli değil.”;**

**}**

**exit(0);**

Ana program kodunu böylece noktalamış olduk.Şimdi ana program içinde kullandığımız subrutinleri yazalım:

**sub zaman**

**{ **

** ($san,$dak,$saat,$gun,$ay,$yil)=localtime(time);**

** return “$gun.$ay.$yil-$saat:$dak:san”;**

** }**

localtime(time) fonksiyonu kullanarak,$san,$dak,$saat,$gun,$ay,$yil değişkenlerine saniye,dakika,saat,ay,gün,yıl verilerini eşitliyoruz.ENTER komutu ile zaman ve tarih string olarak ana programa geri gönderilir.$kayit\_zamani=&zaman() şeklinde bir tanımlamayla ana programda,zaman() subrutini tarafından geri gönderilen zamanı kullanabiliriz.

Aşağıdaki subrutini kullanarak,kullanıcının girdiği bilgilerin kodunu çözüyoruz.

** sub girilen\_bilgileri\_isle()**

**{ **

** local (\*FORM\_BILGILERI)=@\_;**

** local (**

** $veri,**

** @kutu\_deger\_cifti,**

** $elem,**

** $anahtar,**

** $deger);**

Subrutini içinde kullanacağımız değişkenleri deklare ettikten sonra,kodu yazmaya devam ediyoruz.

**read(STDIN,$veri,$ENV{‘CONTENT\_LENGTH’});**

** **POST metodunu kullandığımız için read fonksiyonu ile verileri okumamız gerekiyor.

Birden fazla kutu kullndığımız zaman,veriler & işareti ile birbirine eklenir.

** @kutu\_deger\_cifti=split(/&/,$veri);**

** foreach $elem (@kutu\_deger\_cifti)**

** {**

** ($anahtar,$deger)=split(/=/,$elem);**

** **Foreach döngüsüyle @kutu\_deger\_cifti listesi içinde bulunan elemanlara ulaşıyoruz.Elemanlar kutu1=deger1,kutu2=deger2 şeklinde olduğundan,asıl verilere ulaşabilmemiz için,tekrar split() fonksiyonunu kullanarak,elemanları = işaretinden iki parçaya bölmemiz gerekiyor.

**$deger=~tr/+//;**

** $deger=~s/%(\[/dA-Fa-f\]\[/dA-Fa-f\])/pack(“C”,hex($1))/eg;**

HTML arayüzünde bulunan EKLE düğmesine basınca, veriler aşağıdaki şekilde CGI programına gönderilir:

isim=Ahmet+Yıldırım&email=ahmet%40avrasya.com…

Kullanıcının isim olarak Ahmet Yıldırım olduğunu düşünün. Veri iki kelimeden oluştuğu ve arada bir boşluk olduğu için, isim ve soyad Ahmet+Yıldırım şeklinde kodlanır. Ziyaretçi defterine kayıt yapmadan önce, + işaretini uzaklaştırmamız gerekir. Bu işlemi tr/+// kullanarak gerçekleştirebiliriz.

Perl içinde özel anlam taşıyan işaretler vardır: @, : / \\. Bu işaretler, kullanıcının girdiği verilerde özel bir anlam taşımadığı için, Perl derleyicisi tarafından yorumlanmaması gerekir. Bunu önlemek amacıyla, bu özel işaretler Hex formatında olmak üzere ASCII koduna çevrilir ve başına % işareti eklenir.

Yukarıda kullanılan %40, aslında bir @ işaretinin hex ASCII kodudur. Desimal sistemde hex 40, 64 sayısına eşittir.

email=ahmet%40avrasya.com şeklinde kodlanmış bir veriyi tekrar ahmet@avrasya.com olacak şekilde normale dönüştürmemiz gerekiyor. Bu görevi aşağıdaki satır yerine getiriyor.

$deger=~s/%(\[/dA-Fa-f\]\[/dA-Fa-f\])/pack(“C”,hex($1))/eg;

** **%(\[/dA-Fa-f\]\[/dA-Fa-f\])/ kalıbı, % işaretiyle başlayan tüm kelimeleri tarar. Eğer % işaretinden sonra herhangi bir rakam (/d) ve harf \[A-Fa-f\]** **bulursa, bu, heksa koda çevrilmiş bir özel işaret anlamına gelir ve tekrar normal hale getirilmesi gerekmektedir. pack() fonksiyonunu kullanarak, bu heksa sayıyı (%40) tekrar desimal sayıya (64) çeviriyoruz.%40, 64 desimal rakamına çevrildikten sonra, değer değişkeni içinde yer alan heksa sayılar daha önce tanıştığımız ~s/ regüler terim işlemiyle desimal sayılarla değiştirilir.

(\[/dA-Fa-f\]\[/dA-Fa-f\]) parantezler içinde yer alan terim sonuçta heksadesimal cinsinden bir rakamı belirler (örneğin 20, 3B, 4A gibi). Parantezler içinde yer alan bu rakama ($1) değişkeni üzerinden ulaşabiliriz. Pack () fonksiyonuna hex ($1) şeklinde veri girişi yaptığımızda, pack ve hex fonksiyonları bu heksadesimal formatında olan rakamı desimal bir sayıya çevirirler. Kullanılan eg opsiyonları, satır içinde kullanılan tüm %heksa sayıları bularak, desimal bir rakama çevirir.

**$FORM\_BILGILERI{$anahtar}=$değer,**

** }**

**}**

** **Kullanıcının girdiği bilgileri HASH tipi bir listede saklıyoruz.Kullanıcının girdiği bilgileri aşağıdaki formatta hash içine yerleştireceğiz.

%FORM\_BILGILERI={

“isim”=>”Ahmet Yıldırım”,

“email”=> ahmet@avrasya.com,

“url”=> http://www.avrasya.com,

“yazılan”=>”Burada yazılanlar yer alacak”};

Böylece ziyaretçi defteri örneğimizi tamamlamış olduk.Yazılan kodun tamamı aşağıdaki gibidir:

**#!/usr/bin/perl**

**print”Content-type:text/html”,”\\n\\n”;**

**$metod=$ENV{‘REQUEST\_METHOD’};**

**$veri=$ENV{‘QUERY\_STRİNG’};**

**$dizin=”/usr/local/httpd/htdocs”;**

**$dosya=”/ziyaretçi.html”;**

**$path=$dizin.$dosya;**

**if($metod eq “GET”)**

**{**

**if($veri eq “ekle”)**

**{**

**$kayit\_zamani=&zaman();**

**print<<HTML;**

**<HTML>**

**<BODY>**

**<CENTER><H2>Ziyaretçi Defteri</H2></CENTER>**

**Web sayfamızı ziyaret ettiğiniz için teşekkür ederiz.Lütfen ziyaretçi defterimize kaydınızı bırakınız.**

**<P>$kayit\_zamani</P>**

**<HR>**

**<FORM METHOD=”POST”>**

**<PRE>**

**<EM>İsim: <INPUT TYPE=”text” NAME=”isim” SIZE=40>**

**<EM>E-mail: <INPUT TYPE=”text” NAME=”email” SIZE=40>**

**<EM>URL: <INPUT TYPE=”text” NAME=”url” SIZE=40>**

**</PRE>**

**<P>**

**<EM>Lütfen eklemek istediklerinizi yazınız:<EM><BR>**

**<TEXTAREA ROWS=5 COLS=40 NAME=”yazilan”></TEXTAREA><P>**

**<INPUT TYPE=”submit” VALUE=”EKLE”>**

**<INPUT TYPE=”reset” VALUE=”SİL”>**

**<P>**

**</FORM>**

**<HR>**

**</BODY>**

**</HTML>**

**HTML**

**}**

**elsif($veri eq “goster”)**

**{**

** if(open(DEFTER,”<”.$path))**

**{**

**while(<DEFTER>)**

**{**

**print;**

**}**

**close(DEFTER);**

**}******

**else**

**{**

**print”ziyaretçi.html dosyasını açamadım!!!!!”;**

**}**

**}**

**else**

**{**

**print<<MENU**

**<HTML>**

**<HEAD><TITLE>Menü</TITLE></HEAD>**

**<BODY>**

**<H1>Menü</H1>**

**<P>**

**<HR>**

**<A HREF=”/cgi-bin/ziyaretçi.pl?ekle>Deftere kayıt yap</A><BR>**

**<A HREF=/cgi-bin/ziyaretçi.pl?goster”>Kayitlari göster</A><BR>**

**</BODY>**

**</HTML>**

**MENU**

**}******

**}**

**elsif($metod eq “POST”)**

**{**

**if(open(DEFTER,”>>”.$path))**

**{**

**flock(DEFTER,2);**

**$kayit\_zamani=&zaman();**

**&girilen\_bilgileri\_isle(\*FORM);**

**$FORM{‘isim’}=”Anonim Kişi” if !$FORM{‘isim’};**

**$FORM{‘email’}=”Anonim” if!$FORM{‘email’};******

**$FORM{‘yazılan’}=~s/\\n<BR>/g;**

**print DEFTER<<EKLE;**

**<P>**

**<B>$kayit\_zamani:</B>**

**Yaziyi birakan:<EM>$FORM{‘isim’}</EM><BR>**

**Email:<EM>$FORM{‘email’}</EM><BR>**

**<P>**

**$FORM{‘yazilan’}**

**EKLE**

**if($FORM{‘url’})**

**{**

**print DEFTER<<URL\_EKLE;**

**<P>**

**$FORM{‘isim’},URL adresi:**

**<A HREF=”$FORM{‘url’}”>$FORM{‘url’}</A>**

**URL\_EKLE**

**}**

**print DEFTER”<P><HR>”;**

**flock(DEFTER,8);**

**close(DEFTER);******

**print<<TESEKKURLER**

**Ziyaretçi defterimize kayıt yaptığınız için teşekkür ederim.**

**<A HREF=”/cgi-bin/ziyaretçi.pl”>Geriye</A>**

**TESEKKURLER**

**}**

**else**

**{**

**print”ziyaretçi.html dosyasını yazmak üzere açamadım”;**

**}**

**}**

**else**

**{**

**print”Kullandığınız metot geçerli değil.”;**

**}**

**exit(0);**

**sub zaman**

**{ **

**($san,$dak,$saat,$gun,$ay,$yil)=localtime(time);**

**return “$gun.$ay.$yil-$saat:$dak:san”;**

**}******

**sub girilen\_bilgileri\_isle()**

**{ **

**local (\*FORM\_BILGILERI)=@\_;**

**local ($veri,@kutu\_deger\_cifti,$elem,$anahtar,$deger);******

**read(STDIN,$veri,$ENV{‘CONTENT\_LENGTH’});**

**@kutu\_deger\_cifti=split(/&/,$veri);**

**foreach $elem (@kutu\_deger\_cifti)**

**{**

**($anahtar,$deger)=split(/=/,$elem);**

**$deger=~tr/+//;**

**$deger=~s/%(\[/dA-Fa-f\]\[/dA-Fa-f\])/pack(“C”,hex($1))/eg;**

**$FORM\_BILGILERI{$anahtar}=$değer,**

**}**

**}******

PAGE

PAGE 20

PAGE 1

---
*Kaynak: `PERL VE CGI/PERL VE CGI/PERL ile CGIson.doc` — Bucle — 2001*
