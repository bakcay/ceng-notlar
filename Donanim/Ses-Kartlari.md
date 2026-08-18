# Ses Kartlari

**Ses Kartlari**
İlk IBM uyumlu PC dizayn edildiginde bir is makinesi olarak dizayn edilmisti. Dolayisiyla içerisinde bir ses isleme mimarisi bulunmuyordu. Ve bilgisayarlar uzun süre ses olarak sadece uyari mesajlarini üretebildi. Macintosh beep ve klik seslerinden daha gerçekçi sesler üretebilen eklentilerini üretti, ama PC'ler hala entegre ses sistemlerine sahip degildi. Bu yüzden hala sonradan eklenen ses kartlari kullaniliyor...

**Sesin Anatomisi**
Iki veya daha fazla nesne etkilestiginde, enerjisi sürekli degisen bir dalga yayar. Bu dalga etrafinda hava basinci yaratir. Ve beyin bunu ses olarak algilar.

Ses bir mikrofondan kaydedildiginde, mikrofonun diyaframina uyguladigi basinç, o anki degisimlerine bagli olarak analog bir elektrik akimina dönüsür. Böylece ses dalgasi kaydedilmis olur.

**Ses Kartinin Yapisi**
Modern bir ses karti içerisinde sesi kaydedecek ve olusturacak birimler içerir. Ses olusturmada iki temel yol vardir:

FM synthesiser ile

Dijitallestirilmis ya da örneklenmis ses ile

Ses karti içerisinde 16 bitlik (ses kartina bagli) Dijital-Analog (DAC) ve Analog-Dijital (ADC) dönüstürücüleri ve bir programlanabilir örnek zamanlayici vardir. Bilgisayar bilgiyi dönüstürücülerden okur veya dönüstürücülere gönderir. Örnek zamanlayici da dönüstürücülerin PC tarafindan kontrolünü saglar. Bu sesin örnekleme frekansini belirler.

Çogu ses karti bir veya daha fazla direk bellek erisimi (DMA) kanali kullanarak ses donanimindan yazar ve ondan okur. DMA tabanli ses kartlari çalma ve kaydetme islemi için kanallari kullanirlar. Eger kart Full-Duplex ise çalma ve kaydetme için ayri birer kanal vardir. Eger Half-Duplex ise ayni kanali paylasirlar. Bu yüzden kayit yapilirken bir seyler çalinmasi mümkün degildir.

**Frekans Modülatör. (FM)**
1970'lerde Stanford Üniversitesinden Dr. John Chowning ses kartlarinda kullanilan ilk frekans modülasyon teknolojisini gelistirdi. FM synthesiser'lar tasiyici denen bir sinüs dalgasi olusturur ve onu modülatör denen ikinci bir dalga ile birlestirir. Iki dalganin da frekansi esitlendiginde ortaya kompleks bir dalga çikar. Tasiyici ve modülatör dalganin degisimleri ile enstrüman sesleri olusturulabilir.

**WaveTable**
WaveTable sesi yaratmak için tasiyici ya da modülatör kullanmaz, gerçek enstrüman ses örneklerini kullanir. Bu örnekler enstrümanin olusturdugu ses dalgasinin dijital canlandirmasidir. ISA tabanli ses kartlari üzerindeki ROM'da bunu tasirlar, daha yeni PCI ses kartlari ise bilgisayarin kendi RAM'ini kullanir. Bilgisayar açildiginda sürücü tarafindan örnekler RAM'e yüklenirler. Böylece örnekler yenilenebilir.

**Örnekleme ve Kayit**
Ses karti analog bir sesi kaydettiginde, ses dalgasi dijital bilgiye çevrilip kaydedilir. Kaydedileni duymak için ses karti dijital bilgiyi alip analoga çevirir ve çikisa verir.

Analogu dijitale çevirme islemine örnekleme denir. Ses dalgasi belli araliklarla parçalara bölünür. Ve analog degeri dijital degere çevirir. Ses ne kadar fazla parçaya bölünürse yani bölünme frekansi arttirilirsa ses daha gerçekçi hale gelir.

CD'de örnekler 16 bitlik dinamik siralarda 44.1 kHz örnekleme frekansi ile saklanirlar. Bu saniyede 44100 parçalik ve genligi 16 bitlik bir sayi olan dalgadir.

Çogu ses karti sesi 16 bitlik çözünürlükte 44.1 veya 48 kHz'de örnekler. Daha düsük degerlere de inebilir. Iyi bir ses karti düsük seviyeli parazit ve Dijital-Analog Analog-Dijital dönüstürücüleri ile dikkat çeker.

---
*Kaynak: `SES KARTLARI/SES KARTLARI.doc` — abdullah — 2004*
