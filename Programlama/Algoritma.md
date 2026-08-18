# Algoritma

## **Algoritma**

Bilgisayar yordamı ile bir problem çözüleceğinde sırası ile şu adımların yerine getirilmesi gerekmektedir.

Problemin doğru ve kapsamlı olarak tanımlanması.

Problemin çözümü için etkin bir yöntemin bulunması.

Bu yöntemden yararlanarak, uygun bir algoritmanın geliştirilmesi ve bunun analizi.

Algoritmanın bir bilgisayar programlama dili kullanarak bilgisayara uyarlanması.

Programın denenmesi ve doküman hazırlanması.

Algoritma, bir problemin çözümü (varsa) için gerekli adımların mantıksal bir sıra ile yazılmasıdır. Algoritma her zaman doğru olmalı ve pratik bir zaman içerisinde sona ermelidir. Bir algoritmanın yazılması için, doğal bir dil kullanılabilir ve sözde-kolama(pseudo-code) yapılabilir. sözde-kodlamada kullanılacak olan yapılar algoritma geliştiricisi tarafından önceden tanımlanmalı ve algoritmanın her adımında bu yapılara uyulmalıdır.

**Algoritmanın Tanımı: **Bir problemin çözümüne yönelik, işlem basamaklarının belli bir mantık çerçevesinde adım adım yazılması işlemine *ALGORİTMA* denir.

Algoritma bir bilgisayar programının tüm satırlarının Türkçe ifadelerle yazılmasıdır. Bu ifadeler, bir cümle olabileceği gibi, kısaltılmış ifadeler de olabilir.

Çözüme yönelik farklı algoritmalar aynı problem için yazılabilir. Önemli olan doğru sonuçlara ulaşabilmektir. Algoritma problemle ilgili her türlü soruya cevap verebilmelidir. Bir algoritma üzerinde giriş, işlem ve çıkış bölümlerini taşımalıdır.

**AKIŞ DİYAGRAMI**

Bilgisayarda her şeyin adım adım olduğunu daha önce belirtmiştik. Bu adımları akış diyagramında gösterebiliriz. Akış diyagramı, bir fonksiyonu uygulamak için gereken işlemlerin şematik bir biçimde gösterilmesidir. Bilgisayarın, işlemeleri ne şekilde, hangi sırayla yapacağını belirtir. Bu diyagram ne kadar detaya inerse, o kadar açık yazılmış demektir. Yani biz bir işlemde her türlü olasılığı düşünüp, ona göre bir diyagram yaparsak, işlemi bilgisayara o derece açıklamış oluruz. Bilgisayar hiçbir zaman kendi kendine düşünemediği için, önceden açıklanmamış bir durumla karşılaşınca işlemi sürdüremez.

**Problemin Kavranması: **Akış diyagramı, bize bilgisayarın bir problemi çözerken yürütmesi gereken mantığı gösterir.yani aslında herhangi bir problem için program yazmadan önce yapılması gereken bir şeydir. Özellikle çok karmaşık ve uzun programları yazarken, akış diyagramları bize çok yardımcı olurlar. Bu tip bir program yazmak isteyen bir kişi, eğer zamandan tasarruf etmek amacıyla akış diyagramını çizmeden işe girişirse, sonradan yapabileceği bir yanlışı bulup, işin içinden çıkabilmesi için çok fazla zaman kaybeder.

** **Bu nedenle en basit programları yazarken bile, önce akış diyagramını çizmeli, sonra programımızı ona göre yazmalıyız. Bu şekilde, programı yazmadan önce, kafamızda her şey açık olur. Her türlü olasılık hesaplanmış, ona göre ayrı yollar saptanmıştır. Bize yalnızca akış diyagramdaki eylemleri kullanacağımız dilin komutlarına göre, çevirerek yazmak kalır.

Bunun için, önce problemi kavramamız gerekir. Yani bu problem bizden ne istiyor, sonucunu bulmak için ne gibi işlemler yapmamız gerekir, vs. gibi soruların yanıtlarını bulmamız gerekir. Ancak bu şekilde o problem hakkında bir mantık yürütebiliriz.

Kendimize göre bir mantık koyduktan sonra, akış diyagramını çizebiliriz. Akış diyagramını çizerken, dikkat etmemiz gereken bazı noktaları yineleyelim.

