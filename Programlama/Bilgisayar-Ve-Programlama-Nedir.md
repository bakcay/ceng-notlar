# Bilgisayar Ve Programlama Nedir

Sanırım, C ve C++ adını bilgisayarla az çok haşır neşir olan herkes en az bir kez duymuştur. Sizde bu isimleri duyanlardansanız ve nedir, ne değildir, nasıl kullanılır gibi birçok soruya yanıt arıyorsanız, doğru yerdesiniz. Çünkü bu yazıyla başlayarak C ve C++ ile programlamaya gireceğiz. Önce C ile yolumuza koyulup, belli bir olgunluğa ulaştıktan sonra C++ ile devam edeceğiz.

Okuyucularımızın genelini düşünerek, konuyu en temelden almayı daha doğru bulduk. Yani hedefimiz, programlamayı hiç bilmeyen bir insanın burada okuduklarıyla belli bir yerlere ulaşması. İleri derece de olanlarsa sıkılmamak için biraz beklemeli. Lafı fazla uzatmadan başlayalım.

**Bilgisayar ve Programlama nedir?******

Bilgisayar çok basit düşündüğümüzde üç ana görevi yerine getiren bir makinedir. Girilen bilgiyi alır (INPUT), işler (PROCESSING) ve bu işlenmiş veriden bir sonuç (OUTPUT) çıkarır. Bilgisayar, sadece donanım olarak çalışmaz. Çünkü yazılım olmadan, donanım ne yapacağını bilemez. Bilgisayar donanımına ne yapacağını söyleyecek bir komutlar dizisi gerekir. Yapacağı görevleri, ona anlatan komutlara program diyebiliriz. Yani donanıma “sen şunu yap, sonra bulduğun sonucu şöyle şuraya ekle” gibisinden işler yaptırmak programın veya bir başka deyişle yazılımın işidir. Bir programcı olarak bundan fazlasını bilmek elbette ki avantajdır. Ama bilgisayarın bütün özelliklerini bilmeniz gerekmez. Yani yazacağınız bir program için o bilgisayarın özelliklerini bilmeseniz de olur.

Bilgisayarın anladığı tek dil, Makine Dilidir. Bu 16’lık (Hexadecimal) sistemden oluşan bir programlama tipidir. Makine dilini anlamak çok zordur ve bu dili kullanmak için o bilgisayarın donanım özelliklerini mutlaka bilmeniz gerekir. C de ekrana yazı yazmanızı sağlayan “printf();” gibi çok basit bir fonksiyon, makine dilinde 1A BB 0D BC D5 FF C2 F7... gibi çok daha karmaşık ve hiçbir anlam ifade etmeyen bir hâle dönüşür. Makine dili programlama dilleri arasında en alt seviyedir.

Makine dilinden sonra Assembler Dili gelir. Makine dilini kullanmanın zorluğu ve karmaşası üzerine geliştirilen Assembler, daha basit bir yapıdadır. Ama yine de C ile mukayese ederseniz çok daha zordur ve kullandığınız bilgisayarın donanımına dair hâlen bilgiye gereksinim duyarsınız. Assembler aşağıda ki gibi karmaşık bir yapıdadır.

```asm
SEGMENT COM WORD PUBLIC ‘CODE’
ASSUME CS : COMDS : COM
ORG 100H
ENTRY: MOV DVX,OFFSET MSG
MOV AH,g
.
.
.
```

Şuan bunu anlamaya çalışıp, hiç zamanınızı harcamayın. Çünkü öğreneceğimiz dil C, işlerimizi ve dolayısıyla hayatımızı çok daha kolaylaştırmaktadır. C, orta seviye bir programlama dilidir. Bunun anlamı, hem yazması kolay, hemde üst seviye dillere göre daha çok erişim hakkınızın olduğudur. Üst seviye programlama dilleri ise BASIC, PASCAL, gibi dillerdir. Yazması göreceli olarak daha kolay olsa da C ile yapabileceklerimiz daha çoktur.

**Program yazmak için ne gerekir?******

Program yazabilmek için hiçbir şeye ihtiyacınız yoktur. Program yazmak için windows’un not defterini bile kullanabilirsiniz. Önemli olan yazılan programın derlenmesidir. Derlemeye “compile” ve derleme işini yapan derleyiciyeyse “compiler” denir. C için internet üzerinden birçok Compiler bulabilirsiniz. Ben, program uyarlamalarını Borland tarafından geliştirilen Turbo C++ üzerinden anlatacağım. Aynı şekilde bu versiyonunu kurmanızı tavsiye ederim. Yazıların ve sizin senkronizasyonu için daha uygun olacaktır ve Borland’ın geliştirdiği bu versiyon hem C, hem de C++ derleme özelliğine sahiptir.

