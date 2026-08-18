# Prolog İle Uzman Sistem Hazirlama

** İÇİNDEKİLER**

TEŞEKKÜR i

İÇİNDEKİLER ii

ÖZET viii

ABSTRACT x

1.GİRİŞ 1

2. PROLOG’UN (PROGRAMMING IN LOGIC) TEMELLERİ 3

2.1. Gerçekler: Bilinen olgular 4

2.2. Kurallar: Verilen Gerçeklerden Hüküm Çıkarma 4

2.3. Sorgulamalar: (Querries) 5

2.4. Gerçekler, Kurallar ve Sorgulamaların Bir Araya Yazılması 6

2.5. Değişkenler: Genel Cümleler 7

2.6. Bölüm Özeti 8

2.7. Konuşma Dilindeki Cümlelerin Prolog Programlarına Aktarılması 9

2.8. Cümleler (Gerçekler ve Kurallar) 9

2.9. Olgular Arasındaki İlişkiler: Yüklemler (Predicates) 12

2.10. Değişkenler (Genel Cümleler) 13

2.10.1. Prolog’da Değişkenlerin Değer Alması 13

2.11. Anonim Değişkenler 15

2.12. Hedefler (Sorgular) 16

2.13. Açıklama Satırları 17

2.14. Eşleştirme 18

2.15. Bölüm özeti 18

3. VISUAL PROLOG PROGRAMLARININ TEMEL BÖLÜMLERİ 20

3.1. Clauses(Olgular veya Kurallar) 20

3.2. Predicates (Yüklemler) 20

3.3. Domains (Değişken Tipleri) 20

3.4. Goal (Hedef) 20

3.5. Yüklem Tanımı 20

3.6. Domains (Tip tanımları) Bölümü 22

3.7. Goal Bölümü 25

3.8. Deklarasyon ve Kurallara Ayrıntılı Bakış 25

3.8.1. Char 26

3.8.2. Real 26

3.8.3. String 26

3.8.4. Symbol 26

3.9. Yüklemlerdeki Argümanların Yazılması 27

3.10. Kuralların Yazım Biçimi 29

3.11. Prolog ve Diğer Dillerdeki ‘if’ Komutunun Karşılaştırılması 30

3.12. Otomatik Tip Dönüştürmeler 30

3.13. Bir Programın Diğer Bölümleri 31

3.13.1. Database Bölümü 31

3.13.2. Constants Bölümü 31

3.13.3. Global Bölümü 32

3.14. Derleyici Direktifleri 32

3.14.1. Include Direktifi 32

3.15. Bölüm Özeti 33

4. EŞLEŞTİRME VE GERİYE İZ SÜRME 34

4.1. Geriye İz Sürme 36

4.2. Geriye İz Sürme Mekanizmasının Ayrıntıları 39

4.2.1. Geriye İz Sürmenin 4 Temel Prensibi 40

4.3. Tarama İşleminin Kontrol Edilmesi 44

4.4. fail* *Yükleminin Kullanılması 45

4.5. Geriye İz Sürmeyi Engelleme 46

4.5.1. Cut Komutunun Kullanımı 46

4.5.2. Geriye İz Sürmeyi Engelleme 48

4.6. Determinism ve Cut 49

4.7. Not Yüklemi 50

4.8. Prosedürel Açıdan Prolog 54

4.8.1. Kurallar ve Olguların Prosedürlere Benzerliği 55

4.8.2. Bir Kuralın Case ifadesi Gibi Kullanılması 55

4.8.3. Bir Kural İçinde Test Yapmak 56

4.8.4. Cut Komutunun Goto Gibi Kullanılması 56

4.9. Hesaplanmış Değerleri Görüntüleme 57

5. BASİT VE BİLEŞİK NESNELER 60

5.1. Basit veri nesneleri 60

5.1.1 Veri Nesneleri Olan Değişkenler 60

5.1.2. Veri Nesneleri Olan Sabitler 60

5.1.3. Karakterler 60

5.1.4. Sayılar 61

5.1.5. Atomlar 61

5.2. Bileşik Veri Nesneleri ve Fonksiyon Operatörleri 62

5.3. Bileşik Nesnelerin Eşleştirilmesi 62

5.4. Bileşik Nesneleri Eşleştirmek İçin ‘=’ Sembolünün Kullanılması 63

5.5. Birden Fazla Nesneyi Tek Nesne Olarak Kullanmak 63

5.6. Bileşik Nesnelerin Tiplerini Tanımlamak 67

5.7. Tip Tanımlamaları Üzerine Kısa Bir Özet 69

5.8. Çoklu-Düzey Bileşik Nesneler 69

5.9. Çoklu-Tipli Argümanlar 70

5.10. Listeler 70

6. TEKRARLAMA VE REKÜRSİYON 73

6.1. Tekrarlı İşlemler 73

6.2. Geriye İz Sürme 73

6.3. Önceki ve Sonraki Eylemler 75

6.4. Döngülü Geriye Dönüşün Uygulanması 76

6.5. Rekursif Prosedürler 77

6.5.1. Rekursiyonun Avantajları 78

6.5.2. Sondan Rekursiyon Optimizasyonu 79

6.5.3. Sondan Rekursiyonun Kullanımı 80

6.5.3. Sondan Rekursiyonu Engelleme 80

6.6. Rekursiyonda Cut Kullanımı 83

6.7. Argümanların Döngü Değişkeni Olarak Kullanımı 85

6.8. Rekursiv Veri Yapıları 88

6.9. Ağaç Biçimindeki Veri Türleri 89

6.9.1. Bir Ağaç Yapısında Tarama Yapma 89

6.10. Bir Ağaç Oluşturmak 91

6.11. Binary Arama Ağacı 93

6.12. Ağaca Bağlı Sıralama 95

7. LİSTELER VE REKÜRSİYON 98

7.1. Listeler 98

7.2.1. Liste Tanımlanması 98

7.2.2. Bir Listenin Parçaları: Baş ve Kuyruk 99

7.2.3. Listelerin İşlenmesi 100

7.2.4. Listelerin Kullanılması 101

7.2.5. Liste Elemanlarının Sayılması 102

7.2. Sondan Rekursiyona Yeniden Bakış 103

7.3. Liste Elemanlığı 106

7.4. Listeleri Birleştirme 106

7.5. Rekursiyona Prosedürel Bir Bakış 107

7.6. Bütün Çözümleri Bir Defada Bulma 108

7.7. Bileşik Listeler 109

8. AKIŞ DENETİMİ 111

8.1. Bileşik Akış 112

8.2. Yüklemlerin Akış Biçimlerini Tanımlama 113

8.3. Akış Analizini Kontrol Etmek 113

8.4. Referans Değişkenler 115

8.4.1. Referans Tip Tanımı 116

8.4.2. Referens Tip ve İzleme Dizileri(array) 116

8.5. Referans Tip Kullanımı 117

8.6. Akış Biçimine Yeni Bir Bakış 118

8.7. İkili (Binary) Ağaç Yapısının Referans Tip İle Kullanımı 119

8.8. Referans Tip Kullanarak Sıralama 120

8.9. Binary (İkili) Tip 121

8.9.1. Binary Terimlerin Kullanılması 122

8.9.2. Binary Terimlerin Yazım Biçimi 122

8.9.3. Binary Terimlerin Oluşturulması 122

8.9.3.1. makebinary(1) 123

8.9.3.3. composebinary(2) 123

8.9.3.4. getbinarysize(1) 123

8.9.4. Binary Terimlere Erişim 123

8.9.4.1. getentry(2) 124

8.9.4.2. setentry(3) 124

8.9.5. Binary Terimleri Eşleştirme 124

8.9.6. Binary Terimleri Karşılaştırma 124

8.9.7. Terimleri Binary Terimlere Dönüştürme 126

8.9.7.1. term\_bin(3) 126

8.10. Hatalar ve İstisnalarla Uğraşma 126

8.10.1. exit(0), exit(1) 127

8.10.2. trap(3) 127

8.10.3. errormsg(4) 128

8.10.4. Hataların Bildirilmesi 129

8.11. Hata Düzeyi 129

8.11.1. lasterror(4) 130

8.11.2. Terim Okuyucudan Gelen Hataları Görme 130

8.11.3. consulterror(3) 130

8.11.4. readtermerror(2) 132

8.12. Break Kontrolü (Sadece Metin Modunda) 132

8.12.1. break(1) 132

8.12.2. breakpressed(1) 132

8.13. DOS Metin Modunda Kritik Hata Kontrolü 133

8.13.1. criticalerror(4) 133

8.13.2. fileerror(2) 134

8.14. Dinamik Cut 134

8.15. Programlama Stilleri 136

8.15. Cut Yüklemini Yerleştirmek 138

9. ÖZEL GELİŞTİRİLMİŞ PROLOG ÖRNEKLERİ 139

9.1. Küçük bir Uzman Sistem örneği 139

9.2. Basit bir yön problemi 143

9.3. Hazine Avcısı 144

TARTIŞMA VE SONUÇ 147

KAYNAKLAR 150

ŞEKİLLER ve TABLOLAR 152

ÖZGEÇMİŞ 153

**ÖZET**

Yüksek Lisans Tezi

PROLOG PROGRAMLAMA DİLİ İLE MAKİNE MÜHENDİSLİĞİ ALANINDA UZMAN SİSTEMLERİN HAZIRLANMASI TEKNİKLERİ

Yavuz Selim AYDIN

Harran Üniversitesi

Fen Bilimleri Enstitüsü

Makina Anabilim Dalı

1998, Sayfa: 164

Günümüzde bilgisayar alanında gözlenen hızlı değişim, yeni teknolojik imkanların ortaya çıkmasına neden olmaktadır. İnsanoğlu daha bundan birkaç yıl öncesinde hayal edemediği gelişmelerin günümüzde gerçekleştiğini gördükçe hayretler içerisinde kalmaktadır. Bilgi teknolojiyle yakından ilgilenenler dahi, bu hızlı değişime ayak uydurmada zorlanabilmektedir.

Bilgisayarların insanlar gibi düşünmesine sağlamak için yoğun çalışmalar sürdürülmededir. Mümkün olduğunca insan beyni fonksiyonlarına yakın işlevleri yerine getirebilecek mikroişlemcilerin tasarımı üzerinde çalışmalar sürdürülmektedir. Bu çalışmalar beşinci kuşak bilgisayar dönemine rastladığı ve bu kuşak içerisinde Yapay Zeka (Artificial Intelligece) alanlarında önemli gelişmelerin yer aldığı görülür.

Bilgi teknolojisinin amacı, uzman kişilerin bilgilerini bilgisayarda kullanarak yeni sonuçlar elde etmektir. Uzman sistemler, yapay zekanın bir dalı olup, bir probleme uzman insan düzeyinde bir çözüm bulmak için uzman bilgisini kullanırlar.

Yapay zekada sık kullanılan programlama dillerinden biri de Prolog dilidir. Son versiyonu Visual Prolog olarak piyasaya çıkartılmıştır. Visual Prolog, ifadeler mantığının kullanarak, bilgisayara çözümü aranan problem hakkında bilinen gerçekleri ve kuralları vererek, uygun bir çözüm elde edilmesine sağlar.

Konvansiyonel programlama dillerinde, bir programcı herhangi bir problemin nasıl çözüleceğini bilgisayara adım adım tanıtmak zorundadır. Oysa bir Visual Prolog programcısının yapması gereken şey, çözüm aranan problem hakkında bilinen gerçekler ve kuralları, bunlar arasındaki ilişkileri tanımlamak, daha sonra mümkün olana bütün çözümleri bulmak görevini Prolog’a vermektir. Visual Prolog, aritmetik işlemlerin yapılmasına da imkan tanır.

Visual Prolog, C++ ve diğer bilinen programlama dilleri kadar hızlı çalışır. Hızlı bir derleyici, bilgisayar dünyasında daima aranan bir avantaj olmuştur. Visual Prolog, MS DOS, Windows 3.1, Windows 95, Windows NT, Unix ve OS/2 işletim sistemleri altında programlamaya imkan tanıyan bir çoklu ortam programlama dilidir.

Uzman sistemlerin, bütün kullanıcılara düşük maliyetli uzmanlık, insanlar için tehlikeli olan ortamlarda riski azaltma, emekli olabilen veya vefat edebilen insan uzmanlar yerine, her zaman kalıcı olan uzmanlar ve verilen kararların net açıklanabilmesi gibi güzel özellikleri vardır.

Bu çalışma, yapay zeka alanında çalışma yapan, uzman sistem tasarlamak isteyen fakat Türkçe kaynak bulamayan, kaynak kullanarak Prolog dilini öğrenmek isteyen araştırmacılara faydalı olmak amacıyla gerçekleştirilmiştir. Prologun temel mantığı, elemanların ayrıntılı anlatımı, Prologun en önemli özelliklerinden biri olan Geriye İz Sürme ve bu konuların açık biçimde kullanıldığı örnekler doyurucu bilgi sunmaktadır.

**Anahtar Kelimeler:** Uzman Sistemler, Yapay Zeka, Visual Prolog, Programlama Dilleri

**ABSTRACT**

Master Thesis

TECHNQUES ON THE DESIGN OF EXPERT SYSTEMS IN MECHANICAL ENGINEERING BY USING THE VISUAL PROLOG PROGRAMMING LANGUAGE

Yavuz Selim AYDIN

Harran University

Graduate School of Natural and Applied Sciences

Department of Mechanical Engneering

1998, Page: 164

Rapid advancement in the computer technology has brought new technological facilities. People are surprised to see that the technological innovations which could not even be dreamt of just a few years ago have been achieved. Even those closely involved in the Information Technology may sometimes face some difficulties in coping up with the rapid changes.

Intensive studies have been performed by scientists to enable a computer to imitate human beings in the way he thinks. Studies to design microprocessors capable of performing similar functions of human brain still continue. It is observed that such studies coincided with the evolution period of the fifth generation computers and that important improvements have been recorded in the field of Artificial Intelligence.

Information technology aims at making use of an expert’s knowledge from which new results may be retrieved. Being a subbranch of Artificial Intelligence, expert systems use the knowledge of a human expert to find a solution for a given problem at expert level.

One of the programming languages frequently used in artificial intelligence is Prolog, of which the latest version has been released as the Visual Prolog. It uses logical expressions which tell the computer the facts and rules about a problem so that a solution based on the given facts and rules could be obtained by using a deductive procedure.

In conventional programming languages, a programmer must describe the solution to a problem step by step. In the Visual Prolog, on the other hand, a programmer must only describe the facts and rules about a problem –not steps necessary for the solution- in the form of some relations and then, let the Visual Prolog find all possible solutions for that problem. Visual Prolog is capable of performing arithmetic operations as well.

Visual Prolog runs as fast as C++ and other popular programming languages. A fast compiler has always been an advantage in the computing world. The Visual Prolog is a multiplatform programming language that allows programming under MS DOS, Windows 3.1-95 and NT, Unix and OS/2 operating systems.

Experts systems have some interesting characteristics such as low cost of expertise for all users, low risks in situations dangerous for humans, ever continuing expertise despite to human experts who may retire or pass away, and clear explanation of what has been concluded.

This study has been performed for researchers who wish to carry out studies in the field of Artificial Intelligence, design expert systems in Mechanical Engineering but lack to find a source about the Visual Prolog in Turkish and like to learn this language. Many superior features of the Visual Prolog, including backtracking and recursion, have been clearly explained in this study by providing many sample programs.

**Keywords:** Expert Systems, Artificial Intelligence, Visual Prolog, Programming Languages

**1. GİRİŞ**

İngilizce Expert System kelimelerinden türetilerek Türkçe’ye kazandırılmış olan **Uzman Sistem** yazılımları alanında, ülkemizde yoğun çalışmaların yapıldığı gözlenmektedir.

Bir Uzman Sistem, Bilgisayar Destekli Eğitim amaçlı da kullanılabileceğine göre, eğitim ve öğretim için gerekli olabilecek her türlü formasyonu taşımalıdır. Öğrenme, doğrudan bilgisayardan yapılacağı için, klasik öğretmen merkezli eğitime nazaran, içeriğin daha doyurucu ve cazip özellikler taşıması gerekir. Cazip unsurlar, bilgisayar tarafından yönetilmeli ve uygun ortamlarda ekranda veya bilgisayarın çevre birimlerinde ortaya çıkabilmelidir.

Öğretilmek istenen bir konuda işlem basamaklarının sırası çok önemlidir. Öğrenciye yöneltilecek sorular çok iyi belirlenmeli ve soru sorarken öğretme mekanizması devreye alınmalıdır. Soruların sıralanışında yeterli hassasiyet gösterilmediği takdirde, hem öğrenme eksik olabilir, hem de öğrenci yanlış bilgilendirmeye sevk edilebilir.

Uzman sistem üzerinde çalışan öğrenci, bilgisayarı ile yalnız başına kalacaktır. Sürekli monoton bir ekran görüntüsü yüzünden, öğrencinin öğrenme arzusu kırılabilir, bilgisayar önünde canı sıkılabilir. O halde öğretme esnasında, öğrencinin dikkatinin konuya sevk edilebilmesi için, program arasında görsel ve işitsel yöntemlerle uygun uyarılar yapılabilmelidir.

Bilgisayar destekli eğitimin kullanılabileceği her yere ilave olarak, problemlere çözüm getirilmek istenen her sahada Uzman Sistem kullanılabilir.

Bir Uzman Sistem hazırlanırken asgari olarak aşağıdaki hususların göz önünde bulundurulması gerekir.

Hazırlanacak proje konusu hem güncel olmalı hem de o konuda yeterli kaynak bulunabilmelidir.

Konunun bol miktarda resim ve şekil içermesi, kullanıcının öğrenme hızını artıracak bir faktördür.

Proje başlangıcında, güzel bir sunu yazılımıyla (örneğin Power Point gibi) proje hakkında özet bilgiler verilmeli, proje tasarımcısı ve denetleyen kişilerin isimleri, resimleri ve faydalanılan kaynaklar hakkında bilgi verilmelidir.

Konu anlatımına geçmeden önce, güzel bir müzik eşliğinde bilgisayar, kullanıcının ismini girmesini istenmelidir. Çünkü ilerleyen konular içerisinde bazı yerlerde esprili cümlelerle bilgisayarın kullanıcıya ismi ile hitap etmesi, kullanıcının aniden dikkatini çekmeye neden olabilmekte ve kullanıcı bu durumdan fazlasıyla memnun kalabilmektedir.

**2. PROLOG’UN (PROGRAMMING IN LOGIC) TEMELLERİ**

Bir Prolog programı, (Basic, Fortran, Pascal, C) olduğu gibi bir dizi komut satırından değil, doğruluğu önceden bilinen gerçeklerden ve bu gerçeklerden bilgi sağlamaya yarayan kurallardan oluşur.

Prolog, cümlecikler (**Horn Clauses**) üzerine bina edilmiştir. Cümlecikler, yüklem mantığı denilen formal sistemin bir alt kümesidir.

Prolog’da bir Karar Motoru **(Inference Engine)** vardır. Bu motor, verilen bilgiyi kullanarak cevabı aranan bir problem için, mantıksal bir şekilde karar veren bir işlemdir. Karar motorundaki Kalıp Eşleştirici **(Pattern Matcher)** sorulara uygun olan cevapları eşleştirerek önceden bilinen ve program içine kaydedilen bilgiyi geri çağırır. Prolog, program satırları içinde sorulan bir soruyu veya hipotezi doğrulamak için, doğruluğu önceden bilinen ve veri olarak yüklenmiş olan bilgi kümesini sorgulayıp hipotezin doğruluğu hakkında karar vermeye çalışır. Kısaca söylemek gerekirse, bir Prolog programının temelini, program akışı içinde önceden verilen gerçekler ve kurallar oluşturur.

Prolog’un önemli diğer bir özelliği de şudur: Sorulan sorulara mantıklı cevaplar bulmanın yanısıra, bulduğu tek bir çözümle yetinmez, başka alternatifleri de inceleyerek mümkün olan bütün çözümleri bulur. Prolog, bir programın birinci satırından başlayıp sonuncu satırına kadar ilerleyip sadece bir çözüm bulmak yerine, zaman zaman geriye dönüş yaparak problemin her bir bölümünün çözümü için alternatif yolları da arar.

Yüklem mantığı, mantığa dayalı fikirleri yazılı bir şekilde ifade etmeye yarayacak şekilde geliştirilmiştir ve Prolog’da bu mekanizma gayet iyi kullanılır. Yüklem mantığının yaptığı ilk iş, cümlelerdeki gereksiz kelimeleri ayıklamaktır. Daha sonra cümleler-kelimeler arasındaki ilişkiler ilk sıraya, nesneler ise ilişkilerden sonra sıralanır. Bu nesneler ise ilişkilerin etkili olduğu argümanlar olarak yazılır.

**Konuşma Dili Prolog’daki Karşılığı**

Ahmet bir insandır. insan(Ahmet).

Gül kırmızıdır. kirmizi(gul).

Ahmet, gülü kırmızı ise sever. sever(Ahmet, gul) **if** kirmizi(gul).

Prolog ile program yazarken, ilk önce nesneler ve bu nesneler arasındaki ilişkiler tanımlanır. ‘Ahmet gülleri sever’ cümlesindeki Ahmet ve gül kelimeleri nesne, ‘sevmek’ ise bu iki nesne arasındaki ilişkidir. Bu ilişkinin ne zaman doğru olacağını belirleyen ifadeye ise **Kural **denir. ‘Ahmet, gülü kırmızı ise sever’ cümlesindeki ‘sevmek’ hangi durumda Ahmet’in gülü seveceğini belirttiği için bu durumda **Kural** olur.

**2.1. Gerçekler: Bilinen olgular**

Prolog’da, nesneler arasındaki ilişkiye **Yüklem** denir. Tabii dilde bir ilişki bir cümle ile sembolize edilir. Prolog’un kullandığı yüklem mantığında ise bir ilişki, bu ilişkinin ismi ve bunu takiben parantez içinde yazılan nesne veya nesnelerden oluşan basit ifadelerle özetlenir. Gerçekler, tıpkı cümlelerdeki gibi ‘.’ ile biter. Aşağıdaki örneklerde ‘sevmek’ fiilinin tabii dilde ifade edilmesi gösterilmiştir.

Yasin Esra’yı sever.

Esra Cihat’ı sever.

Yasin kedileri sever.

Yukarıdaki ifadeleri olgu olarak kabul edip Prolog’daki karşılıklarını yazalım:

sever(yasin, esra).

sever(esra, cihat).

sever(yasin, kediler).

Görüldüğü gibi, gerçekler nesnelerin ve ilişkilerin değişik özelliklerini de ifade edebilirler.

**2.2. Kurallar: Verilen Gerçeklerden Hüküm Çıkarma**

Kurallar, gerçek olguları kullanarak bir sonuca varmak için kullanılır. Aşağıda ‘sevmek’ ilişkisinden elde edilen bazı kurallar verilmiştir:

Yasin, Esra’nın sevdiği her şeyi sever.

Hasan kırmızı olan her şeyi sever.

Bu kuralları Prolog dilinde yazmak gerekirse:

sever(yasin, hersey):-sever(esra, hersey).

sever(hasan, hersey):- kirmizi(hersey).

Buradaki :- sembolü, prosedürel dillerdeki **if**(eğer) anlamında olup, bir kuralın iki parçasını birleştirir.

Prolog, sever(yasin, hersey):-sever(esra, hersey) kuralını kullanarak, Yasin’in sevdiği nesneyi bulmak için önce kuralın ikinci kısmını, yani Esra’nın sevdiği nesneyi bulur. Bunun doğruluğu ispatlandıktan sonra Yasin’in sevdiği nesneyi belirler.

**2.3. Sorgulamalar: (Querries)**

Prolog’a bazı gerçekler tanıtıldıktan sonra, artık bu gerçeklerle ilgili sorular sormaya başlanabilir. Bunu **Prolog Sistemini Sorgulama** diyoruz. Veri olarak saklanan gerçekler ve gerçekler arasındaki ilişkiler bilindikten sonra, bu ilişkiler hakkında soru sorup cevap almak kolaydır.

Günlük konuşmalarda Esra Yasin’i seviyor mu? şeklindeki bir soruyu Prolog’da şöyle ifade edilir.

sever(esra, yasin).

Bunun cevabı program akışı içerisinde verdiğimiz gerçeklere bağlıdır. Yasin neyi sever? şeklindeki bir soruyu Prolog’a sormamız mümkündür. Bunu sever(yasin, Neyi) şeklinde kodlarsak, Prolog’dan şu cevabı alırız:

Neyi=esra

Neyi=kediler

2 Solutions

Çünkü önceden verilen sever(yasin, esra) ve sever(yasin, kediler) ilişkileri, bunu ispatlamaktadır.

Burada Yasin ve Esra'ın küçük harfle, Neyi kelimesinin ise büyük harfle başlamaktadır. Çünkü, yüklemdeki Yasin sabit bir nesnedir, yani değeri sabittir. Oysa Neyi bir değişkendir. Yani farklı gerçeklerle beraber, sorgudan alınacak cevaplar da farklı olacaktır. Bu yüzden değişkenler daima büyük harf veya bir ‘\_’ ile başlar.

Bu durumda Neyi kelimesinin cevapları değişebilir. Prolog bir sorguya cevap ararken daima önceden verilen gerçeklerin ilkinden başlar ve hiçbirini ihmal etmeden en sondaki gerçeğe kadar ilerler.

Prolog’da, bir insana sorulabilecek başka soruları da sormak mümkündür. Fakat ‘Mehmet hangi kızı sever?’ şeklindeki bir soruya hiçbir cevap alınamaz. Çünkü yukarıdaki satırlar dikkate alındığında, bu konuyla ilgili bir bilginin mevcut olmadığı görülür. Yasin Esra’yı sevmektedir, fakat Esra’nın kız olduğuna dair bir bilgi mevcut olmadığından, Prologun bu gerçeklerden hareketle bir karara varması mümkün olamaz.

**2.4. Gerçekler, Kurallar ve Sorgulamaların Bir Araya Yazılması**

1. Aşağıdaki gerçekler ve kuralların var olduğunu kabul edilsin.

Büyük araba hızlıdır.

Büyük bir araba iyidir.

Küçük bir araba daha kullanışlıdır.

Kasım, eğer hızlı ise, büyük arabayı ister.

Yukarıdaki gerçeklerden anlaşılan şey, Kasım’ın hızlı ve büyük arabalardan hoşlandığıdır. Prolog da aynı sonuca varacaktır. Zaten hızlı arabalar hakkında bilgi verilmeseydi, hiçkimse Kasım’ın hızlı arabalardan hoşlandığı sonucuna varamazdı. Yapılabilecek tek şey, ne tür bir arabanın hızlı olacağını tahmin etmektir.

Aşağıdaki örneğe bakarak, Prolog’un kuralları kullanarak sorgulara nasıl cevap bulduğu açıklanmıştır.

hoslanir(cengiz, masa\_tenisi).

hoslanir(mehmet, yuzme).

hoslanir(yavuz, futbol).

hoslanir(levent, Spor):-hoslanir(yavuz, Spor).

Son satırdaki hoslanir(levent, Spor):-hoslanir(yavuz, Spor) bir kural olup, konuşma dilindeki karşılığı şudur: Levent, bir spor türünden **eğer **Yavuz da hoşlanıyorsa hoşlanır.

Bu kuralın baş tarafı hoslanir(levent, Spor) ve gövde kısmı hoslanir(yavuz, Spor) olur. Burada Levent’in yüzmeyi sevip sevmediği hakkında hiçbir bilgi yoktur. Bunu öğrenmek için hoslanir(levent,yuzme) şeklinde bir sorgu kullanmak yeterlidir. Cevap bulmak için Prolog hoslanir(levent, Spor):-hoslanir(yavuz, Spor) kuralını kullanır. Yukarıda geçen gerçeklerle bunlar arasındaki ilişkiler, aşağıdaki şekilde bir program haline getirilir

PREDICATES

nondeterm hoslanir(symbol,symbol)

CLAUSES

hoslanir(cengiz, masa\_tenisi).

hoslanir(mehmet, yuzme).

hoslanir(yavuz, futbol).

hoslanir(levent, Spor):- hoslanir(yavuz, Spor).

GOAL hoslanir(levent, futbol).

Bu program Prolog’da derlenirse, ‘yes’ cevabını alınır. Çünkü hoslanir(yavuz, futbol) gerçeği Yavuz’un futboldan hoşlandığını göstermektedir. hoslanir(levent, Spor):-hoslanir(yavuz, Spor*)* kuralı ise Levent’in, Yavuz’un yaptığı spor türlerinden hoşlandığını göstermektedir. İlgili olgu Yavuz’un futboldan hoşlandığını gösterdiği için, Levent’in de futboldan hoşlandığını söylemek mümkündür. Bu yüzden GOAL hoslanir(levent, futbol) sorgusunun cevabı ‘yes’ olur.

Fakat hoslanir(levent, tenis) sorgusunun cevabı ‘no’ olacaktır. Çünkü:

Bu sorgunun doğrulanabilmesi için gerçekler arasında öncelikle Yavuz’un tenisten hoşlandığını gösteren bir olgunun var olması gerekir.

hoslanir(levent,Spor):-hoslanir(yavuz, Spor) kuralı, üstteki gerçekleri kullanarak bu konuda bir karara varamaz. Çünkü kuralın gövdesini doğrulayacak bir bilgi olmadığından, kural başarısız olur.

**2.5. Değişkenler: Genel Cümleler**

Prolog’da değişkenler kullanılarak genel gerçekler, kurallar yazılabilir ve genel sorular sorulabilir. Değişkenler tabii dilde de kullanılır. Tipik bir örnek vermek gerekirse:

Kasım, Ferit’in sevdiği şeyi sever.

Bu bölümün başında da belirtildiği gibi, Prolog’da değişkenler daima büyük harf veya bir ‘\_’ ile başlar. sever(kasim, Sey):-sever(ferit, Sey) şeklinde ifade edilebilecek yukarıdaki cümlede, **Sey** değişkendir. kasim ve ferit kelimeleri sabit semboller oldukları için küçük harfle başlarlar. Bu sabitleri de ekrana büyük harfle başlayacak şekilde yazmak mümkündür. Bunun için sadece (“Kasim”, Sey) veya (“Ferit”, Sey) şeklinde yazmak yeterlidir.

**2.6. Bölüm Özeti**

Bir Prolog programı iki tür ifadelerden oluşur: Gerçekler ve Kurallar.

Gerçekler, programcının doğruluğundan emin olduğu bilgiyi ilişkiler veya özellikler olarak anlattığı satırlardır.

Kurallar, bağımlı ilişkilerdir. Prolog bu kuralları kullanarak bir bilgiden hareketle bir konuda karar verir. Bir kural, verilen şartlar yerine geliyorsa başarılı olur, yani doğru olur.

Prolog’da bütün kuralların iki kısmı vardır: Baş ve Gövde kısmı. Bunlar birbirinden **:-** sembolleri ile ayrılırlar.

Baş kısmı verilen gerçekler doğrulanıyorsa doğrudur. Bu kısım aynı zamanda sonuç veya bağımlı ilişki olarak da bilinir.

Gövde kısmı ise doğru olması gereken şartları taşır. Böylece Prolog, programın baş kısmının doğru olduğunu ispatlayabilir.

Gerçekler ve kurallar birbirinin aynısıdır. Gerçeklerin kurallardan tek farkı, açıklayıcı bilgi taşıyan gövdelerinin olmamasıdır.

Prolog’a bir dizi gerçek veya kural tanıttıktan sonra, bu gerçekler veya kurallar hakkında soru sormak mümkündür. Buna **Prolog Sistemini Sorgulama** denir. Prolog, sorgulama esnasında, verilen gerçekler listesinin başından sonuna kadar tarama yapar ve sorguya uyan cevapları bulmaya çalışır.

Prolog’daki Karar Motoru bir kuralın baş ve gövde kısmını incelerken, bilinen gerçek ve kurallara başvurur. Şartların yerine gelip gelmediğini kontrol eder. Bir kuraldaki bütün şartlar doğrulandıktan sonra, bağımlı olan kısım, yani kuralın baş kısmının doğru olduğuna karar verir. Bütün şartlar, bilinen gerçeklere göre karşılanamazsa, sorguya olumlu cevap verilemez.

**Örnekler:**

Prolog gerçeklerinin konuşma diline çevrilmesi, aşağıda verilmiştir.

yapmaktan\_hoslanir(oya, resim) = Oya, resim yapmaktan hoşlanır.

cocuk(arif).= Arif, bir çocuktur.

bulunur(“Çankaya Köşkü”, “Ankara”). = Çankaya Köşkü Ankara’dadır.

adres(abuzer, zonturlu, “ Fatih Cad. 6. Sokak.”, “Dışkapı”, “ANKARA”, 06412).= Abuzer Zonturlu’nun adresi Fatih Cad. 6. Sokak Dışkapı, ANKARA, 06412’dir.

Şimdi tam tersini yapalım, konuşma dilinden Prolog diline çevrilme ise, aşağıdaki gibi yapılır.

Vedat iyi kebap yapar = yapar(vedat, iyi\_kebap).

Keban Barajı Elazığ’dadır = bulunur(“Keban Barajı”, “Elazığ”).

Kasım Kaya’nın telefon numarası 314 41 17’dir. telefon\_no(“Kasım KAYA”, “314 41 17”).

Hüseyin Meryem’in babasıdır. = baba(huseyin, meryem).

**2.7. Konuşma Dilindeki Cümlelerin Prolog Programlarına Aktarılması**

Bu bölümün ilk kısmında gerçekler, kurallar, ilişkiler, genel cümleler ve sorgulamalar konusunu incelenmiştir. Aynı kelimeler üzerinde çalışmakla beraber, Prolog’la daha fazla ilgili kelimeler üzerinde, yani cümlecikler, yüklemler, değişkenler ve hedefler üzerinde durulacaktır.

**2.8. Cümleler (Gerçekler ve Kurallar)**

Prolog dilini oluşturan iki türlü ifade vardır. Bu ifadeler gerçekler veya kurallardan ibarettir. Prolog dilinin kalbini oluşturan bu ifadelere **clause** denilmektedir.

Bir gerçek, bir nesnenin veya nesneler arasındaki ilişkinin bir özelliğinin sadece tek bir yönünü temsil eder. Bir gerçeğin Prolog tarafından tamamen doğru kabul edildiğini, bir sorgulamaya cevap ararken bu gerçeklerden yola çıkıldığını ve bu gerçeklerin doğruluğunun kontrol edilmediği unutulmamalıdır.

Günlük hayatımızda da doğruluğu bilinen gerçeklerden yola çıkarak bir şeyin doğru olup olmadığı araştırlır. İşte, mevcut gerçeklerden hareket ederek neyin doğru olabileceğini gösteren yapıya Prolog’da Kural denir. Şimdi Prolog’daki Kural yapısına bir örnekle yakından bakalım. Örnek:

Aşağıdaki cümlede, menü’de olan bir yemeğin Mehmet’e uygun olup olmadığı sorgulanmaktadır.

Mehmet ülser olduğu için sadece doktorunun izin verdiği yemekleri yer.

Menü ve yukarıdaki kurala bakarak, Mehmet’in hangi yemeği sipariş edebileceğine karar verilebilir. Bunu yapabilmek için, menüdeki yemeğin belirli şartları taşıyıp taşımadığına bakılmaladır.

Menudeki\_yemek bir sebze mi?

Menudeki\_yemek doktorun tavsiye ettiği listede var mı?

Sonuç: Eğer a ve b şıklarının ikisinin de cevabı ‘Evet’ ise, bu durumda Mehmet menüdeki bu yemeği yiyebilir.

Prolog’da bu tür ilişkilerin bir kuralla ifade edilmesi zorunludur, çünkü verilecek karar tamamen gerçeklere bağlıdır. Yukarıdaki ifadeler; Prolog gerçekleri olarak şöyle yazılabilir:

mehmet\_yiyebilir(Menudeki\_yemek):-

sebze(Menudeki\_yemek), doktor\_tavsiyeli(Menudeki\_yemek).

sebze(Menudeki\_yemek) ifadesinden sonra ‘,’ konulmuştur. Çünkü virgül, iki amaç arasındaki bağlantıyı gösterir ve **‘and’** anlamındadır. mehmet\_yiyebilir(Menudeki\_yemek) ilişkisinin doğrulanabilmesi için, sebze(Menudeki\_yemek), doktor\_tavsiyeli(Menudeki\_yemek) ilişkilerinin her ikisinin de doğru olması gerekir.

**Örnek:**

Ebeveyn ilişkisini anlatan bir Prolog gerçeği aşağıdaki gibi yazılır.

ebeveyn(omer, nejla) = Omer, Nejla’nın ebeveynidir.

Programın veritabanında babalık durumunu gösteren gerçeklerin zaten var olduğunu, yani baba(omer, nejla) gerçeğinin mevcut olduğu ve aynı zamanda annelik ilişkisini de gösteren anne(leyla, nejla) gerçeğinin de var olduğu kabul edilsin. Babalık veya annelik bağı hakkında yeterince bilgi olduğundan, ayrıca baba ve anne bilgilerini anlatmak vakit kaybına neden olur. Bunu yerine genel bir kural yazmak daha mantıklıdır. Yani,

ebeveyn(Sahis1, Sahis2):-baba(Sahis1, Sahis2).

ebeveyn(Sahis1, Sahis2):-baba(Sahis1, Sahis2).

**Örnek:**

Bir müşteri arabayı severse ve araba satılık ise bu arabayı satın alabilir.

Tabii dildeki bu ilişki, aşağıdaki kuralla Prolog’a aktarılabilir:

satin\_alabilir(Musteri, Model):-

sahis(Musteri), araba(Model), hoslanir(Musteri, Model), satilik(Model).

Aynı kural, konuşma dilinde aşağıdaki şekilde ifade edilir.

