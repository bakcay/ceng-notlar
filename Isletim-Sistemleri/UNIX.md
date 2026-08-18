# UNIX

## **UNIX**

## **1. UNIX İşletim Sisteminin Başlangıç Ve Gelişimi******

## **2. Dizayn Prensipleri******

## **3. Temel Unix Komutları******

## **3.1. Dosyaları Görüntüleme******

## **3.2. Bir Dosyayı Başka Bir Yere Kopyalama******

## **3.3. Dizin Oluşturma Ve Silme******

## **3.4. Dosyaları Veya Dizinleri Başka Bir Yere Taşıma******

## **3.5. Dosyaları Silme******

## **3.6. Sistemdeki İşlemler Hakkında Bilgi Alma******

## **3.7. Yeri Bilinmeyen Bir Dosyayı Bulmak******

## **3.8. Şifre Değiştirmek******

## **3.9. Bir Dosyanın İzinlerinin Değiştirilmesi******

## **3.10. Dosyaların Boyutlarını Öğrenmek******

## **3.11. Kimlerin Çalıştığını Öğrenmek******

## **3.12. Yazıcıdan Dosyaların Çıktısını Almak******

## **3.13. Alias ( Farklı İsim ) Tanımlamak******

## **3.14. Bir Dosyanın İçini Görmek İçin Kullanılan Programlar******

**1. Unix İşletim Sisteminin Başlangıç Ve Gelişimi******

UNIX in ilk versiyonu Bell Laboraties araştırma grubunda çalışan Ken Thompson tarafından 1969 yılında PDP-7 de çalışmak üzere geliştirildi. Kısa bir süre sonra Dennis Ritchie Thompson'a katıldı. Thompson, Ritchie ve araştırma grubunun diğer üyeleri UNIX'in ilk versiyonlarını hazırladı.

Ritchie çok yakın geçmiş zamanda MULTICS projesi üzerinde çalışmış olduğundan bu yeni işletim sistemi üzerinde MULTICS in güçlü bir etkisi oldu. Hatta ismi bile MULTICS den gelmedir. Dosya sistemi temel organizasyonu, komut yorumlayıcı fikri (shell), her komut için ayrı bir process ve daha çeşitli özellikler direk olarak MULTICS den geldi.

Ritchie ve Thompson UNIX üzerinde yıllarca çalıştı. Onların çalışmaları PDP-11/20 üzerinde çalışan ikinci versiyona ilerlemeye yol açtı. Üçüncü versiyon işletim sisteminin büyük çoğunluğu assembly dili yerine sistem-programlama dili olan C de yazmalarıyla oluştu.C UNIX i desteklemek için Bell Laboratories' de geliştirildi.UNIX aynı zamanda daha büyük PDP-11 modellerine taşındı örneğin 11/45 ve 11/70. C de tekrar yazıldığı ve multiprogramming desteği olan sistemlere (örneğin 11/45) geçtiği zaman multiprogramming ve diğer gelişmeler UNIX in yapısına eklendi.

UNIX geliştikçe Bell Laboratories' de yaygın olarak kullanıldı ve yavaş yavaş bazı üniversitelere yayıldı. Bell Laboratories dışında yaygın olarak bulunan ilk versiyonu Version 6 idi . 1978 yılında Version 7 dağıtıldı ve bu modern UNIX sistemlerin atasıydı.

Version 7 nin dağıtımından sonra UNIX Support Group (USG) dağıtım için idari kontrol ve sorumluluğu Bell Laboratories den aldı. UNIX bir araştırma aracından çok bir ürün oluyordu. Araştırma Grubu aynı zamanda organizasyonlarındaki kuruluş içi hesaplamaları gerçekleştirmek için kendi UNIX versiyonlarını geliştirmeye devam etti. UNIX in bir sonraki versiyonlarında Remote File System ve Stream I/O system gibi özellikler eklendi.

USG UNIX için desteğini AT&T içinde sağladı. İlk dış dağıtımını yaptığı sistem 1982 yılında System III tü.

Küçük boyut, modülerlik ve UNIX sistemlerin temiz dizaynı Rand, BBN, the University of Illinois, Harvard, Purdue ve Dec gibi birçok bilgisayar bilimi temelli organizasyonlarda UNIX temelli işlere önderlik etti. Bell Laboraties ve AT&T hariç en etkili gruplar Berkeley deki University of California da ortaya çıktı.

