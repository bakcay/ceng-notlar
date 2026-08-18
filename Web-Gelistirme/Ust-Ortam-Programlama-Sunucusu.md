# Üst Ortam Programlama Sunucusu

## **ÜSTORTAM PROGRAMLAMA SUNUCUSU**

## **ÖZET**

Kullanıcısı sayısı her geçen gün artan Internet’te, eğitim kurumlarına destek veren çalışmalar yapan pek çok adres bulunmaktadır.

Bu araştırmada, Linux işletim sistemi ve onun veritabanlarından biri olan mSQL ve Perl programlama dili kullanılarak gerçekleştirilen ve

http://bilmuh.ege.edu.tr/~sorubank/dersler/ustortam adresinde öğrencilerin ve araştırmacıların kullanımına sunulan, "Üstortam Programlama Sunucusu", Ege Üniversitesi Bilgisayar Mühendisliği Bölümünde, Üstortam Programlama-I ve Üstortam Programlama-II derslerinde interaktif öğretim aracı olarak kullanılmaktadır.

## ***HYPERMEDIA PROGRAMMING SERVER***

## **SUMMARY**

On the Internet there are various sites which present services for the educational instutions.

In this research, the “Hypermedia Programming Server” that is developed with the Linux operating system, mSQL and Perl programming language is introduced. The server is available at http://bilmuh.ege.edu.tr/~sorubank/dersler/ustortam for the students and the researchers and it is being used at Ege University Computer Engineering Department as an interactive tool in the classes of Hypermedia Programming-I and Hypermedia Programming-II.

## **LİSANS PROJESİ - 2001**

## **HAZIRLAYAN**

## **Erdem YILMAZ**

1979 yılında Hatay’da doğdu. Lise öğretimini Hatay Osman Ötken Anadolu Lisesi’nde tamamladı. Ege Üniversitesi Mühendislik Fakültesi Bilgisayar Mühendisliği bölümü 2001 yılı mezunudur.

## **DANIŞMAN**

## **Doç.Dr. Ata ÖNAL**

1996 yılında Bilgisayar Yazılımı Anabilim Dalı’nda doçent oldu. Halen Ege Üniversitesi Mühendislik Fakültesi Bilgisayar Mühendisliği Bölümünde Öğretim Üyesi olarak görev yapmaktadır.

## **1. GİRİŞ**

Internet yaşantımızın vazgeçilmez bir parçası olma konusundaki güncelliğini korumaktadır. Araştırmacılar, yaptıkları çalışmaların Internet ortamında kullanılabilmesi için tasarım ve gerçekleştirim çalışmaları yapmakta, kendi WEB sayfalarını ve SERVER’larını kullanıma sunmaktadırlar.

Debian Linux işletim sistemi, mSQL veritabanı ve Perl programlama dili kullanılarak tasarlanıp gerçekleştirilen, "Üstortam Programlama Sunucusu", http://bilmuh.ege.edu.tr/~sorubank/dersler/ustortam adresinde, Html \[1,2\], Java \[3,4,5,6\], Linux \[7\], Perl \[8,9,10\], mSQL \[11\] konularında çalışma yapmak isteyen öğrencilerin ve araştırmacıların kullanımına sunulmuştur.

Bu çalışmada, Üstortam Programlama-I başlığı altında HTML ve JAVA, Üstortam Programlama-II başlığı altında, Linux, PERL, MSQL, Perl-Cgi-MSQL, ve yeni eklenen ( MySql \[12\], Perl-Cgi-MySql, PHP \[13\] ve PHP-Cgi-MySql ) konuların işlenişi ve sınavların nasıl değerlendirildiği ve bu işlemler yapılırken, Üstortam Programlama Sunucusu’nun etkin olarak nasıl kullanıldığı üzerinde durulacaktır.

## **2. ÜSTORTAM PROGRAMLAMA-I**

Üstortam Programlama-I dersi, Ege Üniversitesi Bilgisayar Mühendisliği Bölümünde 5.yarıyılda seçimlik ders olarak okutulmakta ve bu dersin kapsamında HTML ve JAVA konuları işlenmektedir.

HTML bölümünde, fontlar, tablolar, frameler, formlar, linkler, resimler, sesler ve animasyonlar gibi konular üzerinde durulmakta ve HTML kodlaması için, Windows ortamında Notepad, WordPad, Word, Excel, Linux ortamında Pico, Dos ortamında Edit gibi editörlerden ve HotDog, FrontPage, Netscape, Homesite, Dreamweaver gibi yazılımlardan yararlanılmaktadır.

