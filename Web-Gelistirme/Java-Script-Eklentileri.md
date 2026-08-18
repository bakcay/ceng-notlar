# Java Script Eklentileri

**JavaScript******

Java, C++ gibi derleme tabanlı bir dil olmasına rağmen, tek bir derlenmiş programın her tip bilgisayarda çalışabilmesi sağlanacak şekilde değiştirilmiştir. Fakat JavaScript bu tür bir programlama dili değildir. Yorumlanması için bir tarayıcıya ihtiyaç duyar. Bu yüzden script dilidir. Html dosyasını içine gömülüdür. Javascript , Netscape firması tarafından C dilinden esinlenilerek yazılmıştır. Yazılma amacı Html'in sahip olmadığı bazı özelliklerin web sayfalarında kullanılmak istenmesidir. Netscape firması bu konuya ağırlık vererek JavaScript script dilini internet ortamına kazandırmıştır. Kısaca Java derleme tabanlı bir dil, JavaScript ise küçük program parçalarıdır.

Netscape ve Internet Explorer tarayıcıları JavaScript kodlarını farklı yorumlar. Netscape firması JavaScript dilini hazırladığında Microsoft firması bu dilin özelliklerini veya yazılım tarzını tam anlamıyla Internet Explorer'a eklemedi. Kendi yazım kurallarını belirledi. Bu yüzden JavaScript kodu yazarken bu iki tarayıcı özelliklerini de göz önünde bulundurulmalıdır. Fakat bu her kodda karşımıza çıkmaz.

**2.2.1 JavaScript'in genel Özellikleri ******

• Javascript kodlarını yazmak için Windows kullanıcıları için NotePad , Mac. kullanıcıları için Simple Text yeterlidir.

• JavaScript kodları etiketi ile biter.

• Etiketi JavaScript'i anlamayan eski sürüm tarayıcıların bu kısmı geçmeleri içindir.

• Genellikle yazım tarzı

| <script> <!-- JavaScript kodları --> </script> |
| --- |

şeklindedir. Tüm JavaScript kodları HTML ye gömülü olarak bu deyimler arasına yazılmalıdır.

• JavaScript'te açıklama işaretleri tek satır ise // ile başlar. Eğer açıklamanız bir satırdan fazla ise /\* ile başlar \*/ ile biter.

| // bu satır kullanılacak değişkenlerin tanımlanması /\* açıklama satırı 1 açıklama satırı 2 açıklama satırı 3 \*/ |
| --- |

JavaScript kodları Html kodların arasında yer alır. Veya uzantısı js olan dosyalarda saklanarak yine Html içerisinden çağırılır. Java Appletleri gibi Html'den ayrı bir unsur değildir. Javascript Html'in bir parçasıdır.

• Kullanılacak yere göre Html'in içerisinde kullanılır. Fakat genelde < head ></head > etiketleri arasında kullanılır.

• Javascript kodları bittiğinde elinizde asla kendi başına çalışan uzantısı exe veya com olan bir dosya olmaz. Her zaman için tarayıcı tarafından yorumlanması gerekir. Yorumlanması demek Javascript kodunun çalışması anlamındadır.

• Nesne ve buna uygulanan olaylar ile ilgili bir takım görevleri vardır. Javascript kullandığı her unsuru nesne olarak algılar. Siz bu nesneleri tıklamak , üzerine gelmek , üzerinde çıkmak gibi olaylar ile çalıştırırsınız ki bu da Javascript'in ziyaretçi ile etkileşmesi demektir.

• Genel öğrenim yapımız diğer programlama dillerine nazaran biraz farklı olacaktır. Bu Javascript'in bir script dili olmasında ileri gelir.

**2.2.2 Değişkenler ******

**Genel Değişken Özellikleri ******

Değişkenler Javascript'te ve diğer programlama dillerinde olduğu gibi bilgi depolamak bu bilgiyi kullanmak amacıyla kullanılırlar. Değişkenler var komutu ile oluşturulurlar. Karakter olarak kullanıldıklarında işlem yapılamazlar. Nümerik olarak kullanıldıklarında ancak işlem yapabilirler.

| var sayi; var sayi1=10; var yazi1="10"; |
| --- |

Burada birinci satırdaki sayi değişkeni script kodunun herhangi bir yerinde kullanılmak üzere oluşturulmuştur. İkinci satırda sayi1 adındaki değişkenin değeri hemen o satırda = ifadesinden sonra verilmiştir. Böyle değişken tanımı da yapılabilir. Üçüncü satırda ise değişkenin karakter ifadesi olarak kullanımını göstermektedir. Burada önemli olan karakter değişkenlerin alıntı "" ifadesinin arasında kullanılmasıdır. Her değişkenden sonra ; işareti konulmalıdır. Tarayıcı, bir başka komut satırına geçtiğini bu yol ile anlar.

| var sayi1=10; var sayi2=20; var sayi3=sayi1+sayi2; |
| --- |

Birinci ve ikinci satırlarda değişkenler oluşturulmuştur. Üçüncü satırdaki ise sayi3 değişkeni ile diğer iki değişken toplanmıştır. Burada önemli olan işlem yapmak istediğimizde değişken değerinin alıntı "" işaretlerinin arasına *konmamasıdır*. Üçüncü satırı - ileride göreceğimiz write() fonk-

siyonu ile - tarayıcıda yazdırırsak göreceğimiz değer 30'dur.

| var sayi1="10"; var sayi2="20"; var sayi3= sayi1+sayi2 ; |
| --- |

