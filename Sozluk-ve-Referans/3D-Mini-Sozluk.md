# 3D Mini Sözlük

## **3D Mini Sözlük******

Daha önce bir bilgisayar dergisinde yayınlanan bu çalışmamı, sizlere yararlı olabileceği düşüncesi ile buraya yerleştirdim. Bu ufak sözlük var olan bir çok terimden sadece belli başlı bir kaç tanesini içeriyor.

*3D Grafiklerin dünyasına girdiğinizde çok sık karşılaşacağınız bazı temel kavramları içeren kısa bir sözlük hazırlamayı uygun bulduk. Ne yazık ki Türkçemizde, bilgisayar dünyasında kullandığımız çoğu terimin bir karşılığı yok. Biz sizlere terimlerin önce orijinal İngilizce hallerini, daha sonra da mümkün olduğunca Türkçeleştirdiğimiz hallerini sunuyoruz. Kullandığınız yazılımlardan daha fazla verim alabilmek için, bu minik sözlüğe bir göz atıverin!***

**Ray Tracing (Işın İzleme):** Üç boyutlu bir sahneyi, sahnedeki ışık kaynaklarından yayılan ışınları izleyip, ortamdaki cisimlerin bu ışınları kırma,yansıtma gibi hallerini hesaplayarak kaplama işlemi. Oldukça kaliteli sonuçlar ortaya çıkartmasına rağmen, yüksek bir işlemci gücü gerektirir.

**Shading (Gölgeleme):** Üç boyutlu cisimleri çokgen bazlı hallerinden, piksel bazlı görüntülere çevirme.

**Modeling (Modelleme):** Üç boyutlu grafikler dünyasında, modelleme gerçek dünyayı yansıtmak için kullanılan çeşitli metodları anlatır. Bir 3D programı ile bir otomobil oluşturduğunuzda, bir otomobil modellemiş olursunuz.

**3D Scene (Üç Boyutlu Sahne):** Çizgileri, çokgenleri ve yüzleri içeren, temel 3D şekillerin oluşturduğu bütün.

**Vertex (Nokta):** Üç boyutlu uzayda, pozisyonu üç koordinatla belirlenen bir nokta.

**Triangle (Üçgen):** Üç noktanın oluşturduğu üçgen. Çoğu 3D programı, cisimleri çeşitli büyüklükteki üçgenlerle oluşturur.

**Quadrilateral (Dörtgen):** Dört noktadan oluşan çokgen. 3D Programlar dörtgenleri iki adet üçgen kullanarak oluşturur.

**Freeform Surface (Serbest Yüzey):** Eğriler yardımıyla tanımlanan, bu sayede kullanıcı tarafından kolayca değiştirilebilinen üç boyutlu yüzeyler.

**NURBS (NonRational B Spline):** Kontrol noktaları diye adlandırılan bir ağın tanımladığı serbest bir yüzey.

**Geometric Pipeline (Geometrik İşlem Dizisi):** 3 Boyutlu cisimin, 3D koordinat sisteminden, ekranın iki boyutlu koordinat sistemine yansıtılmasını sağlayan işlemler dizisi.

**Camera (Kamera):** 3D Bilgisayar grafikleri gerçek dünyadaki kameraları taklit eder. Aynı gerçek kamera gibi, bir objektif ve bir yansıtma yüzeyi (= fotograf filmi) söz konusudur.

**Projection Plane (Yansıtma Yüzeyi):** 3D sahnenin görüntüsünün oluşturulduğu 2D yüzey. Üç boyutlu dünyayı, iki boyuta indiren bildiğimiz fotograf makinesinin içindeki film, yansıtma yüzeyinin karşılığıdır.

**Phong Lightning (Phong Aydınlatma):** Gerçek hayattaki ışıkları taklit etmeye yarayan matematiksel bir model. Çeşitli ışık tipleri tanımlama imkanı veren bu aydınlatma modeli günlük hayatta karşılaşılan ışık kaynaklarını bilgisayar ortamına aktarmakta oldukça gerçekçi sonuçlar verebilmektedir.

**Attenuation (Sönümlenme):** Işık kaynaklarının yaydıkları ışığın, kaynaktan uzaklaştıkça zayıflamasıdır. Işık, cisimden uzaklaştıkça, uzaklığın karesiyle orantılı olarak sönükleşir.

**Fog (Sis):** 3D programlarındaki sis, gerçek hayattaki sisin etkisini taklit eder. Bu etkiyi deniz altı sahneleri yaratırken özellikle kullanma gereği duyarsınız.

**Wireframe (Tel Çerçeve):** Cisimleri vektörlerle gösterme biçimi.

**Flat Shading (Düz Gölgeleme):** 3D cisimlerin her yüzeyini bir renk tonu ile kaplayarak gösterme biçimi. Çok hızlı bir kaplama metodu olduğu için, sahnelerin genel görüntüsü için bir fikir alınması gerektiği hallerde, hızlı kaplamalar yapmak için kullanılır. Eski 3D bilgisayar oyunlarında yaygın olarak kullanılmış bir metoddur.

**Gouraud Shading (Gouraud Gölgeleme):** Renkler arasında interpolasyon yapma ilkesiyle çalışan bir aydınlatma metodudur. Hızlı bir metod olması ve kullanılabilinir kalitede sonuçlar vermesi nedeniyle günümüz 3D oyunlarının çoğu bu aydınlatma metodunu kullanır.

**Phong Shading (Phong Gölgeleme):** Bu metodda ekrandaki her pixelin rengi ayrı ayrı hesaplanır. Çok gerçekçi çıktılar üreten bu kaplama metodu oldukça fazla işlem gücü gerektirmektedir.

**Texture Mapping (Doku Kaplama):** Doku kaplama 2D bir grafiği, 3D bir cisime uygulamakdır. Bu sayede cisimler gerçekçi görüntüler ve dokular kazanabilmektedir. Çoğu zaman akıllıca uygulanmış bir yüzey dokusu, sizi uzun modelleme çalışmalarından kurtaracaktır. Doku kaplamanın en önemli dezavantajı, kaplanan bitmap grafiklerin büyük hafıza miktarları tüketmesidir. 3D Grafik işlemini bu kadar RAM tüketici yapan en önemli faktörlerden biri budur.

**Interpolation (İnterpolasyon):** İki bilinen değeri kullanarak, aradaki bilinmeyen bir üçüncü değeri hesaplama işlemidir. İki boyutlu görüntülerin ölçeklenmesi işleminde çokça kullanılması gerekir.

**Blending (Karıştırma):** Karıştırma, iki rengi birbirine karıştırıp, üçüncü bir renk oluşturma işlemidir. Genelde 3D görüntülerin 2D görüntülerle birleştirildiği 3D Grafik dünyasında, karıştırma işlemleri sık sık kullanılmaktadır.

**Transparency (Şeffaflık):** Şeffaflık, renk karıştırma işlemi kullanılarak yaratılır. Cam, buz gibi cisimleri yaratmakta kullanacağınız şeffaflık, eğer ışın izleme metodu kullanan bir program kullanıyorsanız, beraberinde ışığın kırılması olgusunu da getircektir.

**©****1997 Levent Pekcan******

---
*Kaynak: `3D MİNİ SÖZLÜK/ekitap-Anonim-3D_Mini_S÷zl³k.doc` — JCSE — 2002*