JAVA bölümdeki konular, Java How to Program, Deitel & Deitel kitabı baz alınarak hazırlanmıştır. Kontrol yapıları, metotlar, string işlemleri, grafik çizimi, imgeler, animasyonlar ve sesler, dosyalar ve streamler, networking ve java utility paketi ve bit işlem gibi konular üzerinde örneklerle durulmaktadır.

HTML ve JAVA konularının işlendiği Üstortam Programlama-I dersinin, Üstortam Programlama Sunucusu’ndaki directory yapısı (Tablo 1)’de verilmiştir.

*Tablo 1 - ÜSTORTAM PROGRAMLAMA SUNUCUSU, *

*ÜSTORTAM PROGRAMLAMA-I DERSİ DIRECTORY YAPISI*

| Home |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | Sorubank |  |  |  |  |  |
|  |  | Dersler |  |  |  |  |
|  |  |  | Ustortam1 |  |  |  |
|  |  |  |  | Html |  |  |
|  |  |  |  |  | Bölüm01 |  |
|  |  |  |  |  |  | Konu/lar |
|  |  |  |  |  |  | Ornek/ler |
|  |  |  |  |  |  | Quiz/ler |
|  |  |  |  |  |  | Odev/ler |
|  |  |  |  |  | Bölüm02 |  |
|  |  |  |  |  | . |  |
|  |  |  |  | Java |  |  |
|  |  |  |  |  | Bölüm01 |  |
|  |  |  |  |  | . |  |
|  |  |  |  | Quizler |  |  |
|  |  |  |  | Ödevler |  |  |
|  |  |  |  | Sınavlar |  |  |
|  |  |  |  |  | Vize-1 |  |
|  |  |  |  |  | Vize-2 |  |
|  |  |  |  |  | Final |  |
|  |  |  |  |  | Bütünleme |  |
|  |  |  |  | Sınav Sonuçları |  |  |

Üstortam Programlama-I dersine kaydolan öğrencilere “Üstortam Programlama Sunucusu”’ndan userid verilir. 1999-2000 öğretim yılı öğrencilerine ilişkin Üstortam Programlama-I userid directory yapısı (Tablo 2)’de verildiği gibidir.

*Tablo 2 - ÜSTORTAM PROGRAMLAMA SUNUCUSU, ÜSTORTAM PROGRAMLAMA-I dersi ****USERID**** DIRECTORY YAPISI*

Home****Users****Ustortam1****1999-2000******Userid**WwwhomederslerUstortam1HtmlBölüm01QuizlerQ1xxxxQ2xxxxodevlerO1xxxxBölüm02JavaQuizlerÖdevlerDönem ÖdeviVize-1Vize-2FinalBütünleme

Dersler 20 kişilik bilgisayar laboratuarında 20 şerli gruplar olarak işlenmektedir. Üstortam Programlama-I dersi, yarıyıl boyunca, haftada 3 saat olmak üzere bölüm/ler - konu/lar – örnek/ler (soru-cevap-source) – quiz/ler (soru-cevap-source) – ödev/ler (soru-cevap-source) ve dönem ödevi \[konu/lar, (örnek/ler, quiz/ler ve ödev/ler) (soru-cevap-source)\] şeklinde planlanmıştır (Tablo 1).

Quiz/ler, ödev/ler ve dönem ödevinden alınan not %20 olarak vize, final ve bütünleme (varsa) notuna yansıtılır. Öğretim elemanı ilk hafta öğrencilere, yarıyıl boyunca, Üstortam Programlama Sunucusu’ndaki, Üstortam Programlama-I dersinin directory yapısının (Tablo 1), bir benzerinin, kendi userid’lerında (WEB sayfalarında) oluşturulacağını belirtir (Tablo 2).

Öğretim elemanı, konuyu (çözümlü örneklerle) anlatırken (Tablo 1), önündeki monitorü kullanabilir. Öğrenciler de öğretim elemanını, önlerindeki monitörü izleyerek dinleyebilirler.

Dersin bitiminden uygun bir zaman önce, öğrencilerden konu kapsamından seçilen bir quiz sorusunu cevaplamaları istenir. Öğrenciler, quiz sorusunu, soru-cevap-source mantığında, kendi WEB sayfalarında, Üstortam Programlama-I dersi sunum mantığına uygun olarak cevaplar. Quiz puanlaması, öğrencilerin cevaplama süreleri dikkate alınarak yapılır.

Ders sonunda öğrencilere bir hafta süreli ödev verilir. Öğrencilerden, ödevlerini WEB sayfalarında, benzer mantıkta, yapmaları istenir. Ödev puanlaması bir sonraki hafta yapılır.

Öğrenciler, dönem ödevlerini, final sınavından 15 gün önce WEB sayfalarına koymalıdırlar. Dönem ödevi, konu anlatımı, örneklerin (soru-cevap-source) yapılışı ve örnek sayısı dikkate alınarak değerlendirilir.

