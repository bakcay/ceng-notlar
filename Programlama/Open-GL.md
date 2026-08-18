# Open GL

***ÖNEMLİ NOT**** *

*Tüm bu seri boyunca okuyucunun C/C++ bildiği varsayılacak ve teknik terimlerin açıklamaları düzenli bir şekilde verilecektir. Tüm kod örnekleri **Courier** fontu ile yazılacak ve aksi belirtilmedikçe C++ olacaktır. Okuyucunun Visual C++ 6 (ya da üzeri / uyumlu bir C++ derleyicisi) kullandığı varsayılacaktır. *

**Bölüm 1: Sistem Altyapısı**

**A- SIMD mimarisi hakkında ön bilgi**

Bu yazı grafik programlama ile ilgili olmasına rağmen, ilk önce elimizdeki sistemi tanıyarak ve bazı kurallar koyarak başlayacağız.

Bilgisayarlar 1983'den bu yana oldukça fazla gelişmelerine rağmen aynı taban üzerinde ayakta kalmaktalar. Süreklilik gerektiren işlerde oldukça yetenekliler, fakat düzensiz işlemlerde, örneğin değişken bir üç boyutlu sahneyi işlemekte, oldukça yavaşlar. Oyunlarda sıkça yapılan şeylerden birisi bu şekildeki verinin işlenmesi oldugu için, bu seride ilk yapacağımız şey, bilgisayarların ne olduğunu (ve olmadığını) öğrenmek ve bu kısıtlamanın üstesinden nasıl gelineceğini öğrenmek olacak.

Bir günümüz bilgisayarı:

*1- Doğrusal ve uzun bloklar halindeki işlemleri daha hızlı yapabilir. *

*2- Ne kadar az hafıza erişimi yaparsa o kadar hızlı çalışır. *

*3- Elimizdeki "düzensiz" veri miktarı arttıkça adresleme hataları da o denli artar. *

Tüm bunlar, Intel'in ve diğer firmaların şu anda kullandığı SIMD (Single Instruction Multiple Data = Tek komutta birden çok veri) tarzı işletim ile neredeyse tamamen örtüşen bir durum oluşturuyor. İlk kısıtlamamiz, bize uzun blokların tek seferde daha hızlı işlendiğini söylüyor, bu da tam olarak SIMD'nin yaptığı şey, uzun blokları tek seferde işlemek. Diğer iki kısıtlama bize adres çözme işleminin problemlerini, yani "cache miss" ve "misalign" sorunlarını anlatıyor. "Cache miss" ile kastedilen, bir adres çözme işlemi sonucu erişilecek verinin kaşe bellekte bulunmadığının anlaşılıp yeniden bir adres çözme işlemine yol açması. "Misalign" ise çözülen adresin 8 (ya da şimdilerde 16 byte)'ın katlarına denk gelmemesi, örneğin hafızanın 3. byte'ında bulunması sonucu gereksiz miktarda verinin birden çok kez okunmasına yol açmasına verilen isim.

Şimdi bu ufak tablodaki kısıtlamalardan kurtulmak için bu seri boyunca uyacağımız kurallara bir göz atalım:

*1- SIMD ve/veya SIMD2 işlemlerine ağırlık vermek ya da bunlara dönüşebilir şekilde kod yazmak. *

*2- Veriyi daima "hizalanmış" hafıza adreslerinden başlatmak. *

*3- Veriyi daima 16 byte'ın katları olarak tutmaya çalışmak, mümkünse {X,Y,Z} gibi sırasız veri akışını {X\[\],Y\[\],Z\[\]} haline getirmek. *

Üçüncü madde biraz karışık gelebilir. Tipik bir programda sakladığımız veri eğer

class nokta

{

float x, y, z;

};

nokta benimNoktalarım\[1024\];

ise, bu SIMD için daha uygun olan:

class yogunNokta

{

float x\[1024\], y\[1024\], z\[1024\];

};

yogunNokta benimNoktalarim;