** Veriler: **Verilerin çok iyi bir şekilde saptanması gerekir. Ne istenenden fazla, ne de istenenden az olmalıdır. Fazla olmasının, sonucun çıkmasına bir etkisi olmaz. Ama, bilgisayarlarla yapılan çalışmalarda işlemi en kısa yoldan yapmak, sonuca en kısa yoldan varmak önemlidir. Bir bilgisayarın ana işlemcisinin kapasitesi ne kadar fazla olursa olsun, bir anda çok fazla sayıda işlem yapabilmesi açısından her bir programın olabilecek en az yeri kaplaması gereklidir. Bunu için gereksiz işlemlerden kaçınmamız gerekir.

** **Eksik olması ise, çok daha sakıncalıdır. Bir bilgisayar, eksik verilerle hiçbir zaman bir sonuç çıkaramaz. Onun için problemi kavramak, gereken verileri kesin olarak saptamak zorunludur. Veriler saptandıktan sonra, asıl fonksiyonun yazılmasına geçilir.

**Fonksiyon: **Fonksiyona geçtiğimizde daha da dikkatli olmamız gerekir. Çünkü fonksiyon yazılımlarında çok daha fazla yanlış yapılır. En ufak bir belirsiz nokta bırakılmamalıdır. Eğer belirsiz bir komut alırsa, ne yapacağını bilemez: bu nedenle de işlemi durdurur.

Ayrıca değerlendirme noktaları, değişik yönler ve tutar iyi saptanmalıdır. Yanlış hazırlanmak bir program, bilgisayarın sonsuza kadar aynı işlemi yinelemesine neden olabilir. Bunu engellemek için akış diyagramları tekrar tekrar kontrol edilmeli, üzerinde uygulama yapılmalıdır. Zaten bir diyagramın zayıf noktalarını yakalamanın en iyi yolu işlemi üzerinde uygulamak, birkaç örnek çözmektir. Bu şekilde daha öncesinden gözden kaçan belirsiz noktalar, eksiklikler ve yanlış komutlar yakalanabilir. Böylece bilgisayarın işlemi durdurması, ya da sonsuza kadar yinelenmesi önlenmiş olur. Bu ön aşamada kontrol etmek için ayıracağımız birkaç dakika sonradan bizi saatlerce düşünüp işin yanlış tarafını aramaktan kurtarabilir. Bunun için, özellikle ilk çalışmalarda zamandan tasarruf etmeye çalışmamalı, programı yazıp bilgisayara vermeden önce tekrar tekrar kontrol etmeliyiz.

** Sonucun Alınması: **Fonksiyon kısmı bittikten sonra akış diyagramının son bölümüne geçilir. Bu bölümde sonuç çıkarılır ve herhangi bir terminalden alınması sağlanır. Çıkışta, yalnızca sonucu almak yeterli olmayabilir. Örneğin bir işlemi değişik koşullarda, değişik verileri uygulamak istemişsek, o verileri de almamız gerekir. Bu şekilde sonuçlar karışmamış olur; ve yine programda herhangi bir yanlış varsa daha kolay bir şekilde açığa çıkar. Çünkü bazen bir programda yanlışlar olsa bile, sonuç çıkabilir. Yalnız bu sonuçlar mantık dışı olabilir. Eğer verilerle sonuçlar birlikte çıkarsa, kısa bir kontrolle yanlış bir yer olup olmadığı anlaşılabilir.

Sonuçla birlikte alınacak çıkışlar saptandıktan sonra çıkış diyagramı bitirilir. Son kontroller de yapıldıktan sonra, sıra program yazmaya gelir. Çıkış diyagramında kullanılan değişik şekillerdeki kutucukların ne anlama geldiğini açıklayalım.

Mete\_ARSLAN 1999215003

PAGE 1

Başla ve bitir

El ile girdi kutusu

İşlem kutusu

Bağlayıcı

Ekran çıktısı

Karar kutusu

Döngü kutusu

Bağlayıcı oklar

Girdi, çıktı

Yazıcı çıktısı

---
*Kaynak: `ALGORİTMA/O-d-e-v-s-i-t-e-s-i-com-19135.doc` — METE ARSLAN — 2001*