Berkeley in 1978 yılındaki VAX UNIX üzerindeki ilk çalışması 32V ye virtual memory, demand paging ve page replacement in Bill Joy ve Ozalp Babaoğlu tarafından 3BSD UNIX i hazırlamak için eklenmesi oldu. Sistem bu özelliklerin kullanıldığı ilk versiyon oldu. Geniş virtual memory nin kullanılması geniş programların çalıştırılabilmesine yol açtı.

DARPA (Defense Advanced Research Projects Agency) için çalışan bir komite TCP/IP protokollerini destekleyen 4.2BSD versiyonunu oluşturdu. Böylece UNIX işletim sistemi LAN lardan WAN lara kadar çeşitli network tipleri üzerinde kullanılmaya başlandı.

Günümüzdeki mevcut UNIX sistem versiyonları Bell Laboraties ve Berkeley in ürettiği ürünlerle sınırlı değildir. Sun Microsystems BSD yi workstationlarında kullanarak popülaritesinin artmasına sebep oldu.UNIX in popülaritesi arttıkça yeni bilgisayar ve bilgisayar sistemlerinde kullanılmaya başlandı. Çok sayıda UNIX ve UNIX benzeri işletim sistemleri geliştirildi. Yaygın bir şekilde bulunmasından dolayı akademik kurumlardan askeri kurumlara kadar bir çok kurumda kullanıldı. Bu sistemlerin çoğu Version 7, System III, 4.2 BSD veya System V tabanlıydı.

UNIX iki tane Bell Laboraties çalışanının kişisel projelerinden uluslararası standartlarla tanımlanan bir işletim sistemi haline geldi. UNIX işletim sistemi işletim sistemleri teorisi için hala eğitim kurumları için en popüler ve önemli bir işletim sistemidir.

**2. Dizayn Prensipleri******

UNIX işletim sistemi time-sharing bir sistem olarak tasarlandı. Standart kullanıcı arayüzü ( shell) basit ve istenildiğinde bir başkası ile değiştirilebilir. Dosyalama sistemi kullanıcılara kendi alt dizinlerini oluşturmaya izin veren multilevel tree yapısıdır. Her kullanıcı dosyası basit byte sıralarıdır.

UNIX multiple process i destekler. Bir process kolaylıkla yeni processler oluşturabilir. CPU scheduling i basit priority algoritmasıdır. 4.3BSD memory ve CPU yönetimini desteklemek için demand paging kullanır. Eğer sistem aşırı paging den dolayı sorun yaşarsa swapping kullanılır.

UNIX başlangıçta iki programcı tarafından geliştirildiği için anlaşılmak için yeterince küçüktür. Algoritmaların çoğu hız veya komplekslik yerine basitliği için seçilmiştir. UNIX programcılar tarafından yine programcılar için tasarlandı. Bü yüzden her zaman interaktif ve program geliştirme özellikleri öncelikli oldu.

UNIX çoğunlukla kendini desteklemek için yazılan C dilinde yazıldı. Çünkü kimse assembly dilinde programlama yapmayı sevmiyordu. Assembly dilinden C diline geçiş UNIX in bir sistemden başka bir sisteme geçişini kolaylaştırdı.

**3. Temel Unix Komutları******

**3.1. Dosyaları Görüntülemek******

Dosyalar ls komutuyla görüntülenir.

ls (seçenekler) (dosya veya dizin...)

*Seçenekler:***

-C : Görüntü çok kolonlu ve dosya isimleri azalan sırada olacaktır.

-F : Dosya isimleri sonunda \* dizin isimleri sonunda / işaretleri görüntülenerek birbirinden ayırt edilmelerini sağlar.

-R : Belirlenen bir dizin içindeki dosyalar yani sıra varsa tüm alt dizinler içerikleriyle birlikte listeler.

-a : . ile başlayan dosyalar dahil dizinin tüm içeriğini listeler.

-c: Dosyaları sıralamak veya bastırmak amacıyla i-düğümlerinin en son düzeltme tarihlerini kullanır.

-l : Dosyalar hakkında daha ayrıntılı bilgi verir.

-g : Eğer ayrıntılı liste alınıyorsa yani tüm bilgiler listelenecek ise ve bu listede dosyanın sahibinin grup adıyla birlikte yer alması isteniyorsa bu seçenek kullanılır.