şeklinde yeniden düzenlenmelidir. Tabii bu şekilde statik veri ayrılması pek önerilen birşey olmadığı için bunu sadece konuyu açıklamak için verdiğimiz bir örnek olarak yorumlamanız gerekiyor, pratikte:

class yogunNokta

{

float \*x,\* y, \*z;

};

yogunNokta benimNoktalarim;

x=(float\*) aligned\_malloc( 1024 \* sizeof(float), 16);

y=(float\*) aligned\_malloc( 1024 \* sizeof(float), 16);

z=(float\*) aligned\_malloc( 1024 \* sizeof(float), 16);

daha doğru bir yaklaşım. Buradaki aligned\_malloc komutu 16 byte'ın katı olan bir adresten başlayacak şekilde bellek ayırmamızı sağlıyor.

**B- Optimizasyon**

Kullandığımız sistem, herşeyden önce, saf C/C++ kodunun daima en basit hedef işlemciye göre (zorlanmadıkça) derlendiği bir sistemdir. Yani yazdığımız aşağıdakine benzer bir satır, eğer biz derleyiciyi buna zorlamazsak, 80386'da hızlı çalışacak şekilde derlenir:

float fArray\[16\] = {1.0f, 4.6f, 12.0f, 43.0f, 61.0f, 52.0f, 2.0f, 1.0f, 3.0f, 4.0f, 6.0f, 13.0f, 421.0f, 54.0f, 654.0f, 1.0f};

for(unsigned long i=0; i<16; i++)

{

fArray\[i\] \*= 2.49f;

}

Bunun assembly karşılığı, standart derleyici çıktısı olarak:

xor eax, eax

$loop1:

fld DWORD PTR \_fArray$\[esp+eax\*4+64\]

fmul DWORD PTR \_\_real@401f5c29

inc eax

cmp eax, 16

fstp DWORD PTR \_fArray$\[esp+eax\*4+60\]

jb SHORT $loop1

olacaktır. Birinci kuralı ihlal ettik. Burada işlemcinin FPU kısmı kullanılarak aynı anda sadece bir sayı ile çarpma yapılmaktadır. Bunun yerine eğer bir P3/P4 derleyicisi ve el ile optimizasyon yöntemleri kullanırsak yukarıdaki kod şu şekli alır:

float fArray\[16\] = {1.0f, 4.6f, 12.0f, 43.0f, 61.0f, 52.0f, 2.0f, 1.0f, 3.0f, 4.0f, 6.0f, 13.0f, 421.0f, 54.0f, 654.0f, 1.0f};

float fPack\[4\] = {2.49f, 2.49f, 2.49f, 2.49f}; // 4 adet çarpan

float \*p1,\*p2;

p1 = &(fArray\[0\]);

p2 = &(fPack\[0\]);

\_asm{

mov ecx,4

mov eax, p2

movups xmm1, \[eax\]

mov eax, p1

mLoop1:

movups xmm0, \[eax\]

mulps xmm0, xmm1

movups \[eax\], xmm0

add eax, 0x10 // 16, 4 tane 4 byte(float)

loop mLoop1

};

Görüldüğü gibi artık tek komutta aynı anda dört çarpma yaparak daha uzun fakat daha hızlı bir kod elde ettik. Buradan da şu yeni kural çıkıyor:

*Uzun kod daha hızlı çalışabilir. *

Tabii bu kullanılan işlemciye göre değişeceği için OpenGL ya da DirectX gibi kütüphanelerde aynı rutin birden fazla işlemciye göre yeniden yazılmış şekillerde bulunurlar.

**Bölüm 2: OpenGL** ** **

**A- OpenGL mi DirectX mi?**

Yeni programlamaya başlayanlar için çok daha az zahmetli olacağına inandığım OpenGL ile seriye başlamak istiyorum. DirectX her ne kadar daha "metale yakın" bir tarza sahip olsa da, burada okuyucunun derleyici ile yüksek bir ihtimalle beraber kurmuş olacağı OpenGL kütüphanelerini kullanacağız. Bu arada çoğu kullanıcının bir çeşit nVidia ya da ATI görüntü kartına sahip olduğunu ve en son OpenGL destekli (beta olmayan) sürücüleri yüklemiş olduğunu da varsayıyoruz.