Müşteri modeli satın alabilir :-

Müşteri bir şahıs ve

Model bir araba ve

Müşteri modelden hoşlanırsa ve

Model satılık ise.

Bu kuralın baş kısmı, gövde kısmındaki her dört şartın da doğrulanması halinde doğru olacaktır. Yukarıda yazılan gerçekler, aşağıdaki şekilde program haline getirilebilir.

PREDICATES

nondeterm satin\_alabilir(symbol, symbol)

nondeterm sahis(symbol)

nondeterm araba(symbol)

hoslanir(symbol, symbol)

satilik(symbol)

CLAUSES

satin\_alabilir(X,Y):-

sahis(X),

araba(Y),

hoslanir(X,Y),

satilik(Y).

sahis(ahmet).

sahis(paki).

sahis(cengiz).

sahis(levent).

araba(buick).

araba(bmw).

araba(passat).

araba(toyota).

hoslanir(paki,buick).

hoslanir(levent, toyota).

hoslanir(cengiz, passat).

hoslanir(ahmet, tenis).

satilik(pizza).

satilik(toyota).

satilik(buick).

satilik(passat).

Yukarıdaki programı yazdıktan sonra Levent ve Cengiz’in ne satın alabileceğini, kimin buick marka arabayı alabileceğini bulmak için aşağıdaki hedef cümleleri kullanılabilir:

satin\_alabilir(Kim, Ne).

satin\_alabilir(levent, Ne).

satin\_alabilir(cengiz, Ne).

satin\_alabilir(Kim, buick).

**2.9. Olgular Arasındaki İlişkiler: Yüklemler (Predicates)**

Bir ilişkinin sembolik ismine **yüklem** denir ve yükleme bağlı olan nesnelere argüman denir. Mesela sever(yasin, esra) gerçeğindeki sever ilişkisi yüklem, yasin ve esra ise bu yüklemin agrümanları olan nesnelerdir.

Argümanlı ve agrümansız yüklem örnekleri:

sahis(soyad, ad, cinsiyet). sahis yüklem; soyad, ad, cinsiyet ise bu yüklemin argümanlarıdır.

basla = argümanı olmayan yüklem

dogum\_gunu(isim, soyisim, tarih). Dogum\_gunu yüklem, isim, soyisim ve tarih nesneleri ise argümanlarıdır. Sınırlı olmakla beraber, bir yüklem argümansız olarak da kullanılabilir.

**2.10. Değişkenler (Genel Cümleler)**

Basit bir sorgulamada, sever(Kim, tenis) kuralını kullanarak kimin tenis oynamaktan hoşlandığı öğrenilebilir. Bu sorguda Kim, değişken olarak kullanılmıştır. Visual Prolog’da değişken isimlerinin daima büyük harfle veya ‘\_’ ile başladığı, daha önceden söylenmişti. İlk karakteri büyük bir harf veya ‘\_’ olmak şartıyla, değişkenler istenilen kadar rakam, büyük veya küçük harf alabilirler. Konu ile ilgili birkaç örnek, aşağıda verilmiştir.

**Geçerli Değişkenler Geçersiz Değişkenler**

Prolog\_ile\_yazdigim\_ilk\_program 1.deneme

\_14\_10\_1978\_tarihinde\_doganlar 14.program

\_1\_nolu\_ogrenci “prolog”

Değişken ismi seçimine dikkat etmek, programın başkaları tarafından rahat bir şekilde okunması ve anlaşılması bakımından önemlidir. sever(Kim, tenis) kuralı sever(X, tenis) kuralına tercih edilir. Çünkü Sahis X’e göre daha fazla anlamlıdır.

**2.10.1. Prolog’da Değişkenlerin Değer Alması**

Diğer programlama dillerinde, değişkenlerin değer almalarına imkan tanıyan atama ifadeleri Prolog’da yoktur. Prolog’u diğer programlama dillerinden ayıran en önemli özelliklerden biri de budur. Prologdaki değişkenler almaları gereken değerleri atamayla değil, gerçekler veya kurallardaki sabitlere eşleştirilirken alırlar.

Bir değişken, değer almadığı müddetçe serbest değişken olarak kalır. Fakat herhangi değer aldığı andan itibaren sınırlı hale gelir. Bu sınırlılık bir sorguya cevap almak için gerekli olan süre kadar sınırlı kalır. Bu işlem bittikten sonra değişken yeniden sınırlı hale gelir, program başa döner ve alternatif çözümler arar. Dolayısıyla bir değişkene bir değer vererek bilgi depolanamaz. Değişkenler bilgi depolamak için değil, kalıp-eşleştirme ve işlemenin bir parçası olarak kullanılır.

PREDICATES

nondeterm sever(symbol, symbol)

CLAUSES

sever(oktay, okuma).

sever(yavuz, bilgisayar).

sever(orhan, tavla).

sever(vedat, uyuma).

sever(ismail, yuzme).

sever(ismail, okuma).

Hem okuma hem de yüzmeden kimin hoşlandığı sorusuna cevap aramak için şu sorguyu kullanılır.

GOAL sever(Sahis, okuma), sever(Sahis, yuzme).

Prolog bu kuralı çözmek ve önce sever(Sahis, okuma) kısmının doğru olup olmadığını bulmak için bütün gerçekleri baştan sonra kadar inceler. Çözüm bulunmadan önce Sahis değişkeninin değeri yoktur, yani serbesttir. Öte yandan okuma kısmı bilinmektedir. İlk sever(oktay, okuma) gerçeğindeki okuma kısmı sorguya uyduğu için Sahis ‘oktay’ değerini alır. Prolog aynı zamanda aşağıya doğru nereye kadar tarama yaptığını göstermek için kuralın başıyla eşleşen ilk noktaya bir ‘pointer’ koymaktadır.

Sorgunun ilk kısmı doğrulandıktan sonra ikinci kısmının da doğrulanması gerekir. Yani yüzmeden hoşlanan kişinin de bulunması gerekir. Sahis değişkeni ‘oktay’ değeri aldığı için artık sever(oktay, yuzme) gerçeğinin doğru olup olmadığı araştırılır. Gerçekler incelenirse, ‘oktay’ isimli şahsın yüzmeden hoşlanmadığı görülür. Bu durumda Prolog Sahis değişkenine atadığı ‘oktay’ değerini etkisiz hale getirir ve Sahis yeniden serbest hale gelir. Kuralın ilk kısmını doğrulayan gerçeği bulmak için Prolog bu kez kuralların başından değil, gerçekler listesine daha önce yerleştirmiş olduğu pointer’den aşağıya kadar doğru taramaya başlar. İlk gerçek gereken şartları sağlayamadığı için artık dikkate alınmaz. Bu işleme **Geriye İz Sürme** denir.

Yapılan taramada okumadan hoşlanan kişinin ismail olduğu görülünce Sahis değişkeni bu kez ‘ismail’ değerini alır. Kuralın ikinci kısmının doğrulanması için tarama yapılırsa, yüzme için gereken şartın yine ‘ismail’ ile sağlandığı görülür. Dolayısıyla Prolog’un vereceği cevap şu olur:

Sahis=ismail

1 Solution

**2.11. Anonim Değişkenler**

Anonim değişkenler, programların gereksiz bilgi ve satırlarla karmaşık hale gelmelerini engeller. Böylece bir sorgulamadan beklenilen bilgileri alabilir ve ihtiyaç olmayan değerler iptal edilmiş olur. Prolog’da anonim değişkenler ‘\_’ ile gösterilir.

Aşağıdaki örnekte anonim değişkenin kullanımı verilmiştir:

PREDICATES

erkek(symbol)

bayan(symbol)

nondeterm ebeveyn(symbol, symbol)

CLAUSES

erkek(selahattin).

erkek(cihat).

bayan(sacide).

bayan(sezen).

ebeveyn(selehattin, cihat).

ebeveyn(sacide, cihat).

ebeveyn(selehattin, sezen).

GOAL ebeveyn(Ebeveyn,\_).

Diğer değişkenlerin yerine kullanılabilen anonim değişkenlerin, normal değişkenlerden tek farkları şudur: anonim değişkenler hiçbir zaman bir değere eşitlenemezler.

Yukarıdaki örnek yazdıktan sonra GOAL ebeveyn(Ebeveyn,\_) sorgusu çalıştırılarak, ebeveyn olan kişilerin isimleri öğrenilebilir. Çocukların isimleri istenmediği için isimlerinin yerine anonim değişken kullanılmıştır.

Programın sonucunda şu sonuç görüntülenir:

Ebeveyn=selehattin /\*Cihat’ın ebeveyni \*/

Ebeveyn=sacide /\* Cihat’ın ebeveyni\*/

Ebeveyn=selehattin /\* Sezen’in ebeveyni\*/

2 solutions

Tanımlanan değişken anonim olduğu için, alınacak cevabın ikinci argümanla bağlantısı olmayacaktır. Anonim değişkenler, gerçeklerin tanımlanmasında da kullanılabilir.

vardir(\_,televizyon).

yemek\_yer(\_).

İfadeleri konuşma dilinde “Herkesin televizyonu var” ve “Herkes yemek yer” olarak çevrilebilir.

**2.12. Hedefler (Sorgular)**

Şimdiye kadar Prolog’a soru sormak anlamında kullanılan **sorgulama **kelimesinin yerine bu andan itibaren **Hedef(Goal)** kelimesi kullanılacaktır. Sorgulamaları hedef olarak tanımlamak daha anlamlıdır, çünkü Prolog’a bir sorgu yöneltmekle, ona yerine getirilmesi gereken bir hedef verilmiş olur.

Hedefler sever(ismail, yuzme) gibi basit olabileceği gibi sever(Sahis, okuma), sever(Sahis, yuzme) gibi daha karmaşık da olabilir. Birden fazla parçadan oluşan hedefe **Birleşik Hedef**, her bir parçaya da **alt hedef** denir.

**2.12.1. Birleşik Hedefler: Bağlaçlar ve Ayraçlar**

Birleşik bir hedefin çözümünü bulmak için her iki alt hedefin doğru olması gerekir. Bu durumda, iki alt hedef arasında (ve) anlamına gelen ‘**,**’ kullanılır. Fakat istenilen durumlarda alt hedeflerden sadece birinin doğru olması şartı da aranabilir. Bu durumda alt hedefler arasında (veya) anlamına gelen ‘**;**’ kullanılması gerekir. Bu duruma **Ayırma işlemi** denilmektedir.

Şimdi bu durumu gösteren bir örnek inceleyelim:

PREDICATES

nondeterm araba(symbol,long,integer,symbol,long)

nondeterm kamyon(symbol,long,integer,symbol,long)

nondeterm arac(symbol,long,integer,symbol,long)

CLAUSES

araba(chrysler,130000,3,kirmizi,12000).

araba(ford,90000,4,gri,25000).

araba(datsun,8000,1,kirmizi,30000).

kamyon(ford,80000,6,mavi,8000).

kamyon(datsun,50000,5,sari,20000).

kamyon(toyota,25000,2,siyah,25000).

arac(Marka,Kilometresi,Yas,Renk,Fiyat):-

araba(Marka,Kilometresi,Yas,Renk,Fiyat);

kamyon(Marka,Kilometresi,Yas,Renk,Fiyat).

GOAL araba(Marka, Kilometresi, Kullanim\_Suresi, Renk, 25000).

Bu örnekteki hedef, cümleciklerde tarif edilen 25000 dolarlık arabayı bulur. Benzer şekilde; fiyatı 25.000 dolardan daha az olan bir araba var mı? şeklindeki bir soruya cevap bulmak da mümkündür. Bunun için araba(Marka, Kilometresi, Kullanim\_Suresi, Renk, Fiyat), Fiyat< 25000 şeklindeki bir sorguyla bu sorunun cevabını bulmak mümkündür. Bu kuralı sorgulandığında, alınacak cevap chrysler olacaktır.

Şimdi ‘fiyatı 25.000 dolardan az olan bir araba **veya** fiyatı 20.000 dolardan daha az olan bir kamyon var mıdır?’ şeklindeki bir soruya uygun bir hedef yazalım:

araba(Marka, Kilometresi, Kullanim\_Suresi, Renk, Fiyat), Fiyat< 25000; kamyon (Marka, Kilometresi, Kullanim\_Suresi, Renk, Fiyat), Fiyat< 20000.

Prolog ilk önce fiyatı 25.000 dolardan daha az olan bir araba olup olmadığını araştırır. Sonuç doğru olsun veya olmasın, ikinci alt hedef de araştırılır. Her ikisinden birinin doğru olması durumunda alınacak cevap olumlu olacaktır. Hedefin doğrulanması için birden fazla alt hedefin aynı anda doğru olması gerekmez. Bu tür hedeflere **ayrıştırma** denilmektedir ve bunun için alt hedefler arasında ‘;’ ayracı kullanılmaktadır.

**2.13. Açıklama Satırları**

Program yazarken program satırları arasına açıklamalar yazmak, başkalarının da programı okuyup anlamasına imkan tanır. Program içerisine yazılan bu yorum satırları derleyici tarafından dikkate alınmaz. Prolog’da yorum satırları bir kaç satırdan oluşacaksa ‘/\*’ ile başlamalı ve ‘\*/’ ile bitmelidir. Eğer tek bir satır yorum yazılacaksa ‘%’ işareti kullanılabilir.

/\* Program yazarken kullanılan değişkenler, yüklem ve kurallar\*/

/\*hakkında bilgi vermek için bu tür yorum satırları yazılabilir\*/

%Tek satırlık yoruma bir örnek.

/\* İç içe /\* yorum \*/ satırı yazmak da mümkündür\*/

**2.14. Eşleştirme**

Prolog’da eşleştirme yapılırken eşlenik yapılar birbiriyle eşleşebilir. ebeveyn(selehattin, X), ebeveyn(sacide, cihat) kuralındaki X değişkeni ‘cihat’ değerini alır ve serbest olan bu değişken artık bağlı hale gelir. Bağlı hale gelen başka bir değişkene atanırsa, diğer değişken de aynı değeri alır.

**2.15. Bölüm özeti**

Prolog’da bir program gerçekler ve kurallardan oluşan cümleciklerden oluşur.

Gerçekler, doğru oldukları kabul edilen ilişkiler ve özelliklerdir.

Kurallar bağımlı ilişkiler olup, gerçekler ve ilişkileri kullanarak bilgi elde etmeye yararlar.

2. Gerçeklerin genel yazılış biçimi şöyledir:

ozellik(nesne1, nesne2,..... nesneN)

veya

ilişki(nesne1, nesne2,..... nesneN)

Burada özellik nesnelerin herhangi bir özelliği, ilişki ise nesneler arasındaki herhangi bir ilişkidir. Özellik ve ilişki kelimelerinin her ikisi de Prolog’da aynı anlamda kullanılır.

Bir programda verilen bir ilişki bir veya daha fazla nesne arasındaki ilişkiden ibarettir. sevmek(ahmet, futbol) gerçeğindeki ‘sevmek’ bir ilişkiyi, ahmet ve futbol ise bu ilişkinin nesnelerini temsil eder. solak(hasan) gerçeğinde ‘solak’ bir özelik, hasan ise bir nesnedir.

Kuralların genel yazılma şekli:

Baş:-Gövde

olup, daha açık hali aşağıdaki gibidir.

ilişki(nesne, nesne, ....., nesne) :-

ilişki(nesne, nesne, ..., nesne),

.

.

ilişki(nesne, nesne, ...., nesne).

İlişki ve nesne isimlerinin yazılması bazı kurallara bağlıdır. Nesne ve ilişki isimleri daima küçük harfle başlar. Bunu takiben istenilen sayıda büyük-küçük harf, rakam, ‘\_’ kullanılabilir.

Değişken isimleri daima büyük bir harf veya ‘\_’ ile başlar. Bunu takiben istenildiği kadar küçük\_büyük harf, rakam vs. kullanılabilir. Değişkenler bir değer almadan önce serbest, değer aldıktan sonra ise bağlı hale gelirler. Bir değişkene değer atayıp bilgi depolamak mümkün değildir. Çünkü bir değişken sadece bir cümlecikte bağımlıdır.

Bir sorgudan sadece belirli bir bilgi alınmak isteniyorsa, anonim değişken (\_) kullanılabilir. Anonim değişkene hiçbir zaman değer atanması yapılamaz.

Prolog’a programda verilen gerçeklere göre bir soru sormak **Prolog Sistemini Sorgulama** olarak adlandırılır ve bu sorguya **Hedef** denir.

Bileşik bir hedef iki veya daha fazla hedeften oluşur. Bu parçaların her birine alt hedef adı verilir. Bileşik hedefler Bağlaç veya Ayraç şeklinde olabilir.

10. Eşleştirme birbirine denk yapılar arasında gerçekleştirilir. Serbest bir değişken bir sabite veya önceden değer alıp bağımlı hale gelmiş başka bir değişkene atanabilir. Serbest olan iki değişken birbirine atanırsa, birinin alacağı değer otomatik olarak diğerine atanmış olur.

**3. VISUAL PROLOG PROGRAMLARININ TEMEL BÖLÜMLERİ**

Bir VIP Programı genelde şu dört bölümden oluşur: Clauses (Gerçekler ve Kurallar), Predicates (Yüklemler), Domains (Değişken Tipleri) ve Goals(Hedefler).

**3.1. Clauses(Olgular veya Kurallar)**

Bu bölüm bir programın kalbi durumundadır. Çünkü programda tanımlı hedefler doğrulanmaya çalışılırken, doğruluğu daha önceden bilinen gerçeklerden yola çıkılır. Gerçek ve gerçekler arasındaki ilişkileri tanımlayan kuralların tanımlandığı yer bu bölümdür. Bir yüklem için tanımlanması gereken bütün clauselar kümesine Procedure denir.

**3.2. Predicates (Yüklemler)**

Yüklemlerin ve yüklemlerdeki argümanların tiplerinin tanımlandığı yer bu bölümdür. Visual Prolog’da mevcut olan hazır yüklemlerin tanımlanması gerekmez.

**3.3. Domains (Değişken Tipleri)**

Burada, Visual Prolog’da olmayan tiplerin tanımlanması yapılır.

**3.4. Goal (Hedef)**

Programdaki sorgular buraya yazılır.

**3.5. Yüklem Tanımı**

Bir yüklemin genel yazılış biçimi şöyledir:

yuklem\_adi(argüman\_tip1, argüman\_tip2, argüman\_tip3,...., argüman\_tipN)

Yüklemlerin bitiş parantezinin clauses bölümündeki gibi ‘.’ ile sonlanmadığına dikkat edilmelidir. Yüklem isimleri en fazla 250 karakterten oluşabilir ve herhangi bir harfle başlayabilir. Yüklemler için isim seçilirken küçük veya büyük harfle başlamak önemli değildir. Fakat küçük bir harfle başlayan bir isim seçilmesi önerilir. Çünkü Prolog derleyicilerin çoğu ancak küçük harfle başlayan yüklem isimlerini kabul etmektedir. Kullanılabilecek karakterler şunlardır:

Büyük harfler: A, B, .........., Z

Küçük harfler: a, b, ............, z.

Rakamlar: 0, 1, .................., 9

Alt tire: \_.

Geçerli Yüklem İsimleri Geçersiz Yüklem İsimleri

Olgu \[olgu\]

Oynar \*gider\*

sahip\_olunan\_servet Sahiptir/araba

tahakkuk\_fisi bu-ayin-bordrosu

10\_kisilik\_sinif <10-kisiden\_biri

**Örnekler:**

domains

isim=symbol

numara=integer

predicates

ilk\_yuklem(isim, numara)

domains

sahis, eylem=symbol

araba, marka, renk=symbol

kilometresi, kullanim\_yili, fiyat=integer

predicates

sever(sahis, eylem)

ebeveyn(sahis, sahis)

satin\_alabilir(sahis, araba)

araba(marka, kilometresi, kullanim\_suresi, renk, fiyat)

yesil(symbol)

derece(symbol, integer)

Yukarıdaki program parçasında yüklem ve argümanların anlamları aşağıda verilmiştir.

sever yüklemi iki argüman alır: sahis ve eylem. Bu argümanların her ikisi de değer olarak symbol, yani alfabetik karakterler alabilir.

ebeveyn yükleminin iki argümanı da sahis olup, domainde tanımladığı şekliyle symbol tipindedir.

satin\_alabilir yüklemi tipi symbol olan sahis ve araba argümanlarını almıştır.

araba yüklemi 5 adet argüman almıştır. İlk ikisinin tipi symbol, son üçünün ise integer’dır (tamsayı).

yesil yüklemi, tipi symbol olan tek bir argüman almıştır. Symbol tipi zaten Visal Prolog’un standart tipleri arasında yer aldığından, ayrıca tanımlamaya gerek yoktur.

derece yükleminin argümanları da standart domain’de yer almaktadır.

**3.6. Domains (Tip tanımları) Bölümü**

Domain kısmında argümanların tipleri tanımlanır. Bir argüman alfabetik, nümerik veya her ikisinden oluşan karakterleri değer olarak alabilir. Domain kısmı, birbirinin aynısı gibi görünebilecek verilere farklı isimler vermemize imkan tanır. VIP programlarında ilişki veya gerçeklerde tanımlanmış olan nesneler (yüklemdeki argümanlar) domainlere aittir. Bu tipler standart olarak tanımlı olabileceği gibi, kullanıcı tarafından sonradan da tanımlanabilir.

Domain kısmı son derece faydalı iki görev icra eder. Birincisi, yüklemlerde tanımlanan argümanların tipleri VIP’de standart olarak tanımlamış olan symbol, tamsayı vs. domainleri olsalar bile, argümanlara farklı anlamlı isimler vermemize imkan tanır. İkincisi, standart domainler tarafından tanımlanmamış veri yapılarını tanımlanmasına imkan sağlar.

Ayrıca, yüklemdeki argümanların net olarak anlatılabilmesi için farklı domainler olarak tanımlanması da faydalıdır.

**Örnekler:**

Aşağıdaki tabii dil cümlesinin VIP’de karşılığını yazıp, özel domain tanımı aşağıdaki şekilde yapılır.

Hasan, 28 yaşında bir erkektir.

Eğer özel olarak domain tanımlanmazsa, yani VIP’deki standart tipler kullanılırsa yukarıdaki cümle şöyle yazılabilir:

sahis(symbol, symbol, integer)

Bu yüklem ve argümanlar doğru biçimde tanımlandığı için çalışır. Fakat sahis yüklemi içinde tanımlanan üç argümanın neye işaret ettiğini hatırlamak zor olabilir.

Bunun yerine:

domains

isim, cinsiyet = symbol

yas = integer

predicates

sahis(isim, cinsiyet, yas)

şeklinde üç ayrı domain tanımlanırsa sahis argümanındaki isim, cinsiyet ve yas argümanlarının anlamı her zaman için barizdir. Bu tanımlamanın bir faydası da argüman tipleri arasında olabilecek tip eşleştirme hatalarını önlemektir.

Özel domainler, argümanların anlamını çok daha iyi ifade ettikleri halde, bütün argümanlar için özel domain kullanmak gerekmez. Bir argüman için belli bir tip tanımlanması yapıldıktan sonra, bu argüman, tipi aynı olan bir başka argümanla hiçbir şekilde karıştırılmaz. Örneğin isim ve cinsiyet argümanlarının her ikisinin de tipi symbol olmasına rağmen birbiriyle karıştırılmazlar. Fakat kullanıcının tanımladığı argümanların hepsi önceden tanımlanmış argümanlarla karıştırılabilir.

Aşağıdaki örnek, çalıştırıldığı zaman bir tip hatası verir.

DOMAINS

carpma, toplam = integer

PREDICATES

toplama\_yap(toplam, toplam, toplam)

carpma\_yap(carpma, carpma, carpma)

CLAUSES

toplama\_yap(X, Y, Toplam):-

Toplam=X+Y.

carpma\_yap(X, Y, Carpma):-

Carpma=X\*Y.

GOAL toplama\_yap(32, 54, Toplam).

Buradaki GOAL toplama\_yap(32, 54, Toplam) doğru çalışır ve

Toplam=86

1 Solution

cevabı alınır. Carpma\_yap fonksiyonu için 35 ve 25 değerlerleri kullanılırsa,

Carpma=875

1 Solution

sonucu alnır.

31 ve 17 sayılarının çarpımını bulup, elde edilen sayıyı kendisiyle toplayıp Cevap argümanının değeri aşağıdaki şekilde bulunur.

carpma\_yap(31, 17, Toplam), toplama\_yap(Toplam, Toplam, Cevap) şeklinde bir hedef yazılabilir. Bu hedefe göre, bulunacak sonucun

Toplam=527 (31\*17), Cevap=1054 (527+527)

olması gerekirken, VIP derleyici bir hata mesajı verir. Çünkü carpma\_yap fonksiyonundaki Toplam argümanı 527 değerini aldıktan sonra bu değeri ikinci yüklem olan toplama\_yap’taki ilk iki argümana taşımaya çalışır. Her iki argüman da tamsayı tipinde olmasına rağmen farklı isimlerde olduklarından, birbirleriyle eşleştirilemezler ve neticede hata mesajı görüntülenir. Bu yüzden bir cümledeki fonksiyonda tanımlanan değişken birden fazla fonksiyonda kullanılacaksa, her fonksiyonda aynı şekilde tanımlanmalıdır.

**Örnek:**

DOMAINS

marka, renk = symbol

yas=byte

fiyat, yol=ulong

PREDICATES

nondeterm araba(marka, yol, yas, renk, fiyat)

CLAUSES

araba(chrysler,130000,3,kirmizi,12000).

araba(ford,90000,4,gri,25000).

araba(datsun,8000,1,siyah,30000).

GOAL araba(renault, 13, 40000, kirmizi,12000).

GOAL araba(ford, 90000, gri, 4, 25000).

GOAL araba(1, kirmizi, 30000, 80000, datsun).

Burada araba yükleminin 5 argümanı mevcuttur. Yas argümanı byte tipinde olduğu için alabileceği değer 8 bitlik ve 0-255 arasında değişen pozitif bir sayıdır. Aynı şekilde yol ve fiyat tipleri ulong (uzun tamsayı) olup 32-bit pozitif tamsayı değerleri alır. Son olarak marka ve renk tipleri symbol tipindedir. Yukarıdaki sorguları tek tek deneyince her birinin ayrı bir tip hatasına neden olduğu görülecektir. GOAL araba(renault, 13, 40000, kirmizi, 12000) sorgusunda byte tipinde olması gereken yas argümanı 40000 değerini almıştır. Bunun 0-255 arasında olması gerekir. İkinci sorguda yas ve renk argümanlarının değerleri yer değiştirmiştir. Bu nedenle yine hataya neden olur.

**3.7. Goal Bölümü**

Goal bölümünün bir kuralın yapısından sadece iki farkı vardır.

Goal kelimesinden sonra ‘if’ anlamındaki ‘:-‘ operatörü kullanılamaz.

Program çalışırken VIP ilk önce GOAL satırını çalıştırır.

**3.8. Deklarasyon ve Kurallara Ayrıntılı Bakış**

Bir yüklemdeki argümanların tiplerini tanımlarken, VIP’de hazır bulunan standart tipler kullanılabilir. Bu tiplerin domains kısmında, ayrıca tanımlanması gerekmez. Aşağıdaki tabloda hazır olarak bulunan tipler verilmiştir (Tablo 1).

Tablo 3.1: Visual Prolog’da Tipler ve Alabilecekleri değerler.

| **Tip** | **Kullanıldığı Yer** |  | **Değer Aralığı** |
| --- | --- | --- | --- |
| **short ** | Bütün Platformlar | 16 Bit | -32768....+32767 |
| **Ushort** | Bütün Platformlar | 16 Bit | 0...65535 |
| **Long** | Bütün platformlar | 32 bit | -2147483648.........+2147483647 |
| **Ulong****** | Bütün platformlar | 32 bit | 0...4294967295 |
| **İnteger** (Bilgisayar ve Mimariye bağlı olarak - veya + değer alabilir) | 16 Bit Platformlar 32 Bit platformlar | 16 Bit 32 Bit | -32768....+32767 -2147483648........+2147483647 |
| **Unsigned **(Bilgisayar ve mimariye bağlı olarak -/+ değer alabilir) | 16 Bit Platformlar 32 Bit platformlar | 16 Bit 32 Bit | 0...65535 0...4294967295 |
| **byte ** | Bütün platformlar | 8 bit | 0-255 |
| **Word** | Bütün platformlar | 16 bit | 0...65535 |
| **Dword** | Bütün platformlar | 32 bit | 0...4294967295 |

Her değişken tipi verilen aralıkta bulunan bir değeri alabilir. Integer ve unsigned tipleri, değişkenlerin tanımlandığı bilgisayar veya sistemlere göre değişen aralıktaki değerleri alırlar.

Domain tanımı yapılırken signed veya unsigned kelimeleri byte, word ve dword domainleri ile birlikte kullanılabilirler.

Domains

i8 = signed byte

tanımı normalde unsigned olan ve bu yüzden 0-255 aralığından değer alan byte yerine -128...+127 değerleri arasında değer alan bir tip haline gelir.

**3.8.1. Char**

İşaretsiz bir byte olarak kullanılır. Örnek: ‘A’, ‘b’...

**3.8.2. Real **

+/- DDDD.DDDD şeklinde olan 8 bitlik bir değişken. (1\*10-307-1\*10+308)

**3.8.3. String**

255 karakter uzunluğunda olabilen bu tipin iki formatı vardır.

İlki küçük harf olmak üzere harf, sayı veya altçizgiden oluşur.

Çift tırnak arasına alınmış karakterlerden oluşur. Örnek

Örnekler: Adı\_soyadı, “Müşterinin Adı”, “Fox Ltd.”

**3.8.4. Symbol**

Formatı string’ler ile aynıdır.

Symbol ve string değişkenler birbirinin aynısı olmakla beraber, VIP bunları farklı şekillerde depolar. Symbol tipleri bir tabloda saklanır. Adresleri ise nesneleri temsil edecek şekilde saklanır. Böylece eşleştirme işleminde hızlı kullanılırlar. Fakat karşılaştırmalarda String tipler karakter bazında eşleştirilir.

**3.9. Yüklemlerdeki Argümanların Yazılması**

Predicates bölümündeki bir argümanın tipini tanımlamaya, argüman tipi tanımlama denilmektedir.

Hasan, 28 yaşında olan bir erkektir = sahis(hasan, erkek, 28).

Sahis bu argümanlarla birlikte kullanan bir yüklem olarak tanımlamak için aşağıdaki satırın predicates bölümünde yazılması gerekir.

sahis(symbol, symbol, unsigned)

Görüldüğü gibi her üç argüman da standart tipte tanımlanmıştır. Yani, program içerisinde her ne zaman sahis yüklemi geçerse, bu yüklemi sadece 3 argümanla birlikte kullanılabilir. Bunların ilk ikisi symbol, üçüncüsü ise unsigned tipinde bir integer olmalıdır.

Alfabedeki bir harfin yerini belirleyen alfabedeki\_yer(Harf, Yer) şeklinde bir ilişkiyi incelendiğinde, Harf ve Yer argümanlarının her ikisi de değişken olarak tanımlandığı görülür. Böylece Harf=a ise Yer=1, Harf=b ise Yer=2 vs. şeklinde devam eder. Bu durum kısaca şöyle ifade edilebilir.

alfabedeki\_yer(Bir\_harf, N).

Bunun için yazılması gereken olgular:

alfabedeki\_yer(‘a’, 1).

alfabedeki\_yer(‘b’, 2).

alfabedeki\_yer(‘c’, 3).

...........

alfabedeki\_yer(‘z’, 29.)

şeklinde olmalıdır.

PREDICATES

alfabedeki\_yer(char, integer)

CLAUSES

alfabedeki\_yer(‘a’, 1).

alfabedeki\_yer(‘b’, 2).

alfabedeki\_yer(‘c’, 3).

GOAL alfabedeki\_yer(‘c’, Nerede).

Program çalıştırıldığında ‘c’ harfinin yerini veren Nerede değişkeni 3 değerini alır.

**Örnek:**

DOMAINS

adi\_soyadi, tel\_no = symbol

PREDICATES

nondeterm telefon\_numarasi(adi\_soyadi, tel\_no)

CLAUSES

telefon\_numarasi("Orhan AYDIN", "255 45 47").

telefon\_numarasi("Arif GÜREL", "3134578").

telefon\_numarasi("Husamettin BULUT", "3145869").

telefon\_numarasi("Kasim YENIGÜN", "3174152").

Bu program, aşağıdaki sorgularla veya yenileri ilave edilerek çalıştırılabilir.

GOAL telefon\_numarasi(Kimin\_Telefonu, "3145869").

GOAL telefon\_numarasi("Orhan AYDIN", Telefon\_Numarasi).

GOAL telefon\_numarasi(Telefon\_Sahibinin\_Adi, Telefon\_Numarasi).

Örnek: Ekrandan girilen bir karakterin harf olup olmadığını kontrol eden bir program yazınız. (Not: char tipi sadece bir tek karakteri tanımlar)

REDICATES

nondeterm aranan\_harf(char)

CLAUSES

aranan\_harf(Harf):-

‘a’<=Harf,

Harf<=’z’.

aranan\_harf(Harf):-

‘A’<=Harf,

Harf<=’Z’.

GOAL

aranan\_harf(‘x’).

aranan\_harf(‘2’).

aranan\_harf(“Merhaba”).

aranan\_harf(‘a’).

aranan\_harf(x).

Yukarıdaki program, verilen bir karakterin alfabenin bir harfi olup olmadığını test etmektedir. Yazılan sorguları kullanarak elde edilen sonuçları inceleyiniz. Bazı şıklarda neden hata verdiğini bulmaya çalışınız.

Predicate bölümünde aynı isimde birden fazla yüklem tanımlanabilir. Fakat bunların argümanlarının farklı sayıda olması gerekir. Predicates ve Clauses bölümlerinde aynı isimde olanların birlikte gruplanmaları gerekir. Bu yüklemler, tamamen farklıymış gibi işlem görürler.

**Örnek:**

DOMAINS

sahis=symbol

PREDICATES

baba(sahis) %Buradaki şahıs bir babadır.

baba(sahis, sahis) %Buradaki birinci kişi ikinci kişinin babasıdır.

CLAUSES

baba(Insan):-,

baba(Insan, \_).

baba(ahmet, mehmet).

baba(omer, yavuz).

**3.10. Kuralların Yazım Biçimi**

VIP’de kurallar, Baş ve Gövde olmak üzere iki kısımdan meydana gelir.

Genel Biçim:

Baş:- <alt hedef1>, <alt hedef2>,......, <alt hedefN>.

Alt hedefler biribirinden ‘,’ ile ayrılır ve sonuncusu nokta ile biter. Alt hedeflerin her biri ayrı bir yüklem çağırır. Alt hedefin doğru olup olmadığı kontrol edilir. Sonuç ne olursa olsun, bu işlem bütün alt hedeflere uygulanır. Alt hedeflerin tamamının olumlu netice vermesiyle beraber o kuralın doğruluğu ispatlanmış olur. Sadece bir alt hedef bile yanlış olursa, bütün kural yanlış olur.

**3.11. Prolog ve Diğer Dillerdeki ‘if’ Komutunun Karşılaştırılması **

VIP’de baş ve gövde kısmını ayıran ‘:-‘ sembolü if anlamına gelir. Örneğin Pascal’daki **if** komutu, öncelikle if komutundan sonra gelen ifadenin doğru olup olmadığını kontrol eder. Eğer ifade doğrulanırsa, komut **then** ifadesinden sonraya geçer geçer.

Yani if x>10 then writeln(“Bu işlem tamam”);

satırında öncelikle x değişkeninin 10’dan büyük olup olmadığı kontrol edilir. Eğer sonuç doğru ise ‘Bu işlem tamam’ satırı görüntülenir. Aksi takdirde program bir alt satırdan itibaren çalışmaya devam eder. Bu tip ifadeye if/then şartlı denir. VIP ise bunun tam tersi olan bir sistem uygular. Öncelikle gövdedeki alt hedeflerin doğru olup olmadığına bakılır. Tamamı olumlu sonuç verirse, kuralın gövde kısmının doğruluğu ispatlanmış olur. Bu ise VIP’da then/if şartının geçerli olduğunu gösterir.

**3.12. Otomatik Tip Dönüştürmeler**

VIP’de iki değişken karşılaştırıldığında her ikisinin de aynı tipte olması her zaman gerekmez. Değişkenler bazen başka tiplerdeki sabit değişkenlere de atanabilir. Çünkü VIP aşağıdaki tipler arasında otomatik olarak tip dönüştürmesini yapar.

string ve symbol

Bütün integral tipler ve reel değişkenler. Bir karakter sayısal bir değere dönüştürülürken, bu karakterin karşılığı, sayının ASCII tablosundaki karşılığı olur.

Örneğin string tipindeki bir agüman symbol tipi ile uyumludur. Benzer şekilde integer olarak tanımlı bir tip real, char, word etc. Tipleriyle uyumludur. Bu tür tip değişikliği şu kolaylıkları sağlar:

string tipiyle tanımlı bir yüklem symbol tipindeki bir argümanla çağrılabilir.

real tipiyle tanımlı bir yüklem integer tipindeki bir argümanla çağrılabilir.

char tipiyle tanımlı bir yüklem integer tipindeki bir argümanla çağrılabilir.

Alfabetik karakterler ASCII değerleri bilinmeden de rahatlıkla kullanılabilir.

Argümanlar, tanımlı olduklarının dışında bir tipe dönüşürken ne gibi kuralların etkili olduğu, sonuçta ortaya çıkan argümanının hangi tipte olacağı konusu ileride incelenecektir.

**3.13. Bir Programın Diğer Bölümleri**

Şimdiye kadar VIP’daki clauses, predicates, domains ve goals bölümleri incelenmiş ve bol miktarda örnek verilmiştir. Şimdi database, constants ve global bölümlerine kısa bir giriş yapılacaktır.