-i : Her dosyayı i düğümleri ile birlikte görüntüler.

-m : Dosya isimleri virgüllerle birbirinden ayrılarak listelenir.

-n : Ayrıntılı listede yer alan ID numaralarını listeler.

-o : Ayrıntılı listeye grup adlarının dahil edilmesini sağlar.

-p : Dizinlerin / işaretiyle simgelenmesini sağlar.

-q : Dosya isimleri içinde ? gibi grafik olmayan karakterler varsa bunların listelenmesine yardımcı olurlar.

-r : Sıralamayı ters yönden yapar.

-s : Blok cinsinden dosyaların boyutunu verir.

-t : Dosyaların değişime uğrama zamanlarına göre sıralanmasını sağlar.

-u : Dosyalara en son erişim zamanlarına göre sıralanmasını sağlar.

*Örnek :***

ls -l aytekin\*

--w-rw--w- 1 e065247 B386 603 Oct 24 22:14 aytekin\_guzelis.html

--w-rw--w- 1 e065247 B386 607 Oct 24 22:23 aytekin.html

**3.2. Bir Dosyayı Başka Bir Yere Kopyalama******

cp komutu ile kopyalama yapılır .

Kullanımı :

cp -\[seçenek\] dosya başkabir\_dosya\_ismi

Örnek :

Cp main.html main\_index.html // main.html'i main\_index.html olarak kopyalar.

cp index.html ~/tmp // index.html'i HOME dizinimdeki /tmp dizininin altına kopyalar

cp -r ~/tmp ~/dump // HOME dizindeki tmp dizinini dump dizininin altına kopyalar.

**3.3. Dizin Oluşturma Ve Silme******

mkdir dizin\_ismi // dizin oluşturur

rmdir dizin\_ismi // içi boş olan bir dizini siler

**3.4. Dosyaları Veya Dizinleri Başka Bir Yere Taşıma******

mv komutu ile dosyaları başka bir dizine, hatta dizinleri başka dizinlere taşıyabilirsiniz. Bu işlemin sonunda orijinal dizinin içindeki dosyaların isimlerinde bir değişiklik olmaz. Mv komutu DOS'taki rename ve move komutuna benzer, ancak onlardan çok daha beceriklidir.

*Kullanımı :***

mv dosya1 dosya2

**3.5**. **Dosyaları Silme******

Unix'te dosyaları silmek için rm komutu kullanılır. Aslında rm'nin yaptığı şey dosyanın sahip olduğu linklerden birini çıkarmaktır. Eğer dosyanın sadece bir link'i varsa sonuçta dosya silinir.

DİKKAT : Unix'te DOS'takine benzer bir UNDELETE komutu yoktur ( mimarilerinin farklı olmasından dolayı ) bu sebeple dosyalarınızı silerken çok dikkatli olmanız gerekir. Eğer bir dosyayı yanlışlıkla silerseniz, sistem sorumlunuza başvurun, belki backup'lardan dosyanızı geri getirebilir.

*Kullanımı :***

rm -\[seçenekler\] Dosya\_ismi Dosya\_ismi ...

Seçenekler :

-e : Dosyanın silinmesinden sonra ekrana bilgi verir.

-f : Sormadan write-protected dosyayı siler.

-i : Dosyayı silmeden önce bunun doğruluğunu sorar.

-r : Recursive olarak alt dizinleri siler.

-R : -r ile aynıdır.

*Örnek :***

rm aytek\* // bulunduğumuz dizindeki aytek ile başlayan tüm dosyaları siler

rm -rf tmp // tmp dizinini ve alt dizinlerini uyarmadan siler

**3.6. Sistemdeki İşlemler Hakkında Bilgi Alma******

ps komutu ile sistemde yürüyen işlemler hakkında bilgi alınır.

*Kullanımı :***

ps (seçenekler)

*Seçenekler:***

-e : Tüm işlemlerle ilgili bilgilerin görüntülenmesini sağlar.

-d : Grup liderleri hariç tüm işlemler hakkında bilgi verir.

-a : Grup liderleri ve terminallerle ilişkisi olanlar dışında kalan tüm işlemler hakkında bilgi verir.

-f : Tam listenin üretilmesine olanak tanır.