**Algoritma Geliştirmek******

C dilini ve komutlarını öğrenmek, programlamaya başlamak için şarttır ama algoritma oluşturamadığımız sürece bir program oluşturmazsınız. Algoritma, mantıktır. Yani neyi, nasıl yapacağınızı belirtir. Algoritma türetmek için geliştirilmiş bir metot yok. Her program için o metodu sizin bulmanız gerekiyor. Ama hiç merak etmeyin, yazdığınız program sayısı arttıkça, algoritma kurmanız daha kolay hâle gelecektir. Algoritma programlama da hayati önem taşır. C dilinde öğrendiğiniz komutlar BASIC veya FORTRAN gibi başka dillerde değişir. Ama programlama mantığını bir kere oturttursanız, C’deki komutlar yerine başka dillerin komutlarını öğrenerek, önemli bir zorluk çekmeden diğer dillerde de program yazabilirsiniz.

Basit bir örnek üzerinden düşünelim. Bir markete gittiniz, kasada ki görevliye aldığınız ürünü gösterdiniz, parayı uzattınız, paranın üstünü aldınız. Günlük hayatta gayet normal olan bu durumu biraz değiştirelim. Karşınızda insan değil, elektronik bir kasiyer olsun. Ona göre bir algoritma geliştirirsek,

1-) Ürüne bak;

2-) Ürün Fiyatını bul;

3-) Parayı al;

4-) Alınan paradan ürün fiyatını çıkar;

5-) Kalan parayı ver.

İnsan zekasının otomatik hâle getirdiği eylemleri, ne yazık ki bilgisayar bilmez ve ona biz öğretmek zorundayız. Öğretirken de hata yapma hakkımız yoktur, çünkü yanlış öğreti yanlış programlamayla sonuçlanır.

**C Programlama Dili******

**Temel Giriş/Çıkış Operasyonları (BASIC I/O):******

C ile ilgili olarak bu ve önümüzdeki yazılarda birçok komut/fonksiyon göreceğiz. Ama hep kullanacağımız ve ilk öğrenmemiz gerekenler temel giriş çıkış fonksiyonlarıdır. C de klavyeden bir değer alabilmek için scanf(); fonksiyonunu kullanırız. Ekrana herhangi bir şey yazdırmak içinse printf(); fonksiyonu kullanılır.

Bir örnekle görelim;

```c
#include<stdio.h>
main()
{
 printf(“Hello World”);
}
```

Eğer bunu derleyicinizde yazıp derlerseniz, -Borland Turbo C++ için, Ctrl+F9 tuşları ile yazdığınız programınızı derleyebilirsiniz- ekrana Hello World yazılacaktır. #include<stdio.h> standart girdi/çıktı’yı destekle gibi bir anlama sahiptir. main() , ana fonksyiondur. Ondan sonra gelen ayraç standarttır. Çift tırnak işaretleri, printf ve parantez standarttır. Noktalı virgülse C dilinde her komutun sonuna konulur. Tırnakların içine istediğinizi yazıp bastırabilirsiniz. Programın sonunda ki ayraçta programın bittiğini gösterir.

Şimdi yukarıda yazdığımız basit programı, biraz daha geliştirelim.

```c
#include<stdio.h>
#include<conio.h>
main()
{
 clrscr();
 printf(“Hello World\n”);
 printf(“Merhaba Dünya”);
 return 0;
}
```

Birkaç yeni satır ekledik. Sırayla ne olduklarını açıklayalım. #include<conio.h> başlık dosyaları (header files) ile ilgilidir. Onu şuan izah etmem için erken. Ama şu kadarını söyleyelim, clrscr(); fonksiyonunu kullanabilmek için bunu yazmamız gerekmektedir. clrscr(); fonksiyonuysa, ekranda önceden yazılan şeyleri temizler ve kullanacağımız ortamın sıfır olmasını sağlar. Az evvel yazdığımız Hello World yazısının sonuna “\n” ekledik. “\n” bir alt satıra geç anlamına geliyor. Eğer \n yazmazsak, ekranda *Hello WorldMerhaba* Dünya şeklinde bir yazı çıkar. \n kullandığımızdaysa, Hello World yazılacak onun ve sonra bir alt satırına geçilecek, oraya Merhaba Dünya yazılacaktır. En alt satırdaysa return 0; adında yeni bir komut görüyorsunuz. Bunu eklemeden de program çalışacaktır. Ancak uyarı verir. Bunu ekleyerek bu uyarıdan kurtulabilirsiniz. Detayına girmek için henüz erken, return konusuna ileride değineceğiz.