**3.13.1. Database Bölümü**

Bir VIP programının gerçekler ve kurallardan oluştuğu bilinmektedir. Program çalışırken bazen kullanılan gerçek ve kuralları değiştirmek, güncellemek, ilave yapmak veya çıkarmak gerekebilir. Böyle bir durumda gerçekler, dinamik bir dahili veritabanı oluşturur. Program çalışırken değiştirilebilecek gerçeklerin tanımlı olduğu bölüme database bölümü denilmektedir.

**3.13.2. Constants Bölümü**

Diğer dillerde olduğu gibi VIP’de de sabit değişkenler kullanılabilir. Bu değişkenler constants bölümünde tanımlanır. Her bir satıra sadece tek bir sabit yazılabilir.

constants

yuz=(10\*(10-1)+10)

pi=3.14159265

maas\_katsayisi=4

mavi=5

Program derlenmeden önce her sabit değişkenin karşısındaki string olduğu gibi atanır. Örnek:

A=yuz\*34, bekle(A)

şeklindeki A değişkenine yuz sabiti yerine 100 değil, yuz sabit değişkeninde tanımlı şekliyle (10\*(10-1)+10) değeri atanır.

Sembolik sabitlerin yazımında şu kurallar geçerlidir:

Sabit bir değişken kendisini çağıramaz. Yani sayi= 2\*sayi/2 yanlıştır.

Büyük veya küçük harfle başlayan sabit değişkenler, farklı olarak işlem görmezler. Bu yüzden büyük harfle başlayan sabit bir değişken clause veya goal bölümünde küçük harfle başlatılmalıdır. Böylece büyük harfle başlamaları zorunlu olan normal değişkenlerle karışmazlar. Örnek:

constants

iki=2

goal A=iki, write(A).

Bir programda birden fazla constants bölümü olabilir. Fakat programda kullanılmadan önce bu değişkenlerin mutlaka tanımlanmış olmaları gerekir.

Tanımlanan sabitler tanımlanan noktadan başlayıp programın sonuna kadar aynı değerde kalırlar. Bir sabit değişken sadece bir kez tanımlanabilir.

**3.13.3. Global Bölümü**

VIP’de şimdiye kadar tanımladığımız domains, predicates ve clauses bölümleri tamamen lokal idi. Bunları global yapmak için programın en başında global domains, global predicates vs. bölümler oluşturulabilir. Bu konu daha sonra incelenecektir.

**3.14. Derleyici Direktifleri**

VIP, yazılan bir program parçasının derleme sırasında belirtilen şekilde işlem görmesi için bazı direktiflerin kullanılmasına imkan tanır. Bu seçenekler menüdeki Options/Compiler Directives başlığından ayarlanabilir.

**3.14.1. Include Direktifi**

Bu direktif daha önce yazılan bir program parçasının veya prosedürün her çağrıldığında aynı program içerisinde tekrar tekrar kullanılmasını sağlar. Bu durum basit bir örnek üzerinde açıklanmaktadır.

İçinde en sık kullanılan tip ve yüklemlerin bulunduğu TEST.PRO isminde bir programın olduğunu varsayalım. Hazırlanan başka bir programda bu program çağırılıp kullanılmak istendiğinde, kullanılan

include “test.pro”

bir derleyici direktifidir. Ana program derlendiği zaman VIP test.pro isimli programı derleyip ana programa ilave eder. Include direktifiyle tanımlanan bir programda da başka bir include satırı bulunabilir ve o da başka bir programı çağırabilir. Fakat bir programda bir dosya sadece bir kez include “dosyaismi.pro” şeklinde kullanılabilir.

**3.15. Bölüm Özeti **

Bir VIP programının yapısı şu şekildedir:

**domains**

argüman1,...,argümanN=tip

**predicates**

yüklem\_ismi(argüman1,..., argümanN)

**clauses**

kurallar ve gerçekler

**GOAL**

alt\_hedef1, alt\_hedef2, ........, alt\_hedefN

Domains bölümünde kullanılacak değişkenlerin tipleri tanımlanır. VIP’da kullanılabilecek bazı tipler: char, byte, short, ushort, word, integer vs.

Yazılmış olan gerçek ve kuralları inceleyerek doğruluğunun sağlanması istenilen Goal (sorgu), programın içine yazılması gerekir. Bu dahili bir sorgudur. Harici olarak tanımlanacak olan bir sorgu program çalışırken açılan Dialog penceresine yazılır.

Aynı isimde fakat farklı sayıda argüman taşıyan yüklemler tamamen farklı yüklemlermiş gibi işlem görür.

Kurallar Baş:- alt\_hedef1, alt\_hedef2, ........., alt\_hedefN genel şekliyle yazılır. Bir kuralın istenilen sonucu vermesi için alt hedeflerin tamamının doğrulanması gerekir.

Prolog’daki if komutu diğer dillerdeki if komutundan farklıdır. Prolog’da then/if şeklinde tanımlı olan bu komut diğer dillerde if/then şeklinde tanımlıdır.

**4. EŞLEŞTİRME VE GERİYE İZ SÜRME**

VIP bir alt hedeften gelen bir çağrıyı clauses bölümünde tanımlı bir cümle ile karşılaştırmaya çalışırken belirli bir işlem kullanır. Bu işleme eşleştirme denir. Bir program çalışırken

Goal yazdi(X,Y).

sorgusunun kullanıldığını kabul edilsin. Bu sorgunun doğruluğunu araştırırken, clauses bölümdeki bütün yazdi(X,Y) cümlecikleri eşleştirme işlemi için test edilir. Goal yazdi(X,Y) ifadesindeki X ve Y argümanları, clauses bölümündeki yazdi(...) cümlecikleriden kontrol edilir. Bunun için bütün cümlecikler tek tek incelenir. Sorguyla eşleşen bir cümle bulunduğu zaman cümledeki değer serbest olan değişkene atanır ve böylece cümle ile goal eşleşmiş olur. Bu duruma ‘sorgunun cümle ile eşleşmesi’, bu işleme de eşleştirme denilir.

**Örnek**

DOMAINS

kitap\_adi, yazar = symbol

sayfa\_sayisi = unsigned

PREDICATES

kitap(kitap\_adi, sayfa\_sayisi)

nondeterm yazdi(yazar, kitap\_adi)

nondeterm roman(kitap\_adi)

CLAUSES

yazdi(eco, "Gülün Adı").

yazdi(tolstoy, "İnsan Ne İle Yaşar").

kitap("İnsan Ne İle Yaşar ", 245).

kitap("Gülün Adı", 760).

roman(Kitap\_adi):- yazdi(\_, Kitap\_adi), kitap(Kitap\_adi, Sayfa\_sayisi), Sayfa\_sayisi> 400.

GOAL yazdi(Yazar, Kitap\_adi).

Sorgudaki Yazar ve Kitap\_adi değişkenleri serbest değişkenler olduklarından herhangi bir argümana eşitlenebilirler. Dolayısıyla sorgu clauses bölümündeki ilk yazdi cümlesi ile eşleşir. Yani yazdi(Yazar, Kitap\_adi) cümleciği yazdi(eco, “Gülün Adı”) olur. Burada Yazar=eco, Kitap\_adi=Gülün Adı değerini alır. Aynı işlem bütün alternatif çözümler için tekrar edileceğinden, Yazar ve Kitap\_adi değişkenleri sırasıyla tolstoy ve İnsan Ne İle Yaşar değerlerini de alır. Yani sonuçta 2 çözüm bulunur.

GOAL roman(Roman\_adi) çağrısının nasıl çalıştığı incelenecektir. Bir çağrının bir olgu veya kuralın baş kısmıyla eşleşip eşleşmediği kontrol edilir. Yani kuralın baş kısmı olan roman(Kitap\_adi) kısmıyla eşleşir. Kullanılan olgudaki argümanlar eşleştirilir. X argümanı bağlı olmadığı için herhangi bir argümanla eşleşebilir. Kuralın başı olan roman(Kitap\_adi)’ında, Kitap\_adi argümanı bağımsız bir değişkendir. Kuralın başıyla sorgu kısmı eşleştirilir. VIP, eşleştirme yapıldıktan sonra alt hedefleri sırasıyla doğrulamaya çalışır.

roman(Kitap\_adi):-

yazdi(\_, Kitap\_adi),

kitap(Kitap\_adi, Sayfa),

Sayfa>400.

GOAL roman(Roman\_adi) kodunda ilk önce yazdi(\_,Kitap\_adi) kısmı sorgulanır. Buradaki ilk argüman anonimdir. Dolayısıyla ilk olgudaki eco ve Gülün Adı ‘\_’ ve ‘Kitap\_adi’ argümanlarıyla eşleşir. Bundan sonra kitap(Kitap\_adi,Sayfa\_sayisi) cümleciğindeki kitap olgusuna çağrı yapılır. İlk cümlecikteki ‘eco’ ve ‘Gülün Adı’ değerlerini alır. İlk alt hedef doğrulandığı için sonraki adım olarak kitap(Kitap\_adi, Sayfa\_sayisi) alt hedefine geçilir. Kitap\_adi argümanı ‘Gülün Adı’ değerine bağlı hale geldiği için çağrı kitap(“Gülün Adı’, Sayfa\_sayisi) şeklinde devam eder. Programın başından başlayan sorgu kitap(“Gülün Adı”, 760) cümleciğinde eşleştirme yapmaz. Çünkü ilk argüman ‘Gülün Adı’ olmuştu. İkinci cümlecik sorguyu doğrular ve Sayfa\_sayisi 760 değerini alır. Sayfa\_sayisi>400 alt hedef halini alır. 760 değeri 400’den büyük olduğu için alt hedef doğrulanır ve böylece bütün hedef doğrulanmış olur. Sonuçta şu mesaj görüntülenir:

Roman\_adi=Gülün Adı

1 Solution

**4.1. Geriye İz Sürme**

Gerçek problemlere çözüm ararken, verilen karar doğrultusunda mantıklı olan bir yol takip eder, yolun sonuca ulaşmaması durumunda alternatif bir yol aranır. Mesela bir labirent oyununda çıkış yolunu ararken sola veya sağa doğru gidilir. Çıkmaz sokağa gelindiğinde geriye döner, başka bir yolu takip eder. Bu yönteme göre devam edilirse, sonunda çıkış noktası bulunur.

VP, geriye iz sürme denilen bu sistemi kullanır. Bir sorgunun doğru olup olmadığı araştırılırken alt hedeflerin herbirinin ayrı ayrı doğrulanmaya çalışılır. VP, doğrulama işlemini yürütürken sorgulanması gereken durumların başlangıç noktasına bir işaret koyar. Sonra bu yolların ilkini dener. Eğer olumlu sonuç alınırsa işleme oradan itibaren devam eder. Sonucun olumsuz çıkması durumunda, işaret konulan yere döner ve ikinci yolu, yani bir sonraki alt hedefi dener. İşte bu ileriye gidiş ve gerektiğinde yine geriye dönüş işlemine **Geriye İz Sürme** denir.

**Örnek**

PREDICATES

nondeterm yemeyi\_sever(symbol, symbol)

nondeterm yemek(symbol)

yemegin\_tadi(symbol, symbol)

CLAUSES

yemeyi\_sever(besir,X):-

yemek(X),

yemegin\_tadi(X, iyi).

yemegin\_tadi(kebap, iyi).

yemegin\_tadi(kapuska, kotu).

yemek(kapuska).

yemek(kebap).

GOAL yemeyi\_sever(besir, Besirin\_Sevdigi\_Yemek).

Programda iki olgu kümesi, bir de kural bulunmaktadır. Kural, Bülent’in, tadı güzel olan yemeklerden hoşlandığını söylemektedir. Sorgunun doğrulanması için VP ilk satırdan başlayarak tarama yapar. Hedefe uyan ilk satır yemeyi\_sever(bulent, X) kuralının başı olduğu için Besirin\_Sevdigi\_Yemek argümanı X ile eşleşir. Bu durumda kuralın geri kalan kısmının doğrulanmasına çalışılır. Buradaki ilk alt hedef yemek(X) cümleciğidir. VP alt hedefi doğrulamak için yine programın en başına gider. VP eşleşen bir olgu ararken yemek(kapuska) cümleciğine ulaşır ve burada X değişkeni ‘kapuska’ değerini alır. VIP, buraya geri dönüş işaretini koyar ve alternatif bir çözüm ararken hareket edilecek ilk noktanın başlangıcı belirtilmiş olur.

Bir sonraki hedef, yemegin\_tadi(X, iyi) alt hedefi olur. X ‘kapuska’ değerini aldığına göre bu cümle yemegin\_tadi(lahana, iyi) şekline dönüşür. Bunun doğrulanması sırasında argümanlar başka bir olguyla eşleşmediği için bu alt hedef olumsuz olur. Dolayısıyla sorgunun bu doğrulanması başarısız olur. İşte bu noktada VP geri dönüş işaretini koyduğu en son noktaya, yani yemek(kapuska) cümleciğine gider. Geri dönüş noktasına gelindiğinde, bu noktadan sonra değer almış olan bütün değişkenler yeniden serbest hale gelirler.

Bu noktadan sonra ilk eşleşme yemek(kebap) olgusu ile olur ve X değişkeni kebap değerini alır. Daha sonraki alt hedef yemegin\_tadi(kebap, iyi) olduğundan, programın başından itibaren yapılacak bir taramadan olumlu sonuç alınır. Çünkü yemegin\_tadi(kebap, iyi) olgusu önceden tanımlanmıştı. Sonuçta görüntülenecek mesaj şu olur:

Besirin\_sevdigi\_yemek=kebap

1 Solution

Geriye İz Sürme yöntemiyle sadece tek çözüm değil, mümkün olan bütün çözümler elde edilir.

DOMAINS

aday=symbol

adayin\_yasi=integer

PREDICATES

nondeterm oyuncu(aday, adayin\_yasi)

CLAUSES

oyuncu(ahmet, 10).

oyuncu(mehmet, 12).

oyuncu(ali, 10).

oyuncu(huseyin, 10).

GOAL oyuncu(Birinci\_oyuncu, 10), oyuncu(Ikinci\_oyuncu, 10),

Birinci\_oyuncu<>Ikinci\_oyuncu.

VP’den yaşları 10 olan çocuklar arasında düzenlenecek bir masa tenisi turnuvası için muhtemel ikili rakip listesi istensin. Eşleştirme sırasında yaşları 10 olan, fakat kendileriyle eşleşmeyecek ikili gruplar istensin. Geriye İz Sürme yönteminin nasıl çalıştığını görmek için VP’nin takip edeceği prosedürü adım adım yazarsak:

VP ilk önce sorgunun oyuncu(Birinci\_oyuncu, 10) alt hedefini doğrulamaya çalışır. Bu hedef oyuncu(ahmet, 10) cümleciğiyle sağlanmış olur. VP hemen ikinci alt hedefi doğrulamaya çalışır. (Bu sırada programın en başına dönüş yapılır) oyuncu(İkinci\_oyuncu, 10) alt hedefini sağlamaya çalışırken yine 10 yaş şartını birinci cümlecik sağlar. Dolayısıyla İkinci\_oyuncu argümanı da ‘ahmet’ değerini alır. Her iki alt hedef sağlandıktan sonra şimdi üçüncü alt hedef sağlanmaya çalışılır. Yani Birinci\_oyuncu<>İkinci\_oyuncu (Birinci ve ikinci oyuncu aynı kişi olmayacak)

Oyuncuların her ikisi de ahmet olarak eşleştiği için bu hedef sağlanamaz, dolayısıyla sorgu başarısız olur. VP’nin Geriye İz Sürme mekanizması yeniden bir önceki alt hedefi, yani ikinci alt hedefi sağlamaya yönelir. Bu kez ikinci\_oyuncu argümanı ali değerini alır.

Üçüncü alt hedef sağlanmış olur. Çünkü ahmet ve ali, yaşları 10 olan farklı kişilerdir. Bütün alt hedefler sağlandığından sorgunun tamamı başarılmış olur. Sonuçta oluşan ilk ikili

Birinci\_oyuncu= ahmet, İkinci\_oyuncu=ali

olarak bulunmuş olur.

VP’nin sadece bir çözüm değil, mümkün olan bütün çözümleri bulur. Bu yüzden 3. alt hedef sağlandıktan sonra başka çözüm olup olmadığını bulmak için bütün alternatifler tükeninceye kadar ikinci alt hedefi sorgulanır. Bu kez ikinci\_oyuncu olarak Hüseyin seçilir. Ahmet ve Hüseyin 3. şartı da sağladığı için ikinci grup ahmet ve hüseyin’den oluşur.

Peki başka çözüm var mı? VP bunu bulmak için yine ikinci alt hedefe dönüş yapar. Görüldüğü gibi son oyuncu olan Hüseyin ile bu şanş tükenmiştir. İşte bu noktada Geriye İz Sürme yine ilk alt hedefe döner. İkinci eşleşme oyuncu(ali, 10) cümlesinde olur. İkinci oyuncu Hüseyin ile eşleşir. En son alt hedef de sağlandığı için bu kez ali=hüseyin ikilisi oluşturulur.

Başka çözüm için VP 2. alt hedefe döner. VP ikinci kez hüseyin ismiyle eşleşme yapar. Fakat kişi aynı olduğundan sonuç alınamaz. Geriye İz Sürme yöntemiyle bütün seçeneklerin sırasıyla denenmesi sonucunda şu tablo ortaya çıkar.

Birinci\_oyuncu=ahmet, İkinci\_oyuncu=ali

Birinci\_oyuncu=ahmet, İkinci\_oyuncu=hüseyin

Birinci\_oyuncu=ali, İkinci\_oyuncu=ahmet

Birinci\_oyuncu=ali, İkinci\_oyuncu=hüseyin

Birinci\_oyuncu=hüseyin, İkinci\_oyuncu=ahmet

Birinci\_oyuncu=hüseyin, İkinci\_oyuncu=ali

6 Solutions

Bulunan sonuçların bazıları, isimlerin sadece yer değiştirilmesinden oluşmuş aynı ikili gruplardır. Bunu engellemek mümkündür.

(Not: Aynı program ile yaşları 10 ve 12 olan ikili grupları bulunuz)

**4.2. Geriye İz Sürme Mekanizmasının Ayrıntıları**

Aşağıdaki programa bakarak Geriye İz Sürme işlemenin nasıl işlediğini anlamaya çalışalım.

DOMAINS

isim, sey= symbol

PREDICATES

sever(isim, sey)

okur(isim)

merakli(isim)

CLAUSES

sever(ahmet, limonata):-!.

sever(murat, yuzme):-!.

sever(murat, kitap):-!.

sever(murat, basketbol):-!.

sever(Z,kitap):-

okur(Z), merakli(Z).

okur(ahmet).

merakli(ahmet).

GOAL sever(X, limonata), sever(X, kitap).

VP hedefi değerlendirirken, doğrulanan ve doğrulanamayan alt hedefleri belirler. Yukarıdaki programa aşağıdaki hedefi göz önüne alarak bakalım. Hedef aşağıdaki gibi bir ağaç dalı şeklinde gösterilebilir. Doğrulanan alt hedefi altı çizili halde, bununla eşleşen cümleciği de bunun hemen altına yazalım.

| sever(X,limonata) | Sever(X,kitap) |
| --- | --- |

**4.2.1. Geriye İz Sürmenin 4 Temel Prensibi**

Yukarıdaki örnekte, hedefin gerçekleştirilmesi için doğrulanması gereken iki alt hedef vardır. Bunun için VP dört temel prensibe göre çalışır:

Bütün alt hedefler, ilkinden başlanmak üzere, birer birer doğrulanmalıdır. Bir cümleciğin doğrulanması için hangi alt hedefin kullanılacağına ikinci kurala göre karar verilir.

Yüklem cümlecikleri (fonksiyonlar) programdaki sırasıyla, yukarıdan aşağıya göre test edilirler. Buna göre yukarıdaki program çalışırken ‘sever’ yüklemini sağlayan sever(ahmet, limonata) cümleciğiyle doğrulanır. Dolayısıyla sever(X, limonata) alt hedefindeki X argümanı ‘ahmet’ değerini alır. Daha sonra ikinci alt hedef doğrulanmaya çalışılır. Burada bağlı hale gelen X=ahmet argümanı kullanılır. Fakat sever(ahmet, limonata) alt hedefi sever(ahmet, kitap) alt hedefine eşitlenemez, çünkü limonata ve kitap aynı değildir. Bütün cümleciklerin sırayla deneneceği için bir sonraki cümlecik sever(murat, kitap) olacaktır. Fakat X daha önce ‘ahmet’ değerini aldığı için bu şık da başarısız olur. Bu yüzden bir sonraki sever cümleciğinin sağlanması gerekir.

sever(Z,kitap):-okur(Z), merakli(Z).

Z argümanı bir değişkendir ve X değişkeni ile eşleşebilir. Zaten ‘kitap’ argümanları da eşleşir. Dolayısıyla hedef, kuralın baş kısmıyla eşleşmiş olur.

Bir alt hedef bir kuralın baş kısmıyla eşleştiği zaman, kuralın gövde kısmının doğrulanması sağlanmalıdır. Böylece kuralın gövdesi doğrulanması gereken bir alt hedefler kümesi oluşturur.

Şimdi yeniden örneğe dönelim.

sever(X,limonata) sever(X,kitap)

okur(Z) merakli(Z)

okur(Z) ve merakli(Z) alt hedeflerinin doğrulanması gerekir. Burada Z değişkeninin ‘ahmet’ değerini aldığı söylenmişti. Şimdi ise her iki alt hedefi de sağlayan sorgulama başlayacaktır. Sonuçta elde edilecek ağaç:

sever(X,wine) sever(X,kitap)

sever(ahmet,wine) sever(Z,kitap)

okur(Z) merakli(Z)

okur(ahmet) merakli(ahmet)

Hedef ağacının her bir dalını sağlayan bir gerçek bulunduğu zaman hedef sağlanmış olur.

Sonuçta

X=ahmet

1 Solution

cevabı görüntülenir. Harici bir hedef doğrulandıktan sonra VP’nin, eğer varsa, bütün alternatifleri bulmak için çalışacağı söylenmişti. Bir alt hedef başarısız olursa, VP yeniden bir önceki alt hedefe döner. Bu alt hedefi, biraz önce başarısız hale gelen alt hedefi de doğrulayacak bir cümlecik ile doğrulamaya çalışır.

VP bir alt hedefi sağlamak için sorgulamaya yüklemi tanımlayan ilk cümlecikten başlar. Bu sırada aşağıdaki durumlardan biri meydana gelebilir:

İlk cümlecik verilen yüklemle eşleşir. Bu durumda;

Alt hedefi doğrulama ihtimali olan başka bir cümlecik varsa, Geriye İz Sürme işleminde kullanılmak üzere bu cümleciğin yanına bir işaret konur.

Alt hedefteki bütün serbest değişkenler cümlecikteki değerleri alır ve bağlı hale gelirler.

Eğer eşleşen cümlecik bir kuralın baş tarafı ise, hemen kuralın gövde kısmı değerlendirilir. Bu durumda gövdedeki bütün alt hedeflerin doğrulanması gerekir.

Eşleşen herhangi bir cümlecik bulunmaz ve sorgu başarısız hale gelir. VP bir önceki alt hedefi doğrulamak için geriye iz sürer. En son geriye dönüş noktasına geldiğinde, VP geriye dönüş noktasından sonra değer almış bütün değişkenleri serbest hale getirir. Daha sonra alt hedefi yeniden doğrulamaya çalışır.

Tarama, programın başından başlar. Geriye İz Sürme işlemi, daha önce yerleştirilen geriye dönüş noktasından itibaren başlar. Sorgu burada da başarısız olursa, geriye iz sürme işlemi tekrar edilir. Bütün alt hedef ve cümlecikler için geriye dönüş işlemi tamamlandığında sonuç elde edilemezse, hedef başarısız olur.

Geriye dönüş işlemi için başka bir örnek.

**Örnek:**

PREDICATES

nondeterm tur(symbol, symbol)

nondeterm canli(symbol, symbol)

yasar(symbol, symbol)

nondeterm yuzebilir(symbol)

CLAUSES

tur(tirnakli, hayvan).

tur(balik, hayvan)

canli(zebra, tirnakli).

canli(alabalik, balik).

canli(kopekbaligi, balik).

yasar(zebra, karada).

yasar(kurbaga, karada).

yasar(kurbaga, suda).

yasar(kopekbaligi, suda).

yuzebilir(Y):-

tur(X, hayvan),

canli(Y,X),

yasar(Y, suda).