-l : Ayrıntılı listeyi görüntüler.

-c dosya : /dev/swap in bulunduğu yerde swapdev dosyasını kullanır.

-t liste : Liste içinde yer verilen terminallerden yürütülen işlemler hakkında özel bilgi sağlar.

-p liste : Listede ID numaraları tanımlanan işlemlere ilişkin özel bilgileri görüntüler.

-u liste : Belirlenen kullanıcılarla ilişkili işlemlere ait özet bilgi.

-g liste : Grup liderlerinin ilişkili olduğu işlemler hakkında bilgi.

x : Sahip olduğunuz tüm işlemleri listeler .

*Örnek :***

/home/e065247/m>ps x

PID TTY STAT TIME COMMAND

81024 pts/7 R 0:00 ps x

113626 - S 0:00 xterm

117927 pts/7 S 0:00 -csh

125165 pts/5 S 0:05 telnet rorqual

129499 pts/12 S 0:00 -csh

132296 pts/5 S 0:00 -usr/local/bin/tcsh

167106 - S 0:06 aixterm

198577 - S 0:00 sh /usr/bin/X11/startx -t -wait

231908 pts/12 S 0:00 telnet rorqual

236990 - S 0:00 mwm

244646 - S 0:00 xterm

Çalışan bir işlem kill komutuyla kesilir.

kill (-sinyal) PID

PID numaraları ps komutu ile görünür.Bir çok sinyal tanımlanabilir. Bunlardan -9 işlemi öldürür.

**3.7. Yeri Bilinmeyen Bir Dosyayı Bulmak******

Find programı ile bulabilirsiniz.

*Kullanımı :***

find yol tanımı seçenekler

*Seçenekler:***

-name isim : aranılacak dosyanın ismi.

-perm izin : İzinleri oktal olarak belirlenmiş dosyaların aranılması.

-links n : linke sahip dosyalar.

-user kullanıcı : Belirli bir kullanıcıya ait dosyaların aranması.

-group isim : Belirli bir gruba dahil dosyaların aranması.

-atime n : n gün içinde erişilen dosyalar.

-mtime n : n gün içinde işlem gören dosyalar.

-ctime n : n gün içinde değiştirilen dosyalar.

-print : bulunan dosyaların ekranda görüntülenmesini sağlar.

*Örnek :***

Bulunduğum dizinden itibaren tüm alt-dizinlerdeki "guzelis" ile başlayan dosyaları bulmak için;

find . -name "guzelis\*" -print

./faq/guzelis\_aytekin.html

./faq/guzelis\_aytekin\_programlama.html

./guzelis

./guzelis/guzelis

./guzelis/guzelis.c

Not1 : Burada arayacağım dosyada wildcard kullandığım için " " işaretini kullandım. Eğer dosyanın tam ismini biliyorsanız buna gerek yoktur.

Not2 : Eğer bir aramayı root'tan ( / ) başlatırsanız çok büyük olasılıkla bazı dosyaları okumaya izniniz olmadığı için size bunu belirten bir uyarı mesajı verilecektir, ve bu mesajlar arasında aradığınız şey ekrana yazılsa bile bunu gözden kaçırabilirsiniz. Bu sebeple çıktıyı bir dosyaya yöneltip, daha sonra o dosyayı okumanızda fayda vardır.

*Örnek :***

find / -name gzip -print > gzip

**3.8. Şifre Değiştirmek******

Kullanıcının şifrelerini değiştirmek için passwd programı kullanılır. Bazı sistemlerde yppasswd olarakta geçebilir. Bu komutu yazdıktan sonra sizden ilk olarak eski şifreniz ardından yeni şifreniz sorulacaktır. Daha sonra tekrar yeni şifreniz kontrol amacı ile sorulur. Eğer bir hata yapmadıysanız şifreniz değiştirilir.

*İyi şifreler nasıl olmalıdır ?***

İçinde noktalama işareti,rakam,boşluk ve hatta kontrol karakterleri bulunduran şifreler seçin. İçinde bunlardan bir tane bile olsa böyle bir şifrenin bulunma olasılığı son derece düşüktür. Eğer bu karakterlerin sayısını arttırırsanız bulunma olasılığı kat kat düşer.

*Kötü şifrelere birkaç örnek :***

serafettin

semsettin

ser\_semsettin

kamyon