Vize-1, Vize-2, Final ve Bütünleme sınavları (Tablo 1) bilgisayar laboratuarında interaktif olarak yapılır. Öğrenciler sınav sorularını Üstortam Programlama Sunucusu WEB sayfasının ilgili sınav bölümünden okur (Tablo 1) ve soru-cevap olarak kendi WEB sayfasının ilgili sınav bölümüne koyar (Tablo 2).

Sınavların değerlendirilmesi, quiz ve ödevlerde olduğu gibi yine öğrencinin WEB sayfasından yapılır. Sınav sonuçları, “Üstortam Programlama Sunucusu” WEB sayfasında sınav sonuçları bölümünde ilan edilir (Tablo 1).

## **3. ÜSTORTAM PROGRAMLAMA-II**

Ege Üniversitesi Bilgisayar Mühendisliği Bölümü 6.yarıyılında, seçimlik ders olarak okutulmakta olan Üstortam Programlama-II dersi kapsamında ise, LINUX, PERL, MSQL, PERL-CGI-MSQL, MYSQL, PERL-CGI-MYSQL, PHP ve PHP-CGI-MYSQL konuları işlenmektedir.

Yarıyıl boyunca öğrencilere deneme amaçlı kullanabilecekleri bir bilgisayar (Deneme Server) ayrılmaktadır.

Öğrencilere öncelikle, değişik Linux yazılımlarının (Slakware, Redhat, Debian, v.b.) kurulumları, Linux directory yapısı, Üstortam Programlama Sunucusu directory yapısı ve Üstortam Programlama-II dersi directory yapısı konularında bilgi verilir.

Öğrenciler isterlerse, Deneme Server’ını kullanarak öğrendiklerini pekiştirebilirler.

PERL bölümünde, Perl 5 by Example by David Medinets, kitabı kapsamındaki konular üzerinde durulmakta ve Perl örneklerinin test edilmesinde Perl Builder yazılımı kullanılmaktadır.

MSQL bölümünde ise, MSQL kurulumu, MSQL uygulaması, Perl-mSQL kurulumu, Perl-Cgi-mSQL uygulaması üzerinde durulmaktadır. Öğrenciler, Perl-Cgi-MSQL uygulamalarını hazırlarken, isterlerse, doğrudan Üstortam Programlama Sunucusu’ndaki user’larını kullanabilirler, ya da isterlerse önce kendi bilgisayarlarında yazılımı tamamlayıp, FTP ile Üstortama Programlama Sunucusu’ndaki user’larına gönderebilirler.

Benzer şekilde sırasıyla, MySql, Perl-MySql, PHP ve PHP-MySql kurulumları ve uygulamaları üzerinde durulmaktadır.

Üstortam Programlama Sunucusu’ndaki, Üstortam Programlama-II dersi directory yapısı (Tablo 3)’de, Üstortam Programlama-II dersi userid directory yapısı (Tablo 4)’de, Üstortam Programlama-II dersi userid Cgi-Bin directory yapısı (Tablo 5)’de verilmiştir.

Üstortam Programlama-II dersinin işlenişi ve sınav değerlendirmesi, Üstortam Programlama-I dersindeki gibi yapılmaktadır.

## ***Tablo 3 - **USTORTAM PROGRAMLAMA SUNUCUSU,** *

*ÜSTORTAM PROGRAMLAMA-II DERSİ DIRECTORY YAPISI*

| home |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | **Sorubank** |  |  |  |  |  |
|  |  | Dersler |  |  |  |  |
|  |  |  | Ustortam2 |  |  |  |
|  |  |  |  | Linux |  |  |
|  |  |  |  | Perl |  |  |
|  |  |  |  |  | Bölüm01 |  |
|  |  |  |  |  |  | Konular |
|  |  |  |  |  |  | Ornekler |
|  |  |  |  |  |  | Quizler |
|  |  |  |  |  |  | Odevler |
|  |  |  |  |  | Bölüm02 |  |
|  |  |  |  |  | . |  |
|  |  |  |  | MSql |  |  |
|  |  |  |  | Perl-Cgi-mSql |  |  |
|  |  |  |  | MySql |  |  |
|  |  |  |  | Perl-Cgi-MySql |  |  |
|  |  |  |  | Php |  |  |
|  |  |  |  | Php-Cgi-MySql |  |  |
|  |  |  |  | Quizler |  |  |
|  |  |  |  | Ödevler |  |  |
|  |  |  |  | Sınavlar |  |  |
|  |  |  |  | Sınav Sonuçları |  |  |