Yukarıda ki programın aynısını şöyle de yazabilirdik;

```c
#include<stdio.h>
#include<conio.h>
main()
{
 clrscr();
 printf(“Hello World”);
 printf(“\nMerhaba Dünya”);
 return 0;
}
```

Bir önce ve şimdi yazdığımız programların ekran çıktısı aynıdır. Bu örnekle anlatmak istediğim, printf(); te çift tırnakların içerisinde nereye \n koyarsak koyalım, ondan sonrası için cursor bir alt satıra geçer.

printf(); daha birçok şekilde kullanılabilir. Diyelim ki yukarıdaki programı tek printf(); komutuyla yazmak istediniz. O zaman ne yaparsınız?

```c
#include<stdio.h>
#include<conio.h>
main()
{
 clrscr();
 printf(“Hello World\nMerhaba Dünya”);
 return 0;
}
```

Gördüğünüz gibi tek bir printf(); kullanarak aynı işlemi yaptırdık.

Varsayalım, ekrana çok uzun bir cümle yazmamız gerekti. Örneğin;

```c
#include<stdio.h>
#include<conio.h>
main()
{
 clrscr();
 printf(“Benim adım Çağatay ÇEBİ ve Kadir Has Üniversitesi’nde okuyorum.”);
 return 0;
}
```

Bu yazdığımız program hata vermez ama compiler’ın çalışma verimini düşürür. Bu düşüş önemsiz olsa bile bizim yazma verimimiz düşecektir. Çünkü ne yazdığını okumak için ok tuşlarını kullanarak bir sağa bir sola gidip gelmemiz gerekir.

Bu programı aşağıda ki gibi yazmamız daha uygundur.

```c
#include<stdio.h>
#include<conio.h>
main()
{
 clrscr();
 printf(“Benim adım Çağatay ÇEBİ”
 “ ve Kadir Has Üniversitesi’nde”
 “ okuyorum.”);
 return 0;
}
```

Tek bir printf(); fonksiyonu kullanılmıştır. Ancak gördüğünüz gibi alt alta yazarak bütün cümleyi tek seferde görülebilir hâle getirdik. Ekrana bunu bastırırsanız, alt alta üç satır basmaz. Bu çok hata yapılan bir noktadır. Sadece tek satır basar ve yazılan bir önceki örnekle aynı olur. Alt alta yazmak için daha önce bahsettiğimiz gibi \n eklememiz gerekir.

Ekrana, Ali: “Naber, nasılsın? diye sordu. şeklinde bir yazı yazdırmamız gerekiyor diyelim. Bu konuda ufak bir problem yaşayacağız. Çünkü printf(); fonksiyonu gördüğü ilk iki çift tırnak üzerinden işlem yapar. Böyle bir şeyi ekrana yazdırmak için aşağıda ki gibi bir program yazmamız gerekir.

```c
#include<stdio.h>
#include<conio.h>
main()
{
 clrscr();
 printf(“Ali: \“Naber, nasılsın?\” dedi.”);
 return 0;
}
```

printf(); fonksiyonunu kullanmayı sanırım iyice anladınız. printf( yazıp, sonra çift tırnak açıyor, yazmak istediklerimizi yazıyor, çift tırnağı sonra da parantezi kapatıyor, sonuna noktalı virgül ekliyoruz. Alt satıra geçmek içinse, yazdıklarımızın sonuna \n ekliyoruz. Çift tırnaklı bir şey kullanmak içinse \“ ... \” kullanıyoruz.

scanf(); fonksiyonuna gelince, bu başında bahsettiğimiz gibi bizim giriş (Input) fonksiyonumuzdur. Ancak yazımı burada noktalıyorum. Çünkü değişkenler işin içine girmekte ve onları anlatmam uzun sürecek. Gelecek haftaki yazımda kaldığımız yerden devam edeceğiz. Yazdıklarımla ilgili öneri, eleştiri veya sorunuz varsa, bana ulaşabilirsiniz. Haftaya ya da en kötü ihtimalle öbür haftaya görüşürüz.

---
*Kaynak: `Bilgisayar ve Programlama nedir/Bilgisayar ve Programlama nedir.doc` — ekim kaya — 2004*