Bir önceki örnekten farklı olarak değişken değerlerinin alıntı işaretleri içerisinde yazılmıştır. Eğer sayi3 adlı değişken tarayıcıda yazdırılırsa göreceğimiz ifade 1020 ifadesidir. Yani tarayıcı karakter olarak tanımladığımız değişkenleri ardada ekledi. Burada unutulmaması gereken şey bunun sadece + işleminde geçerli olmasıdır. Diğer işlem türlerinde bu tür bir sonuç alınamaz.

**Değişkenlere Ad Verirken Uyulması Gereken Kurallar.
**
1) Değişken isimleri harf veya \_ karakteri ile başlayabilir. Rakam kullanmak istersek 2. karakterden

sonra kullanılabilr. Yani değişkenin ilk karakteri rakam olamaz. Değişken isimlerine örnekler;

| var url="turkport"; // doğru var \_rakam=12; // doğru var a1=123; // doğru var 3uzler="üçüzler" // yanlış var x1; // doğru |
| --- |

2) Değişken tanımlarken bir veya birden fazla boşluk bırakmak tanımlama açısından herhangi bir

sorun teşkil etmez.

3) Değişken adı verirken kullandığımız harflerin büyük veya küçük olması bazı tarayıcılarda fark

etmezken çoğu tarayıcıda farklı bir değişken anlamındadır. Yani;

| var say=1; var Say=1; |
| --- |

Birçok tarayıcıda farklı değişkenler olarak algılanır.

**Değişkenlerin işlem operatörleri ile kullanımı ******

Değişkenlere işlem yaptırabilecek işlemcilere operatör denir. JavaScript’te 4 çeşit operatör vardır.

• Aritmetik operatörler

• Karşılaştırmak operatörleri

• Mantıksal operatörler

• Özel operatörler

**Aritmetik Operatörler ******

Her zaman kullandığımız bu operatörler +, - , \* , / , % 'dir.

| var i=10; var j=11; var k=12; var m,n; m=i\*j+k; n=i\*(j+k); |
| --- |

Değişkenler i,j,k,m,n

i=10;j=11;k=12;m,n ye başlangıçta bir değer atanmamış.

m=i\*j+k = 10\*11+12 = 122

n=i\*(j+k)= 10\*(11+12)= 230

| var a=100; var b=9; var c=100%9; //c=100/9 dan kalan değerdir.(Yani 100 Mod(9) göre değeri) |
| --- |

Burada c değişkenin değeri 100/9'un kalanı 1'dir. Yani c değişkeninin değeri 1 olacaktır. Diğer -(eksi) ve / (bölme) operatörlerinin işlemleri kendilerine atanan çıkartma ve bölme işlemidir.Bu operatörlerin kısa kullanımı içinde Javascript bize kolaylık sağlar. Bu operatörleri sıralamak istersek;

-= : \*= : /= : %= : ++ : --

| x+=y; //x=x+y anlamında x-=y; //x=x-y anlamında x\*=y; //x=x\*y anlamında x/=y; //x=x/y anlamında x%=y; //x=x%y anlamında x++; //x=x+1 anlamında x--; //x=x-1 anlamında |
| --- |

| var x,y,z; x=10; y=20; z=30; x++; x+=y; z--; y\*= z; |
| --- |

Değişkenler: x,y,z

x=10;y=20;z=30;

x++ x=x+1 x=10+1=11

x+=y x=x+y x=11+20=31

z-- z=z-1 z=30-1=29

y\*=z y=y\*z y=20\*29=580

**Karşılaştırma operatörleri ******

Bu operatörler değişkenlerin birbirleri ile karşılaştırılmak istendiğinde kullanılır.
Bu operatörler ise;
== operatörü iki değişkenin birbirine eşitliğini kontrol eder.
!= operatörü iki değişkenin birbirine eşit olmadığı durumlarda kullanılır.

< operatörü bilindiği üzere küçüktür operatörüdür. Soldaki değişkenin sağdakinde küçüklüğünü

kontrol eder.
<= soldaki değişkenin sağdaki değişkene küçük eşitliğini kontrol eder.
> soldaki değişkenin sağdaki değişkene göre büyük olup olmadığını kontrol eder.
>= soldaki değişkenin sağdaki değişkene büyük eşitliğini kontrol eder.

**Mantıksal Operatörler ******

Bu tip operatörler iki değişkene bağlı karşılaştırılmaların yapılmak istendiği durumlarda kullanılır.
Operatörler && , || , ! operatörleridir.
&& And (ve) operatörü iki değişkenin de değeri doğru olması istendiğinde kullanılır.
|| Or (veya) operatörü iki değişkenden en az birinin doğru olması durumu istediğinde kullanılır.
! Not (değil) operatörü değişkenin değeri doğru ise yanlış , yanlış ise doğru olması istendiği

durumlarda kullanılır.

**Özel karşılaştırma Operatörü ******

Bu operatör iki değişken(deg) arasında karşılaştırma yapmanın en sade ve kısa yoludur.
Operatörün kullanım biçimi :

| deg1 \[istenen karşılaştırma operatörü\] deg2 ? deg3 :deg4 |
| --- |

| a < b ? c : d |
| --- |

Burada a değişkeninin b değişkeninden küçük olup olmadığı karşılaştırılıyor. Buna göre cevap doğruysa işlemin sonucu c değişkeninin değeri değilse d değişkeni oluyor.

Örnek 1:

| <html> <head><title>ornek01.html</title></head> <body> Değişkenlerin ilk değerleri<br> i=1 j=2 k=3 m=4 n=5 p=6 q=7<br> Değişkenlerin son değerleri<br> <script Language="JavaScript 1.2"> <!— var i=1; var j=2; // Değişkenler tanımlanıyor... var k=3; var m=4; var n=5; var p=6; var q=7; i+=j; // i=i+j anlamında j++; // j=j+1 anlamında k--; // k=k-1 anlamında m=m+k; n\*=j; // n=n\*j anlamında i < j ? 3 : 1 ; // i<j ise işlemin sonucu 3 değilse 1 k <= n ? 0 : 1 ; k=2 && j=5 ? p : q ; i=2 \|\| j=3 ? m : n ; p!=2 ? k : 10 ; // p,2 den farklı ise işlemin sonucu k yoksa 10 document.write(“i=”,i,”j=”,j,”k=”,k,”m=”,m,”n=”,n,”p=”,p,”q=”,q); --> </script> |
| --- |

Değişkenler i,j,k,m,n,p,q i=1;j=2;k=3;m=4;n=5;p=6;q=7;

İfade Anlamı Sonucu

i+=j i=i+j i=1+2=3

j++ j=j+1 j=2+1=3

k-- k=k-1 k=3-1=2

m=m+k - m=4+2=6

n\*=j n=n\*j n=5\*3=15

i<j?3:1 3<3 mü? Hayır,1

k<=n?0:1 2>=15 mi? Evet, 0

k=2 && j=5?p:q k=2 ve j=5 mi? Hayır,7

i=2 || j=3?m:n i=3 veya j=3 mü? Evet, 6

p!=2?k:10 p,2 den farklı mı? Hayır,10

**2.2.3 Ekrana Çıktı ve Klavyeden Bilgi Girişi******

**prompt()******

Ziyaretçiden bilgi alma iki tür JavaScript komutuyla gerçekleşir. Birisi prompt diğeri ise Form yoluyla bilgi alınması. Form yoluyla alınan bilgiler formun Html üzerinde yer alması yüzünden prompt komutu ile birbirinden ayrılır. prompt komutu ile Html sayfasından hariç bir pencere açılır. Alınmak istenen bilgi ziyaretçiye bu yol ile sorulur ve hemen altındaki boşluk yardımıyla cevap alınır.

| prompt ("Sorulan soru" , "Cevap örneği") |
| --- |

Bu komutun yorumu şudur. Html üzerinde Html'den bağımsız bir pencere aç. (bu prompt komutu ile yapılır) İlk çift tırnak içerisinde olan kelime veya kelime grubu, pencerenin üst kısmında ve değiştirilemeyen kısımdır. Burada soru veya pencerenin niçin açıldığı ile ilgili bir açıklama verilir. İkinci çift tırnakta ise doldurulacak olan cevap satırının içinde seçili bir haldedir. Bu ise genel olarak

cevap örneği olarak ziyaretçiye sunulur. Kullanılması zorunlu değildir. Kullanılmadığınızda *undefined* gibi tanımlanmamış uyarısı alınır.

| prompt("Tarayıcınızın Türü ?" ,"Cevabı ie veya nn olarak veriniz"); |
| --- |

Şimdi kullanıcıdan nasıl bilgi alınacağını gördük fakat bu bilgiyi nasıl kullanabiliriz ? Bu sorunun cevabı prompt komutunu var ile bir değişkene atmak suretiyle kullanabiliriz.

| var tara=prompt ("Tarayıcınızın Türü?" ,"Cevabı ie veya nn olarak veriniz"); |
| --- |

Biz bu satır ile, ziyaretçiye prompt komutu ile tarayıcısı soruldu ve bunu var değişken tanımlama komutuyla tara değişkenine atandı. Ziyaretçiden alınan bu bilgi sonucunda tara değişkeni ya ie yada nn değerini alacaktır. Biz daha sonraki satırlarda bu değişkeni belli bir koşul koyarak kullanabiliriz.

**write()******

Html dosyasına yazı yazdırma komutu write dır. Bu kodun yazım kuralları;

| document.write ("görüntülenmek istenenler" , değişken\_ismi ); |
| --- |

Javascript html üzerinde yazı yazmak istediğinde write komutunu tek başına kullanamaz. Bunun için document fonksiyoneli (yardımcısı manasında) ile birlikte kullanılır. document.write komutundan sonra parantez açılır. Daha sonra yazılmak istenen sıraya göre değişken ismi veya görüntülenmek istenenler yazılır. *Değişkenler çift tırnak içerisinde yazılmazlar*. Sadece görüntülenmek istenenler çift tırnak içerisinde yazılır.

Şimdi prompt komutu ile write komutunu birleştirerek bir kod hazırlayalım. Bu kodumuzda prompt aracılığıyla ziyaretçiye adını sorup ad değişkenine atanıyor. Daha sonra bu değişkeni write komutu yardımıyla ziyaretçiye Merhaba deniyor.

Örnek 2:

| <html> <head><title>ornek02.html</title></head> <body> <script> var isim = prompt ("Adınız" , "Küçük harf veya büyük harf farketmez" ); document.write ("Merhaba " , isim , " !" ); </script> </body> </html> |
| --- |

Aynı örnekte Merhaba dedikten sonra alınan ismin bir alt satırda görüntülenmesini istiyorsak bunu Javascript'e şu şekilde yaptırabiliriz.

| document.write ("Merhaba" , "<br>" , isim) ; |
| --- |

Bu tür (yani <br> türünde) Html deyimlerinin tümünü Javascript'e yaptırabilirsiniz.

**alert()******

Ekranın girilen iletiyi yazar.

| alert(“ileti...”) |
| --- |

Örnek 3:

| <html> <head><title>ornek03.html</title></head> <body> <script> alert("Sayfama Hoşgeldiniz") </script> </body> </html> |
| --- |

**2.2.4 Koşul Yapıları******