GOAL yuzebilir(Ne), write(“Bir ",Ne," yüzebilir\\n").

Program yazılıp çalıştırıldığında ilk olarak GOAL bölümü sağlanmaya çalışılır. Şimdi yapılacak işlemleri adım adım yazalım:

yuzebilir yüklemi, ‘Ne’ serbest değişkeni ile çağrılır. Eşleşme olup olmadığını bulmak için program tarandığında ‘Ne’ argümanı ‘Y’ değerini alır.

Hemen sonra hedefin gövde kısmına geçersek tur(X,hayvan) alt hedefinin doğrulanması gerekir. Programın başından itibaren yapılacak bir taramada tur(tirnakli, hayvan) cümleciği bu alt hedefi sağlar. Böylece X=tirnakli değerini alır.

Burada tur(X,hayvan) alt hedefini sağlayabilecek birden fazla alternatif olduğu için, tur(tirnakli,hayvan) cümleciğinin yanına Geriye İz Sürme işareti konur.

X değişkeni ‘tirnakli’ değerini alınca birinci alt hedef doğrulanmış olur. Bu kez ikinci alt hedef yani canli(Y, X) doğrulanmaya çalışılır. Bu hedef ise canli(Y, tirnakli) olarak sağlanır. canli(zebra, tirnakli) cümleciği ikinci alt hedefi sağlar ve Y değişkeni ‘zebra’ değerini alır ve bu hedefi sağlayan başka cümlecikler de mevcut olduğundan, VP bu cümleciğin yanına da bir Geriye İz Sürme işareti koyar.

Şimdi X=tirnakli ve Y=zebra olacak şekilde en son alt hedefin doğrulanması gerekir. yasar(Y, suda) alt hedefinin sağlanması için yasar cümleciklerinin biriyle eşleşmesi gerekir. Fakat cümlecikler arasından bunu sağlayan bir gerçek olmadığı için hedef başarısız olur.

VP bu noktada geriye dönüş işareti koyduğu en son noktaya, yani ikinci alt hedef ve canli(zebra, tirnakli) cümleciğine döner.

Geriye dönüş noktasına geldiğinde, bu noktadan sonra değer almış bütün değişkenler serbest hale gelir. Daha sonra canli(Y, tirnakli) alt hedefine yeni bir çözüm arar.

VP daha önce işaret koyup durduğu satırdan başlamak üzere, geriye kalan cümlecikler arasında tarama yaparak şimdiki alt hedefe uyacak bir çözüm arar. Programımızda alt hedefi doğrulayacak başka bir seçenek bulunmadığından, yapılan çağrı başarısız olur ve VP yeniden bir önceki alt hedefe döner.

Bu kez tur(tirnakli, hayvan) hedefini doğrulamaya çalışır. Çünkü geriye dönüş işareti buraya konulmuştu.

Bütün değişkenler serbest hale getirilir ve yeniden tur(X, hayvan) alt hedefine çözüm arar. Geriye dönüş noktasından sonraki tur(balik, hayvan) cümleciği bu hedefi doğrular ve X=balik değerini alır. VP bu kez geriye dönüş noktasını bu cümleciğin yanına yerleştirir.

VP şimdi kuraldaki ikinci alt hedefi doğrulamak üzere aşağıya doğru hareket eder. Bu tarama yeni bir tarama olduğu için tarama yine cümleciklerin başından, yani canli(Y, tirnakli) cümleciğinden başlar.

canli(alabalik, balik) cümleciği alt hedefi doğrular ve Y=alabalik değerini alır.

Y şimdi ‘alabalik’ değerini aldığı için, yasar(alabalik, suda) alt hedefi çağrılır. Bu da yeni bir çağrı olduğu için program yine baştan başlar.

Cümleciklerde görüldüğü gibi, yasar yüklemleri arasında yasar(alabalik, suda) alt hedefini doğrulayacak bir seçenek yoktur. Bu yüzden çağrı başarısız olur ve bir önceki alt hedefe yeniden dönüş yapılır.

canli(alabalik, balik) geriye dönüş noktasına gidilir.

Bu noktadan sonra değer alın bütün değişkenler yeniden serbest hale geldikten sonra canli(Y, balik) çağrısına cevap aranır.

Bu kez Y=kopekbaligi değeri alt hedefi sağlar.

VP üçüncü alt hedefi yeniden doğrulamaya çalışır. Y ‘kopekbaligi’ değerini aldığı için yasar(kopekbaligi, suda) alt hedefinin doğrulanması gerekir. Bu yeni çağrı doğrulanır, çünkü son cümlecik eşleşmektedir.

Alt hedeflerin doğrulanmasından sonra kuralın baş kısmı da sağlanmış olur. VP, Y değişkeninin aldığı ‘kopekbaligi’ değerini yuzebilir(Ne) kuralındaki Ne değişkenine atar ve böylece Goal bölümündeki write("Bir ",Ne," yüzebilir\\n") alt hedefi de çağrılır. Sonuç:

Bir köpekbalığı yüzebilir

Ne=kopekbaligi

1 Solution

**4.3. Tarama İşleminin Kontrol Edilmesi**

VP’de var olan geriye iz sürme mekanizması bazen gereğinden fazla tarama yapabilir. Bu ise verimi düşürür. Bazen verilen bir problem için sadece bir çözüm bulmak istenebilir. Bazen de, bir çözüm bulunsa bile –varsa- başka alternatif çözümleri de bulmak istenebilir. İşte bu gibi durumlarda geriye dönüş işleminin kontrol edilmesi gerekir.

Geriye İz Sürme işlemini kontrol edebilmek için VP’nin iki özelliğinden faydalanılabilir. Bunlar,: VP’yi geriye iz sürme işlemi yapmaya zorlayan **fail** yüklemi ve geriye dönüş mekanizmasını engelleyen **cut** ‘!’ özelliğidir.

**4.4. fail***** *****Yükleminin Kullanılması**

Alt hedeflerden birinin sağlanamaması durumunda geriye dönüş işlemi yapılır. Bazı durumlarda alternatif çözümleri bulabilmek için bu işlemin yapılması gereklidir. VP’nin fail yüklemi, bir sorgunun başarısız olmasına ve böylece geriye dönüş işleminin yapılmasına imkan tanır.

DOMAINS

isim=symbol

PREDICATES

nondeterm baba(isim, isim)

herkesi\_bul

CLAUSES

baba("Ömer ", yavuz).

baba(ahmet, kasim).

Baba(huseyin, veli).

Baba(murat, yusuf).

herkesi\_bul:-

baba(X,Y), write(X, Y," Babası\\n"),

fail.

herkesi\_bul.

GOAL herkesi\_bul.

Programdaki dahili hedef doğrulandıktan sonra VP’nin geriye iz sürmesine gerek yoktur. Bundan dolayı baba ilişkisine yapılan ilk çağrı başarılı olur ve sadece bir tek çözüm sağlanmış olur. Fakat yüklem bölümündeki **herkesi\_bul** yüklemi **fail** özelliğini kullanarak Prologu geriye iz sürme mekanizmasını kullanmaya zorlar ve mümkün olan bütün çözümlerin bulunmasını sağlar. Herkes yükleminin amacı, görüntülenen cevapların daha net olmasıdır.

Herkes yüklemi VP’yi zorlayarak, baba(X,Y) kuralının sağlanması için geriye dönüş işleminin çalıştırılmasını sağlar. Daima olumsuz cevap vereceği için fail kuralının doğrulanması mümkün değildir. Bu yüzden VP daima bir üstteki alt hedefe geriye dönüş yapar. Geriye dönüş olduğunda VP, birden fazla çözüm verebilecek en son hedefe döner. Bu tür bir çağrı belirsiz (non-deterministic) olarak tanımlanır. Belirsiz bir çağrı, belirli olan ve sadece bir tek çözüm sunabilen bir çağrının tam tersidir.

‘write’ yükleminin doğruluğu yeniden sağlanamaz, çünkü yeni çözümler sunmaz. Haliyle VP kuraldaki ilk alt hedefe geriye dönüş yapar.

‘fail’ yüklemini takiben başka alt hedeflerin yazılması hiçbir işe yaramaz. Çünkü ‘fail’ yükleminin kendisi daima başarısız olacağından, ‘fail’ yüklemini takip eden bir alt hedefin sorgulaması mümkün değildir.

**4.5. Geriye İz Sürmeyi Engelleme**

VP’de ünlem işareti ile gösterilen (!) cut yükleminden itibaren geriye dönüş mümkün değildir. **Cut** yüklemi, bir kuralın içinde herhangi bir alt hedefmiş gibi yazılır. Program çalışırken cut alt hedefi daima doğrulanır ve işlem bir alt hedefe geçer. Bu hedeften önceki alt hedeflere ve cut komutunu içeren alt hedefin kendisine geriye dönüş artık mümkün değildir.

Cut komutu iki amaç için kullanılır:

Alternatif çözümün mümkün olmadığına önceden karar verilirse, vakit ve bellek kaybını önlemek için bu komut kullanılabilir. Böylece program daha hızlı çalışır. Buna **‘green cut (Olumlu Cut)’** denir.

Programın kendi mantığı cut yüklemini gerektiriyorsa, alternatif alt hedeflerin incelenmesini önlemek için de cut kullanılır. Buna ise **‘red cut (Olumsuz Işık)’** adı verilmektedir.

**4.5.1. Cut Komutunun Kullanımı**

Bu bölümde cut komutunun kullanımı ile ilgili örnekler üzerinde çalışalım. r1, r2, r3 kuralları r yüklemini, a, b, c ise alt hedefleri gösterir.

Bir kural içindeki bir alt hedefe geri dönüşü engellemek için

R1:- a, b, !, c. yazılabilir.

Yukarıdaki kuralın anlamı şudur: Kural içerisindeki a ve b alt hedeflerini doğrulayan bir çözüm bulunduğunda programı durdur. Bu yüzden cut komutunu geçip c alt hedefine geçmek mümkün değildir. Dolayısıyla a ve b için alternatif çözümler mümkün olsa da, sadece bulunan ilk çözümle yetinilir. Cut komutu r1 yüklemini tanımlayan başka bir cümlecik içine gitmeyi de engeller.

Örnek

PREDICATES

araba\_satin\_al(symbol,symbol)

nondeterm araba(symbol,symbol,integer)

renkler(symbol,symbol)

CLAUSES

araba\_satin\_al(Model,Renk):-

araba(Model,Renk,Fiyat),

renkler(Renk,cazip),!,

Fiyat > 20000.

araba(murat,yesil,25000).

araba(mersedes,siyah,24000).

araba(bmw,kirmizi,28000).

araba(renault,kirmizi,24000).

araba(toyota, sari, 30000).

renkler(kirmizi,cazip).

renkler(siyah,orta).

renkler(yesil,berbat).

renkler(sari, cazip).

GOAL araba\_satin\_al(bmw, Hangi\_renk).

Bu örneğin verilmesinin amacı, rengi cazip, fiyatı da uygun olan bir BMW almaktır. Veri tabanında BMW için zaten bir satır vardır. Prolog’un yapması gereken tek şey, fiyatının verilen şarta uyup uymadığını kontrol etmektir. Goal içerisindeki ! komutu, BMW için fiyat uygun değilse, başka bir araba aranmasını engeller. Programı çalıştırıldığında

Hangi\_renk=kirmizi

1 Solution

yanıtı alınır.

**4.5.2. Geriye İz Sürmeyi Engelleme**

Cut komutu, bir yüklem için doğru olan bir cümlenin seçildiğini belirtmek için de kullanılabilir.

r(1):-!, a, b, c

r(1):-!, d

r(1):-!, c

r(\_):- write (“Cümlelerin tamamı buraya yazılır”).

Cut komutu r yüklemini deterministic (belirli) yapar. Dolayısıyla r yüklemi bir tamsayı argümanı ile çağrılır. Yapılan çağrının r(1) olduğunu kabul edelim. Prolog yapılan çağrıya uygun bir eşleşme ararken, r’yi tanımlayan bir cümlecik bulur. Birden fazla çözüm mümkün olduğundan, Prolog ilk cümleciğe geri dönüş noktası işareti koyarak aşağıda doğru işleme devam eder ve geri kalan satırlara geçer. Olacak ilk şey, cut komutu geçmektir. Böyle yapmak artık başka bir r cümleciğine geri dönüşü ortadan kaldırır ve geri dönüş noktası ortadan kalktığı için, programın çalışma hızı oldukça artar.

Bu tür yapının diğer dillerde yazılan ‘Case’ yapılarına benzediği görülür. Deneme şartı, kuralın baş tarafında yazılır. Yukarıdaki satırları daha anlaşılır yapmak için şöyle yazalım:

r(x):- X=1, !, a, b, c.

r(x):- X=2, !, d.

r(x):- X=3, !,c.

r(\_):-write (“Cümlelerin tamamı buraya yazılır”).

Örnek:

PREDICATES

arkadas(symbol,symbol)

kiz(symbol)

sever(symbol,symbol)

CLAUSES

arkadas(ahmet,fatma):- kiz(fatma), sever(ahmet,fatma),!.

arkadas(ahmet,mehmet):- sever(mehmet,futbol),!.

arkadas(ahmet,esra):- kiz(esra).

kiz(tuba).

kiz(fatma).

kiz(esra).

sever(mehmet,futbol).

sever(ahmet,esra).

GOAL arkadas(ahmet,Kimin\_Arkadasi).

Program akışı içerisinde Cut komutu kullanılmazsa, yukarıdaki örnekten iki ayrı sonuç elde edilir. Yani Ahmet hem Mehmet’in hem de Esra’nın arkadaşıdır. Fakat arkadas iliskisini tanımlayan ilk cümledeki Cut komutu, bu cümlenin doğrulanıp Ahmet’in bir arkadaşının bulunması durumunda, artık ikinci bir arkadaş bulmanın gereksiz olduğunu vurgular. Bu yüzden yukarıdaki Goal için sadece Mehmet’in Ahmet’in arkadaşı olduğu cevabı görüntülenir.

**4.6. Determinism ve Cut**

Yukarıdaki örnekte ‘arkadas’ yüklemi Cut kullanılmadan tanımlanmış olsaydı, non-deterministic, yani geriye iz sürme işlemiyle birden fazla çözüm üretmesi mümkün bir yüklem olacaktı. Programların ihtiyaç duyacakları bellek miktarı artacağından, özellikle non-deterministic yüklemler ile çalışılırken dikkatli olmak gerekir. VIP non-deterministic yüklemleri dahili olarak kontrol etmekle beraber, güvenli bir program yazmak için ***check\_determ*** derleyici direktifini kullanmak faydalıdır. Eğer ***check\_determ*** programın hemen ilk satırına yerleştirilirse, programın çalıştırılması esnasında non-deterministic yüklemlere gelindiğinde bir uyarı mesajı görüntülenir. Böylece non-deterministic olan bir yüklemin gövde kısmında (body) uygun bir **Cut** komutu kullanarak yüklemi deterministic hale getirebiliriz.

**4.7. Not Yüklemi**

Genel Not Ortalaması 3.5 olan ve beklemeli olmayan Şeref Öğrencisini bulman program:

DOMAINS

isim= symbol

gno= real

PREDICATES

nondeterm seref\_ogrencisi(isim)

nondeterm ogrenci(isim, gno)

beklemeli(isim)

CLAUSES

seref\_ogrencisi(Isim):-ogrenci(Isim,Gno),Gno>=3.5, not(beklemeli(Isim)).

ogrenci ("Kasım Yenigün", 3.5).

ogrenci("Ferit DAĞDEVİREN", 2.8).

ogrenci("Orhan AYDIN", 3.8).

beklemeli("Kasım Yenigün").

beklemeli("Ferit DAĞDEVİREN").

GOAL seref\_ogrencisi(Seref\_Ogrencisinin\_Adi\_Soyadi).

Not komutunu kullanırken dikkat edilmesi gereken tek bir kural vardır: Not komutu, sadece alt hedefin doğruluğunun ispatlanamaması durumunda işlem görür. Serbest değişkenli bir alt hedef Not içerisinden çağrıldığı zaman, Prolog, **Free variables not allowed in ‘not’ or ‘retractall’** (Not veya retractall içerisinde serbest değişkenler kullanılamaz) hata mesajını verecektir. Prolog’un bir alt hedefteki serbest değişkenlere değer ataması için, bu alt hedefin başka cümlecikle eşleşmesi ve alt hedefin doğrulanması gerekir. Not içeren bir alt hedefteki bağımsız değişkenleri kullanmanın en doğru yolu anonim değişkenler (\_) kullanmaktır.

Aşağıda bu konu ile ilgili yanlış ve doğru örnekler verilmiştir:

sever(ahmet, Herhangi\_Biri):- /\* ‘Herhangi\_Biri çıktı argümanıdır’\*/

sever(esra, Herhangi\_Biri),

not(nefret\_eder(ahmet, Herhangi\_Biri).

Burada Herhangi\_Biri, nefret\_eder(ahmet, Herhangi\_biri) alt hedefinin doğru olmadığı ispatlanmadan önce Herhangi\_biri argümanı sever(esra, Herhangi\_biri) alt hedefindeki Herhangi\_biri argümanına atanmış olur. Dolayısıyla yukarıdaki kod tam olarak arzu edildiği gibi çalışır. Yukarıdaki kısa program

sever(ahmet, Herhangi\_biri):- /\* ‘Doğru çalışmaz’\*/

not(nefret\_eder(ahmet, Herhangi\_biri),

sever(esra, Herhangi\_biri).

şeklinde yazılacak olursa, ilk önce Not ile başlayan cümlecik çağrılmış olur. Not cümleciği içinde serbest değişken tanımlamak mümkün olmadığı için, Prolog hata mesajı vermiş olur. Çünkü not(nefret\_eder(ahmet, Herhangi\_Biri) cümleciğindeki Herhangi\_biri argümanı serbest değişkendir ve hiçbir değeri yoktur. Programdaki Herhangi\_biri yerine anonim değişken olan (\_) kullanılsa bile, Prolog yine yanlış bir sonuç verecektir.

sever(ahmet, Herhangi\_biri):- /\*Doğru çalışmaz\*/

not(nefret\_eder(ahmet, \_),

sever(esra, Herhangi\_biri).

Çünkü yukarıdaki cümlelerden anlaşılan şudur: Eğer Ahmet’in nefret ettiği bir şey bilinmiyorsa ve eğer esra Herhangi\_biri’ni seviyorsa, Ahmet Herhangi\_biri’ni sever. Anlatılmak istenen şey ise şudur: Esra’nın sevdiği ve Ahmet’in de nefret etmediği Herhangi\_biri varsa, Ahmet bu Herhangi\_biri’ni sever.

Not yüklemini kullanırken çok dikkatli olmak gerekir. Yanlış kullanım, ya hata mesajı alınmasına ya da program içerisinde mantıksız bir yapıya neden olacaktır.

Örnek:

PREDICATES

Nondeterm alisveristen\_hoslanir(symbol)

Nondeterm kredi\_kartina\_sahip(symbol, symbol)

kredisi\_bitmis(symbol, symbol)

CLAUSES

alisveristen\_hoslanir(Kim):-

kredi\_kartina\_sahip(Kim,Kredi\_karti),not(kredisi\_bitmis(Kim,Kredi\_karti)),

write(Kim, Kredi\_karti, "ile alışveriş yapabilir\\n").

kredi\_kartina\_sahip(yavuz, visa).

kredi\_kartina\_sahip(yavuz, diners).

kredi\_kartina\_sahip(ahmet, shell).

kredi\_kartina\_sahip(mehmet, masterkart).

kredi\_kartina\_sahip(asaf\_bey, akbank).

kredisi\_bitmis (yavuz, diners).

kredisi\_bitmis (asaf\_bey, masterkart).

kredisi\_bitmis (yavuz, visa).

GOAL alisveristen\_hoslanir(Kim).

**Örnek:**

DOMAINS

isim,cinsiyet,meslek,cisim,yardimci,madde = symbol

yas=integer

PREDICATES

nondeterm sahis(isim, yas, cinsiyet, meslek)

nondeterm iliskili(isim, isim)

ile\_oldurdu(isim, cisim)

oldurdu(isim)

nondeterm katil(isim)

sebep(yardimci)

uzerinde\_leke\_var(isim, madde)

sahip(isim, cisim)

nondeterm birbirine\_benzer(cisim, cisim)

nondeterm sahip\_oldugu\_cisim(isim, cisim)

nondeterm supheli(isim)

/\* \* \* Katil hakkındaki gerçekler \* \* \*/

CLAUSES

sahis(huseyin,55,m,arastirma\_gorevlisi).

sahis(yavuz,25,m,futbolcu).

sahis(yavuz,25,m,kasap).

sahis(ahmet,25,m,yankesici).

iliskili(fatma,ahmet).

iliskili(fatma,huseyin).

iliskili(deniz,ahmet).

ile\_oldurdu(deniz,sopa).

oldurdu(deniz).

sebep(para).

sebep(kiskanclik).

sebep(durustluk).

uzerinde\_leke\_var(huseyin, kan).

uzerinde\_leke\_var(deniz, kan).

uzerinde\_leke\_var(yavuz, camur).

uzerinde\_leke\_var(ahmet, cikolata).

uzerinde\_leke\_var(fatma,cikolata).

sahip(huseyin,tahta\_bacak).

sahip(ahmet,tabanca).

/\* Temel Bilgiler \*/

birbirine\_benzer(tahta\_bacak, sopa).

birbirine\_benzer(demir, sopa).

birbirine\_benzer(makas, bicak).

birbirine\_benzer(futbol\_sopasi, sopa).

sahip\_oldugu\_cisim(X,futbol\_sopasi):-sahis(X,\_,\_,futbolcu).

sahip\_oldugu\_cisim(X,makas):-sahis(X,\_,\_,kuafor).

sahip\_oldugu\_cisim(X,Cisim):-sahip(X,Cisim).

/\* Susan'ın oldürüldüğü silaha sahip herkesi şüpheli kabul edilsin \*/

supheli(X):-

ile\_oldurdu(deniz,Silah) ,

birbirine\_benzer(Cisim,Silah) ,

sahip\_oldugu\_cisim(X,Cisim).

/\* Susan ile ilişkisi olan insanlar da şüpheliler listesine girmeli \*/

supheli(X):-

sebep(kiskanclik),

sahis(X,\_,m,\_),

iliskili(deniz,X).

/\* Susan'ın, ilişkilerinden haberdar olduğu bayanlar da şüpheli listemizde olmalı \*/

supheli(X):-

sebep(kiskanclik),

sahis(X,\_,f,\_),

iliskili(X,Erkek),

iliskili(deniz,Erkek).

/\* Şüpheli, para için katil olan bir yankesici olabilir \*/

supheli(X):-

sebep(para),

sahis(X,\_,\_,yankesici).

katil(Katil):-

sahis(Katil,\_,\_,\_),

oldurdu(Olduruldu),

Olduruldu <> Katil, /\* It is not a suicide \*/

supheli(Katil),

uzerinde\_leke\_var(Katil,Devam),

uzerinde\_leke\_var(Olduruldu,Devam).

GOAL

katil(Katil\_Kim).

**4.8. Prosedürel Açıdan Prolog**

Prolog tanımsal yapıya sahip bir dildir. Program hazırlarken problem olgular(önceden bilinen gerçekler) ve kurallarla tanımlanır. Bunu takiben bilgisayardan çözüm bulması beklenir. Pascal, BASIC ve C gibi diller ise tamamen prosedürlere dayanırlar. Bilgisayarın belli bir probleme çözüm bulabilmesi için, programcının, yapılması gereken işlemleri alt programlar ve fonksiyonlar halinde adım adım tanımlaması gerekir.

**4.8.1. Kurallar ve Olguların Prosedürlere Benzerliği**

Prolog’daki bir kuralı diğer dillerdeki bir procedure olarak görmek mümkündür. Örneğin

sever(ahmet, Birsey):- sever(gul, Birsey).

şeklindeki bir kural ‘Ahmet’in bir şeyi sevdiğini ispatlamak için, Gül’ün de aynı şeyi sevdiğini ispat et’ anlamına gelir. Aynı şekilde

sever(Orhan, Baklava).

şeklindeki Prolog kuralı “Orhan’ın baklava sevdiğini ispat etmek için dur” anlamındaki bir procedure olarak düşünmek mümkündür. Burada sever(Kim, Ne) şeklinde bir sorgu gelirse, Kim ve Ne serbest değişkenleri sırasıyla Orhan ve Baklava değerlerini alırlar.

Case ifadesi, boolean testleri ve goto komutu diğer dillerde mevcut olan procedure örnekleridir. Benzer işlemleri, kuralları kullanarak yapabiliriz.

**4.8.2. Bir Kuralın Case ifadesi Gibi Kullanılması**

Prolog’daki Kural ile diğer dillerdeki Procedure arasındaki büyük farklardan biri, Prolog’un aynı procedure için birden fazla alternatif tanımlama imkanı vermesidir.

Pascal’daki CASE ifadesi kullanıyormuş gibi, her argüman değeri için farklı bir tanım yazarak çoklu tanım kullanabilirsiniz. Prolog kuralları peşpeşe kullanarak eşleşenleri bulur ve kuralın tanımladığı işlemi yapar.

Örnek:

PREDICATES

nondeterm basilan\_tus(integer)

CLAUSES

basilan\_tus(1):-

nl,

write("1 Tuşuna Bastınız."), nl.

basilan\_tus(2):-

nl,

write("2 Tuşuna Bastınız."), nl.

basilan\_tus(3):-

nl,

write("3 Tuşuna Bastınız."), nl.

basilan\_tus(N):-

nl,

N<>1, N<>2, N<>3, write("Hangi Tuşa Bastığınızı Bilmiyorum"), nl.

GOAL write("1-3 arasında bir sayı yazınız: "), readint(Sayi), basilan\_tus(Sayi).

Örnekte, 1, 2 veya 3 haricindeki rakamlar girildiğinde eşleşme olamaz ve çözüm bulunmaz.

**4.8.3. Bir Kural İçinde Test Yapmak**

Yukarıdaki örnekte geçen basilan\_tus(N) cümleciğinde; verilecek herhangi bir değere otomatik olarak N’e atanacaktır. Burada verilen sayının sadece 1-3 aralığı dışında olması durumunda ‘Hangi Tuşa Bastığınızı Bilmiyorum’ mesajının görüntülenmesi gerekir. Bu N<>1, N<>2, N<>3 alt hedefleri ile gerçekleştirilmektedir. Prolog ilk önce yazılan değerin 1-3 arasında olup olmadığını doğrulamaya çalışır. Doğru olmadığını görünce geriye dönüş işlemi yapmaya çalışır. Fakat başka alternatif olmadığı için bu cümlenin geriye kalan kısmına geçiş yapamaz.

Basilan\_tus ilişkisi atanacak olan seçeneklere dayanır. Eğer basilan\_tus ilişkisi argümanı serbest olan bir değişken ile çağılırsa, GOAL bu cümlelerin hepsiyle eşleşir ve ilk üç kural alternatif çözümler olarak sunulur. Son cümle ise hataya neden olur. Çünkü bağımsız bir değişkeni bir sayı ile eşleştirmek mümkün değildir.

**4.8.4. Cut Komutunun Goto Gibi Kullanılması**

Yukarıdaki örnek vakit kaybına neden olur. Çünkü doğrulanan bir kural bulunsa bile, Prolog’un son kuralı da test edip başka alternatif araması gerekir. Prolog’a alternatif aramaktan vazgeçmesini söylemek için Cut komutu kullanılabilir. Bunun sonucu, bize zaman ve bellek tasarrufu sağlanır.

Yukarıdaki program, şimdi de Cut komutu ile yazılsın.

PREDICATES

nondeterm basilan\_tus(integer)

CLAUSES

basilan\_tus(1):- !,

nl,

write("1 Tuşuna Bastınız."), nl.

basilan\_tus(2):- !,

nl,

write("2 Tuşuna Bastınız."), nl.

basilan\_tus(3):- !,

nl,

write("3 Tuşuna Bastınız."), nl.

basilan\_tus(\_):- !, write("Hangi Tuşa Bastığınızı Bilmiyorum"), nl.

GOAL write("1-3 arasında bir sayı yazınız: "), readint(Sayi), basilan\_tus(Sayi).

Cut komutunun işleme girebilmesi için Prolog’un içinde Cut bulunan bir kurala gitmesi ve Cut komutunun bulunduğu noktaya kadar gelmiş olması gerekir.

Cut komutu basilan\_tus(X):- X>3, !, write(“Yazdığınız rakam çok yüksek”) gibi testlerden önce gelebilir. X>3 alt hedefi doğrulandığı anda Cut komutu önemli hale gelir. Burada kuralların sırası oldukça önemlidir. 13. örnekte kurallar; arzu edilen sıraya göre yazılabilir. Çünkü onlardan sadece biri girilen bir sayı ile eşleşir. Fakat Cut kullanılan yukarıdaki örnekte, bilgisayarın write("Hangi Tuşa Bastığınızı Bilmiyorum") kuralına diğer üç kuralı denemeden önce kesinlikle geçmediğinden emin olmak gerekir. Çünkü buradaki Cut komutları red\_cut, yani olumsuz cut, görevi görürler ve programın mantığını değiştirirler.

Eğer yukarıdaki programda X<>1, X<>2 ve X<>3 şeklindeki karşılaştırma anahtarlarını tutup her cümleye sadece bir Cut komutu yerleştirilirse, buradaki Cut komutları Green Cut olarak görev yaparlar. Cut, diğer programlama dillerinde tıpkı GOTO komutu gibi görev görür. Cut komutunun kullanımı faydalıdır, fakat içinde Cut kullanılan programları anlamak bazen zor olabilir.

**4.9. Hesaplanmış Değerleri Görüntüleme**

Program akışında, ilk başta herhangi bir değeri olmayan argümanlar, daha sonra belirli değerle alırlar. Örneğin

sever(orhan, gulsah).

şeklindeki bir olgu

sever(orhan, Kim)

şeklindeki bir hedef cümlesindeki Kim argümanına ‘Gulsah’ değerini atamış olur. Yani

GOAL sever(orhan, Kim) hedef cümlesindeki Kim argümanı ilk önce serbest olmasına rağmen, sever(orhan, gulsah) olgusunu çağırdığı anda olgudaki Gulsah değeri Kim argümanına atanır ve Kim argümanı sınırlı hale gelir.

Örnek:

PREDICATES

nondeterm ekrana\_yaz(integer, symbol)

CLAUSES

ekrana\_yaz(0, sifir).

ekrana\_yaz(Sayi, negatif):- Sayi<0.

ekrana\_yaz(Sayi, pozitif):- Sayi>0.

GOAL ekrana\_yaz(14, Sayinin\_isareti).

‘ekrana\_yaz’ ilişkisinin ilk argümanı daima sabit bir sayı ve bağlı bir değişken olmak zorundadır. İkinci argüman ise sınırlı veya sınırsız bir değişken olabilir. İlk değişkene bağlı olarak sıfır, negatif veya pozitif bir sayı olabilir.

Yukarıdaki GOAL cümleciğinin bulacağı cevap elbette yes olacaktır. Çünkü 14 sıfırdan büyük bir sayıdır ve pozitiftir. Burada sadece 3. cümlecik doğrudur.

GOAL ekrana\_yaz(14, negatif).

Hedef cümlesiyle aynı prosedür takip edilir ve no cevabı alınır. Prolog’un sonuç alması incelenirse,

İlk önce ilk cümlecik incelenir. Belirle ilişkisindeki argümanlar, yani 14 ve negatif değerleri, 0 ve sifir değerleriyle eşleşmezler.

İkinci cümleciğe sıra geldiğinde, Sayi 14’e eşitlenir fakat sayi<0 testi doğrulanamaz.

Üçüncü argümana gelindiğinde bu kez ikinci argümanlar eşleşmez, yani pozitif kelimesi negatif ile eşleşemez.

Anlamlı bir cevap almak için örneğin GOAL belirle(14, Sayinin\_Isareti) kullanılırsa,

Sayinin\_Isareti=pozitif

1 Solution

cevabı alınır.

Yukarıdaki örneğin çalışması esnasında, işlemler aşağıdaki sıra ile yapılacaktır.

ekrana\_yaz(14, Sayinin\_Isareti) hedef cümlesi, ilk cümleciğin ekrana\_yaz(0, sifir) kısmıyla eşleşmez. Bu yüzden ilk cümlecik kullanılamaz.

ekrana\_yaz(14, Sayinin\_Isareti) hedef cümlesi ikinci cümleciğin baş kısmıyla eşleşir ve Sayi=14, Sayinin\_Isareti=negatif olur. Fakat hemen sonraki Sayi<0 yanlış olduğundan Prolog bu cümlecikten geriye döner ve Sayi=14 değeri iptal edilir.

ekrana\_yaz(14, Sayinin\_Isareti) hedef cümlesi üçüncü cümleciğin baş kısmıyla eşleşir ve Sayi=14, Sayinin\_Isareti=pozitif olur. Sayi>0 eşitliği de sağlandığı için Prolog artık geriye iz sürme işlemini yapmaz ve sonucu görüntüler.

**5. BASİT VE BİLEŞİK NESNELER**

Şimdiye kadar Prolog’da kullanılan veri nesnelerinden number, symbol, string gibi birkaç tip incelenmiştir. Bu bölümde basit ve bileşik veri türlerinin tamamı incelenecektir. Standart tip olarak tanımlanabilen veriler, bazı bileşik veri yapılarını içermezler. Bu yüzden farklı veri yapılarına göz atarak, bunların domains ve predicates bölümlerinde nasıl tanımlanabileceği göreceğiz.

**5.1. Basit veri nesneleri**

Basit bir veri nesnesi, bir değişken veya bir sabitten oluşabilir. Sabit, **constants **bölümünde tanımlanan veri tipi değil; char, integer, symbol, string gibi değişmeyen bir nesnedir.

**5.1.1 Veri Nesneleri Olan Değişkenler**

VIP değişkenleri A-Z arasındaki büyük bir harf veya (\_) ile başlamalıdır. (Değişken isimlerinde ç, İ, ö, ğ, ş vs. gibi Türkçe karakterler kesinlikle kullanılamaz) Yalnız başına kullanılan (\_) değişkeninin anonim değişken olduğunu ve herhangi bir değerle eşleşebileceği bilinmektedir. Prolog’daki değişkenler global değil, lokaldir. Yani iki ayrı cümlecikte aynı isimle -örneğin X- gösterilen bir değişken farklıdır. Eşleşme sırasında birbiriyle eşleşebilir, fakat temelde birbiri üzerinde hiçbir etkisi yoktur.

**5.1.2. Veri Nesneleri Olan Sabitler**

Sabitler karakter, sayı veya atom biçiminde olabilirler.

**5.1.3. Karakterler**

Karakterler char kelimesi ile gösterilir ve 0-9, A-Z ve a-z, ASCII 127 karakter tablosundaki değerleri alabilirler. Fakat ASCII 32 (boşluk) ve daha küçük karakterler kontrol amacıyla kullanılırlar.

Tek karakterlik bir sabit şöyle yazılır:

‘a’ ‘3’ ‘\*’ ‘{’ ‘W’ ‘A’ ‘\\\\’=\\ ‘\\’’=’ ‘\\225’=β (ASCII 225)

Bunların dışında başka fonksiyonları olan karakterler de vardır.

‘\\n’ Yeni satıra geçiş komutu

‘\\r’ Satır sonu

‘\\t’ Yatay sekme (tab)

**5.1.4. Sayılar**

Sayılar tamsayı ve reel olabilirler. Reel sayılar 10-308-10+308arasında değişirler.

Örnek:

Tamsayılar Reel Sayılar

10 3.

-77 34.96

32034 -32769

-10 4\*10+27

**5.1.5. Atomlar**

Bir atom symbol veya string olabilir. İkisi arasındaki fark genelde Prolog’un çalıştırıldığı sisteme bağlıdır.

Prolog string ve symbol tipleri arasında otomatik dönüştürme yapabilir. Dolayısıyla symbol ve string tipindeki değişkenler birbirinin yerine kullanılabilirler. Fakat programcılıkta yaygın olan adet, çitf tırnak (“) içine alınması gereken sabitleri string, çitf tırnak gerektirmeyen sabitleri de symbol olarak kabul etmektir.

**Symbol:** küçük harfle başlayan ve sadece harf, rakam ve \_ karakterlerini içerir.

**String:** Çift tırnak içine alınabilen ve string sonunu belirleyen 0 (Sıfır) hariç, herhangi bir karakteri içerebilir.

Symbol String

Yemek “Yavuz AYDIN”

Ahmetin\_babasi “ 12. Cadde”

A “a”

PdcProlog “Visual Prolog Development Center”

**5.2. Bileşik Veri Nesneleri ve Fonksiyon Operatörleri**

Bileşik veri nesneleri, birden fazla parçadan oluşan verileri tek bir parçaymış gibi kullanma imkanı tanır. Mesela 16 Mayıs 1998 tarihi gün, ay ve yıl olarak 3 parçadan oluşan bir bilgiyi temsil eder. Bu tür bir bilgiyi tek bir parçaymış gibi kullanmaya imkan tanıyan sabitler vardır.

**Örnek:**

Domains

Islem\_tarihi= date(string, unsigned, unsigned)

şeklindeki bir tanımdan sonra D=date(“Mayıs”, 16, 1998) şeklinde yazılabilir. Burada D bir olgu değil, symbol veya sayı gibi kullanılabilecek bir veridir. Bu tür ifadeler genelde bir fonksiyon operatörü ve takip eden 3 argüman ile başlar. Operatörler herhangi bir hesaplama yapamazlar. Sadece bir tür bileşik veri nesnelerini tanımlar ve argümanların tek veriymiş gibi tutulmasına imkan tanır.

Bileşik veri nesnelerinin argümanları da bileşik olabilir. Örneğin

Dogum\_Gunu

Kisi date

“Ahmet”“SAGMEN” “Mart” 15 1976

şeklinde gösterilen bir tarihi Prolog’da

dogum\_tarihi(kisi(“Ahmet”,“SAGMEN”),date(“Mart”,15,1976)) şeklinde yazılabilir.

Bu örnekte dogum\_tarihi bileşik nesnesinin iki bölümü vardır: kisi(“Ahmet”, “SAGMEN”) ve date(“Mart”, 15, 1976)*. *Buradaki operatörler kisi ve date’dir.

**5.3. Bileşik Nesnelerin Eşleştirilmesi**

Bileşik bir nesne basit bir değişken veya kendisine uyan diğer bir bileşik nesne ile eşleşebilir. Örneğin date(“Nisan”, 18, 1983) şeklindeki bir clause tarih clause’una tam olarak eşleşir. Aynı şekilde date(“Nisan”, 18, 1983) date(Ay, Gun, Yil) cümleciğinde Ay=Nisan, Gun=18, Yil=1983 değerlerine atanır.

**5.4. Bileşik Nesneleri Eşleştirmek İçin ‘=’ Sembolünün Kullanılması**

VIP iki durumda eşleştirme işlemi yapar. İlki bir Goal veya çağrı fonksiyonunun bir cümleciğin baş kısmıyla eşleşmesi durumunda meydana gelir. İkincisi ise ‘=’ işaretinin argümanlar arasında kullanılması durumunda meydana gelir.

Prolog, eşitliğin her iki tarafındaki aynı işaretli nesneleri eşleştirmek için gerekli bağlantıları yapar. Aşağıdaki örnekte, soy isimleri aynı olan iki kişiyi bulup her ikisinin adreslerini eşitleyelim.

DOMAINS

sahis=sahis(isim, adres)

isim=isim(adi, soyadi)

adres=adres(cadde, sehir, ulke)

cadde=cadde(cadde\_no, cadde\_ismi)

sehir, ulke, cadde\_ismi=string

adi, soyadi= string

cadde\_no= integer

GOAL

P1 = sahis(isim(orhan, aydin), adres(cadde(5, "1. Cadde"), "Elazig", "Turkiye")),

P1= sahis(isim(\_, aydin), Adres),

P2= sahis(isim(oktay, aydin), Adres),

write("Birinci Sahis =", P1), nl,

write("İkinci Sahis =", P2), nl.

**5.5. Birden Fazla Nesneyi Tek Nesne Olarak Kullanmak**

Prolog’da yazılmış programlarda bileşik nesneleri tek bir nesne gibi kullanmak kolaydır. Bu da programcılığı oldukça kolaylaştırır. Örneğin

sahiptir(fatih, kitap(“Visual Prolog İle Programlama”, “Prof.Dr. Asaf VAROL”)).

cümlesi ‘Fatihin Prof.Dr. Asaf Varol tarafından yazılan Visual Prolog ile Programlama adlı bir kitabı var’ anlamındadır. Benzer şekilde;

sahip(fatma, sevgili(can)).

cümlesi “Fatma’nın, ismi Can olan bir sevgilisi var” anlamına gelir. kitap(“Visual Prolog İle Programlama”, “Prof.Dr. Asaf VAROL”) ve sevgili(can) cümlelerdeki bileşik nesnelerdir.

Bileşik nesne kullanmanın önemli bir avantajı, birden fazla argümandan oluşan cümleleri sadece bir argüman olarak kullanabilmektir.

**Örnek:**

Basit bir telefon rehberi veritabanı programı

PREDICATES

Adres\_listesi(symbol, symbol, symbol, symbol, integer, integer) /\*(adi, soyadi, telefonu, ay, gun, yil)\*/

clauses

adres\_listesi(davut, yildirim, 3128456, ocak,6, 1978).

adres\_listesi(maksut, hazneci, 3154878, nisan,14, 1969).

adres\_listesi’ndeki 5 argümanı

sahis(Adi, Soyadi), dogum\_tarihi(Ay,Gun,Yil).

şeklinde yazmak mümkündür. Yeni şekliyle program şöyle yazılabilir:

Domains

Adi= sahis(symbol, symbol) /\* (Adi, Soyadı)\*/

Dogum\_tarihi= d\_tarihi(symbol, integer, integer) /\*(Ay, Gün, Yıl)\*/

Telefon\_no= symbol /\* Telefon no\*/

Predicates

adres\_listesi(adi, telefon\_no, d\_tarihi)

clauses

adres\_listesi(sahis(davut, yildirim), 3128456, d\_tarihi(ocak,6, 1978)).

adres\_listesi(sahis(maksut, hazneci), 3154878, d\_tarihi(nisan,14, 1969)).

Şimdi yukarıdaki küçük programa birkaç kural daha ilave edip, doğum tarihleri bugünün tarihi ile uyuşanları bulmaya çalışalım. Programda standart yüklem olan date kullanılarak bugünün tarihi bilgisayardan alınacaktır.

DOMAINS

adi = sahis(symbol,symbol) /\* (Adı, Soyadı) \*/

dogum\_gunu = d\_gunu(symbol,integer,integer) /\* (Ay, Gun, Yıl) \*/

tel\_no = symbol /\* Telefon Numarası \*/

PREDICATES

nondeterm tel\_listesi(adi,symbol,dogum\_gunu)

d\_gunu\_ayini\_bul

ay\_donustur(symbol,integer)

d\_gunu\_ayini\_kontrol\_et(integer,dogum\_gunu)

sahsi\_yaz(adi)

CLAUSES

d\_gunu\_ayini\_bul:-

write("====Bu ay doğanların listesi ======="),nl,

write(" Adı\\t\\t Soyadı\\n"),

write("=============================="),nl,

date(\_, Bu\_ay, \_), /\* Tarihi bilgisayardan oku \*/

tel\_listesi(Sahis, \_, Date),

d\_gunu\_ayini\_kontrol\_et(Bu\_ay, Date),

sahsi\_yaz(Sahis),

fail.

d\_gunu\_ayini\_bul:-

write("\\n\\n Devam etmek için herhangi bir tuşa basın "),nl,

readchar(\_).

sahsi\_yaz(sahis(Adi,Soyadi)):-

write(" ",Adi,"\\t\\t ",Soyadi),nl.

d\_gunu\_ayini\_kontrol\_et(Yeni\_ay,d\_gunu(Ay,\_,\_)):-

ay\_donustur(Ay,Ay1),

Yeni\_ay = Ay1.

tel\_listesi(sahis(paki, turgut), "267 78 41", d\_gunu(ocak, 3, 1965)).

tel\_listesi(sahis(arif, gurel), "338 41 23", d\_gunu(subat, 5, 1972)).

tel\_listesi(sahis(mehmet\_can, hallac), "512 56 53", d\_gunu(mart, 3, 1965)).

tel\_listesi(sahis(cuma, cetiner), "267 22 23", d\_gunu(nisan, 29, 1963)).

tel\_listesi(sahis(omer, akgobek), "355 12 12", d\_gunu(mayis, 12, 1971)).

tel\_listesi(sahis(fatih, dilekoglu), "438 63 42", d\_gunu(haziran, 17, 1970)).

tel\_listesi(sahis(levent, aksun), "567 84 63", d\_gunu(haziran, 20, 1972)).

tel\_listesi(sahis(cengiz, gok), "255 56 53", d\_gunu(temmuz, 16, 1973)).

tel\_listesi(sahis(kasim, yenigun), "132 22 23", d\_gunu(agustos, 10, 1968)).

tel\_listesi(sahis(husamettin, bulut), "412 48 34", d\_gunu(eylul, 25, 1967)).

tel\_listesi(sahis(arif, demir), "315 24 21", d\_gunu(ekim, 20, 1992)).

tel\_listesi(sahis(sezen, demir), "233 13 12", d\_gunu(kasim, 9, 1980)).

tel\_listesi(sahis(nebahat, arslan), "337 22 23", d\_gunu(kasim, 15, 1987)).

tel\_listesi(sahis(leyla, aydin), "145 41 50", d\_gunu(aralik, 24, 1940)).

ay\_donustur(ocak, 1).

ay\_donustur(subat, 2).

ay\_donustur(mart, 3).

ay\_donustur(nisan, 4).

ay\_donustur(mayis, 5).

ay\_donustur(haziran, 6).

ay\_donustur(temmuz, 7).

ay\_donustur(agustos, 8).

ay\_donustur(eylul, 9).

ay\_donustur(ekim, 10).

ay\_donustur(kasim, 11).

ay\_donustur(aralik, 12).

GOAL d\_gunu\_ayini\_bul.

Yukarıdaki program kodu incelendiğinde, bileşik nesnelerin neden faydalı olduğu açıkça görülür. Dogum\_tarihi\_ayi yüklemi, en yoğun kullanılan cümle durumdadır.

Program ilk önce sonuçları bir pencerede görüntüler.

Sonra sonuçların yorumlanacağı bir başlık kısmı görüntülenir.

Daha sonra hazır fonksiyonlardan biri olan date kullanılarak bilgisayarın saatinden bugünkü tarih okunur ve ay belirlenir.

Bundan sonra yapılması gereken tek şey, satırlar halinde sıralanan veritabanından isim, telefon no, doğum tarihi okutmaktır. Burada doğum tarihi sistemden okunan ay ile karşılaştırılıp aynı olanlar bulunur. adres\_listesi(Sahis,\_, Date) çağrısı adı ve soyadını Sahis değişkenine atar ve sahis operatörü Sahis’a atanmış olur. Date değişkeni de ilgili şahsın doğum tarihini alır. Buradaki adres\_listesi bileşik bir değişken olup, bir kişi hakkındaki bütün bilgileri saklar.

Daha sonra aranan kişinin doğum tarihini Date değişkenine atar. Bir sonraki alt hedefte tamsayıyla gösterilen bugünkü ay ve kişinin doğum tarihi dogum\_gununu\_kontrol\_et yüklemine iletilir.

dogum\_gununu\_kontrol\_et yüklemi iki değişkenle birlikte çağrılır. İlk değişken bir tamsayıya, ikincisi ise dogum\_tarihi’ne bağlanır. dogum\_gununu\_kontrol\_et kuralını tanımlayan kuralın baş kısmındaki Bu\_ay Mon değişkenine atanır. İkinci argüman olan Date ise dogum\_tarihi(Ay, \_,\_) cümleciğine atanır. Sadece bugünkü tarihten ay ile ilgilendiğimiz için, gün ve yıl için anonim değişkenler kullanılmıştır.

dogum\_gununu\_kontrol\_et yüklemi ayın sembolik değerini tam sayıya dönüştürür ve bu değeri sistemden okunan ay değeri ile karşılaştırır. Karşılaştırmanın başarılı olması durumunda bir sonraki alt hedefe geçer. Karşılaştırma başarısız olursa geriye iz sürme işlemi başlar.

İşlenmesi gereken bir sonraki alt hedef adini\_yaz’dır. İstenilen bilgi, doğum tarihi bu ay olan kişinin ismi olduğu için, ekrana bu kişinin adı ve soyadı yazılır. Bir sonraki cümle ‘fail’ olduğu için otomatik olarak geriye iz sürme işlemi başlar.

Geriye iz sürme daima en son kullanılan **non-deterministic** yükleme geri gider. Bizim programımızda zaten non-deterministic bir yüklem bulunduğu için işlem hemen adres\_listesi’ne gider. Program burada işleme konmak üzere başka bir isim aramak için veritabanına gider. Eğer veritabanında işleme konacak başka biri kişi yoksa işlemdeki cümle başarısız olur. Prolog, veritabanındaki diğer satırları inceler ve dogum\_gununu\_kontrol\_et kuralını tanımlayan başka bir cümle bulur.

**5.6. Bileşik Nesnelerin Tiplerini Tanımlamak**

Bu bölümde bileşik nesne tiplerinin nasıl tanımlanacağı üzerinde duralım.

sahiptir(ahmet, kitap(“Pascal 7”, “Ömer AKGÖBEK”))

sahiptir(ahmet, at(firtina)).

şeklinde tanımlanan ilişkiler

GOAL sahiptir(ahmet, Ne)

sorgusuyla irdelenirse Ne değişkeni iki ayrı argüman ile eşleşebilir. Bunlardani biri kitap, diğeri ise at’tır. Sahiptir yüklemi artık sahiptir(symbol, symbol) şeklinde tanımlanamaz. İkinci argüman symbol tipindeki nesnelere işaret etmez. Bunun yerine

sahiptir(isim, esyalar)

şeklinde bir yüklem tanımlamak mümkündür. Tipleri tanımlarken

Domains

esyalar= kitap(kitap\_adi, yazar); at(atin\_adi)

kitap\_adi, yazar, atin\_adi = symbol

yazılabilir.

Yukarıdaki ‘;’ işareti ‘veya’ anlamına gelir. Bu durumda iki alternatiften bahsetmek mümkündür. Bir kitap, kitabın adı ve yazarının adıyla, bir ‘at’ ise sadece ismiyle tanımlanabilir. Kitap\_adi, yazar, atin\_adi değişkenlerinin tamamı symbol tipindedir.

Tip tanımlanmasına daha fazla alternatif rahatlıkla ilave edilebilir.

**Örnek**

DOMAINS

esyalar= kitap(kitap\_ismi, yazar); at(atin\_adi); araba; banka\_hesabi(nakit)

kitap\_ismi, yazar, atin\_adi=symbol

nakit = real

isim=symbol

PREDICATES

nondeterm sahiptir(isim, esyalar)

CLAUSES

sahiptir(ahmet, kitap("Pascal 7.0", "Ömer AKGÖBEK")).

sahiptir(ahmet, at(firtina)).

sahiptir(ahmet, araba).

sahiptir(ahmet, banka\_hesabi(1000)).

GOAL sahiptir(Kim, Sahip\_oldugu\_esyalar).

Programı derlenip çalıştırıldığında

Sahip\_oldugu\_esyalar=kitap(“Pascal 7.0”, “Ömer AKGÖBEK”)).

Sahip\_oldugu\_esyalar=at(firtina)).

Sahip\_oldugu\_esyalar=araba

Sahip\_oldugu\_esyalar= banka\_hesabi(1000)).

4 Solutions

cevabı görüntülenir.

**5.7. Tip Tanımlamaları Üzerine Kısa Bir Özet**

Bileşik nesnelerin tip tanımları genel bir şekilde gösterilecek olursa:

Domain= alternatif1(Tip, Tip, ......); alternatif2(Tip, Tip, .....)

Burada alternatif1 ve alternatif2 farklı operatörlerdir. (Tip, Tip, ...) gösterimi standart veya başka yerde ayrıca tanımlanan symbol, integer, real vs. gibi tip isimlerdir.

**Not:**

Alternatifler birbirinden daima ‘;’ ile ayrılırlar.

Her alternatif bir operatör ve bu argümana ait tip tanımlarını içerir.

Eğer operatörde herhangi bir argüman kullanılmazsa, bunu alternatifN veya alternatifN( ) biçiminde yazılabilir.

**5.8. Çoklu-Düzey Bileşik Nesneler**

Prolog’da, birden fazla dereceden oluşan bileşik nesne kullanmak mümkündür. Örneğin

kitap(“Atatürk: Bir Milletin Yeniden Doğuşu”, “Kinross”)

olgusundaki ‘Kinross’ soyismi yerine, yazarın adını ve soyadını ayrıntılı olarak gösteren bir yapı kullanmak mümkündür.

kitap(“Atatürk: Bir Milletin Yeniden Doğuşu”, yazar(“Lord”, “Kinross”))

Daha önceden yapılan tip tanımında

kitap(kitap\_adi, yazar)

yazılıyordu. İkinci argüman olan yazar, operatör durumundadır. Fakat yazar=symbol sadece bir isimi kapsadığından, yetersiz kalır. Bu durumda yazar değişkeninin de bileşik nesne olarak tanımlanması gerekir. Bunu da:

yazar=yazar(isim, soyisim)

şeklinde tanımlamak mümkündür. Şimdi tip tanımlarına geçelim.

Domains

esyalar=kitap(kitap\_adi, yazar); /\*İlk derece\*/

yazar=yazar(adi, soyadi) /\*ikinci derece\*/

kitap\_adi, isim, soyisim=symbol /\*Üçüncü derece\*/

Birden fazla dereceden oluşan bileşik nesneler kullanırken, ağaç biçiminde bir yapı kullanmak büyük kolaylık sağlar.

Kitap

Kitap\_adi yazar

İsim, soyisim

Tip tanımı yapılırken bir anda ağaç yapısının sadece bir derecesi kullanılabilir. Örneğin

kitap=kitap(kitap\_adi, yazar(adi, soyadi))

Şeklindeki tip tanımı yanlıştır.

**5.9. Çoklu-Tipli Argümanlar**

Bir yüklemin farklı tiplerde bilgi verebilmesi için bir operatör tanımının yapılması yapmamız gerekir. Aşağıdaki örnekte sizin\_yasiniz cümleciği yas argümanını kabul edilmektedir. Yas argümanı ise string, real veya integer olabilir.

DomaIns

yas=i(integer); r(real); s(string)

Predicates

siniz\_yasiniz(yas)

CLAUSES

sizin\_yasiniz(i(Yas)):-write(Yas).

sizin\_yasiniz(r(Yas)):-write(Yas).

sizin\_yasiniz(s(Yas)):-write(Yas).

**5.10. Listeler**

Öğretim üyelerinin verdikleri dersleri liste halinde saklamak istediğimizi kabul edelim. Bunun için aşağıdaki kodun yazılması yeterlidir.

PREDICATES

profesor(symbol, symbol,symbol) /\*Adı, soyadı ve verdiği ders\*/

CLAUSES

profesor(asaf, varol, bilgisayar).

profesor(ali, erdogan, betonarme).

profesor(ahmet, aydogan, fizik).

Bu tür bir programda, bütün hocaların isimlerini ve verdikleri dersleri tek tek sıralamak mümkündür. Her hoca için ayrı bir olguyu veritabanına ilave etmek gerekir. Kolay görünen bu işin yüzlerce öğretim üyesi olan bir üniversite için yapıldığında ne kadar zor olduğunu açıktır. Prolog’daki liste bir veya daha fazla değer alabilir ve benzer işlerde büyük kolaylıklar sağlar. Bir listedeki değişkenlerin aldıkları değerleri ‘\[\]’ arasında yazmak gerekir.

DOMAINS

dersler=symbol\*

PREDICATES

profesor(symbol, symbol, dersler)

CLAUSES

profesor(asaf, varol, \[bilgisayar, termodinamik, iklimlendirme\]).

profesor(ali, erdogan, \[betonarme, statik, malzeme\]).

profesor(ahmet, aydogan, (fizik, matematik, kimya\]).

Şeklindeki satırlarda dersler liste tipinde bir değişken olarak tanımlanmıştır. Buradaki ‘\*’ sembolü dersler değişkeninin liste tipinde olacağını gösterir. Aynı biçimde, listenin tamsayılardan oluştuğu bir değişken tipi

Domains

tamsayilar\_listesi=integer\*

şeklinde tanımlanabilir.

**Örnek:**

DOMAINS

notlar=integer\*

PREDICATES

nondeterm sinav\_sonuclari(symbol, symbol, notlar)

CLAUSES

sinav\_sonuclari(orhan, aydin, \[78, 98, 100\]).

sinav\_sonuclari(kasim, yenigun, \[45, 54, 60\]).

sinav\_sonuclari(husamettin, bulut, \[80, 90, 95\]).

sinav\_sonuclari(huseyin, karasu, \[\]).

GOAL sinav\_sonuclari(orhan,\_,Aldigi\_Notlar).

Programı çalıştırıldığında Orhan’ın aldığı notlar görüntülenir.

**6. TEKRARLAMA VE REKÜRSİYON**

Prosedür ve veri yapılarında tekrarlama işlemleri Visual Prolog’da kolay bir şekilde yapılır. Bu bölümde önce tekrarlı işlemler (döngüler ve rekursif prosedürler), daha sonra ise rekursiv veri yapıları incelenecektir.

**6.1. Tekrarlı İşlemler**

Pascal, BASIC veya C gibi konvansiyonel programlama dilleriyle çalışanlar, Prologla çalışmaya başladıklarında FOR, WHILE, REPEAT gibi ifadeleri göremeyince şaşırabilirler. Çünkü Prologda iterasyonu anlatan direkt bir yol yoktur. Prolog sadece iki türlü tekrarlama-geriye dönüş imkanı tanır. Bu işlemlerde bir sorguya birden fazla çözüm bulmak ve bir prosedürün kendisini çağırdığı rekürsiyon işlemine imkan tanır.

**6.2. Geriye İz Sürme**

Bir prosedür, istenilen bir hedef için uygun bir çözüm yerine alternatif başka çözümler aramak için geriye döner. Bunun için geriye henüz denenmemiş bir alternatifi kalan en son alt hedefe gidileceğini, bu noktadan tekrar aşağıya doğru inileceği bilinmektedir. Geriye dönüşü iptal edip tekrarlı işlemler yaptırmak mümkündür.

**Örnek:**

PREDICATES

nondeterm ulke\_adi(symbol)

ulke\_adlarini\_yaz

CLAUSES

ulke\_adi("Türkiye").

ulke\_adi("Kazakistan").

ulke\_adi("Azerbaycan").

ulke\_adi("Amerika").

ulke\_adlarini\_yaz:-

ulke\_adi(Ulke), write(Ulke), nl, fail.

ulke\_adlarini\_yaz.

GOAL ulke\_adi(Ulke).

Yukarıdaki ulke\_adi yüklemi sadece ülke isimlerini sıralar. Dolayısıyla GOAL ulke\_adi(Ulke) şeklindeki bir hedefin birden fazla sonucu vardır ve ulke\_adlarini\_yaz yuklemi bunların hepsini görüntüler.

ulke\_adlarini\_yaz :- ulke\_adi(Ulke), write(Ulke), nl, fail.

satırıyla söylenmek istenen şey şudur: “Bütün ülke isimlerini yazmak için, önce ulke-adi(Ulke) cümlesine cevap bul, bunu yaz, yeni bir satıra geç ve işlemi yeniden başlat.”

‘fail’ komutunun programa yüklediği görev şöyle özetlenebilir: “GOAL cümlesine uygun bir çözüm bulunduğunda, geriye dönüş yap ve başka alternatiflere bak”.

‘fail’ yerine, sonucu daima yanlış olan ve bu yüzden geriye dönüşü zorlayan başka bir alt hedef kullanmak mümkündür. Örneğin, 10=5+6 satırı her zaman yanlış olacağı için, Prolog başka alternatifler bulmak için daima geriye dönüş yapar.

Örneğimizde ilk önce Ulke=Türkiye olur ve sonuç ekrana yazılır. ‘fail’ komutuna sıra geldiğinde program, bir alt hedefe geri döner. Fakat nl veya write(Ulke) satırları için kullanılabilecek herhangi bir veri olmadığı için, bilgisayar ulke\_adi(Ulke) ilişkisi için başka çözümler arar.

Ulke\_adi(Ulke) ilişkisi çalıştırıldığında, önceden boş değişken olan Ulke değişkeni ‘Türkiye’ değerini almıştı. Bu yüzden bu ilişkiyi yeniden kullanmadan önce Ulke değişkeni yeniden serbest hale getirilir. Daha sonra Ulke değişkeninin alabileceği başka bir olgu aranır. İkinci oluguda bu sağlanır ve ulke\_adi yüklemindeki Ulke değişkeni ‘Kazakistan’ değerini alır. Bu işlem böylece devam eder ve sonuçta şu satırlar görüntülenir.

Türkiye

Kazakistan

Azerbaycan

Amerika

4 Solutions

Eğer ulke\_adlarini\_yaz yüklemi ‘fail’ komutundan sonra yazılmamış olsaydı, cevap yine aynı olurdu fakat ‘yes’ yerine ‘no’ satırı görüntülenirdi.

**6.3. Önceki ve Sonraki Eylemler**

Bir hedef için gerekli olan bütün çözümleri sağlayan bir program, çözüm yapmadan ve yaptıktan sonra başka şeyler de yapabilir. Örneğin

Yaşanacak güzel yerler

Ulke\_adi(Ulke) yükleminin bütün sonuçlarını yaz.

Başka yerler de olabilir...

Şeklinde bir mesaj yazarak bitirebilir.

Ulke\_adlarini\_yaz cümlesin ulke\_adi(Ulke) yükleminin bütün sonuçlarını içerir ve sonunda bir bitiş mesajı yazar.

Örnekte geçen ilk ulke\_adlarini\_yaz cümlesi yukarıdaki adımlardan ikincisi içindir ve bütün çözümleri yazar. İkinci cümlesi ise üçüncü adıma tekabül eder ve sadece hedef cümlesini başarılı bir şekilde bitirmek içindir. Çünkü ilk cümle daima yanlıştır.

Programı başka şekilde yazmak gerekirse:

PREDICATES

nondeterm ulke\_adi(symbol)

ulke\_adlarini\_yaz

CLAUSES

ulke\_adi("Türkiye").

ulke\_adi("Kazakistan").

ulke\_adi("Azerbaycan").

ulke\_adi("Amerika").

ulke\_adlarini\_yaz:-

write("Yaşanacak bazı yerlerin listesi.."), nl, fail.

ulke\_adlarini\_yaz :-

ulke\_adi(Ulke), write(Ulke), nl, fail.

ulke\_adlarini\_yaz:-

write("Başka güzel yerler de vardır..."), nl.

GOAL ulke\_adlarini\_yaz.

İlk cümledeki ‘fail’ komutu çok önemlidir. Çünkü bu komut ilk cümle çalıştırıldıktan sonra programın ikinci cümleye geçişini sağlar. Buradaki write ve nl komutlarının başka bir iş yapmaması çok önemlidir. Son ‘fail’ komutundan sonra programın ikinci cümleciğe geçişi sağlanmalıdır.

**6.4. Döngülü Geriye Dönüşün Uygulanması**

Geriye dönüş işlemi bir hedefin bütün çözümlerinin bulunması açısından son derece önemlidir. Birden fazla çözüm sunamayan hedefler için yine de geriye dönüş işlemi yapılabilir. Bu da tekrarlama işlemini yapar. Örneğin:

tekrar.

tekrar:-tekrar.

gibi iki cümlecik sonsuz sayıda çözüm olduğunu göstermektedir.

Örnek:

PREDICATES

nondeterm tekrar

nondeterm karakteri\_ekrana\_yaz

CLAUSES

tekrar.

tekrar:-tekrar.

karakteri\_ekrana\_yaz:-

tekrar, readchar(Harf), /\*Klavyeden girilen harfi oku ve C'ye ata\*/

write(Harf),

Harf='\\r', !. /\* Satır sonu tuşuna (Enter/Return) basılmadıysa devam et\*/

GOAL karakteri\_ekrana\_yaz, nl.Yukarıdaki örnekte tekrar işleminin nasıl yapılacağını görülebilir. Karakteri\_ekrana\_yaz:-... kuralı, ‘Enter/Return’ basılmadığı müddetçe, klavyeden girilen kararterleri kabul edip ekranda gösteren bir prosedür tanımlamaktadır.

Karakteri\_ekrana\_yaz kuralının çalışma mekanizması şöyle sıralanabilir:

tekrar’ı çalıştır. (Hiçbir şey yapmaz)

bir karakter oku (Harf)

Harf karakterini yaz

Harf’in satır sonu karakteri olup olmadığını kontrol et.

Eğer satır sonu elemanı ise, işlemi bitir, değilse, geriye iz sürme işlemini yap ve alternatif ara. Buradaki write ve readchar kurallarının hiçbiri alternatif sağlayamaz. Dolayısıyla geriye dönüş hemen tekrar kuralına gider, bunun ise alternatif sunması tabiidir.

İşlem devam eder. Bir karakter oku, onu ekrana yaz, satır sonu elemanı olup olmadığını kontrol et.

Harf’e değer atayan readchar(Harf) yükleminin öncesine geriye dönüş yapıldığı anda, Harf değişkeni serbest hale gelir. Değişken değerinin kaybolması geriye dönüş işlemi sayesinde alternatif çözümler elde etmek için çok önemlidir. Fakat geriye dönüş işlemi başka bir iş için kullanılamaz. Çünkü geriye dönüş işlemi alternatif ararken, işlemleri birçok kez tekrar edebilir. Fakat bu tekrarlar sırasında bir tekrardan diğerine geçişte hiçbir şey hatırlayamaz. Daha önce de söylediğimiz gibi, işlemlerden sonra değer ataması yapılan değişkenlerin tamamı, geriye dönüş işlemi sırasında bütün bu değerleri kaybederler. Böyle bir döngüde sayaç gibi bir şey kullanıp toplam, kayıt sayısı vs. gibi bir değeri tutmanın kolay bir yolu yoktur.

**6.5. Rekursif Prosedürler**

Tekrarlama işlemin yapmanın diğer bir yolu da rekursiyondur. **Kendisini çağırabilen prosedüre rekursiv prosedür diyoruz**. Rekursiv prosedürler çalışırken yaptıkları işlerin sayısını, toplamını veya işlemlerin ara sonuçlarını saklayabilir ve bunları bir döngüden diğerine rahatlıkla aktarabilirler.

**Örnek:**

N sayısının faktoriyelini hesaplamak için

1. Eğer N=1 ise, faktoriyel=1

2. Diğer durumlarda N-1’in faktoriyelini bul ve bunu N ile çarp

şeklindeki emirleri anlayıp uygulayan bir program yazalım. Örneğin 3 sayısının faktöriyelini bulmak için 2’nin faktöriyelini, 2’nin faktöriyelini bulmak için de 1’in faktöriyelini bulmamız gerekir. 1’in faktöryeli zaten bilindiğinden yapılması gereken tek şey 2 ve 1’in faktöriyellerini N sayısı olan 3 ile çarpmaktır. Görüldüğü gibi işlemler burada sonsuza kadar gitmemektedir. Şimdi bunları Prolog ile ifade etmeye çalışalım:

PREDICATES

faktoriyel(unsigned, real)

CLAUSES

faktoriyel (1, 1):-!.

faktoriyel (X, Faktoriyel\_X):-

Y=X-1,

faktoriyel(Y, Faktoriyal\_Y),

Faktoriyel\_X=X\*Faktoriyal\_Y.

GOAL X=6, faktoriyel(X, Faktoriyel).

Programı 6 sayısının faktöriyelini bulur.

Burada ilginç bir durum vardır. Bilgisayar faktöriyel işleminin yarısında iken nasıl olur da faktöriyeli hesaplar? Faktöriyel kuralını X=6 olacak şekilde çağırılırsa, faktöriyel kendini X=5 için çağırılacaktır. Bu durumda X değeri 6 mı olacak 5 mi?

**Cevap şudur:** Bilgisayar faktöriyel prosedürünün bir kopyasını oluşturur ve bu kopyayı çağır. Kopyanın kendini faktoriyel prosedürünün aynısıymış gibi çalışır. Sadece argümanların ve değişkenlerin kopyalarına ihtiyaç duyulur.

Bu bilgi yığın olarak hafızada saklanır ve bir kural çağrıldığında her seferinde yeniden oluşturulur. Kural non-deterministic değil ise sona erdiği zaman bellek yığını sıfırlanır.

**6.5.1. Rekursiyonun Avantajları**

Başka türlü güvenli bir şekilde ifade edilemeyen algoritmaları daha açık bir şekilde ifade edebilir.

Mantıksal olarak iterasyondan çok daha basittir.

Listeleri işlemede çok yaygın olarak kullanılır.

Rekursiyon işlemi özellikle problem içerisinde dallanmaların mevcut olduğu, yani bir problemin çözümünün bir alt probleme bağlı olduğu durumlarda çok faydalıdır.

**6.5.2. Sondan Rekursiyon Optimizasyonu**

Rekursiyon işleminin en önemli dezavantajı, belleği fazlaca kullanmasıdır. Bir prosedür başka bir alt prosedürü çağırdığında, çağrıyı yapan prosedürün çağrıyı yaptığı anki çalışma durumu mutlaka kaydedilmelidir. Böylece çağrılan prosedürün yapması gereken işlem bittiği zaman, çağrıyı yapan prosedür kaldığı yerden işleme devam edebilir. Bunun dezavantajı şudur: Örneğin bir prosedür kendisini 100 defa çağırırsa, her seferki durum kaydedileceği için tam olarak 100 değişik durum hafızaya alınmış olur. Hafızaya alınan her duruma stack frame (yığın alanı) denir. 16 bitlik PC DOS sisteminde bu alan 64K ile sınırlı olup, ancak 3000-4000 yığın alacak kapasitedir. 32 Bit’lik sistemlerde teorik olarak bu alan GB düzeyine kadar çıkabilir, fakat bu kez de başka engeller ortaya çıkar. Yığın alanın azaltmak için ne yapılabilir?

Bir prosedürün, başka bir prosedürü kendisinin en son adımı olarak çağırdığını düşünelim. Çağrılan prosedür görevini yaptıktan sonra, çağrıyı yapan prosedürün yapması gereken başka şey kalmaz. Çağrıyı yapan prosedürün kendisin çalışma anını kaydetmesi gerekmez, çünkü o andaki bilgi artık gereksizdir. Çağrılan prosedür biter bitmez, program akışı normal biçimde devam eder.

Bu durum daha açık olarak aşağıdaki şekilde ifade edilebilir. A prosedürünün B prosedürünü, B prosedürünün ise C prosedürünü son adım olarak çağırdığını düşünelim. B prosedürü C’yi çağırdığında, B’nin başka bir şey yapması gerekmez. Yani C’nin o anki çalışma durumunu B olarak kaydetmek yerine, B’nin kaydedilen eski durumun C’ya aktarmak, depolanan bilgi içinde uygun değişiklik yapmak mümkündür. C bittiği zaman, doğrudan A prosedürü tarafından çağrılmış gibi olacaktır.

B prosedürünün C’yi çağırmak yerine, kendisini işlemin en son adımı olarak çağırdığını düşünelim. B prosedürü yine B’yi çağırdığı zaman, çağrıyı yapan B’nin yığın bilgisi, çağrılan B’nin yığın bilgisi ile yer değiştirilmelidir. Bu ise çok basit bir işlemden yani argümanların yeni değerleri almasından ibarettir. Daha sonra işlem, prosedürün baş kısmına gider. Prosedürel olarak bu olay bir döngüdeki kontrol değerlerinin yenilenmesine benzer.

Bu işlemlere **sondan rekursiyon optimizasyonu** veya **son-çağrı optimizasyonu** adı verilmektedir.

**6.5.3. Sondan Rekursiyonun Kullanımı**

Prologda bir prosedürün başka bir prosedürü ‘kendisinin en son adımı olarak çağırmasının’ ne anlama geldi konusu incelenecektir.

Çağrı, cümlenin en son alt hedefidir.

Bu cümlenin ilk kısımlarında geriye dönüş noktaları yoktur.

Aşağıdaki örnek bu iki şartı sağlamaktadır:

sayac(Sayi):-

write(Sayi), nl,

yeni\_sayi=Sayi+1,

sayac(Yeni\_sayi).

İşte bu prosedür sondan rekursif bir prosedürdür ve hafızada yeni bir yığına neden olmaksızın kendisini çağırır. Dolayısıyla hafızayı tüketmez. Bu programa GOAL sayac(0) değeri verilse, 0 ile başlayan tam sayılar yazılmaya başlanır ve işlem bitmez.

Örnek:

PREDICATES

sayac(ulong)

CLAUSES

sayac(Sayi):-

write('\\r',Sayi),

Yeni\_sayi=Sayi+1,

sayac(Yeni\_sayi).

GOAL nl, sayac(0).

Bu programa GOAL sayac(0) ile çalıştırılırsa, 0’dan başlamak üzere tam sayılar yazılmaya başlanır ve işlem bitmez.

**6.5.3. Sondan Rekursiyonu Engelleme**

Eğer rekursiv çağrı en son adım değilse, prosedür sondan rekursiv değildir. Örneğin;

PREDICATES

rakam\_yaz(ulong)

CLAUSES

rakam\_yaz(Sayi):-

write('\\r', Sayi),

Yeni\_sayi=Sayi+1,

rakam\_yaz(Yeni\_sayi), nl.

Goal nl, rakam\_yaz(0).

Rakam\_say prosedürü kendisini çağırdında, kontrolün yeniden rakam\_say(Sayi) dönmesi için hafızada bir yığın kaydedilir. Çünkü son alt hedef ‘nl’dir ve bunun işleme girmesi gerekir. Dolayısıyla döngü bir süre sonra hata mesajı vererek durur.

2. Sondan rekursiyonu engellemenin bir diğer yolu da rekursiyonun yapıldığı anda, geriye henüz denenmemiş bir alternatifin kalmasıdır. Bu durumda prosedürün son durumunun kaydedilmesi gerekir. Çünkü rekürsiv çağrının başarısız olması durumunda çağrıyı yapan prosedürün geriye gidip denenmemiş bir alternatifi deneyebilmesi gerekir.

Örnek:

Clauses

rakam\_yaz(Sayi):-

write('\\r', Sayi),

Yeni\_sayi=Sayi+1,

rakam\_yaz(Yeni\_sayi).

rakam\_yaz(Sayi):-

Sayi<0, write(“Sayi sıfırdan küçüktür.”).

GOAL rakam\_yaz(0).

Burada rakam\_yaz cümlesi, ikinci cümle denenmeden önce kendisini çağırır. Program yine bir süre sonra hafıza tükenmesinden dolayı durur.

Denenmemiş alternatifin rekursiv prosedürün kendisi için ayrı bir cümle olması gerekmez. Rekürsiv prosedürün çağırdığı başka bir cümlede bir alternatif de olabilir. Örnek:

rakam\_yaz(Sayi):-

write('\\r', Sayi),

Yeni\_sayi=Sayi+1,

Kontrol\_et(Yeni\_sayi).

rakam\_yaz(Yeni\_sayi).

Kontrol\_et (Z):-Z>=0.

Kontrol\_et (Z):- Z<0.

Sayi değişkeninin değeri normalde pozitiftir. Bu durumda rakam\_yaz her ne zaman kendisini çağırsa, kontrol\_et yükleminin ilki doğrulanır, fakat ikinci kontrol\_et yüklemin henüz doğrulanmamış durumdadır. Bu yüzden rakam\_yaz yüklemi, geriye dönüş işlemi sırasında kontrol etmek üzere yığın bölgesine bir kopya almak zorundadır.

PREDICATES

yanlis\_sayac1(long)

yanlis\_sayac2(long)

yanlis\_sayac3(long)

kontrol\_et(long)

CLAUSES

/\* Rakam\_yaz: Rekursiv çağrı son adım değildir.\*/

yanlis\_sayac1(Sayi):-

write ('\\r', Sayi),

Yeni\_sayi=Sayi+1,

yanlis\_sayac1(Yeni\_sayi), nl.

/\* Rakam\_yaz2: Rekursiv çağrı yapıldığı anda henüz denenmemiş bir clause var.\*/

yanlis\_sayac2(Sayi):-

write ('\\r', Sayi),

Yeni\_sayi=Sayi+1,

yanlis\_sayac2(Yeni\_sayi).

yanlis\_sayac2(Sayi):-

Sayi<0,

write ("Sayı negatiftir.").

/\* Rakam\_yaz3: Rekursiv çağrıdan önce çağrılan yüklemde denenmemiş bir alternatif var.\*/

yanlis\_sayac3(Sayi):-

write ('\\r', Sayi),

Yeni\_sayi=Sayi+1,

kontrol\_et(Yeni\_sayi),

yanlis\_sayac3(Yeni\_sayi).

kontrol\_et(Z):-

Z>=0.

kontrol\_et(Z):-

Z<0.

GOAL yanlis\_sayac1(1458).

**6.6. Rekursiyonda Cut Kullanımı**

Bir prosedürün sondan rekürsiyonlu olup olmadığından kesin olarak emin olunamayacağı düşünülebilir. Rekursiv olan çağrıyı, son cümleciğin en son alt hedefi yaparak, bu problemi çözmek mümkündür. Fakat yine de hedef cümlesinin çağıracağı diğer prosedürler arasında denenmemiş başka bir alternatif olmadığını nasıl garantiye alabiliriz?

Bunu garantiye almak gerekmez, çünkü ‘!’ yani Cut komutunu kullanarak bulunabilecek bütün alternatiflerin önünü kesmek mümkündür. Cut komutunun anlamı şöyleydi. Goal cümleciği ile belirlenen yükleme uygun çözüm ararken, gelinen nokta bizim aradığımız noktadır. Artık öteye gitmeye gerek bulunmamaktadır. Alternatifler de ortadan kalktığı için, artık hafızada yığın oluşturmaya gerek kalmaz.

Yukarıdaki örnekte görülen rakam\_say cümlesini, şöyle düzeltmek mümkündür (İşlemdeki ismini değiştirelim):

Cut\_sayaci3(Sayi):-

Write (‘\\r’, Sayi),

Yeni\_sayi=sayi+1,

Kontrol\_et(Yeni\_sayi), !, cut\_sayaci3(Yeni\_sayi).

Cut komutu yanlis\_sayac2 cümleciğinde aynı şekilde etkili olur. Çünkü testi negatife düşürüp ikinci cümlecikten birinciye taşır.

Cut\_sayaci2(Sayi):-

Sayi>=0, !,

Write (‘\\r’, Sayi),

Yeni\_sayi=Sayi+1,

cut\_sayaci2(Yeni\_sayi).

Cut\_sayaci2(Sayi):- write (“Sayi negatiftir.”).

Cut komutunu non-deterministic olan, yani birden fazla çözüm sağlayan yüklemlerle çalışırken, alınan bilginin yeterli olduğuna inanıldığı anda rahatlıkla kullanılabilir.

Aynı şey yanlis\_sayac3 için de geçerlidir. Kontrol\_et yüklemi işaretine bağlı olarak Sayi üzerinde biraz daha işlem yapılmasını gerektiren bir durumu göstermektedir. Fakat kontrol\_et kodu non-deterministic olduğu için Cut komutu iyi bir çözümdür. Kontrol\_et yüklemi şöyle yazılabilir:

Kontrol\_et(Z):- Z>=0, !, /\* Z’yi kullanarak işlem yapmak\*/

Kontrol\_et(Z):-......

Cut komutu kullanıldığı zaman bilgisayar denenmemiş bir alternatifin kalmadığına karar verir ve bu yüzden de yığın oluşturma yoluna gitmez. Aşağıdaki programda yanlis\_sayac2 ve yanlis\_sayac3’ün düzeltilmiş hali vardır.

PREDICATES

cut\_sayaci2(long)

cut\_sayaci3(long)

nondeterm kontrol\_et(long)

CLAUSES

/\* Rekursiv çağrı yapıldığı anda henüz denenmemiş bir seçenek var\*/

cut\_sayaci2(Sayi):-

Sayi>=0, !,

write('\\r', Sayi),

Yeni\_sayi=Sayi+1,

cut\_sayaci2(Yeni\_sayi).

cut\_sayaci2(\_):-

write("Sayi negatiftir.").

/\* Rekursiv çağrıdan önceki cümlecikte henüz denenmemiş bir seçenek var\*/

cut\_sayaci3(Sayi):- write('\\r', Sayi),

Yeni\_sayi=Sayi+1,

kontrol\_et(Yeni\_sayi), !, cut\_sayaci3(Yeni\_sayi).

kontrol\_et(Z):-Z>=0.

kontrol\_et(Z):-Z<0.

GOAL cut\_sayaci3(214).

**6.7. Argümanların Döngü Değişkeni Olarak Kullanımı**

Rukursiyon bölümünde verilen bir sayının faktöriyelini hesaplayan bir program geliştirilmişti. Bu durum Pascal’da şöyle ifade edilebilir:

P:=1;

For I:=1 to N do P:= P\*I;

FactN:=P;

N, faktöriyeli hesaplancak olan sayı, FactN, N sayısının faktöriyeli, I değeri 1’den N’e kadar değişen döngü değişkeni ve P ise ara sayıların değerlerinin toplandığı değişkendir.

Bu programı Prolog’a aktarırken yapılması gereken ilk şey, for komutu için daha basit bir döngü kurmak ve her adımda I değişkenine ne olduğunu daha açık şekilde göstermektir. Program while ile, aşağıdaki biçimde yazılır.

P:=1; /\* P ve I değişkenlerine ilk değeri ata.\*/

I:=1;

While I<= N do /\* Döngü kontrolü\*/

Begin

P:=P\*I; /\*P ve I değişkenlerine yeni değerleri ata\*/

I:=I+1;

End;

FactN:=P; /\* Sayının Faktöriyelini Yaz..\*/

Aynı program Prolog ile aşağıdaki gibi yazılır.

PREDICATES

faktoriyel(unsigned, real)

carpanlarin\_faktoriyeli(unsigned, long, unsigned, long)

CLAUSES

faktoriyel(Sayi, Sayinin\_Faktoriyeli):-

carpanlarin\_faktoriyeli(Sayi, Sayinin\_Faktoriyeli, 1, 1).

carpanlarin\_faktoriyeli(Sayi, Sayinin\_Faktoriyeli, I,P):-

I<=Sayi, !,

Yeni\_P=P\*I,

Yeni\_I=I+1,

carpanlarin\_faktoriyeli(Sayi, Sayinin\_Faktoriyeli, Yeni\_I, Yeni\_P).

carpanlarin\_faktoriyeli(Sayi, Sayinin\_Faktoriyeli, I, P):-

I>Sayi,

Sayinin\_faktoriyeli=P.

GOAL faktoriyel(5, Sayinin\_Faktoriyeli).

Programın ayrıntıları aşağıda verilmiştir.

Faktoriyel cümleciğinin Sayi ve Sayinin\_Faktoriyeli olmak üzere iki değişkeni vardır. Bunlardan sayı, faktöriyeli bulunacak sayı, diğeri ise bu sayının faktöriyelidir. Rekursiyon işlemi aslında carpanlarin\_faktoriyeli(Sayi, Sayinin\_Faktoriyeli, I, P) cümlesinden meydana gelir. Bu cümledeki 4 değişkenin bir adımdan diğerine aktarılması zorunludur. Bu yüzden faktoriyel sadece carpanlarin\_faktoriyeli yüklemini harekete geçirir ve sayı, sayının faktöriyeli, I ve P’nin ilk değerlerini buraya aktarır. Böylece

faktoriyel(Sayi, Sayinin\_Faktoriyeli):-

carpanlarin\_faktoriyeli(Sayi, Sayinin\_Faktoriyeli, 1, 1).

sayesinde I ve P değişkenleri ilk değerlerini almış olurlar. Burada dikkat çeken şey, faktoriyel yükleminin hiçbir değeri olmayan Sayinin\_faktoriyeli değerini carpanlarin\_faktoriyeli yüklemindeki sayinin\_faktoriyeli değişkenine aktarmasıdır. Prologun yaptığı tek şey, iki cümlede bulunan Sayinin\_faktoriyeli değişkenlerini eşleştirmektir. Aynı şey carpanlarin\_faktoriyel’i yüklemindeki sayinin\_faktoriyeli değişkeninin rekursiv çağrı esnasında kendisine atanmasında da olur. Son aşamada ise Sayinin\_faktoriyeli bir değer alacaktır. Bu değeri aldığı zaman daha önceki bütün sayinin\_faktoriyeli değişkeni aynı değeri alır. Gerçekte ise sayinin\_faktoriyeli değişkeninin bir değeri vardır. Çünkü Sayinin\_faktoriyeli değişkeni, ikinci cümledeki carpanlarin\_faktoriyeli cümlesinden önce hiçbir zaman gerçek anlamda kullanılmaz.

Şimdi carpanlarin\_faktoriyeli yüklemine gelelim. Bu yüklem, döngünün devam şartı olan I sayısının Sayi’dan az veya eşit olup olmadığını kontrol eder. Daha sonra Yeni\_I ve Yeni\_P değerleriyle kendisini rekursiv olarak çağırır. Burada Prolog’un başka bir özelliği ortaya çıkmaktadır. Diğer dillerin çoğunda mevcut olan

P=P+1

şeklindeki bir ifade Prolog’da yanlıştır. Bu yüzden Prolog’da bir değişkenin değerini değiştirmek mümkün değildir. Bunun yerine

Yeni\_P=P+1

şeklinde bir ifade kullanmak gerekir. Bu durumda ilk cümlecik

carpanlarin\_faktoriyeli(Sayi, Sayinin\_Faktoriyeli, I,P):-

I<=Sayi, !,

Yeni\_P=P\*I,

Yeni\_I=I+1,

carpanlarin\_faktoriyeli(Sayi, Sayinin\_Faktoriyeli, Yeni\_I, Yeni\_P).

şeklinde yazılabilir. Buradaki Cut komutu, cümlecik yüklemde en sonda olmasa da, son çağrı optimizasyonuna imkan tanır. Zamanla I değişkeninin değeri Sayi değişkeninin değerine geçer. Bu durumda işlem P’nin o anki değerini sayinin\_faktoriyeli ile eşleştirir ve rekursiyonu bitirir. Bu nokta ikinci cümlede, yani birinci cümledeki I<=Sayi testinin yanlış çıktığı zaman meydana gelecektir.

carpanlarin\_faktoriyeli(Sayi, Sayinin\_faktoriyeli, I, P):- I>Sayi, sayinin\_faktoriyeli=P.

haline dönüşür. Sayinin\_faktoriyeli=P ifadesinin ayrı bir satırda olması gerekmez. Çünkü sayinin\_faktoriyeli değişkeninin yerine P değişkenini yazarak değer ataması yapılabilir. Ayrıca I>Sayi testi de gereksizdir, çünkü bunun tersi zaten birinci cümlede denenmiş olmaktadır. Bunun son hali:

carpanlarin\_faktoriyeli(\_, Sayinin\_faktoriyeli,\_, Sayinin\_Faktoriyeli) olur.

PREDICATES

faktoriyel(unsigned,real)

faktoriyel(unsigned,real,unsigned,real)

CLAUSES

faktoriyel(Sayi, Sayinin\_faktoriyeli):-

faktoriyel(Sayi, Sayinin\_faktoriyeli,1,1).

faktoriyel(Sayi, Sayinin\_faktoriyeli, Sayi, Sayinin\_faktoriyeli):-!.

faktoriyel(Sayi, Sayinin\_faktoriyeli,I,P):-

Yeni\_I = I+1,

Yeni\_P = P\*Yeni\_I,

faktoriyel(Sayi, Sayinin\_faktoriyeli, Yeni\_I, Yeni\_P).

GOAL faktoriyel(12, Sayinin\_Faktoriyeli).

**6.8. Rekursiv Veri Yapıları**

Sadece kurallar değil, aynı zamanda veri yapıları da rekursiv olabilir. Prolog bu tür yapıların kullanılmasına imkan tanıyan yaygın kullanılan tek programlama dilidir. Bir veri türü, kendisi gibi yapıları içeren başka yapıların kullanımına izin veriyorsa, bu tür veri tiplerine rekursiv denir. En temel rekursiv veri türü listelerdir. Fakat ilk bakışta rekursiv yapıda oldukları belli olmaz.

Şimdi rekursiv olan bir veri türü tanımlayıp, bunu oldukça hızlı bir sıralama programında kullanılması gösterilecektir. Bu veri türünün yapısı aşağıda ağaç yapısında verilmiştir. Görüldüğü gibi Ali ve Ayşe ile gösterilen her bir dal kendi içinde ayrıca alt dallara ayrılmıştır. Bundan dolayı da bu tür bir yapı rekursiv olarak adlandırılır.

Şekil 6.1. Aile Fertlerinin Şecere Olarak Gösterilmesi

**6.9. Ağaç Biçimindeki Veri Türleri**

Rekursiv veri türleri, ALGOL60 dilinden Pascal dilini çıkaran Niklaus Wirth tarafından popüler hale getirilmiştir. Bu veri tiplerini Pascal’da kullanmamış, fakat faydalarına değinmiştir.

Visual Prolog, otomatik olarak oluşturulup, pointerlar içereren gerçek rekursiv tip tanımlara imkan tanır. Örneğin aşağıdaki biçimde bir ağaç yapısı tanımlamak mümkündür.

Domains

Agac\_yapisi= agac(string, agac\_yapisi, agac\_yapisi)

Bu ifade agac isimli bir operatör tanımlandığını, bunun da biri string, ikisi ayrıca ağac yapısında, toplam üç değişkeninin olduğunu gösterir.

Ağaç yapısındaki hiçbir veri türü sonsuza kadar gidemeyeceği, rekursiyonu da bitirmek mümkün olmadığı için bu ifade tam olarak doğru değildir. Örneğin bazı hücrelerin diğer hücrelerle bağlantıları yoktur. Prolog’da ağaç yapısındaki bir veri yapısında iki tip operatör tanımlanır. Bunlar üç ayrı argümanı olan agac veya hiçbir argümanı olmayan bos operatörleridir.

Domains

Agac\_yapisi= agac(string, agac\_yapisi, agac\_yapisi); bos

Yukarıdaki agac ve bos adındaki yüklemlerin Prolog’da önceden tanımlı bir anlamları yoktur ve programcı bunların yerine istediği başka isimleri kullanabilir. Şimdi Şekil 6.1’de gösterilen tablonun Prolog’da nasıl ifade edilebileceği incelenecektir.

agac("Emine", agac("Ali", agac("Hasan", bos, bos) agac("Fatma", bos, bos))

agac("Ayşe", agac("Fuat", bos, bos) agac("Leyla", bos, bos)))

**6.9.1. Bir Ağaç Yapısında Tarama Yapma**

Ağaç şeklindeki yapılarda yoğun olarak yapılan işlem, ya bütün hücreleri incelemek ve hücreleri bir şekilde işlemek veya belirli bir değeri aramak ve bütün değerleri toplamaktır. Buna bir ağacı taramak adı verilmektedir.

Bunun en temel algoritmalarından biri şudur:

Eğer ağaç boş ise hiçbir şey yapma

Eğer dolu ise, o anki noktayı incele, buradan soldaki alt dala geç ve daha sonra sağdaki alt dalı incele.

Algoritma da tıpkı ağaç yapısı gibi rekursivdir. Soldaki ve sağdaki ağaç yapılarını orijinal ağaç gibi inceler. Prolog bunu iki cümlecik ile ifade eder, biri boş diğeri de dolu ağaç içindir.

incele(bos)

incele(agac(A, B, C)):-

incele(A), incele(B), incele(C).

Aşağıdaki ağaç tarama algoritması **aşağıya-doğru-arama** olarak bilinir. Çünkü Prolog her dalda mümkün olduğu kadar derinlemesine gider, bu dalın sonuna ulaştığı anda geriye döner ve başka bir dalı incelemeye başlar. (Şekil 6.2).

Şekil 6.2. Şekil 6.1’deki ağaç yapısında **Aşağıya-Doğru-Arama*** *metodunun uygulanması.

Prologun yukarıdaki ağacı nasıl tarayacağı yukarıda belirtilmiştir. Aşağıdaki program, ağaç yapısını tarayarak ağacın her elemanını ekranda görüntülenir.

DOMAINS

agac\_yapisi=agac(string, agac\_yapisi, agac\_yapisi); bos\_dal

PREDICATES

agaci\_tara(agac\_yapisi)

CLAUSES

agaci\_tara(bos\_dal).

agaci\_tara(agac(Isim, Sol, Sag)):-

write(Isim, '\\n'),

agaci\_tara(Sol), agaci\_tara(Sag).

GOAL

agaci\_tara(agac("Emine", agac("Ali", agac("Hasan", bos\_dal, bos\_dal),

agac("Fatma", bos\_dal, bos\_dal)), agac("Ayşe", agac("Fuat", bos\_dal, bos\_dal), agac("Leyla", bos\_dal, bos\_dal)))).

Programı yazıp çalıştırılırsa ekranda şunlar görülür.

Emine

Ali

Hasan

Fatma

Ayşe

Fuat

Leyla

yes

**aşağıya-doğru-arama** Prolog’un bir veri tabanını tararken kullandığı yönteme çok benzer. Bu tarama esnasında cümlecikler ağaç şeklinde düzenlenir ve her bir dal ayrı ayrı incelenerek sorgu başarısız oluncaya kadar işleme devam edilir.

**6.10. Bir Ağaç Oluşturmak**

Ağaç biçiminde bir yapı oluşturmanın bir yolu operatörlerden ve argümanlardan oluşan iç içe geçmeli bir yapı yazmaktır. Prolog, hesaplama yaparak elde ettiği değerlerden bir ağaç oluşturabilir. Her bir adımda, argümanların eşleştirilmesiyle boş alt dalın içine boş olmayan bir dal yerleştirilir. Basit verileri kullanarak bir hücreli bir ağaç oluşturmak çok basittir.

agac\_olustur(Sayi, agac(Sayi, bos\_dal, bos\_dal)).

Yukarıdaki satır Prolog için “Eğer Sayi bir sayı ise, agac(Sayi, bos\_dal, bos\_dal) tek hücreli bir ağaç olup veri olarak bu sayıyı içerir” anlamına gelir. Ağaç yapısı oluşturmak da en az bu kadar basittir. Örneğin

sola\_yerlestir(Sayi, agac(A, \_, B), agac(A, Sayi, B)).

Prosedürü üç argümandan oluşmuştur. İlk ağacı, ikinci ağacın alt dalı olarak alır ve üçüncü ağacı da sonuç olarak verir. Yapılan tek şey ise, sadece argümanları bire bir eşleştirmektir. Örneğin agac(“Ali”, bos\_dal, bos\_dal) şeklindeki bir yapıyı agac(“Emine”, bos\_dal, bos\_dal) yapısının sol alt dalı olarak yerleştirilmek istenirse, yazılması gereken tek şey şu hedefi çalıştırmaktır.

sola\_yerlestir(agac(“Ali”, bos\_dal, bos\_dal), agac(“Emine”, bos\_dal, bos\_dal), T).

T’nin değeri agac(“Emine”, agac(“Ali”, bos\_dal, bos\_dal), bos\_dal)

olur. Aşağıdaki örnekte bu teknik gösterilmiştir.

DOMAINS

agac\_yapisi = agac(string,agac\_yapisi,agac\_yapisi); bos\_dal()

PREDICATES

agac\_olustur(string,agac\_yapisi)

sola\_yerlestir(agac\_yapisi,agac\_yapisi,agac\_yapisi)

saga\_yerlestir(agac\_yapisi, agac\_yapisi, agac\_yapisi)

basla

CLAUSES

agac\_olustur(A,agac(A,bos\_dal,bos\_dal)).

sola\_yerlestir(X,agac(A,\_,B),agac(A,X,B)).

saga\_yerlestir(X,agac(A,B,\_),agac(A,B,X)).

basla:-

%Tek daldan oluşan ağaçları oluşturalım

agac\_olustur("Hasan",Ha),

agac\_olustur("Fatma",Fa),

agac\_olustur("Ali",Al),

agac\_olustur("Fuat",Fu),

agac\_olustur("Leyla",Le),

agac\_olustur("Ayse",Ay),

agac\_olustur("Emine",Em),

%dalları birleştirelim

sola\_yerlestir(Ha, Al, Al2),

saga\_yerlestir(Fa, Al2, Al3),

sola\_yerlestir(Fu, Ay, Ay2),

saga\_yerlestir(Le, Ay2, Ay3),

sola\_yerlestir(Al3, Em, Em2),

saga\_yerlestir(Ay3, Em2, Em3),

%sonucu göster

write(Em3,'\\n').

GOAL basla.

Program yazılıp çalıştırılınca ekranda şu sonuç görüntülenir.

agac("Emine",agac("Ali",agac("Hasan",bos\_dal,bos\_dal),agac("Fatma",bos\_dal,bos\_dal)),agac("Ayse",agac("Fuat",bos\_dal,bos\_dal),agac("Leyla",bos\_dal,bos\_dal)))

yes

Prolog’da bir değişken herhangi bir değeri aldıktan sonra, artık bu değeri değiştirmenin bir yolu yoktur. Bundan dolayı yukarıdaki örnekte çok sayıda değişken ismi kullanılmıştır. Her yeni değer oluştuğunda, yeni bir değişken tanımlamamız gerekir.

**6.11. Binary Arama Ağacı**

Şimdiye kadar ağaç yapısı, bir ağaç ve elemanları arasındaki ilişkileri göstermek için kullanıldı. Temel amaç bu olsaydı, bunun yerine cümleciklerle ifade edilen olgular kullanmak mümkün olurdu. Oysa ağaç yapısının başka kullanımları da vardır. Ağaç yapılarını kullanarak veri saklamak ve istenildiğinde bu değerleri bulmak çok kolaydır. Bu maksatla oluşturulan ağaç yapısına **arama ağacı*** *adı verilir. Programcı açısından buna liste veya array tipindeki verilere bir alternatif gözüyle bakılabilir. Basit bir ağaç yapısını tararken, öncelikle o an içinde bulunulan hücreye, daha sonra bu hücrenin solu ve sağına, belirli bir değeri ararken, bir ağaç yapısındaki bütün hücrelere bakılması gerekebilir.

İşte binary arama ağacı, herhangi bir hücreye bakarak aranan bir değerin hangi alt dalda bulunacağını tahmin edebilecek şekilde tasarlanır. Bunun için veri parçaları arasında ne tür sıralama olacağının (Örneğin alfabetik veya sayısal sıralama) tanımlanması gerekir. Sol taraftaki alt dalda bulunan veri, o an içinde bulunulan hücredeki veriden önce gelir ve sağ taraftan devam edilir. Aşağıdaki akış şemasını inceleyim.

Şekil 6.3. Binary tarama yapısı

Farklı sırada yerleştirilen aynı isimlerin farklı bir ağaç şeması oluşturur. Ayrıca, şemada 10 isim olmasına rağmen, bunlardan herhangi biri en fazla 5 adımda bulunabilir.

Binary bir tarama yapısında bir hücreye bakarken, geriye kalan hücrelerin yarısını elimine edilir. Bu yüzden tarama çok çabuk ilerler. Bir Binary Tarama Yapısındaki bir maddeyi bulmak için gereken zaman ortalama olarak log2N’dir.

Bir ağaç oluştururken, işe önce boş bir ağaç ile başlanır. Daha sonra diğer parçalar teker teker ilave edilir. Bir madde ilave etmek için gereken prosedür, bir maddeyi aramak için gereken ile tamamen aynıdır.

Eğer içinde bulunulan nokta boş bir ağaç ise, buraya bir madde yerleştir.

Değilse, buraya yerleştirilecek maddeyi, orada saklı olan madde ile karşılaştır. Karşılaştırmanın sonucuna göre, maddeyi sol veya sağ alt dala yerleştir.

Bunun için Prolog’a 3 cümle gerekir. İlk cümle:

yerlestir(Yeni\_Madde, bos, agac(Yeni\_madde, bos, bos):-!.

Bunu konuşma diline “Yeni\_madde’yi bos olan yere yerleştirmenin sonucu agac(Yeni\_madde, bos, bos) olur.” Buradaki Cut komutu, cümlenin uygun olması durumunda başka bir cümlenin **denenmemesi **içindir.

İkinci ve üçüncü cümleler boş yerlere yerleştirmek için kullanılır.

Yerlestir(Yeni\_Madde, bos, agac(Eleman, Sol, Sag), agac(Eleman, Yeni\_Sol, Sag):- Yeni\_Madde<Eleman, !, yerlestir(Eleman, Sol, Yeni\_Sol).

Yerlestir(Yeni\_Madde, bos, agac(Eleman, Sol, Sag), agac(Eleman, Sol, Yeni\_Sag):- yerlestir(Yeni\_Madde, Sag, Yeni\_Sag).

Eğer Yeni\_Madde<Eleman olursa, değer sol alt dala yerleştirilir; aksi takdirde sağ alt dala yerleştirilir.

**6.12. Ağaca Bağlı Sıralama**

Ağaç yapısı oluşturulduktan sonra, bu yapı içerisindeki bütün maddeleri alfabetik olarak elde etmek çok kolaydır. Kullanılacak algoritma aşağıya-doğru-tarama yönteminin değişik bir şeklidir:

Eğer ağaç boş ise hiçbir şey yapma.

Değilse, sol tarafta olan bütün değerleri, daha sonra o anki elemanı, sonra da sağ taraftaki bütün elemanları al.

Prolog diliyle, aşağıdaki şekilde ifade edilir.

Hepsini\_al(bos).

Hepsini\_al(agac(Madde, Sol, Sag)):-

Hepsini\_al(Sol), isleme\_devam\_et(Madde), hepsini\_al(sag).

**Örnek:**

Aşağıdaki programda ekrandan yazılan karakterler, daha sonra alfabetik sırayla görüntülenmektedir. Karakterler kendi aralarında büyük veya küçük olmalarına göre de sıralanmaktadır. Programda kullanılan bazı yüklemler daha sonra incelenecektir.

DOMAINS

karakter\_dizisi = agac(char, karakter\_dizisi, karakter\_dizisi); son

PREDICATES

nondeterm basla(karakter\_dizisi)

eylem(char, karakter\_dizisi, karakter\_dizisi)

agac\_olustur(karakter\_dizisi, karakter\_dizisi)

yerlestir(char, karakter\_dizisi, karakter\_dizisi)

agaci\_yaz(karakter\_dizisi)

nondeterm tekrar

CLAUSES

basla(Agac):-

tekrar,nl,

write("\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*"),nl,

write("Agaci guncelleme : 1 \\n"),

write("Agaci incelemek : 2 \\n"),

write("Programi bitirmek : 7 \\n"),

write("\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*"),nl,

write("Tercihiniz > "),

readchar(X),nl,

eylem(X, Agac, Yeni\_agac),

basla(Yeni\_agac).

eylem('1',Agac,Yeni\_agac):-

write("Istediginiz karakterleri yaziniz, bitirmek için # karakterini giriniz: "),nl,

agac\_olustur(Agac, Yeni\_agac).

eylem('2',Agac,Agac):-

agaci\_yaz(Agac),

write("\\nDevam etmek için bir tusa basiniz.."),

readchar(\_),nl.

eylem('7', \_, son):-

exit.

agac\_olustur(Agac, Yeni\_agac):-

readchar(C),

C<>'#',!,

write(C, " "),

yerlestir(C, Agac, Gecici\_agac),

agac\_olustur(Gecici\_agac, Yeni\_agac).

agac\_olustur(Agac, Agac).

yerlestir(Yeni,son,agac(Yeni,son,son)):-!.

yerlestir(Yeni,agac(Eleman,Sol,Sag),agac(Eleman,Yeni\_sol,Sag)):-

Yeni<Eleman,!,

yerlestir(Yeni,Sol,Yeni\_sol).

yerlestir(Yeni,agac(Eleman,Sol,Sag),agac(Eleman,Sol,Yeni\_sag)):-

yerlestir(Yeni,Sag,Yeni\_sag).

agaci\_yaz(son).

agaci\_yaz(agac(Madde,Sol,Sag)):-

agaci\_yaz(Sol),

write(Madde, " "),

agaci\_yaz(Sag).

tekrar.

tekrar:-tekrar.

GOAL write("Yazilan karakterleri siralama "),nl, basla(son).

**7. LİSTELER VE REKÜRSİYON**

Çok sayıda eleman içeren nesnelerle çalışmak, yani liste işlemek, Prolog’un güçlü yönlerinden biridir. Daha önce kısaca anlatılan bu konu, burada daha ayrıntılı olarak ele alınacaktır. Listelerin ne oldukları, nasıl tanımlandıkları ve uygulama programlarında nasıl kullanılabilecekleri hakkında bazı örnekler çözülecektir. Liste işleme metoduna rekursiv ve prosedürel yönlerden yaklaşırken, Prolog’un çok önemli yüklemlerinden olan **member** ve **append** üzerinde durulacaktır.

Daha sonra verilen dahili bir sorgu için mümkün olan bütün çözümleri bulan ve görüntüleyen findall standart yüklemini incelenecektir.

**7.1. Listeler**

Bir listenin, çok sayıda nesne içeren bir nesne olduğu bilinmektedir. Prolog’daki bir liste, diğer dillerdeki dizilere(array) karşılık gelir. Listelerin dizilerden en önemli farkı, bir diziyi kullanmadan önce bu dizide kaç tane eleman olacağını önceden belirtmenin **gerekmemesidir**. Eğer birleştirilecek nesnelerin sayısı önceden biliniyorsa, bunlar tek bir bileşik veri yapısının argümanı haline getirilebilir.

Elemanları a, b ve c olan bir liste

\[a, b, c\]

şeklinde ifade edilir. Burada a, b ve c birer elemandır ve bu elemanlar bir virgül ile ayrılarak \[.....\] arasında yazılırlar.

**Örnekler:**

\[araba, ev, televizyon\]

\[“Mahmut AKSOY”, “Sefer KAÇAR”, “Mahmut ÜSTÜNDAĞ”\]

**7.2.1. Liste Tanımlanması**

Liste tanımları programların **domains** bölümlerinde yapılır. Tamsayılardan oluşan bir liste

Domains

tamsayilar\_listesi = integer\*

şeklinde tanımlanır. Burada \* tamsayilar\_listesi argümanının tamsayılardan oluşan bir liste olduğunu gösterir. Liste tanımlarken, listeye verilen ismin Prolog’da hiçbir önemi yoktur. Önemli olan şey \* ile tanımlı kelimenin bir listeyi temsil ettiğinin belirtilmesidir.

Bir listenin elemanları herhangi bir şey olabileceği gibi, başka listeler de eleman olarak kullanılabilirler. Dikkat edilmesi gereken şey, bir listedeki elemanların tamamının aynı tipde olması, bu elemanların tipinin de ayrıca tanımlanmasıdır.

**Örnek:**

Domains

Benim\_listem = elemanlarim\*

elemanlarim= integer /\*real, symbol vs. olabilir.\*/

Fakat bir listede bulunan standart tiplerin karışık olarak kullanılması mümkün değildir. Örneğin

benim\_listem = elemanlarim\*

elemanlarim= integer; real; symbol

tanımlaması yanlıştır. Fakat integer, real ve symbol tiplerinden oluşan bir liste tanımlamak için farklı operatörler kullanılabilir:

benim\_listem = elemanlarim\*

elemanlarim= tamsayi(integer); reel\_sayi(real); karakter(symbol)

**7.2.2. Bir Listenin Parçaları: Baş ve Kuyruk**

Bir liste iki kısımdan oluşur. Bunlar listenin ilk elemanının oluşturduğu **baş** ve geriye kalan elemanların oluşturduğu **kuyruk** kısmıdır. Yani bir listenin baş kısmı daima sadece tek eleman, kuyruk kısmı ise daima ayrı bir listeden ibarettir.

**Örnek:**

\[a, b, c\] listesinde a listenin başı; b ve c ise kuyruk kısmıdır.

\[a\] listesinde listenin başı **a** olur. \[\], yani boş bir liste de listenin kuyruk kısmıdır. Boş bir listeyi baş ve kuyruk olarak ayırmak mümkün değildir. Dolayısıyla bir listenin kuyruk kısmının her seferinde ilk elemanı alınırsa, sonuçta boş bir listeye ulaşılır. Bu yüzden listeleri bileşik nesneler gibi ağaç yapısında görmek mümkündür. Örneğin \[a, b, c, d\] listesine bu işlem aşağıdaki gibi uygulanır.

liste

/ \\

a liste

/ \\

b liste

/ \\

c liste

/ \\

d \[ \]

Burada \[a\] ile a birbirinin aynısı değildir. Çünkü **a** tek başına bir eleman iken \[a\] tam bir bileşik yapıdadır. Çünkü \[a\]

liste

/ \\

a \[ \]

şeklinde ifade edilir.

**7.2.3. Listelerin İşlenmesi**

Prologda bir listenin elemanlarını virgüle ayırmak yerine, baş ve kuyruk kısımlarını daha belirgin olarak ifade etmek için sadece baş ve kuyruk kısımları dikey çizgi ile ‘|’ ayrılır.

**Örneğin: **

\[a, b, c\] yerine \[a|\[b, c\]\] veya benzer şekilde devam edersek \[a|\[b|\[c\]\]\] biçimi kullanılabilir. Burada \[c\] listesini de baş ve kuyruk olarak ayırırsak, \[a|\[b|\[c|\[\]\]\]\] olur.

Tablo 7.2. Listelerin baş ve kuyruk halinde gösterilmeleri

| **Liste** | **Baş ** | **Kuyruk** |
| --- | --- | --- |
| \['a', 'b', 'c'\] | 'a' | \['b', 'c'\] |
| \[ 'a' \] | 'a' | \[\] /\* Boş liste\*/ |
| \[ \] | Tanımsız | Tanımsız |
| \[\[1, 2, 3\], \[2, 3, 4\], \[\]\] | \[1, 2, 3\] | \[\[2, 3, 4\], \[\]\] |

Tablo 7.3: Liste eşleştirme örnekleriTC "Table lists**Hata! Yer imi tanımlanmamış.**. list**Hata! Yer imi tanımlanmamış.**: Unification of Lists" \\f table

| **Liste 1** | **Liste 2** | **Değişken eşleştirme** |
| --- | --- | --- |
| \[X, Y, Z\] | \[kedi, eti, yedi\] | X=kedi, Y=eti, Z=yedi |
| \[7\] | \[X \| Y\] | X=7, Y=\[\] |
| \[1, 2, 3, 4\] | \[X, Y \| Z\] | X=1, Y=2, Z=\[3,4\] |
| \[1, 2\] | \[3 \| X\] | Yanlış (Neden?) |

**7.2.4. Listelerin Kullanılması**

Listeler gerçek anlamda rekursiv bileşik veri yapıları olduklarından bunların kullanılmaları için rekursiv algoritmaların kullanılması gerekir. Liste işlemesinin en temel yöntemi, listenin son elemanına ulaşıncaya kadar listenin her elemanını incelemektir. Bu tür işlemde kullanılması gereken algoritmalar genelde iki cümleden oluşurlar. Bir cümle, baş ve kuyruk olarak ikiye bölünebilen listeler için, ikincisi ise boş listeler için kullanılır.

Örneğin aşağıdaki programda bir listenin elemanlarını nasıl görüntüleyeceğimizi görelim:

DOMAINS

benim\_listem = string\*

PREDICATES

benim\_listemi\_yaz(benim\_listem)

CLAUSES

benim\_listemi\_yaz (\[\]). /\*Liste boş ise yapılacak bir şey yok.\*/

benim\_listemi\_yaz (\[Bas|Kuyruk\]):-write(Bas), nl,

benim\_listemi\_yaz (Kuyruk).

GOAL benim\_listemi\_yaz(\["Visual", "Prolog", "4.0"\]).

Bu programdaki benim\_listemi\_yaz (\["Visual", "Prolog", "4.0"\]* *sorgusuyla Bas=”Visual”, Kuyruk=\["Prolog","4.0"\] değerlerini alır ve Visual değeri yazılır. Daha sonra benim\_listemi\_yaz yüklemi rekursiv olduğu için \["Prolog", "4.0"\] kısmı yeniden bölünür. Bu kez Bas=Prolog, Kuyruk=4.0 olur ve Prolog değeri görüntülenir. Rekursiv işlem bir kez daha “4.0” için uygulanır ve bu defa Bas=4.0, Kuyruk=\[\] olur. Kuyruk kısmı boş liste olduğundan sadece 4.0 görüntülenir. Rekursiv çağrı bu kez boş liste için yapılır, fakat listenin Baş ve Kuyruk kısımlarının eşleşebilecekleri değer olmadığından, program akışındaki benim\_listemi\_yaz(\[\]) cümlesi çağrılır ve program bir şey yapmadan normal şekilde durur. benim\_listemi\_yaz (\[\])* *şeklindeki cümle, programın normal bir biçimde durmasını sağlar.

**7.2.5. Liste Elemanlarının Sayılması**

Bir listenin kaç elemandan oluştuğunu nasıl bulabiliriz? Bunun için kullanılması gereken temel mantık şudur.

Liste boş \[\] ise, listedeki toplam eleman sayısı 0’dır.

Bunun dışındaki listelerin eleman sayısı 1+ Kuyruk Uzunluğu ile bulanabilir. Prolog’da karşılığı aşağıda verilmiştir.

DOMAINS

liste=integer\*

PREDICATES

liste\_uzunlugu(liste, integer)

CLAUSES

liste\_uzunlugu(\[\], 0).

liste\_uzunlugu(\[\_|Kuyruk\],Eleman\_sayisi):-liste\_uzunlugu(Kuyruk, Kuyruk\_uzunlugu),

Eleman\_sayisi=Kuyruk\_uzunlugu+1.

GOAL liste\_uzunlugu(\[1, 2, 3\], Eleman\_sayisi).

İlk cümledeki \[\_|Kuyruk\] boş olmayan bütün listelerle eşleşebilir. Bizim için önemli olan kısım listenin kuyruk kısmı olduğu için baş kısmı yerine anonim değişken kullanılmıştır.

GOAL liste\_uzunlugu(\[1, 2, 3\], Eleman\_sayisi).

sorgusu ikinci cümle ile eşleşir ve Kuyruk=\[2, 3\] olur. Daha sonraki adım Kuyruk uzunluğunu hesaplamaktır. Bu yapıldığı zaman Kuyruk=2 olur. Uzunluk=kuyruk\_uzunluğu+1 olduğundan Uzunluk=3 olur.

Liste\_uzunlugu yüklemi kendisini çağırarak \[2, 3\] listesinin uzunluğunu bulur. Bunun için

Cümledeki kuyruk=\[3\] değerini alır.

Kuyruk\_uzunlugu=Eleman\_sayisi değerini alır.

Her rekursiv cümlenin kendisine ait değişken kümesi olduğundan, cümledeki kuyruk\_uzunlugu ve sorgudaki kuyruk\_uzunlugu birbirine karışmadığı unutulmamalıdır.

Bu durumda bütün mesele \[3\] uzunluğunu bulmaktır. Bu 1 olduğu için buna 1 ilave edilirse \[2, 3\] için toplam uzunluk 2 olur. \[3\] listesinin uzunluğu için liste\_uzunlugu yüklemi kendisin tekrar çağırır. Bu kez \[3\] listesinin kuyruk uzunluğu Kuyruk=\[\] olur. Kuyruk uzunluğunu hesaplamak için ise liste\_uzunlugu(\[\], Kuyruk\_uzunlugu) ilk cümle ile eşleşir ve Kuyruk\_uzunlugu=0 olur. Şimdi bilgisayar bu değere, yani 0’a 1 ilave ederek \[3\]’ün uzunluğunu bulur. Buna 1 ilave ederek \[2, 3\]’ün uzunluğunu bulur. Nihayet buna da 1 ilave ederek \[1, 2, 3\] listesinin toplam uzunluğunu bulur.

Şimdi bu işlemlerin tamamını sıralayarak konuyu biraz daha netleştirelim.

Liste\_uzunlugu(\[1, 2, 3\], Eleman\_sayisi1).

Liste\_uzunlugu(\[2, 3\], Eleman\_sayisi2).

Liste\_uzunlugu(\[3\], Eleman\_sayisi3).

Liste\_uzunlugu(\[\], 0).

L3=0+1=1

L2=L3+1=2

L1=L2+1=3

**7.2. Sondan Rekursiyona Yeniden Bakış**

Rekursiv bir çağrı, cümledeki son adım olamayacağı için liste\_uzunlugu’nun sondan rekursiv olamayacağı bellidir. Bunu sondan rekursiv yapmanın yolu vardır.

Burada problem olan şey, kuyruk uzunluğu bilinmeden bir listenin toplam uzunluğunun hesaplanamayışıdır. Yani bu probleme bir çözüm bulunabilirse, liste\_uzunlugu yüklemini sondan rekursiv yapmak mümkündür. Bunun için liste\_uzunlugu yükleminin üç argümanının olması gerekir.

Birincisi, her seferinde kırpılarak sonunda boş bir liste elde edilecek listenin kendisi.

Bir diğeri, liste uzunluğunu saklayacak boş bir değişken

Sonuncusu ise 0 ile başlayan ve her seferinde değerinin 1 arttığı bir sayaç değişken.

Geriye sadece boş olan liste kaldığı zaman bu sayaç hiçbir değişkene atanmamış olan sonucu alır.

DOMAINS

liste=integer\*

PREDICATES

liste\_uzunlugu(liste, integer, integer)

CLAUSES

liste\_uzunlugu(\[\], Sonuc, Sonuc).

liste\_uzunlugu(\[\_|Kuyruk\], Sonuc, Sayac):-

Yeni\_sayac=Sayac+1,

liste\_uzunlugu(Kuyruk, Sonuc, Yeni\_Sayac).

GOAL liste\_uzunlugu(\[1, 2, 3\], Uzunluk, 0), write ("Uzunluk =", Uzunluk), nl.

Verilen bir listedeki elemanlar üzerinde işlem yaptıktan sonra bu elemanların yerine hesaplanan elemanlardan oluşan başka bir liste oluşturmak mümkündür. Aşağıdaki örnekte listenin her elemanını 1 ilave ederek yeni bir liste elde edilmiştir.

DOMAINS

liste = integer\*

PREDICATES

yeni\_deger\_ilave\_et(liste, liste)

CLAUSES

yeni\_deger\_ilave\_et(\[\], \[\]). /\* İlk şart\*/

yeni\_deger\_ilave\_et(\[Bas|Kuyruk\],\[Bas1|Kuyruk1\]):- /\* Bas ve Kuyruk ayrılması\*/

Bas1=Bas+1, /\* Listenin ilk elemanına 1 ilave et\*/

yeni\_deger\_ilave\_et(Kuyruk, Kuyruk1). /\* elemanı listenin geriye kalanıyla çağır\*/

GOAL yeni\_deger\_ilave\_et(\[1, 2, 3\], Yeni\_Liste).

Yukarıda yapılan işlemler, sözel olarak aşağadaki şekilde yazılır.

Boş bir listenin bütün elemanlarına 1 ilave etmek için sadece başka bir boş liste oluştur.

Boş olmayan herhangi bir listenin bütün elemanlarına 1 ilave etmek için, listenin baş kısmına 1 ilave et ve ilave edilen bu değeri yeni listenin başı olarak al. Daha sonra kuyruk kısmının bütün elemanlarına 1 ilave et ve yeni değerleri de yeni listenin kuyruk kısmı olarak al. Sonucu Yeni\_liste olarak ekranda görüntüle.

Verilen liste \[1, 2, 3\] olduğu için:

Önce Baş ve Kuyruk kısımları ayrılır ve sırasıyla \[1\] ve \[2, 3\] olurlar.

Sonuç listenin baş ve kuyruk kısımlarına Bas1 ve Kuyruk1 değerlerini ata. Burada Bas1 ve Kuyruk1’in henüz değer almadığına dikkat edilmelidir.

Bas kısmına 1 ilave et ve Bas1’i elde et.

Rekursiv olarak Kuyruk kısmındaki bütün elemanlara 1 ilave et ve Kuyruk1’i elde et.

Bu yapıldığı zaman Bas1 ve Kuyruk1 kendiliğinden sonuç listesinin Bas ve Kuyruk kısmı olur. Bunları birleştirmek için ayrı bir operasyon gerekmez. Dolayısıyla rekursiv çağrı gerçekten de prosedürün son adımı durumundadır.

**Örnek: **

Bir listedeki sayıları tarayıp negatif olanları eleyen program

DOMAINS

liste=integer\*

PREDICATES

negatifleri\_ele(liste, liste)

CLAUSES

negatifleri\_ele(\[\], \[\]).

negatifleri\_ele(\[Bas|Kuyruk\], IslenmisKuyruk):-

Bas<0, !, negatifleri\_ele(Kuyruk, IslenmisKuyruk).

negatifleri\_ele(\[Bas|Kuyruk\], \[Bas|IslenmisKuyruk\]):-

negatifleri\_ele(Kuyruk, IslenmisKuyruk).

GOAL negatifleri\_ele(\[2, -45, 3, 4, -5, -45\], Yeni\_Liste).

Aşağıdaki yüklem, bir listenin her elemanını başka bir listeye iki kez aktarmaktadır.

elemanlari\_ikile(\[\], \[\]).

elemanlari\_ikile(\[Bas|Kuyruk\], \[Bas, Bas|Ikilenmis\_Kuyruk\]):-

elemanlari\_ikile(Kuyruk, İkilenmis\_Kuyruk).

**7.3. Liste Elemanlığı**

Ahmet, Mehmet, Hasan ve Nejla isimlerini eleman olarak içeren bir listede, örneğin Ahmet isminin var olup olmadığını öğrenilmek istensin. Yani isim ve bir isim arasında bir ilişki sorgulansın. Bunun için kullanılan bir yüklem vardır.

uye(isim, isimlistesi). /\*Burada ‘isim’ listede geçen bir isimdir.\*/

DOMAINS

isim\_listesi = isim\*

isim = symbol

PREDICATES

nondeterm uye(isim, isim\_listesi)

CLAUSES

uye(Isim, \[Isim|\_\]).

uye(Isim, \[\_|Kuyruk\]):- uye(Isim, Kuyruk).

GOAL uye(ahmet, \[ mehmet, ahmet, hasan, nejla\]).

Yukarıdaki örnekte önce birinci cümleyi inceleyelim. uye(Isim, \[Isim|\_\]) cümlesindeki Isim değişkeni listenin öncelikle baş kısmında araştırılır. Eğer eşleşme sağlanırsa üyeliğin var olduğu sonucuna varılır ve olumlu sonuç görüntülenir. Listenin kuyruk kısmı bizi ilgilendirmediği için burada anonim değişken kullanılmıştır.

Eğer aradığımız isim listenin baş kısmı ile eşleşmezse bu kez listenin kuyruk kısmını incelemek için ikinci cümle kullanılır.

**7.4. Listeleri Birleştirme**

Aşağıdaki iki cümleyi tekrar inceleyelim. Bu iki cümleye prosedürel ve dekleratif olarak bakmak mümkündür.

uye(Isim, \[Isim|\_\]).

uye(Isim, \[\_|Kuyruk\]):- uye(Isim, Kuyruk).

Bu cümlenin dekleratif olarak anlamı şudur:

Eğer cümlenin baş kısmı Isim değişkenine eşitse, bu durumda Isim, listenin bir elemanıdır. Bu durum doğru değilse, Isım değişkeni kuyruk kısmının üyesi ise Isim listenin bir elemanıdır.

Prosedürel olarak bu iki cümle şöyle yorumlanabilir.

Bir listedeki herhangi bir elemanı bulmak için, listenin baş kısmını; aksi takdirde, bu listenin kuyruk kısmının bir üyesini bulunuz.

Bu iki durumu denemek için uye(2, \[1, 2, 3, 4\]) ve uye\[X, \[1, 2, 3, 4\]) sorgularını kullanınız. İlk sorgu, bir durumun doğru olup olmadığını sorgulamak için kullanılırken, ikinci sorgu listenin bütün üyelerini bulmak için kullanılmaktadır.

**7.5. Rekursiyona Prosedürel Bir Bakış**

Bu kısımda bir listeyi başka bir listeye ekleyen bir yüklem oluşturulacaktır. Ekle yükleminin üç argümanla birlikte tanımlanması gerekir.

Ekle(Liste1, Liste2, Liste3)

Ekle yüklemi Liste1'i Liste2'ye ilave ederek Liste3'ü elde eder. Eğer Liste1 boş ise, bu durumda 1. Listeyi 2. Listeye ilave etmek bir şeyi değiştirmez. Yani:

Ekle(\[\], Liste2, Liste2).

Eğer liste1 boş değilse,

Ekle(\[Bas|Kuyruk1\], Liste2, \[Bas|Kuyruk3\]):-ekle (Kuyruk1, Liste2, Kuyruk3\]).

Liste1 boş değilse, rekursiv olan yüklem her seferinde bir elemanı Liste3'e transfer eder. Liste1 boş olduğunda ilk cümle Liste2'yi liste3'ün sonuna ilave eder.

**Örnek:**

DOMAINS

sayilar=integer\*

PREDICATES

ekle(sayilar, sayilar, sayilar)

CLAUSES

ekle(\[\], Liste, Liste).

ekle(\[Bas|Kuyruk1\], Liste2, \[Bas|Kuyruk3\]):-

ekle (Kuyruk1, Liste2, Kuyruk3).

GOAL ekle (\[1, 3, 5\], \[2, 4, 6\], Yeni\_Liste).

Yukarıdaki programı sadece birleştirilen iki listenin sonucunu almak için değil, aynı zamanda sonuç listesini yazıp ilk iki liste için geçerli bütün alternatifleri bulmak için kullanmak mümkündür. Örneğin GOAL ekle (Birinci\_Liste, Ikinci\_liste, \[2, 4, 5, 6\]). Denendiğinde toplam 5 çözüm bulunur. Ayrıca GOAL ekle (\[3, Ikinci\_eleman\],Liste\_2, \[3, 4, 5, 6\]) şeklindeki bir sorgu ile birinci listenin, örneğin ikinci elemanı ve ikinci listenin tamamını bulmak da mümkündür.

**7.6. Bütün Çözümleri Bir Defada Bulma **

Rekursiyon ve geriye iz sürme işlemlerini karşılaştırırken rekursiyonun daha avantajlı olduğu daha önce belirtilmişti. Bunun nedeni, rekursiyon esnasında argümanlar vasıtasıyla aradaki adımlarda elde edilen verilerin saklanabilmesidir. Öte yandan geriye dönüş işlemi bir sorguyu sağlayan bütün çözümleri bulabilirken, rekursiyon bunu yapamaz.

Bunun için Prolog'un hazır yüklemlerinden olan **findall** yüklemi kullanılır. Findall bir sorguyu kendi argümanlarından biri olarak alır ve bu sorgunun bütün çözümlerini tek bir liste altında toplar. Findall yükleminin toplam 3 argümanı vardır.

İlk değişken, örneğin **Degisken\_Ismi**, yüklemden listeye aktarılacak değişkenin hangisi oldugunu gösterir.

İkinci değişken, örneğin yeni\_yuklem, değerlerin alınacağı yüklemi gösterir.

Üçüncü argüman, örneğin Yeni\_Degisken, geriye dönüş işlemiyle elde edilen değerlerin listesi tutan bir değişkendir. Yeni\_degisken değerlerinin ait olduğu bir tip tanımının kullanıcı tarafından yapılmış olması lazımdır.

Bir gruptaki yaş ortalamasını bulan bir program, aşağıdaki şekilde yazılabilir.

DOMAINS

isim, adres = string

yas = integer

liste = yas\*

PREDICATES

nondeterm kisi(isim, adres, yas)

toplam\_liste(liste, yas, integer)

calistir

CLAUSES

toplam\_liste(\[\], 0, 0).

toplam\_liste(\[Bas|Kuyruk\], Toplam, N):-

toplam\_liste(Kuyruk, S1, N1),

Toplam=Bas+S1, N=1+N1.

kisi("Oktay DUYMAZ", "Cumhuriyet Cad.", 36).

kisi("O.Faruk AKKILIÇ", "Nail Bey Mah. ", 30).

kisi("Hakay TAŞDEMİR", "Firat Cad. No: 17", 28).

calistir:-

findall(Yas, kisi(\_,\_, Yas), L),

toplam\_liste(L, Toplam, N),

Ortalama=Toplam/N,

write("Ortalama = ", Ortalama), nl.

GOAL calistir.

Programdaki findall cümlesi L listesini oluşturarak **kisi** yükleminden elde edilen bütün yaşları buraya aktarır.

**7.7. Bileşik Listeler**

Şimdiye kadar oluşturulan listelerde daima aynı türden olan elemanlar saklanmıştır. Listeler tamsayı, symbol vs.den oluşuyordu. Bir liste içerisinde farklı tipte elemanları bir arada yazmak oldukça faydalı olur. Birden fazla tipte olan elemanları bir arada tutmak için özel tanımlamaların yapılması gerekir. Bu da farklı operatörler tanımlamakla olur.

**Örnek:**

Domains.

Benim\_listem = 1(liste); i(integer); c(char); s(string)

Liste=benim\_listem\*

\[i(2), i(9), 1(\[s("araba"), s("bilgisayar")\]), s("kalem")\]

Örnek:

DOMAINS

benim\_listem =l(liste); i(integer); c(char); s(string)

liste=benim\_listem\*

PREDICATES

ekle(liste, liste, liste)

CLAUSES

ekle(\[\], L, L).

ekle(\[X|L1\], L2, \[X|L3\]):-

ekle(L1, L2, L3).

GOAL

ekle(\[s(sever), l(\[s(ahmet), s(deniz)\])\], \[s(ahmet), s(ayse)\], Sonuc),

write("Ilk Liste : ", Sonuc, "\\n"),

ekle(\[l(\[s("Bu"), s("bir"), s("listedir.")\]), s(test)\], \[c('c')\],Sonuc2),nl,

write ("İkinci Liste: ", Sonuc2,'\\n').

**8. AKIŞ DENETİMİ**

Bir yüklem içinde değeri bilinen değişkenlere **input** (giriş değişkenleri), bilinmeyenlere ise **output** (çıkış değişkenleri) denir. Bu argümanların, input argümanları ise başlangıç değeri verilerek, output argümanları ise çıktı almak üzere uygun biçimde kullanılmasına **akış biçimi** denir. Örneğin bir argümanın iki değişkenle çağrılması durumunda 4 farklı akış biçiminden söz edilebilir.

(i, i) (i,o) (o,i) (o, o)

Programlar derlendiği zaman yüklemlerin global bir akış analizi yapılır. Ana sorgu ile başlayıp bütün programın değerlendirmesi yapılır. Bu esnada programdaki bütün yüklemlere akış biçimleri atanmış olur.

Akış analizi oldukça basittir. Çünkü program yazarken farkında olmadan aynı şey tarafımazdan da yapılmaktadır.

**Örnek:**

GOAL cursor(R, C), R1=R+1, cursor(R1, C).

Cursor yüklemine yapılan ilk çağrıda R ve C değişkenlerinin hiçbir değeri olmadığı için serbest değişken durumundadırlar. Dolayısıyla akış biçimi cursor(o, o) olur. R1=R+1 ifadesinde R değişkeninin değeri cursor yükleminden geleceği için, R değişkenin bağlı olduğu bellidir. Bu çağrıdan sonra R1 değişkeni değer almış olur. Eğer R değişkeni boş olsaydı, bu durumda bir hata mesajı görüntülenirdi.

Cursor yükleminin son kez çağrılmasında R1 ve C değişkenlerinin ikisi de önceden çağrıldığı için artık giriş değişkenleri olarak işlem görürler. Yani çağrının akış biçimi cursor(i, i) olur.

Burada sadece DOS Metin Modu ortamında çalışan aşağıdaki örnekler irdenelecektir.

Predicates

ozellik\_degistir(Integer, Integer)

Clauses

ozellik\_degistir(Yeni\_ozellik,Eski\_ozellik):-ozellik(Eski\_ozellik), ozellik(Yeni\_ozellik).

GOAL ozellik\_degistir(112, Eski), write("Merhaba"), ozellik(Eski, write(" millet").

GOAL kısmındaki ilk çağrı ozellik\_degistir(i, o) ile yapılır. Burada 112 bilinen, Eski ise bilinmeyen değişkendir. Bu durumda ozellik\_degistir cümlesi Yeni\_ozellik değişkeni ile çağrıldığında bunun değeri belli olduğu için input, Eski\_ozellik'in değeri belli olmadığı için output olacaktır. Akış denetçisi ilk alt hedef olan ozellik(Eski\_ozellik) cümlesine geldiği zaman ozellik yüklemi ozellik(o) akış biçimi ile çağrılır. Ozellik yükleminin ikinci çağrılışı ozellik(i) şeklinde olacaktır. Ana sorgudaki ozellik yüklemine yapılan çağrı input olacaktır, çünkü ozellik\_degistir yükleminden alınır.

**8.1. Bileşik Akış**

Bir yüklemdeki değişken bileşik bir nesne ise, akış biçimi bileşik bir şekilde olabilir. Şimdi aşağıdaki örnekte olduğu gibi, bir ülke hakkında bilgilerin verildiği bir veritabanı düşünelim. Yeni bilgileri rahatlıkla ilave edebilmek için her bilgiyi kendi tipiyle saklamak istenebilir.

DOMAINS

ulke\_bilgileri=alan(string, ulong); nufus(string, ulong);baskent(string, string)

PREDICATES

nondeterm ulke(ulke\_bilgileri)

CLAUSES

ulke(alan("Türkiye",876000)).

ulke(nufus("Türkiye", 65000000)).

ulke(baskent("Türkiye", "Ankara")).

ulke(alan("Almanya",840000)).

ulke(nufus("Almanya", 50000000)).

ulke(baskent("Almanya", "Bohn")).

GOAL ulke(alan(Ad, Alan)), ulke(nufus(Ad, Nuf)).

Sorguyu aşağıdaki cümlelerle deneyiniz:

ulke (C) (o)

ulke(alan(Ulke\_adi, Alani)) (o,o)

ulke(nufus("Türkiye", Nuf)) (i, o)

ulke(baskent("Türkiye", "Ankara")) (i)

Son örnekteki bütün terimler bilindiği için akış biçim düz metindir.

**8.2. Yüklemlerin Akış Biçimlerini Tanımlama**

Yüklemler için uygun bir akış biçimi tanımlamak bazen daha güvenlidir. Yüklemlerin sadece özel akış biçimleri durumunda geçerli olacağı biliniyorsa, önceden akış biçimi tanımlamak faydalıdır. Çünkü bu durumda akış denetçisi bu yüklemlerden yanlış kullanılanı çok rahatlıkla bulabilir. Tip tanımı yapıldıktan sonra '-' işareti yazarak akış biçimi vermek mümkündür.

PREDICATES

musteri\_bilgi\_listesi(string, string, slist) -(i, o, o)(o, i, o)

**8.3. Akış Analizini Kontrol Etmek**

Analiz mekanizması, standart bir yüklemin yanlış bir akış biçimi ile çağrıldığını tesbit ettiği an hata mesajı verir. Bu hata mesajı, standart yüklemleri çağıran yüklemler tanımladığımız zaman, bunlardan akış biçimi anlamsız olanları tesbit etmede bize yardımcı olur.

**Örnek:**

C=A+B

ifadesinde A ve B serbest değişken olduğundan, akış denetçisi bu yüklem için akış biçimi olmadığını bildiren bir hata mesajı verecektir. Bu durumu kontrol etmek için **free** ve **bound** standart yüklemleri kullanılır.

İki sayı arasında toplama yapmak veya toplam ile ilk sayısı verilen bir durumda ikinci sayıyı bulan, bütün akış biçimleriyle çağrılabilen **topla** adında bir yüklem tanımlayalım.

**Örnek:**

PREDICATES

nondeterm topla(integer, integer, integer)

nondeterm sayi(integer)

CLAUSES

topla(X,Y,Z):-

bound(X),

bound(Y),

Z=X+Y. /\* (i,i,o) \*/

topla(X,Y,Z):-

bound(Y),

bound(Z),

X=Z-Y. /\* (o,i,i) \*/

topla(X,Y,Z):-

bound(X),

bound(Z),

Y=Z-X. /\* (i,o,i) \*/

topla(X,Y,Z):-

free(X),

free(Y),

bound(Z),

sayi(X),

Y=Z-X. /\* (o,o,i) \*/

topla(X,Y,Z):-

free(X),

free(Z),

bound(Y),

sayi(X),

Z=X+Y. /\* (o,i,o) \*/

topla(X,Y,Z):-

free(Y),

free(Z),

bound(X),

sayi(Y),

Z=X+Y. /\* (i,o,o) \*/

topla(X,Y,Z):-

free(X),

free(Y),

free(Z),

sayi(X),

sayi(Y),

Z=X+Y. /\* (o,o,o) \*/

/\* 0'dan başlayan sayıları bulma\*/

sayi(0).

sayi(X):-

sayi(A),

X = A+1.

GOAL topla(Ilk\_sayi,7,10).

**8.4. Referans Değişkenler**

Akış denetçisi bir cümleyi incelerken, bu cümlenin başındaki bütün çıktı değişkenlerinin cümlenin gövdesinde bağlı olup olmadığını kontrol eter. Bir cümlede bir değişken bağlı değilse, bu değişkenin referans değişkeni olarak işlem görmesi gerekir. Bu karmaşayı gösteren bir örnek aşağıda verilmiştir.

Predicates

p(integer)

Clauses

p(X):-!.

Goal p(V), V=99, write(V).

Sorgudaki p yüklemi çıktı biçiminde çağrılır fakat clauses bölümündeki p yükleminde bulunan X değişkeni bağlı değişken değildir. Akış denetimi sırasında bu fark edildiğinde, değişkenin domains bölümündeki tip tanımına bakılır. Eğer değişken tipi referans olarak tanımlıysa problem çıkmaz. Tanımsızsa uyarı mesajı görüntülenir.

Bir cümledeki bir değişken bağlı değilse, bu durumda cümlenin herhangi bir değer aktarması mümkün değildir. Bunun yerine **referans değişkenine** bir **pointer** yollayarak daha sonra bu noktaya gerçek değerin yazılması sağlar. Bu, bu tipteki bazı değişkenlere değer aktarmak yerine, tip tanımının tamamına aynı işlemin yapılmasını gerektirir. Kayıtlara gönderilen pointerlar referans tipe ait argümanlara iletilir. Yani bileşik bir tip referans bir tip haline gelirse, bu durumda bütün alt tiplerin de referans tip olarak işlem görmesi gerekir. Bileşik bir tipin referans tip olarak tanımlanması durumunda, derleyici diğer bütün alt tipleri de referans tip olarak kabul eder.

**8.4.1. Referans Tip Tanımı**

Akış denetçisi program içerisinde bağımsız bir değişken bulduğunda değişken sadece bir cümleden dönüş sırasında bağımlı değilse uyarı verir. Bu durum sizin için uygunsa, bu tip tanımı otomatik olarak referans tip olarak kabul edilir. Bununla birlikte referans tip olarak tanımlamak istenen bir tipi domains bölümünde net olarak tanımlamak daha mantıklıdır.

**8.4.2. Referens Tip ve İzleme Dizileri(array)**

Zorlama ve ekstra eşleştirme gerektirdiği için, referans tipler programın çalışma hızında genel bir azalmaya neden olur. Fakat referans tip tanımının neden olduğu problemler daha etkili biçimde kullanılabilir ve bu tip tanımlarının etkileri azaltılabilir.

Referans tipler kullanıldığı zaman, Visual Prolog izleme dizini kullanır. Bu izleme dizini referans değişkenlerin değer aldıkları anı bildirmek için kullanılırlar. Referans bir değişkenin oluşturulması ve değer alması arasındaki herhangi bir noktaya geriye dönüş yapıldığı zaman, bu değişkenin yeniden değer almamış hale getirilmesi gerekir. Fakat bu problem düz değişkenlerle uğraşırken meydana gelmez. Çünkü bunların oluşturulması ve değer alma noktaları aynıdır. İzlemede kaydedilen her bir çağrı 4 byte (32 bit bir pointerin büyüklüğü) kullanır.

Gerektiğinde kuyruk büyüklüğü otomaki olarak arttırılır. İzin verilen maksimum büyüklük 16-bit Visual Prolog için 64K, 32-bit için ise sınırsızdır.

Standart tipleri referans tip olarak kullanmak iyi bir fikir değildir. Çünkü program kullanıcının tanımladığı bu referans tipi, aynı tip için daima geçerliymiş gibi kullanır. Bunun yerine, istenilen temel tip için referans bir tip tanımlamak daha uygundur. Örneğin aşağıdaki program parçasında kullanıcının tanımladığı tamsayi\_referans\_tipi tamsayılar için referans tiptir. Dolayısıyla tamsayi\_referans\_tipi her kullanımda referans tip olarak işlem görür. Fakat tamsayı tipindeki değişken referans tip olarak değil, normal olarak integer olarak işlem görür,.

Domains

tamsayi\_referans\_tipi= reference integer

Predicates

P(tamsayi\_referans\_tipi)

Clauses

P(\_).

**8.5. Referans Tip Kullanımı**

Referans tip kullanımının en doğru biçimi, sadece gerekli olan birkaç yerde kullanıp geri kalan kısımların tamamında referans olmayan tipi kullanmaktır. Zaten gerekli olan durumlarda referans ve referans olmayan tipler arasında dönüşüm yapmak mümkündür. Şimdi referans olan bir tamsayıyı referans olmayan bir tamsayıya dönüştürelim.

Domains

Referans\_tamsayi=reference integer

Predicates

Donustur(referans\_tamsayi, tamsayi)

Clauses

Donustur(X, X).

İsmi aynı olan bir değişken referans ve referans olmayan tipte kullanıldığı zaman dönüşüm otomatik olarak yapılır. Yukarıdaki örnekte referans\_tamsayi ve tamsayi arasında dönüşüm otomatik olarak yapılır. Referans bir değişkenin, referans olmayan bir değere dönüştürülebilmesi için öncelikle bir değer almış olması gerekir. Yani referans tip olarak tanımlı bir değişkeni dönüştürmek için (örneğin referans tamsayılardan referans karaktere) öncelikle bu değişkenin bir değer almış olduğundan emin olmak gerekir. Aksi takdirde serbest değişken kullanılamaz şeklinde hata mesajı görüntülenir. Referans tip tanımlarının nasıl çalıştığını tam olarak anlamak için aşağıdaki programı değişik sorgularla çalıştırılmalıdır.

DOMAINS

referans\_tamsayi = integer

referans\_liste= reference referans\_tamsayi\*

PREDICATES

nondeterm eleman(referans\_tamsayi, referans\_liste)

ekle(referans\_liste, referans\_liste, referans\_liste)

CLAUSES

eleman(X, \[X|\_\]).

eleman(X, \[\_|L\]):-

eleman(X, L).

ekle(\[\], L, L).

ekle(\[X|L1\], L2, \[X|L3\]):-

ekle(L1, L2, L3).

GOAL eleman(1, L).

Aşağıdaki sorguları da deneyin

eleman(X, L), X=1. Elemanları arasında 1 olan bütün listeleri bul.

eleman(1, L), eleman(2, L). Elemanları arasında 1 ve 2 olan bütün listeleri bul

X=Y, eleman(X, L),eleman(Y, L), X=3. X ve Y’nin eleman olduğu listeler

eleman(1, L), ekle(L, \[2, 3\], L1).

ekle(L, L, L1), eleman(1, L). 1’in iki kez eleman olduğu listeler.

**8.6. Akış Biçimine Yeni Bir Bakış**

Referans bir değişken serbest halde olmasına rağmen, bir yüklem çağrısı içinde çağrıldığı anda mevcut olabilir. Ülkeler hakkındaki programda ayni\_baskentler:-ulke(baskent(Kent, Kent), write(Kent, ‘\\n’), fail şeklindeki bir sorguyla, başkentleri ülke ismiyle aynı olan bütün ülkeleri bulmak isteyelim. Burada kent değişkeni iki kez çıktı akışı ile kullanılmıştır. Fakat bu sorgu satırının söylediği şey; Kent değişkeni değer aldığı anda ikinci değişken olan Kent’in de aynı değeri alması gerektiğidir. Bu yüzden her iki değişken çağrı yapılmadan önce yaratılıp eşleştirilir. İşte bunu yapabilmek için bunların tipi referans tipe dönüştürülür ve iki değişken çağrı anından itibaren kullanıma girerler.

Standart tip tanımlarının referans tip haline getirmenin çok yanlış bir kullanım olacağı daha önce söylenmişti. Eğer böyle bir şey yapılmak isteniyorsa, uygun bir referans tip tanımlamak daha mantıklıdır.

**8.7. İkili (Binary) Ağaç Yapısının Referans Tip İle Kullanımı**

Önceki sıralama işlemleri ikili ağaç yapısı ile çözülmüştü. Aynı şeyi referans tip tanımı ile daha güzel biçimde yapmak mümkündür. Ağaç yapısındaki bir dalı, bir değer aldıktan sonra değiştirmek mümkün değildir. Ağaç oluşturulurken pek çok noktanın kopyası oluşturulur. Sıralama işlemini büyük miktarda veri üzerinde yapıldığı düşünülürse, bunun hafıza taşmasına neden olabileceği görülür. Referans bir tip, ağacın dallarını serbest değişken olarak bırakarak, bu durumu düzeltebilir. Bir referans tipi bu şekilde kullanarak yeni bir dalın ilave edileceği noktanın üzerindeki dalı kopyalamaya gerek kalmaz.

**Örnek:**

Domains

agac = reference t(isim, agac, agac)

isim = string

PREDICATES

araya\_ekle(isim, agac)

CLAUSES

araya\_ekle(ID, t(ID,\_,\_)):-!.

araya\_ekle(ID, t(ID1, Agac,\_)):-

ID<ID1, !, araya\_ekle(ID, Agac).

araya\_ekle(ID, t(\_,\_,Agac)):-

araya\_ekle(ID, Agac).

GOAL

araya\_ekle("Alper", Agac),

araya\_ekle("Kasim", Agac),

araya\_ekle("Paki", Agac).

İlk araya\_ekle(“Alper”, Agac) alt hedefi ilk kural ile eşleşir ve bileşik nesne t(“Alper”,\_,\_) biçimini alır. T’deki son iki argüman bağlı değişken olmasalar da t diğer alt hedefe iletilir:

araya\_ekle(“Kasim”, Agac).

Bu, agac değişkenini t(“Alper”, t(“Kasim”,\_,\_),\_) değerini aldırır. Son olarak son alt hedef araya\_ekle(“Paki”, Agac) agac değişkenini t(“Alper”, t(“Kasim”,\_, t(“Paki”,\_,\_)),\_) değerine atar ve sonuçta bu değer görüntülenir.

**8.8. Referans Tip Kullanarak Sıralama**

Daha önce ikili ağaç kullanarak yapılan sıralama örneğini, referans ve referans olmayan tipler arasında ayrım yaparak nasıl yapabileceğini gösteren bir örnek, aşağıda verilmiştir.

DOMAINS

agac=reference t(deger, agac, agac)

deger=integer

liste = integer\*

PREDICATES

araya\_ekle(integer, agac)

agac\_ekle(liste, agac)

nondeterm agacin\_elemanlari(integer, agac)

sirala(liste, liste)

CLAUSES

araya\_ekle(Deger, t(Deger,\_,\_)):-!.

araya\_ekle(Deger, t(Deger1,Agac,\_)):-

Deger<Deger1,!,

araya\_ekle(Deger, Agac).

araya\_ekle(Deger, t(\_,\_,Agac)):-

araya\_ekle(Deger, Agac).

agac\_ekle(\[\],\_).

agac\_ekle(\[Bas|Kuyruk\],Agac):-

araya\_ekle(Bas,Agac), agac\_ekle(Kuyruk, Agac).

agacin\_elemanlari(\_,Kuyruk):-

free(Kuyruk),!, fail.

agacin\_elemanlari(X,t(\_,L,\_)):-

agacin\_elemanlari(X, L).

agacin\_elemanlari(X,t(RefStr,\_,\_)):-

X=RefStr.

agacin\_elemanlari(X,t(\_,\_,R)):-

agacin\_elemanlari(X, R).

sirala(L,L1):-

agac\_ekle(L, Agac),

findall(X, agacin\_elemanlari(X,Agac), L1).

GOAL sirala(\[10,9,17,21,114,5\], L), write("Liste= ", L),nl.

Bu örnekte referans tipler sadece agac değişkeninde kullanılmıştır. Diğer argümanların tamamı referans olmayan tiplerdedir.

**8.9. Binary (İkili) Tip**

Visual Prolog’da ikili verileri kullanmak için özel tip, ikili terimlerin elemanlarına erişmek için özel yüklemler vardır. İkili terim kullanmanın tek amacı, başka türlü anlamlı bir şekilde gösterilemeyen verileri kullanmak ve bunları saklamaktır. Binary terimleri okuma, bunları dosyaya aktarma işlemi için özel yüklemler vardır.

Binary terimlerin temel amacı mantıksal olmayan nesneler diğer programlama dillerinin içine kolayca yerleştirilmesine imkan tanımaktır. Binary terimler, geriye iz sürme mekanizması çerçevesinde Prologdaki diğer terimlerden farklı davranırlar. Geriye iz sürme mekanizması, binary terimin oluşturulduğu noktadan öncesine giderse, binary terimlerin o ana kadar aldıkları değerleri kaybederler. Geriye dönüş, herhangi bir binary terimin oluşturulduğu noktadan öncesine dönmezse, binary terimdeki değişikliklere bir şey olmaz.

**8.9.1. Binary Terimlerin Kullanılması**

Bir binary terim byte biçiminde bir dizi ve bu dizinin büyüklüğünü saklayan word (16 bit) veya dword(32 bit ortam) değişkenden oluşur.

Diğer dillerden çağrı yapıldığında, binary tipindeki bir terim (diğer bir dildeki fonksiyonun çağrısayla aktarılan değişken) gerçek içeriğe işaret eder. Buradaki büyüklük alanı, alanın kendisinin sahip olduğu büyüklüktür. Binary terimler 16 bit platformlarda genelde 64K ile sınırlıdır.

**8.9.2. Binary Terimlerin Yazım Biçimi**

Binary terimler okunup metin biçimde yazılabilir. Visual Prolog’da program satırları gibi yazılabilir. Yazılım biçimi:

$\[b1, b2, ....., bn\]

Burada b1, b2 vs. ilgili terimin byte olarak yazılmış halidir. Program akışı içerisinde yazıldığı zaman, buradaki her byte uygun bir pozitif biçimde desimal, hegzadesimal, oktal veya karakter olarak yazılabilir. Karakter olarak yazılan byte, program çalışırken daima hegzadesimal biçime dönüştürülür ve “0x” kısımları bulunmaz.

**Örnek:**

GOAL write("Binary terimi metin biçiminde yaz: ", $\['C', 12, 15, 0x14, 'e', 5\], '\\n').

**8.9.3. Binary Terimlerin Oluşturulması**

Binary terim oluşturmak için Visual Prolog’da mevcut olan yüklemler sırayla aşağıda verilmiştir.

**8.9.3.1. makebinary(1)**

makebinary, tanımlanan byte sayısında bir binary terim oluşturur ve içeriğini binary 0 olarak ayarlar.

...., Bin=makebinary(10), ....

Burada byte sayısı, alan büyüklüğü hariç, net büyüklük olmalıdır.

**8.9.3.2. makebinary(2)**

İki argüman alabilen biçiminde eleman büyüklüğü tanımlanabilir.

...., Usize=sizeof(unsigned), Bin=makebinary(10, Usize), ....

Bu yüklem, terim büyüklüğü eleman sayısının eleman büyüklüğüyle çarpımıyla belirtilen bir binary terim oluşturur. Örnekte eleman sayısı 10, eleman büyüklüğü ise sizeof(unsigned) olarak tanımlıdır. Terim içeriği 0 olur.

**8.9.3.3. composebinary(2)**

Mevcut olan bir pointer ve bir uzunluktan bir binary terim oluşturur. Kullanım biçimi:

..., Bin=composebinary(StringVar, Buyukluk), ....

**8.9.3.4. getbinarysize(1)**

getbinarysize, verinin önündeki alan büyüklüğünü hariç tutarak, bir binary terimin net büyüklüğünü byte türünden verir.

..., Buyukluk=getbinary(Bin), ...

**8.9.4. Binary Terimlere Erişim**

4’ü giriş, diğer 4’ü de çıkış elde etmek için kullanılan 8 yüklem binary terimlere erişmek için kullanılabilir. Bunların hepsi binary terim büyüklüğü, tanımlı indeks ve istenilen maddenin büyüklüğüne (byte, word, dword veya real) bağlı olarak bu değişkenlerin doğru aralıklarda olup olmadıklarını kontrol eder. Bu yüzden bu girişleri, ikili terimlerin tanımlı sınırları dışında tanımlamak ve çağırmak hataya neden olur.

İndislerin (eleman numaraları) 0’a göre değişir. Yani binary bir terimin ilk elemanının indisi 0, en son elemanın da N-1 olur.

**8.9.4.1. getentry(2)**

getentry yüklemi getbyteentry, getwordentry, getdwordentry veya getrealentry biçimlerinden biri olur ve sırasıyla byte, word, dword veya real tiplerinde giriş yapıp, giriş alabilir.

Deger= getbyteentry(Bin, 3), ....

**8.9.4.2. setentry(3)**

getentry’ye karşılık gelen bir yüklem olup byte, word, dword eya real girişleri yapar.

...., setbyteentry(Bin, 3, Baytlar), ....

**8.9.5. Binary Terimleri Eşleştirme**

Binary terimler de diğer terimler gibi eşleştirilebilir. Kullanım biçimi:

..., Bin1=Bin2, ....

Eşleştirme anında terimlerden biri serbest halde ise, birbirine eşitlenirler. Her ikisi de bağlı ise, bu durumda binary terimlerin birbirine eşit olup olmadıkları kontrol edilir.

**8.9.6. Binary Terimleri Karşılaştırma**

Binary iki terim eşleştirilirken şu sonuçlara dikkat edilir:

Eğer büyüklükleri farklı ise, büyük olan büyük kabul edilir, değilse byte bazında karşılaştırılırlar. İki farklı byte bulunduğu anda karşılaştırma durur, sonuç toplam terimin karşılaştırılması olarak gönderilir. Örneğin $\[1, 2\] $\[100\]’den daha büyüktür fakat $\[1,3\]’den daha küçüktür.

Binary terimlerin bazı özelliklerini gösteren bir program aşağıda verilmiştir.

PREDICATES

binary\_karsilastir\_ve\_eslestir

binary\_karsilastir(binary, binary)

al(binary)

CLAUSES

binary\_karsilastir\_ve\_eslestir:-

Bin=makebinary(5),

binary\_karsilastir(Bin, \_),

binary\_karsilastir($\[1,2\], $\[100\]),

binary\_karsilastir($\[0\], Bin),

binary\_karsilastir($\[1, 2, 3\], $\[1, 2, 4\]).

binary\_karsilastir(B,B):-!,

write(B, " = ", B, '\\n').

binary\_karsilastir(B1, B2):-

B1>B2, !,

write(B1, " > ", B2, '\\n').

binary\_karsilastir(B1, B2):-

B1<B2, !,

write(B1, " < ", B2, '\\n').

al(Bin):-

setwordentry(Bin, 3, 255), fail.

al(Bin):-

Buyukluk=getbinarysize(Bin), X=getwordentry(Bin, 3),

write("\\nBuyukluk= ", Buyukluk, "X = ", X, " Binary= ", Bin, '\\n').

GOAL

binary\_karsilastir\_ve\_eslestir, % Binary kaşılaştırma ve eşleştirme için

KelimeBuyuklugu=sizeof(word), Bin=makebinary(4,KelimeBuyuklugu), al(Bin),

write("Run-time hataları yanlış indeksten kaynaklanıyor:\\n"), Indeks=4,

trap(Setwordentry(Bin, Indeks, 0), E,

write(Bin, "teriminin kelime indeksi", Indeks, " olustururken ", E, " hatasi olustu", '\\n')).

**8.9.7. Terimleri Binary Terimlere Dönüştürme**

Bileşik bir terimin argümanları belleğin değişik yerlerinde olabilir. Basit tipleri doğrudan kayıtlı terimde tutulurken karmaşık olanlar (pointer ile erişilenler ve global bir stack’da olanlar) içindeki göründükleri terimin yakınlarında olmayabilir. Böyle bir terimi programdan dışarıya yollamak zor olur. Çünkü terimin bütün içeriğinin kopyasını almanın açık bir yolu yoktur. Dolayısıyla bir terimdeki değişkeni başka bir değişkenle eşleştirirken sadece bu terime giden pointerin bir kopyası alınmış olur.

term\_str yüklemini kullanarak, bir terimi diziye ve diziden tekrar terime dönüştürmek mümkündür. Bu ise, sadece terimi içeriğini kopyalamak için gerektiğinde, oldukça yetersiz kalır. İşte bu problemi term\_bin** **yüklemini çözer.

**8.9.7.1. term\_bin(3)**

term\_bin, herhangi bir tipteki terim ve binary veri bloku arasında dönüşümü, terim içeriği ve pointer sabitle bilgisini tutarak, yapar. Pointerin sabitleme bilgisi, binary veriye dönüştürülmüş terimi yeniden diziye dönüştürmek için kullanılır. Kullanımı şöyledir:

term\_bin(tip, Terim, Bin) /\* (i,i,o), (i,\_,i) \*/

Tip, Terimin ait olduğu tip, Bin ise Terimin içeriğini tutan binary terimdir.

**8.10. Hatalar ve İstisnalarla Uğraşma**

Kaliteli yazılımlar geliştikçe, güvenilir programlar üretmek için hataların bulunması ve tek tek ayıklanması da önemli hale gelmektedir. Visual Prolog, program çalışırken meydana gelen hataları kontrol etmek için standart yüklemlere sahiptir. Programın işleyişi esnasında meydana gelebilecek bütün hatalar DOS ortamıda PROLOG.ERR, UNIX ortamında PDCProlog.err dosyasında saklanır. Hata mesajı numarası 10000 ve yukarısı kullanıcının programında kullanması için exit kodları olarak ayrılmıştır.

Hata ve istisna durumlarıyla uğraşmak için Visual Prolog’da temel olarak trap yüklemi kullanılır. Bu yüklem, run-time hatalarını ve exit yüklemiyle harekete geçirilen istisna durumları yakalayabilir. Bu yüklem kullanarak, örneğin Ctr+Break tuşlarına basılıp basılmadığını da kontrol edilebilir.

**8.10.1. exit(0), exit(1)**

exit yüklemine yapılan bir çağrı, run-time hataya eşdeğerdir. Kullanım biçimleri:

exit ve exit(CikisKodu)

Argüman kullanmadan exit yüklemini kullanmak, exit(0) gibi çalışır. exit’e giden çağrı trap yükleminde doğrudan veya dolaylı olarak çalıştırılırsa, CikisKodu trap yüklemine geçer.

**8.10.2. trap(3)**

Üç argüman alan bu yüklem hata yakalama ve istisna yönetimini gerçekleştirir. İlk ve son argümanlar yüklem çağırma, ikinci argüman ise değişkendir. Kullanım biçimi:

trap(YuklemCagirma, CikisKodu, HataDurumundaCagrilacakYuklem)

Örneğin trap(islem(P1,P2,P3), CikisKodu, hata(CikisKodu,P1)),.... şeklindeki bir çağrı göz önüne alınırsa, işlem yüklemi çağrılırken hata oluşursa CikisKodu ilgili hatayı verirken hata yönetme yüklemi olarak tanımladığımız hata yüklemi çağrılmış olur. Hata yükleminden dönüşte ise trap yüklemi başarısız olur.

Metin modu ortamında BREAK açıkken BREAK yapılırsa, yani Ctrl+Break tuşlarına basılırsa, trap yüklemi bunu yakalar ve CikisKodu değerini olarak 0’ı görüntüler.

**Örnek: **

Açılmamış olan bir dosyadan dolayı hata mesajı yakalayan program aşağıda verilmiştir.

include "c:\\\\vip\\\\include\\\\error.con"

DOMAINS

file = giris\_dosyasi

PREDICATES

hata\_yakalama(integer, file)

satir\_al(file, string)

CLAUSES

hata\_yakalama(err\_notopen, Dosya):-!,

write(Dosya, " isimli dosya açık değil\\n"),

exit(1).

hata\_yakalama(Hata, Dosya):-!,

write(Dosya, "adli dosyada",Hata, " hatasi ", '\\n'),

exit(1).

satir\_al(Dosya, Satir):-

readdevice(Eski),

readdevice(Dosya),

readln(Satir),

readdevice(Eski).

GOAL trap(satir\_al(giris\_dosyasi, Ilk), Hata, hata\_yakalama(Hata, giris\_dosyasi)), write(Ilk).

**8.10.3. errormsg(4)**

errormsg yüklemi, Visual Prolog hata mesajları dosyasıyla aynı biçimde olan dosyalara erişmek için kullanılabilir. Kullanım biçimi:

errormsg(DosyaAdi,HataNo,HataMesaji,YardimMesaji) / (i, i, o, o)/

Bu işlem için aşağıdaki program örneği kullanılabilir:

PREDICATES

hata(integer)

ana\_kisim

/\* .......... \*/

CLAUSES

hata(0):-!. % Ctrl+Break tuşuna basılınca bir şey yapma

hata(H):-

errormsg(“prolog.err”, H, HataMesaji, \_),

write(“\\nSayin Kullanici, Programınızda”, H, “nolu “, ErrorMsg, “hatasi meydana geldi”),

write(“\\nDosyanizi”, hata.txt,” dosyasina yaziyorum”),

save(“hata.txt”).

GOAL trap(ana\_kisim, CikisKodu, hata(CikisKodu)).

**8.10.4. Hataların Bildirilmesi**

Visual Prolog’daki bazı derleyici direktiflerini kullanarak, programlarınız içindeki run-time hataları kontrol edilebilir. Bu direktifler şu amaçlarla kullanılır:

Tamsayı taşma(overflow) hatalarını kontrol edip etmeme durumu

run-time hataları hangi ayrıntı düzeyinde verileceği

Yığın taşması(Stack overflow) kontrolünü yapma

Bu direktifler programın baş tarafında verilebileceği gibi, VIP çalıştırıldıktan sonra Compiler Options seçeneğiyle de verilebilir.

**8.11. Hata Düzeyi**

Visual Prologun, run-time hatanın oluştuğu yeri göstermeye yarayan çok güzel bir mekanizması vardır. Meydana gelen hatanın hangi düzeyde bildirileceğini, hatanın meydana geldiği yeri, derleyicinin errorlevel direktifi belirler. Kullanım biçimi şöyledir:

errorlevel=n

n’nin alabileceği değerler 0, 1 veya 2 olabilir. Bu değerlere göre derleyicinin sunacağı hata düzeyi şunları kapsar:

0 Bu durumda en küçük ve en etkin hata mesajı verilir. Fakat hatanın yeri kaydedilmez, sadece hatanın numarası verilir.

1 Default olarak kabul edilen düzey budur. Hata meydana geldiğinde hatanın meydana geldiği nokta, dosyanın başlangıcından itibaren byte türünden gösterilir.

2 Bu düzey seçildiğinde, 1 durumunda gösterilmeyen stack overflow, heap overflow, trail oveflow vs. gibi hataları görülebilir. Burada da hatanın meydana geldiği yer bildirilir.

Proje bazında çalışırken hata mesajı düzeylerini ayarlarken dikkatli olmak gerekir. Bir projede birden fazla dosya bulunacağı için, birbirine bağlı olan dosyalardaki hata düzeyleri farklı biçimde ayarlanırsa, errorlevel=0 olan bir alt dosyada hata meydana gelirse ve ana dosyada errorlevel=1 veya 2 olursa, bu durumda hatanın meydana geldiği yeri tam olarak bulmak imkansız olur.

**8.11.1. lasterror(4)**

lasterror, en son olan hatayla ilgili bütün bilgiyi verir. Kullanım biçimi:

lasterror(HataNo,Modul,IncDosyasi,HataYeri)

Burada Modul, hatanın meydana geldiği dosya adı, IncDosyasi ise include dosyasıdır. Bellek taşması hatalarının doğru olarak alabilmek için programın errorlevel=1 olarak derlenmesi gerekir. Sadece basit hataların mesajları alınması isteniyorsa errorlevel=1 yeterlidir.

**8.11.2. Terim Okuyucudan Gelen Hataları Görme**

**consult** veya **readterm** yüklemleri çağrıldığında okunacak satırda bir hata var ise, bu yüklemlerin hata mesajı vererek duracakları bilinmektedir. Hata nedenleri ise okunacak satırın uygun biçimde hazırlanmamış **olmamasıdır**.

**Örneğin:**

Bir diziyi sonlandırmamak

Symbol türünde bir karakter yerine integer bir karakter yazmak

Yüklem adı için büyük harfler kullanmak

Sabit değerleri “ “ içinde yazmamak vs.

**readtermerror** ve **consulterror** yüklemlerini kullanarak readterm veya consult yüklemlerinin okumaya çalıştığı dosyalarda ne tür hatalar meydana geldiğini kontrol edebililir.

**consult** ve **readterm** yüklemlerinden gelen hatalar trap yüklemi tarafından yakalanırsa, consulterror ve readtermerror yüklemlerini kullanarak hatanın nedenini görmek ve yazmak mümkündür.

**8.11.3. consulterror(3)**

consulterror, hatalı yazımın bulunduğu satırdaki hata hakkında bilgi verir. Kullanım biçimi

consulterror(Satir, HataYeri, DosyadakiYeri)

Satir, hatanın bulunduğu satır, HataYeri hatanın bulunduğu nokta, 3. parametre ise hatalı satırın bulunduğu yer verilir.

**Örnek:**

CONSTANTS

yardim\_dosyasi="prolog.hlp"

hata\_dosyasi="prolog.err"

DOMAINS

dom = a(integer)

liste= integer\*

DATABASE - firat\_dba

p1(integer, string, char, real, dom, liste)

PREDICATES

consult\_hatalarini\_ayiklama(string, integer)

CLAUSES

consult\_hatalarini\_ayiklama(Dosya, Hata):-

Hata>1400, Hata<1410, !,

retractall(\_, firat\_dba),

consulterror(Satir, Hatanin\_Yeri,\_),

errormsg(hata\_dosayasi, Hata, Mesaj, \_),

str\_len(Bosluklar, Hatanin\_Yeri),

write(Dosya, " dosyasinin ", Satir, " satırında ", Bosluklar, Mesaj, "meydana gelmistir"),

exit(1).

consult\_hatalarini\_ayiklama(Dosya, Hata):-

errormsg(hata\_doyasi, Hata, Mesaj, \_),

write(Dosya, " dosyasi açılmaya çalışırken ", Mesaj, " hatası oluştu"),

exit(2).

GOAL Dosya="test.dba",

trap(consult(Dosya, firat\_dba), Hata, consult\_hatalarini\_ayiklama(Dosya, Hata)),

write("\\n Tamam \\n").

**8.11.4. readtermerror(2)**

readtermerror, readterm yükleminin okuduğu satırdaki hatayı verir. Kullanım biçimi:

readtermerror(Satir, HataYeri)

**8.12. Break Kontrolü (Sadece Metin Modunda)**

Visual Prolog’daki break mekanizmasının nasıl çalıştığına bakalım. Genelde, break için gerekli komutlar o anda çalışan programı hemen durdurmazlar. Prolog’da, istisnai durumları yöneten bir birim vardır. Sinyal ile aktif edilen bu parça bir flag yerleştirir. Visual Prolog bu flagı iki farklı durumda kontrol eder.

Yazılan program, break-kontrolü açık halde derlenirse, her yüklem girildiğinde break-flag durumu kontrol edilir. Break-kontrol seçeneği, VIP seçeneklerinden iptal uygun direktif seçilerek (Options/Compiler Directives/Run-time check) iptal edilebilir.

Library rutinlerinin bazıları break-flag kontrolü yaparlar.

**8.12.1. break(1)**

break, bir program çalışırken break-flag kontrolünün yapılıp yapılmayacağını belirtir. Kullanım biçimleri şöyledir.

break(on), break(off)

break(BreakDurumu)

DOS tabanlı pgogramlar için break komutundan kaynaklanan çıkış kodları daima 0 olur.

**8.12.2. breakpressed(1)**

break-flag kurulmuşsa, break(off) olsa veya program nobreak seçeneğiyle derlense bile, breakpressed yüklemi başarılı olur. Başarılı olunca, yakalanan en son sinyale göre bir çıkış kodu verir ve break-flagı siler.

**8.13. DOS Metin Modunda Kritik Hata Kontrolü**

Bu bölüm sadece DOS metin modu ortamında geçerlidir. Dolayısıyla VPI programlarına uygulanamaz.

Visual Prolog’un DOS versiyonu hata durumlarıyla ilgilenen bazı rutinler içerir. Bir DOS hatası olduğu zaman DOS, criticalerror rutinini çağrır. Visual Prolog’daki sistem ise, run-time editörü de bir dosya hatası bulduğunda fileerror yüklemini çağırır. Bu yüklemler global olarak tanımlanır ve kendinize ait cümlecikler kullanırsanız, library’deki rutinler yerine size ait rutinleri programa bağlar. Dolayısıyla hataları daha iyi kontrol etmek mümkündür. Bu durumda .EXE programlarının büyüklüğü büyük oranda azalır. criticalerror ve fileerror için global deklerasyon include dosyasında error.pre içinde hazır olarak bulunmaktadır.

**8.13.1. criticalerror(4)**

Visual Prolog, bu rutini DOS kritik hatalarıyla uğraşmak için tanımlar. criticalerror yüklemi kullanılmak istenirse, ERROR.PRE dosyası programa dahil edilmelidir. Tanımlanması şöyledir:

global predicates

criticalerror(HataNo, HataTuru, DiskNo, Eylem)

criticalerror yüklemi daima başarılı olmalıdır. Bu yüklem sadece .EXE dosyasından çalışır ve DOS kritik hata interrupt tutucusuyla yer değiştirir. Aşağıdaki tabloda criticalerror yükleminin argümanlarının aldığı değerler verilmiştir.

Tablo 8.4. Criticalerror yükleminin argümanlarının aldığı değerler

| **Argüman ** | **Değer** | **Anlamı** |
| --- | --- | --- |
| HataNo | = 0 = 1 = 2 = 3 = 4 = 5 = 6 = 7 = 8 = 9 = 10 = 11 | Yazma korumalı diskete yazma teşebbüsü Bilinmeyen ünite Sürücü hazır değil Bilinmeyen komut Veri içinde CRC hatası Yanlış sürücü isteği yapı uzunluğu Arama hatası Bilinmeyen medya türü Sektör bulunamadı = 12 Yazıcıda kağıt bitmiş Yazma hatası Okuma hatası Genel hata |
| HataTürü | = 0 = 1 = 2 | Karakter araç hatası Disk okuma hatası Disk yazma hatası |
| DiskNo | = 0-25 | A-Z’ye kadar sürücü |
| Eylem | = 0 = 1 = 2 | Çalışmayı durdur İşlemi yeniden dene İşlemi iptal et (Tehlikeli olabilir ve tavsiye edilmez) |

**8.13.2. fileerror(2)**

Metin modundaki bir dosya eylemi başarısız olunca fileerror yüklemi harekete geçirilir. Kendinize ait fileerror yüklemini tanımlarsanız, bu yüklemin başarısız olmasına izin verilmez ve bu yüklem sadece .EXE uygulamalarından çalışır. fileerror’un ERROR.PRE dosyasındaki tanımlanması şöyledir:

global predicates

fileerror(integer, string) – (i, i) language c as “\_MNU\_FileError”

Bu tanım tipi doğrudur. Kaynak kod Prolog’da olsa bile language c mutlaka belirtilmelidir.

**8.14. Dinamik Cut**

Prolog’daki cut statiktir. Geleneksel cut işleminde, program akışı ancak ! sembolüne geldiği zaman cut devreye girer ve sadece içinde bulunulan cümleleri etkiler. Dolayısıyla bir cut komutunun etkisini başka bir yükleme aktarmak mümkün değildir. Normal cut komutunun diğer bir dezavantajı da; yüklemde cut komutunu takip eden cümlelerdeki geriye dönüş noktalarını ortadan kaldırmadan, bir alt hedefteki diğer çözümleri arama ihtimalini ortadan kaldırmanın mümkün olmamasıdır.

Visual Prolog’da dinamik kesme mekanizmasında getbacktrack ve cutbacktrack yüklemleri kullanılır. Bu mekanizma sayesinde bu iki dezavantaj ortadan kalkmış olur. getbacktrack, geriye iz sürme noktalarının yığını içerisinde en üstteki pointer’i verir. Bu noktanın üstünde kalan bütün geriye dönüş noktaları silinebilir.

Bu iki yüklemin kullanımı hakkındaki örnekler, aşağıda verilmiştir.

Elimizdeki veritabanında sahislarin isim ve aylık gelirleri var. Bu sahısların arkadaşlarını kaydetmiş durumdayız.

database

sahis(symbol, income)

arkadas(symbol, symbol)

Arkadaşı olan veya az bir vergi ödeyen insanların listesini görmek için aşağıdaki cümlecikleri kullanabiliriz:

sansli\_insanlar(aradasi\_var(P)):-sahis(P,\_), arkadas(P,\_).

sansli\_insanlar(zengindir(P)):-sahis(P, AylikGelir), not(zengin(AylikGelir)).

Bir şahsın birden fazla arkadaşı varsa, ilk cümlecik birden fazla çözüm getirir. Bu arada dinamik cut kullanabiliriz.

sahsli\_insanlar(arkadasi\_var(P)):-

sahis(P,\_), getbacktrack(BTOP), arkadas(P,\_), cutbacktrack(BTOP).

Geriye dönüş mekanizması yapılırsa, arkadaş yüklemi birden fazla çözüm sunabilir. Fakat cutbacktrack yüklemi çağrılarak bu ihtimal ortadan kaldırılır.

Dinamik cut kullanmanın daha önemli avantajı, geriye dönüş pointerini başka bir yükleme geçirmek ve cut komutunu şartlı olarak çalıştırmaktır. Pointer pozitif tipte olup yine pozitif tipteki değişkenlere aktarılabilir.

**Örnek: **

Bir tuşa basıncaya kadar ekrandan girilen rakamları okuyan bir program, aşağıda sunulmuştur.

PREDICATES

sayi(integer)

sayilari\_yaz(integer)

kullanici\_komutu(unsigned)

CLAUSES

sayi(0).

sayi(N):-sayi(N1), N=N1+1.

sayilari\_yaz(N):- getbacktrack(BTOP), sayi(N), kullanici\_komutu(BTOP).

kullanici\_komutu(BTOP):- keypressed, cutbacktrack(BTOP).

kullanici\_komutu(\_).

Derleyici, cümleleri determinism bakımından kontrol eden yüklemdeki cutbacktrack yüklemini tanımaz. Yani check\_term direktifini kullanırken non-deterministic cümle uyarısı alınabilir. Dinamik kesme kullanırken çok dikkatli olmak gerekir. Çünkü programın tamamını tahrip etmek, programı çalışamaz hale getirmek mümkündür.

**8.15. Programlama Stilleri**

Visual Prolog’da program yazarken dikkat edilmesinde fayda olan bazı temel özellikler vardır. Bu özellikler artık kural haline gelmiştir. Etkili programlama yapabilmek için şu kurallara dikkat edilmelidir:

*Kural 1. Fazla yüklem yerine daha fazla değişken kullanın*

Bu kural programın okunabilirliği ile ters orantılıdır. Genelde Prolog’un dekleratif olan stili, diğer konvansiyonel yaklaşımlara göre daha az verimlidir. Örneğin, bir listenin elemanlarını tersine çeviren bir yüklem yazmak için aşağıdaki program parçası kullanılabilir:

tersine\_cevir(A, B):- tersine\_cevir1(\[\], A, B).

tersine\_cevir1(B, \[\], B).

tersine\_cevir1(A1, \[U|A2\], B):- tersine\_cevir1(\[U|A1\], A2, B).

*Kural 2. Çözüm olmadığı zaman program çalışmasının etkili bir biçimde bittiğinden emin olun*

Yazdığımız bir maksimum\_deger yüklemiyle bir listedeki tamsayıların büyük bir sayıya kadar düzenli olarak arttığını, daha sonra yine düzenli bir şekilde azaldığını kontrol etmek istiyoruz. Bu yüklemi kullanarak

maksimum\_deger(\[1, 2, 5, 7, 11, 8, 6, 4\]) şeklindeki bir sorgu başarılı olur. Fakat

maksimum\_deger(\[1, 2, 3, 9, 6, 8, 5, 4, 3\]) başarısız olur.

*Kural 3. Geriye İz Sürme mekanizmasını mümkün olduğunca çok kullanın.*

esitlik seklinde tanımlanan bir yüklemin iki listenin elemanlarını karşılaştırmak için kullanalım. Bunun için:

esitlik(\[\], \[\]).

esitlik(\[U|X\], \[U|Y\]):- esitlik(X, Y)

kullanmak gereksizdir. Çünkü bunun yerine daha basit olan esitlik(X, X) kullanılabilir.

*Kural 4. Rekursiyon veya Tekrarlama Yerine Geriye İz Sürme Mekanizmasını Kullanın*

Geriye İz Sürme mekanizması bellek ihtiyacını azaltır. Bu yüzden rekursiyon yerine repeat-fail kombinasyonunu kullanmak gerekir. Bu konu hakkında birkaç örnek verelim.

Alt hedefleri tekrarlı bir şekilde kullanmak için genelde basla gibi bir yüklem tanımlayıp sonuçları hesaplamak gerekir.

**Örnek:**

basla:-

readln(X), islem\_yap(X, Y), write(Y), basla.

Bu tür bir tanımlama gereksiz yere rekursiyon yapar. islem\_yap(X,Y) non-deterministic ise sistem tarafından gereksiz olan bu rekursiyon otomatik olarak ortadan kaldırılabilir.

Bu durumda repeat...fail ikilisi kullanmak gerekir. Bunun için yukarıdaki işlemleri şöyle yazmak mümkündür.

basla:-

tekrar, readln(X), islem\_yap(X, Y), write(Y), fail.

fail komutu, islem\_yap yükleminine geriye dönüş yapar, buradan da tekrar yüklemine geçer, bu yüklem daima başarılı olur. Burada önemli olan şey bu döngünün dışına çıkmaktır. Genelde döngü dışına çıkmak için belli şartlar aranıldığı için, döngü içine bu şartı yazmak mümkündür. Yani:

basla:-

tekrar, readln(X), islem\_yap(X, Y), write(Y), bitisi\_kontrol\_et(Y), !.

**8.15. Cut Yüklemini Yerleştirmek**

check\_determ direktifi, cut yükleminin nereye yerleştirilmesi gerektiği konusunda karar verirken çok faydalıdır. Non-deterministic davranışı olan cümlecikleri deterministic hale getirip geriye dönüşü engellemek için cut kullanılmadır.

Böyle bir durumda genel bir kural olarak şunu söyleyebiliriz: cut komutunu, programın mantığını bozmayacak şekilde, mümkün olduğuca bir kuralın başına yakın bir yere konulmalıdır. Derleyici aşağıdaki iki kuralı dikate alarak bir cümleciğin deterministic veya non-deterministic olduğuna ;

Cümlede cut yoksa ve cümlenin başındaki argümanlarla eşleşebilecek başka bir cümlecik varsa

Cümle gövdesinde non-deterministic başka bir yükleme çağrı varsa ve non-deterministic olan bu çağrıdan sonra cut yoksa bulunarak karar verilir.

**9. ÖZEL GELİŞTİRİLMİŞ PROLOG ÖRNEKLERİ**

**9.1. Küçük bir Uzman Sistem örneği**

Bu örnekte, bazı özellikleri hakkında kullanıcıya soru sorarak 7 hayvandan biri bulunacaktır. Bu hayvanlar hakkında bilinen olgulardan hareketle geriye dönüş mekanizması kullanılarak doğru cevap bulunmaya çalışılacaktır.

DATABASE

xpositif(symbol,symbol)

xnegatif(symbol,symbol)

PREDICATES

nondeterm aranan\_canli(symbol)

nondeterm canli\_turu(symbol)

soru\_sor(symbol,symbol,symbol)

sakla(symbol,symbol,symbol)

positif(symbol,symbol)

negatif(symbol,symbol)

olgulari\_sil

basla

CLAUSES

aranan\_canli(cita):-

canli\_turu(memelil),

canli\_turu(etobur),

positif(sahiptir,sari\_kahverengi\_renklere),

positif(sahiptir,siyah\_benekler).

aranan\_canli(tiger):-

canli\_turu(memeli),

canli\_turu(etobur),

positif(sahiptir, sari\_kahverengi\_renkler),

positif(sahiptir, siyah\_seritli).

aranan\_canli(zurafa):-

canli\_turu(tirnakli),

positif(sahiptir,uzun\_boyunlu),

positif(sahiptir,uzun\_bacakli),

positif(sahiptir, siyah\_benekler).

aranan\_canli(zebra):-

canli\_turu(tirnakli),

positif(sahiptir,siyah\_seritli).

aranan\_canli(devekusu):-

canli\_turu(kus),

negatif(eylem,ucar),

positif(sahiptir,uzun\_boyunlu),

positif(sahiptir,uzun\_bacakli),

positif(sahiptir, siyah\_beyaz\_renk).

aranan\_canli(penguen):-

canli\_turu(kus),

negatif(eylem,ucar),

positif(eylem,yuzer),

positif(sahiptir,siyah\_beyaz\_renk).

aranan\_canli(albatros):-

canli\_turu(kus),positif(eylem,iyi\_ucar).

canli\_turu(memeli):-

positif(sahiptir,tuylu).

canli\_turu(memeli):-

positif(eylem,sut\_verir).

canli\_turu(kus):-

positif(sahiptir,kus\_tuyleri).

canli\_turu(kus):-

positif(eylem,ucar),

positif(eylem,yumurtlar).

canli\_turu(etobur):-

positif(eylem,et\_yer).

canli\_turu(etobur):-

positif(sahiptir,sivri\_disleri),

positif(sahiptir, pencelere),

positif(sahiptir,patlak\_gozler).

canli\_turu(tirnakli):-

canli\_turu(memeli),

positif(sahiptir,toynaklar).

canli\_turu(tirnakli):-

canli\_turu(memeli),

positif(eylem,gevis\_getirme).

positif(X,Y):-

xpositif(X,Y),!.

positif(X,Y):-

not(xnegatif(X,Y)),

soru\_sor(X,Y,evet).

negatif(X,Y):-

xnegatif(X,Y),!.

negatif(X,Y):-

not(xpositif(X,Y)),

soru\_sor(X,Y,hayir).

soru\_sor(X,Y,evet):-!,

write(X," aranan canli:",Y,'\\n'),

readln(Cevap),nl,

frontchar(Cevap,'e',\_),

sakla(X,Y,evet).

soru\_sor(X,Y,hayir):-!,

write(X," aranan canli: ",Y,'\\n'),

readln(Cevap),nl,

frontchar(Cevap,'h',\_),

sakla(X,Y,hayir).

sakla(X,Y,evet):-

assertz(xpositif(X,Y)).

sakla(X,Y,hayir):-

assertz(xnegatif(X,Y)).

olgulari\_sil:-

write("\\n\\nBitirmek icin space tusuna basiniz.\\n"),

retractall(\_,dbasedom),readchar(\_).

basla:-

aranan\_canli(X),!,

write("\\n Aradiginiz canli bir ",X, "olabilir."),

nl,nl,olgulari\_sil.

basla :-

write("\\nAradiginiz canliyi bulmak mumkun degildir.\\n\\n"),

olgulari\_sil.

GOAL basla.

Veritabanındaki her hayvan, sahip olduğu veya olmadığı bazı özelliklerle tanımlanmıştır. Kullanıcının cevaplayacağı sorular olumlu(A, B) veya olumsuz(A, B) şeklindedir. Sorulan bir soruya evet veya hayır şeklinde cevap aldıktan sonra, verilen cevabın veritabanına eklenmesi gerekir. Böylece program karar verirken eski bilgileri kullanır. Burada olumlu ve olumsuz olmak üzere sadece iki yüklem kullanılmıştır.

database

xpozitif(symbol, symbol)

xnegatif(symbol, symbol)

Böylece aradığımız hayvanın tüylü değilse, xnegative(vardir, tuy) şeklindeki olguyu kullandık. Pozitif ve negatif kurallar, kullanıcının verdiği cevabın önceden bilinip bilinmediğini kontrol eder.

pozitif(X,Y):-

xpozitif(X,Y),!.

pozitif(X,Y):-

not(xnegatif(X,Y)),

soru\_sor(X,Y,evet).

negatif(X,Y):-

xnegatif(X,Y),!.

negatif(X,Y):-

not(xpozitif(X,Y)),

soru\_sor(X,Y,hayir).

Pozitif ve negatif kurallarının ikinci kuralı, kullanıcıya yeni bir soru sormadan önce arada bir zıtlık olup olmadığını kontrol eder. Tanımladığımız soru\_sor yüklemi kullanıcıya soru sorar ve alınan cevapları düzenler. Cevap e ile başlarsa olumlu, h ile başlarsa olumsuz olarak kabul edilir.

ask(X,Y,yes):-!, write(X," it ",Y,'\\n'), readln(Reply),nl,

frontchar(Reply,'y',\_), remember(X,Y,yes).

ask(X,Y,no):-!, write(X," it ",Y,'\\n'), readln(Reply),nl,

frontchar(Reply,'n',\_), remember(X,Y,no).

remember(X,Y,yes):-assertz(xpositive(X,Y)).

remember(X,Y,no):-assertz(xnegative(X,Y)).

clear\_facts:-write("\\n\\nÇıkmak için boşluk tuşuna basınız\\n"), retractall(\_,dbasedom),readchar(\_).

**9.2. Basit bir yön problemi**

Türkiye’deki birkaç şehir arasındaki en uygun yolu bulmak için bir program yapalım. Program bize iki şehir arasında yol olup olmadığını sorsun. Vereceğimiz cevaba göre en uygun yolu bize göstersin. Burada geriye iz sürme ve rekursiyon metotlarını kullanacağız.

DOMAINS

sehir = symbol

mesafe = integer

PREDICATES

nondeterm yol(sehir,sehir,mesafe)

nondeterm guzergah(sehir,sehir,mesafe)

CLAUSES

yol(mardin,sanliurfa,190).

yol(gaziantep,mardin,320).

yol(sanliurfa,gaziantep,146).

yol(sanliurfa,elazig,348).

yol(gaziantep,elazig,540).

guzergah(\_1\_Sehir,\_2\_Sehir,Mesafe):-

yol(\_1\_Sehir,\_2\_Sehi, Mesafe).

guzergah(\_1\_Sehir,\_2\_Sehir,Mesafe):-

yol(\_1\_Sehir,X,Mesafe1),

guzergah(X,\_2\_Sehir,Mesafe2),

Mesafe=Mesafe1+Mesafe2, !.

GOAL guzergah(sanliurfa,elazig, Toplam\_Mesafe).

Yol yüklemi için kullanılan her bir cümlede, bir şehirden diğerine olan yolun km cinsinden değeri verilmiştir. guzergah yüklemi ise iki şehir arasında yol olduğunu göstermektedir. Güzergahı takip eden bir sürücünün mesafe parametresiyle gösterilen miktarda gideceği belirtilmiştir. Burada güzergah yüklemi rekursiv olarak tanımlanmıştır. Güzergah, birinci cümlede olduğu gibi sadece tek yol olabilir. Bu durumda toplam mesafe sadece iki şehir arasındaki yoldur. Bir şehirden diğerine gittikten sonra ana hedefe gidiliyorsa, bu durumda toplam yol Mesafe1+Mesafe2 olur.

**9.3. Hazine Avcısı**

Labirent biçimindeki dehliz ve mağaralardan oluşan bir yerde gizli bir hazine bulunsun. Aynı yerden tekrar geçmeden, tehlikeye yakalanmadan giriş noktasından başlayıp emniyetli bir şekilde çıkıştan geçmek ve hazineyi almak için hangi yolu takip etmeliyiz?

Önce hazinenin yerini gösteren haritaya bakalım.

DOMAINS

oda = symbol

odalarin\_listesi = oda\*

PREDICATES

nondeterm galeri(oda,oda)

nondeterm komsu\_oda(oda,oda)

buralara\_girmek\_tehlikeli(odalarin\_listesi)

nondeterm git(oda,oda)

nondeterm guzergah(oda,oda,odalarin\_listesi)

nondeterm eleman(oda,odalarin\_listesi)

CLAUSES

galeri(giris,canavar).

galeri(giris,cesme).

galeri(cesme,bataklik).

galeri(cesme,gida).

galeri(cikis,hazine).

galeri(cesme,denizkizi).

galeri(haydut,hazine).

galeri(cesme,haydut).

galeri(gida,hazine).

galeri(denizkizi,cikis).

galeri(canavar,hazine).

galeri(hazine,cikis).

komsu\_oda(X,Y):-galeri(X,Y).

komsu\_oda(X,Y):-galeri(Y,X).

buralara\_girmek\_tehlikeli(\[canavar,haydut\]).

git(Baslama\_noktasi,Bitis\_noktasi):-

guzergah(Baslama\_noktasi,Bitis\_noktasi,\[Baslama\_noktasi\]).

git(\_,\_).

guzergah(Oda,Oda,Gidilen\_odalar):-

eleman(hazine,Gidilen\_odalar),

write(Gidilen\_odalar),nl.

guzergah(Oda,Cikis\_yolu,Gidilen\_odalar):-

komsu\_oda(Oda,Sonraki\_oda),

buralara\_girmek\_tehlikeli(Tehlikeli\_odalar),

not(eleman(Sonraki\_Oda,Tehlikeli\_odalar)),

not(eleman(Sonraki\_Oda,Gidilen\_odalar)),

guzergah(Sonraki\_Oda,Cikis\_yolu,\[Sonraki\_Oda|Gidilen\_odalar\]).

eleman(X,\[X|\_\]).

eleman(X,\[\_|H\]):-eleman (X,H).

GOAL git(cikis, giris).

Buradaki her dehliz bir olguyla temsil edilmiştir. git ve guzergah yüklemleri kuralları belirler. Sorgudan elde edeceğimiz cevapta hazineyi alıp emniyetli bir şekilde dışarı çıkmak için gerekli güzergah belirtilecektir. Programdaki önemli bir özellik, rekursiv olarak tanımlı olan guzergah sayesinde gidilen odaların kataloga alınmasıdır. Çıkış odasına geldiğiniz anda üçüncü parametre o ana kadar ziyaret ettiğiniz odaları listeler. Bu odalar arasında hazine var ise, hedefe varıldı demektir. Eğer listede hazine odası yoksa, Sonraki\_oda seçeneği tehlikeli odalara gidilmeyecek şekilde genişletilir.

**TARTIŞMA VE SONUÇ**

Yapay Zeka kavramı ortaya çıktıktan sonra, yurtdışında bu konuda çok sayıda teorik çalışma, değişik disiplinlerde kullanılan birçok uygulama program gerçekleştirilmiştir. Bu programlar sayesinde, bir insan tarafından yapılması çok zaman alabilen ve hata oranı oldukça yüksek olabilen durumlar ortadan kalkmıştır. Örneğin Digital firması yetkilileri, müşterilerinin siparişlerine göre yeni bir sistem dizaynı yaparken, bu sistemde kullanılabilecek donanım seçeneklerinin çokluğu, her bir parçanın birden fazla parça ile uyumlu çalışabilmesi veya bazı parçaların birbirleriyle hiç uyuşmaması gibi durumlardan dolayı, yapılan montajlarda büyük oranda hataların ortaya çıktığını; ancak yazılan bir uzman sistem ve parçalar hakkındaki gerçeklerden oluşan bir bilgi veritabanı ile bu durumun ortadan kalktığını, ayrıca yılda milyonlarca dolar tasarruf sağladıklarını belirtmişlerdir. Bunun haricinde farklı alanlarda kullanılmak üzere hazırlanan ve başarılı bir şekilde çalışan çok sayıda uzman sistem örneği vermek mümkündür.

Tıpta teşhis ve tedavi planlaması amacıyla bilgi tabancı sistemler, birçok alanda (Örneğin Laboratuar, Onkoloji veya Kardiyoloji gibi) kullanım sahası bulmaktadır. Diş tedavisi alanında bilgisayar kullanımı daha ziyade sadece kayıt amaçlı kullanılmaktadır. Karlsruhe’deki Diş Hekimliği Akademisi ile Bremen Üniversitesi Yapay Zeka Laboratuarı arasında işbirliği yapılarak, bir yazılım geliştirilmiştir. Bu çalışma, diş doktorları için bilgi tabanlı bir dökümantasyon ve karar verme sisteminin oluşturulmasını sağlamaktadır. Sistemin kullanılması halinde, diş hekimliği ile ilgili teşhis ve tedavi önerileri yapılabilmektedir.

Türkiye’de ise, bu alanda çok ciddi çalışmaların var olduğunu söylemek çok zordur. Gebze Yüksek Teknoloji Enstitüsü’ndeki Yapay Zeka Bölümü’nde, askeri amaçlı projeler üzerinde çalışmalar yürütülmektedir. Ayrıca Bilkent ve Orta Doğu Teknik Üniversitelerinde yürütülmekte olan TurkLang gibi büyük projeler mevcuttur. Fakat bu çalışmaların çoğu Unix ortamında yapılmakta olup, bireysel ve endüstriyel kullanıma yönelik değildir.

Yapay Zeka ve bunun alt bölümleri olarak kabul edilen Uzman Sistemler, Yapay Sinir Ağları, Tabii Dil İşlenmesi gibi alanlarda program yapmak için mantık dillerinin yanı sıra, Pascal, C++ gibi konvansiyonel programlama dilleri de kullanılmaktadır. Prolog (**Pro**gramming in **Log**ic) mantık dillerinden en popüler olanıdır. Önceleri daha çok Unix, VAX gibi işletim sistemleriyle çalışan anaçatı bilgisayarlarda kullanılan Prolog, zamanla DOS, daha sonraları ise Windows ve diğer işletim sistemlerine de aktarılmıştır. Visual Prolog, işte bu aşamalardan sonra çıkarılan, çoklu ortamlarda rahatlıkla kullanılabilen bir mantık dilidir. Visual Prolog’un diğer konvansiyonel dillerden ayrıldığı bazı özellikler şunlardır:

Visual Prolog prosedürel değil tamamen dekleratif bir yapıya sahiptir. Yani çözümü aranan bir problemin nasıl çözüleceğini tanımlamak yerine, problemin kendisini tanımlamak yeterlidir. Kullanıcı tarafından verilen gerçeklere dayanarak, Prolog’da var olan Inference Engine(Karar verme motoru) istenilen problem için mümkün olan bütün çözümleri bulur.

Visual Prolog’daki **Geriye İz Sürme** mekanizması, konvansiyonel dillerin hiçbirinde bulunmayan güçlü bir özelliktir. Bu özellik sayesinde konvansiyonel dillerdeki FOR..NEXT, DO..WHILE gibi döngüler ortadan kalkar. Prolog, bu özelliği sayesinde, çözüm aranan bir sorguya uygun bütün çözümleri kendiliğinden bulur. Bu durum, döngü komutlarının neden olabileceği hataları baştan itibaren ortadan kaldırır.

Visual Prolog’un diğer bir özelliği ise, nesneler arasındaki ilişkilerin çok kolay bir şekilde tanımlanabilmesi, bu ilişkilere dayalı işlemler yapabilmesidir. Örneğin, kullanilir(“Visual Prolog”, uzman\_sistemler) şeklinde ifade edilebilen ‘Visual Prolog dili uzman sistemlerde kullanılır’ cümlesini, konvansiyonel dillerle ifade etmek mümkün değildir.

Visual Prolog ile uygulama Programları yazarken, nesneler arasındaki ilişkileri ifade etmek son derece kolay olmasına rağmen, uygulamanın sonuçları hakkında Türkçe bilgi vermek ve Türkçe’de düzgün cümleler kurmak açısından bazı zorluklar mevcuttur. Bunun temel nedeni, İngilizce ve Türkçe cümle yapılarında öğelerin dizilişlerinde farklılıklar bulunmasıdır. Bu yüzden, Türkçe ifade edilen bir cümlede, özne ve yüklem arasında akıcı bir ilişki kurabilmek için, öğeler arasındaki özelliklerin önceden veritabanına yüklenmesi faydalı olacaktır. Bu çalışma sayesinde, Prolog’un Türkçe’ye uyarlanmasında karşılaşılan problemler detaylı olarak ele alınmış, problemlerin en doğru şekilde nasıl çözümlenebileceği konusunda bazı yazılımlar geliştirilmiştir.

Visual Prolog kullanarak yapay zeka konusunda çalışma yapacaklar için önemli birçok ipuçları örneklerle verildiği bu tez çalışması sayesinde, yapay zeka alanında Türkçe uygulamalarda önemli gelişmeler sağlanabilecektir.

**KAYNAKLAR**

(1) STERLING; Leon; SHAPHIRO, Ehud; The Art of Prolog, Advanced Programming Techniques, The MIT Press, London, England, 1992.

(2) CLOCKSIN, W.F, MELLISH, C.S, Programming in Prolog, Springer-Verlag Berlin Heidelberg, Germany, 1987.

(3) O’KEEFE, Richard A.; The Craft of Prolog, The MIT Press, London, England, 1990

(4) CASTILLO, E., ALVAREZ, E., Expert Systems: Uncertainity and Learning, Computational Mechanics Publications, Southampton, Boston, America, 1991

(5) GIARRATANO, JOSEPH. C, Expert Systems: Principles and Programming, PWS-KENT Publishing Company, Boston, America,1989.

(6) IGNIZIO, JAMES. P., Introduction to Expert Systems, McGraw-Hill, Inc., America, 1991.

(7) PDC, Visual Prolog Language Tutorial, Copenhagen, Denmark, 1996.

(8) KUŞ, M.; VAROL, A.; OĞUROL, Y.; VAROL, Y.: Verarbeitung von unsiherem Wissen mit Fuzzy-Prolog, Second Turkish-German Joint Computer Application Days, 15-16 October, Konya, 1998

(9) OĞUROL, Y.; VAROL, A.; KUŞ, M.: Anforderungen und Lösungsansätze einer transferierbaren Entwicklungsumgebung für die medizinische Wissenverarbeitung, Second Turkish-German Joint Computer Application Days, 15-16 October, Konya, 1998.

(10) VAROL, A.; VAROL, N.: ESTA İle Bilgisayar Destekli Eğitim, Beta Basım Yayım Dağıtım A.Ş., 299, 1996.

(11) VAROL, A.; VAROL, N.: ESTA Bilgisayar Yazılımı İle Uzman Sistemlerin Hazırlanması Teknikleri, Süleyman Demirel Üniversitesi, Makine Mühendisliği Dergisi, Cilt 1, Sayı 9, 67-72, 1996.

(12) KUŞ, M.; VAROL, A.; OĞUROL, Y.: Uzman Sistemin Dişçilik Alanında Kullanımına Ait Bir Uygulama, Endüstri&Otomasyon, Aylık Elektrik, Elektronik, Makine, Bilgisayar ve Kontrol Sistemleri Dergisi, Sayı: 18, 1998

(13) KUŞ, M.; VAROL, A.; OĞUROL, Y.: Uzman Sistemin Dişçilik Alanında Kullanımına Ait Bir Uygulama, Endüstri&Otomasyon, Aylık Elektrik, Elektronik, Makine, Bilgisayar ve Kontrol Sistemleri Dergisi, Sayı: 18, 1998

(14) VAROL, A.; VAROL, N.: Uzman Sistemlerde ESTA Yazılımının Önemi, Bilişim'96, 18-22 Eylül 1996 İstanbul, Bildiriler Kitabı, 289-294, 1996.

(15) VAROL, A.; VAROL, N.: Uzman Sistem Hazırlanırken Hangi Kriterler Göz Önünde Bulundurulmalı, GAP 2. Mühendislik Kongresi, 21-23 Mayıs 1998, Şanlıurfa, Bildiri Kitabı, S: 559-566, 1998.

**ŞEKİLLER ve TABLOLAR**

** **Şekil 1. Aile Fertlerinin Şecere Olarak Gösterilmesi 88

Şekil 2. Şekil 6.1’deki ağaç yapısında **Aşağıya-Doğru-Arama*** *metodunun uygulanması. 90

Şekil 3. Binary tarama yapısı 94

Tablo 3.1: Visual Prolog’da Tipler ve Alabilecekleri değerler. 25

Tablo 7.2. Listelerin baş ve kuyruk halinde gösterilmeleri 100

Tablo 7.3: Liste eşleştirme örnekleri................................................................... 101

Tablo 8.4. Criticalerror yükleminin argümanlarının aldığı değerler 134

PAGE 2

PAGE x

PAGE xi

PAGE 16

---
*Kaynak: `PROLOG İLE UZMAN SİSTEM HAZIRLAMA/PROLOG İLE UZMAN SİSTEM HAZIRLAMA.doc` — Yavuz Selim AYDIN — 2004*