şifre

.....

*İyi şifrelere birkaç örnek :***

.bir/iki

\[mb&elf\]

**3.9. Bir Dosyanın İzinlerinin Değiştirilmesi******

chmod izin modu dosya : Bir dosyaya verilen izinlerin değiştirilmesi.

ls -l \[dosya\] yazdığınızda en solda görülen bilgiler, o dosyanın izinlerini gösterir.

*Örnek :***

ls -l ayt\*

--w-rw-r-- 1 e065247 B386 603 Oct 24 22:14 aytekin\_index.html

Görüldüğü gibi en soldaki kısım 10 tane alandan oluşmaktadır. Bunların ilki dosyanın niteliğini ( dizin yada dosya ) sonraki 9'u da o dosyanın izinlerini gösterir.

Eğer en soldaki alan "d" ile baslarsa bu onun bir dizin olduğunu, "-" ile baslarsa normal bir dosya olduğunu gösterir ( NOT : Unix'te her dizin özel bir dosyadır ! ) Bu ilk karakterden sonra gelen 9 karakter de kendi aralarında 3 gruba bölünür.

İlk 3 Alan : Kullanıcı izinlerini

Sonraki 3 Alan : Grup ile ilgili izinleri

En Sağdaki 3 Alan : Diğer kullanıcılarla ilgili izinleri gösterir.

Her bir bölümde 3'e bölünür :

r : Read ( okuma ) hakkı;

w : Write ( yazma ) hakkı;

x : Execute ( çalıştırma ) hakkı.

*Örnek :***

-rw-r--r-- 1 e065247 B386 533 Oct 24 21:35 pensacola.html

gibi bir dosya bu dosyanın herkes tarafından okunabilir olduğunu, ama sadece o dosyanın sahibi tarafından yazılabilir olduğunu gösterir.

chmod programında kullanılan izin modları iki türlü belirtilebilir :

*1- **Nümerik olarak :***

r'nin değeri : 4

w'nin değeri : 2

x'in değeri : 1 dir.

*Örnekler :***

**ORANTILI İZİN KODLARI**

------------------------------------------------

Orantılı kod - İzin durumu -

------------------------------------------------

0400 - Dosya sahibi için okuma -

0200 - Dosya sahibi için yazma -

0100 - Dosya sahibi için çalıştırma -

0040 - Gruptakiler için okuma -

0020 - Gruptakiler için yazma -

0010 - Gruptakiler için çalıştırma -

0004 - Diğerleri için okuma -

0002 - Diğerleri için yazma -

0001 - Diğerleri için çalıştırma -

------------------------------------------------

ls -l

--w-rw--w- 1 e065247 B386 603 Oct 24 22:14 aytekin.html

--w-rw--w- 1 e065247 B386 607 Oct 24 22:23 aytekin\_guzelis.html

chmod 0220 aytekin\* // Kullanıcıya ve gruba yazma hakkı verelim

ls -l

--w--w---- 1 e065247 B386 603 Oct 24 22:14 aytekin.html

--w--w---- 1 e065247 B386 607 Oct 24 22:23 aytekin\_guzelis.html

*2- **Karakter olarak :***

u : Dosyanın sahibi.

g : Grup

o : Diğerleri

a : Herkes

+ : İzin vermek

- : İzinleri kaldırmak.

= : Belirli bir izin atamak üzere.

chmod go+r aytekin\* // Ek olarak gruba ve diğerlerine okuma hakki verelim

ls -l

--w-rw-r-- 1 e065247 B386 603 Oct 24 22:14 aytekin.html

--w-rw-r-- 1 e065247 B386 607 Oct 24 22:23 aytekin\_guzelis.html

**3.10. Dosyaların Boyutlarını Öğrenmek******

Başlıca 2 yolu vardır;

*1- **du komutu***

Du komutu bulunduğunuz dizinden itibaren tüm alt dizinleri tarayarak block cinsinden ne kadar yer kapladığını gösterir.Block size'ları genelde 512 byte'tır bu sebeple çıkan sayıyı iki'ye bölerek o dizinin ne kadar yer kapladığını görebilirsiniz.

En aşağıda da toplam miktar belirtilir.

*Örnek :***

/home/e065247/m>du

72 ./.m

8 ./m

8 ./ch

496 ./temp

632 .

*2- **quota komutu***

Quota komutu toplam olarak ne kadar yer kapladığınızı ve sizin ne kadar yazma hakkinizin olduğunu gösterir. Aynı zamanda eğer geçici disk sınırınızı aştıysanız, kalan gün miktarı vs. gibi bilgileride gösterir.

*Örnek :***

/home/e065247/m>quota

Disk quotas for user e065247 (uid 517):

Filesystem blocks quota limit grace files quota limit grace

/home211 2748 3000 5000 302 1000 1500

**3.11. Kimlerin Çalıştığını Öğrenmek******

w \[seçenekler\]

w komutu sistemin yükü, ve çalışanların faaliyetleri konusunda bazı bilgiler verir. Komutu çalıştırdıktan sonra çıkan bilgilerden ilki, sistem hakkındadır : sistem saati, o anda kaç kişinin açık olduğu, ve sistemin yükü gibi.. Sistem yükü genelde 0 ile 40 arasında değişen bir değer ile gösterilir. Eğer sistemin i çok kullanıcılı ya da ağır işlerin yapıldığı makinelerde bu sayı 5 ten çok çok fazla olabilir.

Yükü 0-5 arasında ise sistemin o anda fazla yüklü olmadığını söyleyebiliriz.

Bu ilk satırın ardından gelen satırlarda sıralar halinde kullanıcılarla ilgili bilgiler bulunur. Soldan sağa doğru ;

İlk alan : Kullanıcının userid si.

2. alan : Bağlandığı tty'si.

3. alan : Ne zaman login olduğu.

4. alan : Enson komutu çalıştırmasından sonra geçen zaman. (idle time)

5. alan : Makinenin açılmasından beri yapılan process'lerin getirdiği toplam yük.

6. alan : Yapılan en son işin verdiği yük.

7. alan : Yaptığı iş !

*Örnek :***

/home/e065247/m>w e065247

01:09AM up 10 hrs, 40 users, load average: 2.44, 5.04, 5.33

User tty login@ idle JCPU PCPU what

e065247 pts/5 11:50PM 1 5 5 telnet

e065247 pts/7 11:56PM 0 1 0 w

e065247 pts/12 11:50PM 0 0 0 telnet

**3.12. Yazıcıdan Dosyaların Çıktısını Almak******

lp (seçenekler) dosyalar

Burda dosya hemen yazdırılmayarak spool a atılacaktır.

*Seçenekler:***

-c : Lp komutu kullanıldığında yazdırılacak dosyanın bir kopyasının oluşturulması isteniyorsa -c seçeneği kullanılır.Bu seçenek kullanılmadığında kopyalama işlemi yerine link işlemi gerçekleştirilir.

-dyazici : Yazma işleminin yapılacağı yazıcının veya yazıcılar sınıfının belirlenmesi amacı ile bu seçenek tercih edilir.

-m : Dosyaların yazıcıdan bastırılması ardından mesaj gönderilmesine olanak sağlar.

-nsayi : Yazdırılacak dosyanın kopya sayısını saptamak üzere bu seçenekten yararlanılır. Kullanılmazsa 1 olduğu varsayılır.

-s : lp den "request id is.."gibi mesajların atılmasını sağlar.

-tbaslik : Yazıcıdan alınan çıkışa bir başlığın yazdırılması isteniyorsa bu seçenek kullanılır.

Yazıcıya yolladığım dosyanın durumunu nasıl öğrenebilirim ?

lpstat (seçenekler)

*Seçenekler:***

-a(liste) : Listede belirtilen yazıcılara gönderilen istekler hakkında bilgi verir.

-c(liste) : Yazıcı sınıfları ve onların üyelerini görüntüler.

-d :sistemin kabul ettiği yazıcıyı görüntüler.

-o(liste) : Yazdırılmak üzere gönderilen dökümleri görüntüler.Liste yazıcı isimlerini sınıfları ve istekleri kapsar.

-r : Lp istek tablosunun durumunu görüntüler.

-s : Sistemin kabul ettiği yazıcının ismi ver her bir yazıcının sahip olduğu özel dosya isimlerini görüntüler.

-t : Tüm durum raporunu görüntüler.

-u(liste): Liste içinde belirtilen kullanıcılara ilişkin durum raporunu görüntüler.

Yazıcıya yolladığım bir dosyayı henüz basılmadı ise iptal edebilir miyim ?

Evet. Bunun için ;

cancel (liste numarasi) (yazıcılar)

**3.13. Alias ( Farklı İsim ) Tanımlamak******

Alias tanımlamaları kullandığınız shell programına göre değişir.

C tabanlı shell'lerde ( csh , tcsh ) bu is oldukça kolaydır ;

*Kullanımı :***

alias kısaltma 'komut dizisi'

*Örnek :***

alias dir 'ls -lFa | more'

bundan sonra her dir yazdığınızda ls -lFa | more komut dizisi işleyecektir.

Sh tabanlı shellerde ( sh, ksh vs.) :

*Kullanımı :***

alias kısaltma="komut dizisi"

*Örnek :***

alias dir="ls -lFa |more"

**3.14. Bir Dosyanın İçini Görmek İçin Kullanılan Programlar******

cat \[dosya\_ismi\] \[dosya\_ismi\] ...

Bir dosyanın içine bakmaya yarar. Dosyanın içeriği hiçbir şekilde durmadan ekrandan akıp geçer. Boyları küçük olan dosyalara bakmak için kullanılabilir, ancak büyük dosyalara bakmak için uygun değildir. Ancak başka amaçlar için kullanılabilir örneğin

cat file1 >> file2

komutu file1 dosyasının içeriğini file2 dosyasının arkasına kopyalar. Bu işlem sonunda file1'in içeriğinde bir değişiklik olmaz.

pg seçenekler (dosya..)

*Seçenekler:***

-numara: Her defasında görüntülenecek satırların sayısını gösterir.

-p dizgi: Normal olarak sayfanın en alt satırında (:)işareti olarak kullanıcının return a basması beklenir.

-c:Her bir sayfa görüntülenmeden önce ekran temizlenir ve imlece başlangıç konumuna döner.

-e: Her dosyanın sonunda kullanıcının return a basması gerekmez.

-n: Normal olarak komutlar yeni satir karakteri ile son bulur.Otomatik olarak komut sonunun belirlenmesine olanak sağlar.

-s: msg ların görüntülenmesini sağlar.

+satir no: Belirli bir satırdan itibaren dosya görüntülenmek isteniyorsa doğrudan satir numarası yazmak sureti ile bu sağlanır.

+/kalip/: Belirlenen kalıbı içeren ilk satiri bulmak amacıyla bu tur bir tanım yapılabilir.

more \[dosya\_ismi\] \[dosya\_ismi\] ...

Bir dosyanın içeriğini ekranda görmek için kullanılır, ancak cat'ta olduğu gibi dosyanın içeriği ekrandan kayıp geçmez. Her sayfanın sonunda ekranın sol alt köşesinde --More--(x%) seklinde bir yazı belirir. Buradaki x' dosyanın yüzde kaçının görüldüğünü gösterir. Bu dosyanın büyüklüğü hakkında size bilgi verebilir. --More--(x%) yazısını gördükten sonra aşağıdaki tuş'ları kullanabilirsiniz.

SPC : Arka sayfaya geçilmesini sağlar.

K : K ' herhangi bir tam sayıdır. Bu sayı kadar ileriye gidilmesini sağlar

Kb : K sayısı kadar geri dönülmesini sağlar.

Ks : K sayısı kadar ileri gidilir, ancak aradaki satırlar görüntülenmez.

= : Bulunduğunuz satır numarası verilir.

/ : Dosyada arama yapmak için kullanılır.

v : vi editorünü çağırır.

q : programdan çıkar.

less \[seçenekler\] \[dosya\] \[dosya\] ....

More ve vi programlarının bir karışımıdır denilebilir. İleri olduğu gibi geriye doğruda kolaylıkla işlem yapılabilmesini sağlar.

H, h : Komutların kısa bir özetini gösterir.

SPC,^V,f,^F : Arka sayfaya geçer.

Kz : K sayısı kadar ileri gider.

RETURN,e,j : Bir satır ileri gider.

d,^D : Yarım sayfa ileri gider.

b,^B : Bir sayfa geriye gider.

y,k : Bir satır geriye gider.

u,^U : Yarim sayfa geriye gider.

r,^R,^L : Ekranı temizler.

q : Programdan çıkar.

---
*Kaynak: `UNIX/UNIX.doc` — T01 — 2004*