OpenGL, DirectX'in aksine sürekli genişletilen (ve genişletilebilen) bir altyapıya sahip. Örneğin eğer bir firma bir kartı bu gün piyasaya çıkartır ve "raytrace destekliyor" olduğunu söylerse, bunun için (SGI ile konuşup eklentiyi kayıt ettirmenin yanında) tek yapmaları gereken bir adet "eklenti" yazmak ve bunu sürücülerine dahil etmek olacaktır. DirectX bu şekilde genişletilemez, sadece "yazılım ile render" eklentilerini kabul eder ve bunlar da donanınm ile çalışmazlar, sadece yazılımsal eklerdir ve "yeterince hızlı" değillerdir.

OpenGL desteğimiz tam olduğuna göre, ilk OpenGL testimiz ile işe başlayabiliriz...

**B- Önce biraz ön bilgi **

OpenGL, bir "state machine" dir, yani her an verilen bir konumdadır ve sonraki komutlar bu konumda olunduğu göz önüne alınarak çalışır. Örneğin "ışıklandırma açık" ya da "kapalı" gibi. OpenGL aynı zamanda "batch" komut işletebilir, yani ardışık komutları saklayıp "bitir" sözcüğü ile birtilkte işletmeye alabilir.

Bu yapısı yüzünden OpenGL ile çalışırken her an hangi durumda olduğumuzu kesinleştirmek için uzun işlemler öncesi yeniden durumlarımızı ayarlarız. Örneğin ekrana yazı yazarken ışıklandırma gereksiz olduğu için kapatırken, sahne çizimini yapan kod parçası ışıkları tekrar açmalıdır. Her durum değişikliği bir çok hesaplama ve/ya da donanıma erişim gerektirdiği için çok iyi bir dizayn yaparak bunları minimum seviyede tutmakta yarar vardır.

Örneğin, her üçgeni çizmeden önce bir doku seçmek son derece yavaş olacaktır, bunun yerine aynı dokuyu paylaşan üçgenleri bir araya toplayıp tek seferde çizmek en iyi metodlardan biridir. Bu yüzdendir ki bazı basit BSP uygulamaları modern kartlarda yavaştır, çünkü sırasız ve düzensiz durum değişikliklerine yol açarlar.

Sıkça kullanılan bir yöntem de bir çok dokuyu tek bir büyük dokunun içerisine toplamaktır, böylece sadece bir kez doku seçilir.

Fakat bu iki probleme yol açar:

*1- Doku gereğinden fazla büyük olur ve ya video belleğe sığmaz ya da yavaş erişime yol açar. *

*2- Doku ufak tutulur, fakat bu sefer ortalama kalite yarıya ya da daha kötü bir orantıya iner. *

Bir başka çare de büyük ve kalitesiz bir dokunun üzerine birden fazla ufak ve detaylı doku konumlandırmaktır. Bu tip dokulara "detay dokusu" adını verebiliriz. En hızlı yöntemlerden biri olmakla birlikte kendine has problemleri (detay dokusunun tekrarladığının belli olması gibi) vardır.

İşte bu tip problemler varken, dokuları ufak tutup bunları bir "lightmap" (ışık dokusu) arkasına saklamak en basit ve hızlı çaredir. Böylece normal doku tekrarlasa bile, yüzeyin her noktasında farkı bir ışık değeri alacağı için tekrarsızmış gibi görünecektir.

**C- Henüz FPS söz konusu değilken...**

İlk yapacağımız şey, Windows alt sisteminden arınmış bir şekilde çalışmak olacak. GLUT kullanarak (openGL Utility Library = OpenGL yardımcı fonksiyon kütphanesi) oluşturduğumuz ilk örnek programımız iki adet üçgen ile bir kare çiziyor ve bunu ışıklandırıp renklendiriyor, fakat henüz doku içermiyor. Programımızın kodunu burada verip sizi yazma zahmetinden kurtarıyoruz:

**[Örnek1.zip](http://www.merlininkazani.com/files/opengl/ornek1.zip)**

Bu kodu Visual C++ 6 ile derleyebilir ve ilk iki üçgenimize bakabilirsiniz. Fakat bundan fazlası için okumaya devam etmeniz gerekiyor...

**D- Adım adım inceleme**

Kodun bir kısmı (GLUT fonksiyonları) gözlerimizden uzakta OpenGL'i bir pencerede başlatıyor ve işin basit kısmı ile bizi başbaşa bırakıyor. Aşağıdaki satırlara bir göz atalım:

void display(void)

{

glClear(GL\_COLOR\_BUFFER\_BIT | GL\_DEPTH\_BUFFER\_BIT);

glColor4f(.2,.4,.2,1.0);

glNormal3f(0.0, 1.0, 0.0);

glBegin(GL\_TRIANGLES);

glVertex3f(-20.0,-15,20.0);

glVertex3f(20.0,-15,20.0);

glVertex3f(-20.0,-15,-20.0);

glVertex3f(20.0,-15,-20.0);

glVertex3f(-20.0,-15,-20.0);

glVertex3f(20.0,-15,20.0);

glEnd();

glutSwapBuffers();

}

Burada sırayla şu işlemleri uyguluyoruz:

*1- **glClear**: ekran dışı belleği sil (renk ve derinlik kanallarının ikisini de) *

*2- **glColor4f**: bundan sonraki noktalar için renk seç (yaklaşık yeşil, %100 opak) *

*3- **glNormal3f**: bundan sonraki noktaların işaret ettiği yönü belirt (tam yukarıya) *

*4- **glBegin**: buradan sonra verilen her üç nokta bir üçgene denk gelecektir (**GL\_TRIANGLES**) *

*5- her 6 nokta için: **glVertex3f**: noktanın uzaydaki konumu *

*6- **glEnd**: bitir (burada OpenGL iki adet üçgeni "gerçekten" çizer) *

*7- **glutSwapBuffers**: GLUT ekran dışı belleği ekrana taşır (böylece çizdiğimizi görebiliriz) *

Buradaki kod, tamamen "inline" (kod içerisinde) bulunan veri ile iki adet yeşil üçgen çiziyor. Dışarıdan dosya okuma gibi işleri sonraki yazılara bırakacağız o yüzden şimdilik böyle olması gerekiyor.

**E- Her noktaya farklı renk**

Yukarıdaki örnekte sadece bir adet glColor komutu yer alıyor. OpenGL bir "durum saklayan makina" (yukarıyı okuyun) olduğu için bu "durum" tüm çizim işlemleri boyunca geçerliliğini koruyor. Eğer iki adet farklı renkte üçgen çizmek istersek kodu şu şekilde değiştirmemiz gerekiyor:

glBegin(GL\_TRIANGLES);

glColor4f(.2,.4,.2,1.0);

glVertex3f(-20.0,-15,20.0);

glVertex3f(20.0,-15,20.0);

glVertex3f(-20.0,-15,-20.0);

glColor4f(.2,.2,.4,1.0);

glVertex3f(20.0,-15,-20.0);

glVertex3f(-20.0,-15,-20.0);

glVertex3f(20.0,-15,20.0);

glEnd();

Böylece bir yeşil bir mavi üçgenimiz oldu. Aslında bir adım daha ileriye giderek her noktaya bir renk verebiliriz:

glBegin(GL\_TRIANGLES);

glColor4f(.2,.4,.2,1.0);

glVertex3f(-20.0,-15,20.0);

glColor4f(.4,.4,.2,1.0);

glVertex3f(20.0,-15,20.0);

glColor4f(.4,.4,.4,1.0);

glVertex3f(-20.0,-15,-20.0);

glColor4f(.2,.2,.4,1.0);

glVertex3f(20.0,-15,-20.0);

glColor4f(.2,.4,.4,1.0);

glVertex3f(-20.0,-15,-20.0);

glColor4f(.4,.2,.4,1.0);

glVertex3f(20.0,-15,20.0);

glEnd();

Değişikliğe dikkat edin, üçgenlerimiz yine bir durum değişkenine uyarak "Gouraud" ışıklandırıldılar, yani kenar noktaları arasında renk değerleri doğrusal olarak dolduruldu.

Bu durumu kontrol eden komut:

glShadeModel(GL\_SMOOTH)

satırı. İsterseniz şimdi diğer bölüme geçip, daha önceden ihmal ettiğimiz "durum" ayarlarına bir göz atalım.

**F- Sahnenin çizim için ayarlanması**

Programımızın yukarıdaki kısmına gelmeden önce kısa bir rutin ile bir takım ayarlar yapmıştık. Bu ayarlar, OpenGL'in aktardığımız veriyi nasıl yorumlayacağını düzenlemek üzere bir ihtiyaç doğdukça yapılan türden, örneğin kameranın konumu değiştiği zaman tekrar bir kamera transformasyonu ayarlamamız gerekiyor. Aşağıdaki kod sırası ile anlatılan işlemleri yapmakta:

// derinlik testi açık

glEnable(GL\_DEPTH\_TEST);

// ışığı renklendir

glLightfv(GL\_LIGHT0, GL\_SPECULAR, isik\_renk);

// ışığı konumlandır

glLightfv(GL\_LIGHT0, GL\_POSITION, isik\_konum);

// ışığı aç

glEnable(GL\_LIGHT0);

// OpenGL ışıklandırma açık

glEnable(GL\_LIGHTING);

// yüzey saklama açık

glEnable(GL\_CULL\_FACE);

// arka yüzeyleri sakla

glCullFace(GL\_BACK);

// ışık ve rengin çalışması için gerekli

glEnable(GL\_COLOR\_MATERIAL);

// gouraud tipi ışıklandırma

glShadeModel(GL\_SMOOTH);

// projeksiyon

glMatrixMode(GL\_PROJECTION);

gluPerspective(

60.0, // 60 derece bakış açısı

1.0, // pixel deformasyon orantısı (y/x)

1.0, // yakın düzlem

10000.0); // uzak düzlem

// kamera transformasyonu

glMatrixMode(GL\_MODELVIEW);

gluLookAt(

10.0, 20.0, 30.0, // göz noktası

0.0, -20.0, 0.0, // hedef

0.0, 1.0, 0.); // yukarı ** **

Burada en önemli durum değişkenimiz GL\_LIGHTING. Eğer bu durumu "enable" ile açık duruma getirmezsek pek birşey görmemiz mümkün değil. Sahnede en az bir adet ışık kaynağı bulunması gerekiyor ki cisimlerin derinlik ve konumlarını algılamamız kolay olsun. Tabii ışıkları aktif hale getirmeden önce glLight() ile konum ve renk bilgisini vermemiz gerekiyor. Göreceğimiz üzere glLight'ın ikinci parametresi pozisyon ya da renk bilgisini vermekte olduğumuzu belirtiyor.

gluLookAt, kamerayı konumlandırmak için kullanabileceğimiz en kolay rutin ve çok basit 3 parametre alıyor:

gluLookAt( kamera\_pozisyonu, hedef\_pozisyonu, yukarı\_vektörü);** **

Burada "yukarı\_vektörü", o anki projeksiyon düzleminin "yukarısı" için kabul ettiği yönü tarif etmek için kullanılıyor. Bunun ile oynayarak, örneğin bir oyunda karakterin adımları ile oluşan sağa-sola yaylanma hareketini (ve bu nedenle oluşan kamera sarsıntısını) vermek mümkün.

Bütün bunları bir araya koyarsak, temel bir OpenGL programının yapısı şu şekilde olmakta:

*1- Sahneyi (ışık ve kamera) hazırla *

*2- Her ekran tazeleme işlemi için, sahneyi sil ve baştan çiz *

Bu şekilde özetlediğimiz kadarıyla, OpenGL dünyanın en kolay grafik arabirimlerinden biri gibi görünmekte. Aslında gücünü de bu basit yapısından alıyor, söz ile anlatabileceğimiz her grafik problemini OpenGL kullanarak ekrana dökmek mümkün.** **

**G- OpenGL komutlarının sözdizimi**

Şu ana kadarki komutların bazıları, eğer fark ettiyseniz, sonlarında 2f, 3f gibi ekler içermekte. Bunun amacı, o komuta verilecek olan parametrelerin türünün kullanıcı tarafindan belirtilebilmesini sağlamak. Örneğin bir glColor4f komutu, aşağıdaki şekilleri alabilir:

void glColor3b(GLbyte red, GLbyte green, GLbyte blue);

void glColor3d(GLdouble red, GLdouble green, GLdouble blue);

void glColor3f(GLfloat red, GLfloat green, GLfloat blue);

void glColor3i(GLint red, GLint green, GLint blue);

void glColor3s(GLshort red, GLshort green, GLshort blue);

void glColor3ub(GLubyte red, GLubyte green, GLubyte blue);

void glColor3ui(GLuint red, GLuint green, GLuint blue);

void glColor3us(GLushort red, GLushort green, GLushort blue);

void glColor4b(GLbyte red, GLbyte green, GLbyte blue, GLbyte alpha);

void glColor4d(GLdouble red, GLdouble green, GLdouble blue, GLdouble alpha);

void glColor4f(GLfloat red, GLfloat green, GLfloat blue, GLfloat alpha);

void glColor4i(GLint red, GLint green, GLint blue, GLint alpha);

void glColor4s(GLshort red, GLshort green, GLshort blue, GLshort alpha);

void glColor4ub(GLubyte red, GLubyte green, GLubyte blue, GLubyte alpha);

void glColor4ui(GLuint red, GLuint green, GLuint blue, GLuint alpha);

void glColor4us(GLushort red, GLushort green, GLushort blue, GLushort alpha);

Kural gereği kullanılan ekleri atarak komutun adını glColor() olarak telaffuz ederiz. Anlaşılacağı üzere eklenen kısaltmalar bize parametrelerin 8, 16, 32 ya da 80(ya da 96) byte uzunluğunda olduğunu belirtiyor. Bu kullanılan renk aralığının hassasiyetini artırmaz, sadece kullanıcıya bir kolaylık sağlar. Dahili olarak tüm renkler ekran kartlarında tamsayı ya da "32 bit float" olarak işlenir.

Bütün parametre alan komutlar bu şekilde isimlendirilirer ve benzer kurallara uyarlar. Diğer komutların yazılışı için Visual C++ içerisinde yer alan yardım dokümanına ve gl.h dosyasına göz atmanızı tavsiye ederiz.

OpenGL, eklerle sürekli genişlemektedir. Bu yüzden yeni komutların yazılışı, parametreleri vb vb için <a href="http://www.opengl.org/">www.opengl.org</a> ya da SGI'daki dokümanlardan faydalanmamız gerekiyor.

**H- Sonuç**

Buraya kadar temel bilgileri edindik. Elimizdeki örnek kodun çizim kısmını değiştirerek, örneğin diskten veri okuyarak bir çok cismi çizmek mümkün. Fakat bu şekilde çok hızlı görüntü elde etmek olanaksız olduğu için, bir sonraki yazımızda öncelikle sistem belleğinde bulunan üçgen listelerinin çizimine başlayacağız. Ardından, "strip" yapısını anlatıp bunun avantaj / dezavantajlarına değinecek ve ilk doku kaplı yüzeyimizi çizeceğiz.

Tüm sorularınız için email adresim : [engin@vividimage.co.uk](mailto:engin@vividimage.co.uk)

---
*Kaynak: `OPEN GL/openGL_TR.htm`*