*Tablo 4 - **USTORTAM PROGRAMLAMA SUNUCUSU,** ÜSTORTAM PROGRAMLAMA-II dersi ****USERID**** DIRECTORY YAPISI*

HomeUsersUstortam21999-2000**Userid**WwwhomederslerUstortam2LinuxPerlBölüm01quizlerQ1xxxxQ2xxxxodevlerO1xxxxO2xxxxBölüm02.MsqlPerl-Cgi-MsqlMySqlPerl-Cgi-MySqlPhpPhp-MySqlQuizlerÖdevlerDönem ÖdeviVize-1Vize-2FinalBütünleme

## *Tablo 5 - **USTORTAM PROGRAMLAMA SUNUCUSU,** *

*ÜSTORTAM PROGRAMLAMA-II dersi ****USERID**** ****CGI-BIN**** DIRECTORY YAPISI*

VarLibHttpdCgi-binUsersUstortam21999-2000**Userid**derslerUstortam2Perl-Cgi-MsqlquizlerQ1xxxxQ2xxxxodevlerO1xxxxO2xxxxPerl-Cgi-MySql****

## **4. SONUÇ**

Ege Üniversitesi Araştırma Fonu 1998-Müh-021 nolu projesi olan ÜSTORTAM PROGRAMLAMA SUNUCUSU \[14\], Pentium-II 300 MMX, 128MB RAM, 12GB HD donanımlı, Linux – mSQL - PERL yazılımlı bir SERVER olarak tasarlanıp gerçekleştirilmiş ve http://bilmuh.ege.edu.tr/~sorubank/dersler/ustortam adresinde kullanıma sunulmuştur.

Bu adresine erişen kullanıcılar, Üstortam Programlama dersleri kapsamında bulunan (Html, Java, Linux, Perl, mSQL, MySql, Php) konuları öğrenebilmekte, server’dan userid alabilmekte, kendi WEB sayfalarını tasarlayabilmekte ve Veritabanı uygulaması yapabilmektedirler.

Üstortam Programlama Sunucusu, 1998-1999 öğretim yılından itibaren, Ege Üniversitesi Bilgisayar Mühendisliği Bölümü derslerinden Üstortam Programlama-I ve Üstortam Programlama-II dersini seçen öğrenciler tarafından, ders sırasında bilgisayar laboratuvardaki bilgisayarlardan, ders dışında Internete bağlı tüm bilgisayarlardan 24 saat süreyle kullanılabilmektedir.

Üstortam Programlama-I ve Üstortam Programlama-II derslerinde aktif olarak kullanılmakta olan Üstortam Programlama Sunucusu, dersler, ders konuları ve soru-cevap-source şeklindeki örnek, quiz ve ödev sayıları günün koşullarına uygun olarak yenilenerek çoğaltılmaktadır.

Ayrıca, öğrenciler, WEB sayfalarının dersler bölümünde, benzer şekilde konu anlatımları, soru–cevap-source şeklinde örnekler, quizler ve ödev soruları olarak kişisel görüşlerini de kullanıma sunabilmektedir.

Benzer işleri yapabilen, değişik donanım ve yazılım özellikli SERVER’lar da oluşturulabilir.

Üstortam Programlama Sunucusu gibi SERVER’ların, eğitimde daha aktif kullanılabilmesi için, benzer araştırma çalışmalarının çoğalması gerekmektedir.

## **KAYNAKÇA**

\[1\] HTML 3.2 and CGI Professional Reference Edition UNLEASHED

\[2\] HTML By Example, by Todd Stauffer

\[3\] Deitel, H. M., Deitel, P. J., JAVA How To Program, Prentice-Hall, New Jersey.

\[4\] Mark Wutka, et. al., JAVA Expert Solutions.

\[5\] Patrick Naughton & Herbert Schildt, JAVA: The Complete Reference www.perl.com, Perl.

\[6\] Platinum Edition, Using HTML 3.2, Java 1.1, and CGI

\[7\] http://www.linux.com

\[8\] David Medinets, Perl 5 by Example.

\[9\] David Harlan, et al., Special Edition Using Perl for Web programming.

\[10\] Herrmann, E. (1997), CGI Programming with Perl 5 in a week, Sams.net.

\[11\] http://www.Hughes.com, Mini SQL 2.0.

\[12\] http://www.mysql.com

\[13\] http://www.php.net

\[14\] Önal, A., Demirkan, B., Demirten, M., 1999, Üstortam Programlama Sunucusu, Ege Üniversitesi 1998-Müh-021 nolu Araştırma Projesi.

## PAGE

## PAGE 4

---
*Kaynak: `ÜST ORTAM PROGRAMLAMA SUNUCUSU/ÜST ORTAM PROGRAMLAMA SUNUCUSU.doc` — sorubank — 2004*