Hiçbir bilgisayar kendine göre yorum yapamaz. Bizim verdiğimiz belli kıstasları göz önünde bulundurarak seçim yapar. Diğer programlama dillerinde olduğu gibi JavaScript’te de koşul yapıları mevcuttur.

**if****,****if-else**** ******

Javascript'te çoğu dilde olduğu gibi koşul yapısının kodu if deyimidir. Yani if deyimi koşullu işlem yapma deyimidir. if ve else tek bir karşılaştırma deyimi olup else in kullanımı isteğe bağlıdır. Eğer koşul olumlu ise küme yürütülür ve else den sonraki küme atlanır; olumsuz ise, if den sonraki küme atlanır ve eğer varsa, else den sonraki küme yürütülür.

if deyiminin kullanımı:

| if (koşul){ ⇓ küme başlangıcı ... deyimler;\[küme\] ... } ⇓ küme sonu |
| --- |

if-else deyimlerinin kullanımı:

| if(koşul){ /\* koşul olumlu ise \[küme1\] \*/ ... /\* koşul olumsuz ise \[küme2\] \*/ deyimler;\[küme1\] /\* yürütülür. \*/ } else{ ... deyimler;\[küme2\] ... } |
| --- |

Örnek 4:

| <html> <head><title>ornek04.html</title></head> <body> <script> var parola=1999; var gir=prompt(“Parola:”,”Parolayı girin?”); if(gir==parola){ document.write(“Parola kabul edildi”,”<br>”,”Sayfa Açılıyor...”) } else{ document.write(“Parola kabul edilmedi”,”<br>”,”İyi düşün!..”) } </script> </body> </html> |
| --- |

Örnek 5:

| <html> <head><title>ornek05.html</title></head> <body> <script language="JavaScript"> <!-- //eski sürüm tarayıcılardan kodumuzu saklayalım var gun = prompt ("Bugün günlerden ne ?" ,"lütfen küçük harf kullanınız"); if (gun=="pazar") { document.write ("Bugün ",gun ," olduğuna göre hatfa sonundayız" ,"<br>") document.write ("<b>" , "İyi tatiller.." , "</b>") } else { document.write ("Bugün pazar olmadığına göre Hafta sonu değil!" ,"<br>") document.write ("<u>",**”**İyi çalışmalar..",**”**</u>") } //saklamayı bitir--> </script> </body> </html> |
| --- |

**switch()******

Bir değişkenin içeriğine bakarak, programın akışını bir çok seçenekten birine yönlendiren bir karşılaştırma deyimidir. Bu deyim BASIC dilinde ONGOSUB ve Pascal dilinde Case deyimine benzerdir. C dilinde ise karşılığı aynıdır. Bu deyimin genel yazım biçimi;

| switch(değişken){ case “sabit1” : ...deyimler; case “sabit2” : ...deyimler; ... case “sabitN” : ...deyimler; } |
| --- |

| var sec; sec = prompt ("Çıkmak istiyor musunuz " ,"Evet(E/e);Hayır(H/h)") switch (sec){ case "e" : case "E" : document.write ("Tekrar hoşgeldiniz") //yapılması istenen işlemler case "h": case "H" : document.write ("Bizi tercih ettiğiniz için teşekkürler") break; //Çıkılması istendiği için döngüyü kesmek için break komutunu //kullanıyoruz. İleride break deyimi açıklanacaktır. |
| --- |

**2.2.5 Döngü Deyimleri******

Bu tip deyimler bir kümenin belli bir koşul altında yinelenmesi için kullanılır. while,do...while ve for olmak üzere üç tip döngü deyimi vardır.Javascript'te diğer programlama dillerinde olduğu gibi istediğiniz işlemi 2 veya daha fazla kez yaptırmak için belli program kodları mevcuttur.

**while******

Tekrarlama deyimidir. Bir küme ya da deyim while kullanılarak bir çok kez yinelenebilir. Yinelenmesi için koşul sınaması çevrim başında yapılır. Genel yazım biçimi;

| while(koşul){ ... döngüdeki deyimler; \[küme\] ... } |
| --- |

Koşul olumlu olduğu sürece çevrim yinelenir. İki veya daha çok koşul mantıksal operatörler birleştirilerek verilebilir.

Örnek 6:

| <html> <head><title>ornek06.html</title></head> <body> <script Language="JavaScript"> <!-- var yil=0;var para=1000; while(para<50000){ para+=para\*0.75; // para=para+para\*0.75; yil++; } document.write("1000 TL ",yil," sonra ",para," TL olur.") --> </script> </body> </html> |
| --- |

**do...while******

Bu deyim while dan farkı, koşulun döngü sonunda sınanmasıdır. Yani koşul sınanmadan çevrime girilir ve döngü kümesi en az bir kez yürütülür. Koşul olumsuz ise döngüden sonraki satıra geçilir.

Genel yazım biçimi;

| do{ ... döngüdeki deyimler; ... }while(koşul); |
| --- |

Örnek 7:

| <html> <head><title>ornek07.html</title></head> <body> <script Language="JavaScript"> <!-- do{ var sayi=prompt("Girilen Sayının Karesi","Bir sayı giriniz"); document.write("Sayı=",sayi," Karesi=",sayi\*sayi,"<br>") }while(sayi>0); document.write("Çevrim sona erdi...") --> </script> </body> </html> |
| --- |

**for******

Diğer döngü deyimleri gibi bir öbeği bir çok kez tekrarlamakta kullanılır. Koşul sınaması while da olduğu gibi girmeden yapılır. Bu döngü deyimin içinde diğerlerinden farklı olarak başlangıç değeri ve döngü sayacına sahip olmasıdır.

Genel yazım biçimi;

| for(başlangıç;koşul;artım){ ... döngüdeki deyimler; ... } |
| --- |

Örnek 8:

| <html> <head><title>ornek08.html</title></head> <body> <script language="JavaScript"> <!-- for(sayi=0;sayi<=10;){ sayi++; document.write( "5 \* ",sayi," =",5\*sayi,"<br>") } --> </script> </body> </html> |
| --- |

Örnek 9:

| <html> <head><title>ornek09.html</title></head> <body> <script> var i;var fact=1; var sayi=prompt(“Faktoriyel Hesabı”,”Faktoriyeli hesaplanacak sayı”) for(i=1;i<=sayi;i++){ fact\*=i; } document.write(sayi,“ != ”,fact) </script> </body> </html> |
| --- |

Not: iç-içe bir çok döngü kullanılabilir.

**break**** ve ****continue**** İfadeleri ******

Döngü deyimleri içindekiler yürütülürken, çevrimin, koşuldan bağımsız kesin olarak sonlanması gerektiğinde veya döngünün bir sonraki çevrime geçmesi istendiğinde bu deyimler kullanılır.

Örnek 10:

| <html> <head><title>ornek10.html</title></head> <body> <script> var x=0;var y=1;var z=6; do{ y++; x+=y; if(x>=z) {break; } // while deki koşula bakılmaksızın döngü sonuna gider. if(y<=3) {continue;}// y<=3 olduğu sürece döngü bir sonraki çevrime girer. }while(x<10); // x<10 olduğu sürece çevrime devam et. document.write(”x=”,x ,”y=”,y ,”z=”,z); </script> </body> </html> |
| --- |

**2.2.6 Fonksiyon Kavramı ******

Çoğu zaman Javascript kodunuzda bir işlemin birden fazla yapılması gerekebilir. Hatta kimi zaman Javascript'e bir işlem yaptırmadan önce başka bir işlemi yaptırmak istenebilir. İşte bu tür tekrarlanan işin yapılması için gerekli işlem ve komut gruplarına Fonksiyon adı verilir. Fonksiyonlar genelde, filanca isimli gruptaki işlemleri yap oradan bir değer al bunu filanca isimli gruba götür gibi işlemler için kullanılır.Bu tür komut sistemleri Javascript'te en çok kullanılan komut türlerindendir. Fonksiyonun yazım kuralları şu şekildedir ;

| function fonksiyon\_ismi(parametre1, parametre2 , .... ) { yapılması istenen işlemler;} |
| --- |

**Fonksiyona Değer Gönderme ve Değer Alma ******

Bir fonksiyonun Javascript içerisindeki ilk önemli görevi diğer fonksiyonlardan veya herhangi bir yerden bir değer alıp onu kendi içerisinde işletip sonra istenilen fonksiyona veya yere göndermektir.
Bir sonucu bir fonksiyondan çağırmak için return deyimi kullanılır.

Örnek 11:

| <html> <title>ornek11.html</title> <head> <script language="JavaScript"> function carp(a,b){ var c=a\*b; return t; } </script> </head> <body> <script language="JavaScript"> var x = prompt("İki Sayının Çarpımı","Birinci Sayı"); var y = prompt("İki Sayının Çarpımı","İkinci Sayı"); var z = carp(x,y); document.write( x,"\*",y,"= ",z); </script> </body> </html> |
| --- |

**2.2.6 Nesneler ve Özellikleri******

Günümüzde sıkça kullanılan bir deyim *Nesneye Yönelik Programlama*. Nedir bu Nesneye Yönelik programlama ? Bu tip programlamada kullanılan her öğe bir nesne olarak kabul edilir. Bu nesnelerin özelliklerini kullanarak onları değiştirerek program yazılır. Javascript'te bu tür bir programlama dilidir. Örneğin webde sörf yaparken herkesin karşısına çıkan formlar birer nesnedir. Bu nesnelerin tepkiye göre cevap vermesi gibi özellikler de onun yani nesnenin özellikleridir.Örneğin şimdiye kadar çoğu kez kullanılan document.write komutu aslında bir nesnenin özelliğine atıfta bulunmaktan başka bir şey değildir. Yani document nesnesinin write özelliğini kullanarak html sayfamıza yazı yazdırıyoruz.

**window**** Nesnesi******

Genel olarak pencere özellikleri ile ilgili bir nesnedir.

**Pencere açmak ve kapamak ******

Birçok yerde gördüğünüz pencere açma pencerelerin çeşitli özelliklerini değiştirme bu nesne yardımıyla\_yapılmaktadır.

Pencere açmak için :

| window.open("Url\_adı" , "pencere\_adı" , "pencere\_özellikleri"); |
| --- |

Pencere kapatmak için :

| window.close(); |
| --- |

Pencere kapatmak için window.close() komutu vermek yeterlidir. Burada kapatılan pencere ona kullanılmakta olan penceredir.Pencere açma işleminde window.open() ile pencerenin açılmak istendiği belirtilir. Parantez içerisinde verilenler ise açılması istenen pencerenin özelliklerini belirtir.

Url\_adı : Buraya yazılacak dosya ismi açılacak pencerenin içerisinde olacaktır.

| window.open("http://www.gantep.edu.tr") |
| --- |

veya;

| window.open("index.html") |
| --- |

Pencere\_adı : Bu açılacak pencerenin adını belirtir. Birden çok pencere ile işlemler yapıyorsanız

hangi pencereye bir komut gönderdiğinizin belli olması için gereklidir.

| window.open("index.html" , "ana"); |
| --- |

Pencere\_özellikleri : Bu özellikte adından belli olduğu ölçüde pencerenin özellikleri ile

ilgilidir. Bir pencerenin değiştirilebilir özellikleri şunlardır :

menubar : Tarayıcıların en üst kısmında bulunan File(Dosya) , Edit(Düzen) vb. menülerin

bulunduğu satırdır.
toolbar : Tarayıcılarda üst kısımda Back(Geri) , Forward(İleri) vb. tuşların bulunduğu

kısımdır.
location : Tarayıcılarda ziyaret etmek istediğiniz web adresini yazdığınız kısım.
status : Tarayıcıların en alt kısmında hangi dosyanın yüklendiği ile ilgili bilgi veren

kısımdır.
scrollbars : Sağ tarafta bulunan sürgü çubuklarıdır.
resizable : Pencerenin boyutlarının kullanıcıya bırakılması veya kesin değerler almasıyla

ilgilidir.
width : Açılacak olan pencerenin piksel cinsinden genişliğidir.
height : Açılacak olan pencerenin piksel cinsinden boyudur.
left : Açılacak olan pencerenin ekranın sol tarafından kaç piksel uzaklıkta olacağını

belirler.
top : Açılacak olan pencerenin ekranın üstünden kaç piksel aşağıda olacağını belirler.

Eğer pencere özellikleri kısmında değişmesini istemediğiniz bir özellik varsa onu

yazmanıza gerek yoktur. Bu değerler tarayıcının banko(default) değerlerinden

alınır.

200x300 ebatlarında http://www.gantep.edu.tr adresine bağlanan bir pencere açmak için;

| window.open ("http://www.gantep.edu.tr", "ana" ," menubar=no, toolbar=no, scrollbars=yes, location=yes, width=200, heigt=300";) |
| --- |

**window.location.protocol******

window nesnesinin location.protocol nesnesi ise yüklenen dosyanın sabit diskten mi yoksa internetten mi yüklendiğini gösterir.

| if (window.location.protocol == "http:" ) { document.write ("Bu belge Internet'ten geliyor.") } else { document.write ("Bu belge sabit diskten geliyor") } |
| --- |

http: Dosyanın internetten yüklendiğini belirtir.
file: Dosyanın sabit diskten yüklendiğin belirtir.

**window.history.go ******

window un history özelliği ile bir önceki sayfaya erişim sağlanabilir. Örneğin kullanıcı herhangi bir formu doldurmadı ve işlem yapılamadı bu durumda bir hata mesajı ile kullanıcıyı uyardıktan sonra history nesnenisin kullanarak bir önceki sayfaya kullanıcı göndererilebilir.

| window.history.go(-1) |
| --- |

Bir önceki sayfaya -1 ile ulaşabilirsiniz. Bu değeri arttırarak daha önceki sayfalara da ulaşabilirsiniz.

**window.status.bar**** kullanımı ******

status.bar, window nesnesinde belirttiğimiz gibi tarayıcıların en alt kısmında yer alan hangi dosyaya gidileceği veya yüklendiği ile ilgili bilgi veren kısımdır.

| window.status="Ahmet Hoca iyi günler diler!"; |
| --- |

**window.moveTo(x,y)******

IE veya NN penceresini bir x,y ile belirlenmiş noktaya taşımak için kullanılır. Taşınan nokta ekranın sol üst köşesidir. Normalde bu noktanın varsayılan değeri (0,0).

| Window.moveTo(100,100); // Internet penceresini 100,100 noktasına taşır. |
| --- |

Döngü deyimleri kullanılarak IE veya NN penceresi hareketli duruma getirilebilirsiniz.

Örnek 12:

| <html> <head><title>ornek12.html</title></head> <body> <script> <!-- var y; for(y=400;y>=0;y-=8){ // x değeri her zaman 0, y değeri 400. pikselden window.moveTo(0,y); // başlıyor. } --> </script> <center>Web Sayfama Hoşgeldiniz...</center> </body> </html> |
| --- |

**Tarayıcı Nesnesi ******

Tarayıcılar Javascript tarafından bir nesne olarak algılanır. Bu nesnenin özelliklerini şöyle sıralayabilir.

appname : Tarayıcı adı
appVersion : Tarayıcının Versionu
appCodeName: Tarayıcının kod adı
userAgent : Tarayıcının ana makinaya(server) kendini tanıtırken verdiği isim

Örnek 13:

| <html> <head><title>ornek13.html</title></head> <body> <script language="javascript1.2"> <!-- document.write("Kullandığınız tarayıcının özellikleri :" , "<br>"); document.write(navigator.appname + navigator.appVersion + navigator.appCodeName + navigator.useAgent ); --> </script> </body> </html> |
| --- |

**2.2.7 Internet Explorer & Netscape Navigator******

Giriş kısmında belirtildiği gibi Javascript kodlarında MSIE (Microsoft Internet Explorer) ve NN (Netscape Navigator) yönünden farklılık vardır. Bu tarayıcının html dökümanı nasıl modellediğine bağlıdır. Tarayıcının nesne döküman modeli, bir Html sayfasındaki çeşitli elemanların tarayıcı tarafından nasıl algılanıp yorumlandığı ile ilgilidir. Tarayıcı farkının nasıl ayırt edilebileceğini aşağıda anlatılmıştır.

| ie4 = (document.all) ? true : false ; nn4 = (document.style) ? true : false ; |
| --- |

Bu iki satırla ,önceki ders olan değişkenler ve mantıksal operatörler yardımıyla, iki tarayıcıyı da kontrol altına alınmıştır.

| <script language="Javascript"> <!-- // Kodları eski sürüm tarayıcılardan saklayalım. ie4 = (document.all) ? true : false ; nn4 = (document.style) ? true : false ; if (ie4){ // MSIE 4.0 için uygun kodları buraya } else{ // NN 4.0 için uygun kodları buraya } // Saklamayı bitir --> </script> |
| --- |

If(ie4)\_ve\_if(nn4)
Bu kodları Javascript'in anlayış tarzı şu şekilde olacaktır. Eğer nn4 , ie4 değişkenlerinden doğru olanı ie4 ise -ki bunu true ve false değerlerinden algılar- alt satıra geçip ona uygun kodu uygulayacaktır. Şayet ie4=false yani nn4=true ise diğer if koşulu yorumlanarak işleme konulacaktır. Bu da nn4 için gerekli kodun çalıştırılması demektir. Aşağıda verilen örnekleri dikkatlice inceleyin.

Örnek 14-1:

| <html> <head><title>ornek14-1.html</title><head> <script language="Javascript"> <!-- function tarayici() { ie4 = (document.all) ? true : false ; nn4 = (document.style) ? true : false ; if (ie4){window.location="ornek14-2.html";} else{ window.location="ornek14-3.html"; } } // tarayici //Saklamayı bitir --> </script> </head> <body onLoad=tarayici()> </body> </html> |
| --- |

Örnek 14-2:

| <html> <head><title>ornek14-2.html</title></head> <body><h3>Tarayıcınız Internet Explorer</h3></body> </html> |
| --- |

Örnek 14-3:

| <html> <head><title>ornek14-3.html</title></head> <body><h3>Tarayıcınız Netscape Navigator</h3></body> </html> |
| --- |

Önemli! : Bu üç (14-1-2-3) Html dosyasınında aynı klasör de olması gereklidir.

**2.2.8 Olaylar******

Ziyaretçiye sunulan bir web sayfası üzerinde ziyaretçinin yaptığı her tür hareket bir bağlantıyı tıklaması , bir resmin üzerine gelmesi , resmin üzerinde ayrılması , bir formu yanlış doldurup hataya yol açması hep bir olaydır.

**onMouseOver,onMouseOut ******

Bu tür nesne olayları ,ingilizce adı onMouseOver = fare işaretçisi(imleç) üzerindeyken , onMouseOut = fare işaretçisi üzerinden ayrıldığında, fare işaretçisinin istenen bir linkin üzerindeyken ve değilken açıklama yapmak için kullanılır.

Örnek 15:

| <html> <head><title>ornek15.html</title> <script language="javascript1.2"> <!-- function uzerinde() {window.status="Tıklayın ve Gaziantep Üniversite sine bağlanın" } function disinda() {window.status="Gaziantep Üniversitesi ne bağlanmak istiyormusun?" } --> </script></head> <body> <a href="http://www.webteknikleri/index.htm" onMouseOver = uzerinde() onMouseOut =disinda()> Webteknikleri.com </a> </body> </html> |
| --- |

**onLoad ****, ****onUnLoad**** ******

Bu olaylar bize sayfanın yüklenmeye başlamasında (onLoad) sayfadan ayrılıncaya (onUnLoad) kadar olan yapılacak işlemler için gereklidir. Bir Javascript fonksiyonun web sayfası yüklenmeye başladığında otomatik olarak çalışmasını istiyorsak onLoad olayını kullanırız. Autoexec.bat dosyası nasıl makine açıldığında yapılmak istenenleri yapıyorsa onLoad olayında da sayfa yüklenmeye başladığında nelerin otomatik olarak başlatılacağını belirleyebiliriz. Mesela sayfa yüklenmeye başladığında ziyaretçiye Web sitemiz hoş geldiniz diyebiliriz. Sayfadan ayrıldığında ise Hoşçakalın diyebiliriz. Web sayfası kod açısında iki kısıma ayrılır. Bunlar head ve body kısmıdır. Tarayıcı açısında body kısmı asıl kısımdır. head kısmında sayfanın nasıl görüntüleneceği gibi bölümler yer alır. Bu yüzden onLoad ve onUnload kısmı body etiketleri arasında yer alır.

Örnek 16:

| <html> <head> <title>ornek16.html</title> <script language="javascript1.2"> <!-- function hosgeldiniz() {alert("Web Sitemize Hosgeldiniz")} function gulegule() {alert("Hoşçakalın")} --> </script> </head> <body onLoad="hosgeldiniz()" onUnload="gulegule()"> </body> </html> |
| --- |

**onError******

Ziyaretçi sayfayı herhangi bir neden yüzünden tam haliyle yükleyememiş olabilir. Bu nedenler aktarım hızı veya tarayıcının Javascript kodunu tam manasıyla yorumlayamamış olmasıdır. İşte bu durumda Error(hata) oluşur. Html üzerinde oluşan en sık error(hata) resim haritalarının (image-map) tam anlamıyla yüklenmemesinden kaynaklanır. Çünkü bu durumda resim tam yüklenmemiştir. Bu da ziyaretçinin resim üzerinde tıklayacağı yerlerin yorumlanmamasını doğurur.

| <img src="resim.gif" onError="alert("Resim tam olarak yüklenemedi!..")"> |
| --- |

onmousedown ve event.button

Web sayfanızı ziyaret eden bir kişinin farenin sağ tuşu ile işlem yapmasını istemiyorsanız bu iki deyimi kullanmalısınız.

Örnek 17: Bu program parçasını mutlaka web sayfanıza ekleyin!..

| <html> <head> <title>ornek17.html</title></head> <body> <script language="JavaScript"> <!-- document.onmousedown=click; function click(){ if((event.button==2) \|\| (event.button==3)){ alert("Oynama...");} } --> </script> </body> </html> |
| --- |

**2.2.8 Javascript ile DHTML (Dinamik HTML)******

Bu kısımda Javascript ile Katman(layer) özelliklerinin nasıl değiştirilebileceğini göreceğiz. Javascript bize html sayfamızı oluşturan önemli unsurlardan biri olan layer(katman) ların tüm özelliklerini değiştirmemize olanak sağlar. Ayrıca hemen her yerde gördüğünüz resim değiştirme tekniğini de bu işlemle yapılır.

**Katman Özelliklerini Değiştirme ******

Katman sayfanın üzerinde ne sayfadan bağımsız ne de her yönüyle sayfaya bağlı bir unsurdur. Katman kullanarak istediğimiz herhangi bir yapıyı (yazı,resim,video,form) sayfamızın istediğimiz yerine koordinatları vermek koşulu ile yerleştirebiliriz. Zaten katmanın kullanım alanı en çok budur. Şimdi bir katman oluşturalım ve değiştirilebilir özelliklerini görelim.

Örnek 18:

| <html> <head><title>ornek18.html</title></head> <body> <div id="deneme" style="position:absolute ; left:100px ; top:200px; width:300px ; height:400px ; visibility:visible" > Su anda bir katman(layer)in icerisindeyim </div> </body> </html> |
| --- |

Layer oluşturmak istediğinizde <div> deyimi ile başlar </div> deyimi ile kodunuz tamamlarsınız.

id : Katmanın ismi

style : Katmanın özelliklerini belirtmek için
absolute : Katmanın koordinatlarının kesin olacağını belirler
left : Katmanın soldan kaç piksel sonra başlayacağını belirler
top : Katmanın üstten kaç piksel sonra başlayacağını belirler
width : Katmanın kaç piksel genişliğinde olacağını belirler
height : Katmanın kaç piksel boyunda olacağını belirler
visibility : Katmanın görünür mü görünmez mi olacağını belirler

Şimdi de Javascript komutlarıyla bu özelliklerin nasıl değiştirildiğini görelim. Fakat burada karşımıza bir sorun çıkmaktadır. IE ve NN tarayıcılarının doküman nesne modelleri farklı olduğundan katmana ulaşma teknikleri de farklıdır.

Internet Explorer kod tekniği

katman\_adı.style.değiştirilmesi\_istenen\_özellik=yeni\_değer;

Örnek :

| deneme.style.left=50px; |
| --- |

Netscape Navigator kod tekniği
document.katman\_adı.değiştirilmesi\_istenen\_özellik=yeni\_değer;

Örnek :

| document.deneme.left=50px; |
| --- |

Örnek 19: Bu örnek yukarıdaki iki örneği de içermektedir.

| <html> <head><title>ornek19.html</title> <script language="javascript1.2"> <!-- function tara(){ var tarayici= navigator.appName if (tarayici=="Netscape") degisim = document.katman; if (tarayici=="Microsoft Internet Explorer") degisim = katman.style; }//tara function hareket1(){ degisim.left=100 degisim.top=100 }//hareket1 function hareket2(){ degisim.left=300 degisim.top=300 }//hareket2 --> </script></head> <body onLoad="tara()"> <div id="katman" style="position:absolute ; left:400px; top:10px"> Bu katmanin yeri degisecek </div> <p><p><p> <a href="javascript:hareket1()">Burayı tıklayın ve katmanınız 100x100'e gitsin</a><br> <a href="javascript:hareket2()">Burayı tıklayın ve katmanınız 300x300' gitsin</a> </body></html> |
| --- |

Buradaki örnekte olduğu gibi sizde katmanın diğer özelliklerini (width,height)değiştirebilirsiniz. Fakat görünebilirlik özelliği için özel bir durum vardır. Katman özelliklerine erişimde olduğu gibi bu özellikte de Internet Explorer ve Netscape Navigator farklılıkları vardır.

Internet Expolorer için görünebilirlik özelliği Katmanı görünebilir kılmak için:
katman\_adı.style.visibility="visible"
Katmanı gizleyebilmek için.

katman\_adı.style.visibility="hidden"

Netscape Navigator için Görünebilirlik özelliği Katmanı görünebilir kılmak için:

document.katman\_adı.visibility="show"
Katmanı gizleyebilmek için.

document.katman\_adı.visibility="hide"

Örnek 20:

| <html> <head><title>ornek20.html</title> <script language="javascript1.2"> <!-- function sakla(){ var tarayici= navigator.appName if (tarayici=="Netscape") document.katman.visibility="hide" if (tarayici=="Microsoft Internet Explorer") katman.style.visibility="hidden" }//sakla function goster(){ var tarayici= navigator.appName if (tarayici=="Netscape") document.katman.visibility="show" if (tarayici=="Microsoft Internet Explorer") katman.style.visibility="visible" }//goster --> </script></head> <body> <div id="katman" style="position:absolute ; left:400px; top:10px"> Bu katmanin tikladiginizda yok olacak </div><p><p><p> <a href="javascript:sakla()">Burayi tiklayin ve katmaniniz yok olsun</a><br> <a href="javascript:goster()">Burayi tiklayin ve katmaniniz geri gelsin</a> </body></html> |
| --- |

Sizde bu tıklama özelliklerin değil de onMouseOver ve onMouseOut olay yönlendiricilerini kullanarak çok daha güzel şeyler üretebilirsiniz.

---
*Kaynak: `JAVA SCRİPT EKLENTİLERİ/ekitap-Anonim-JavaScript_Eklemek.doc` — Guest — 2002*
