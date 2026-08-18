# Autocad Ders Notlari

## **ÇİZİME RESİM EKLEMEK**

Bu ayki yazımızda, çizimlerimize resim eklemek ve bu resimler üzerinde değişiklik yapmak hakkında biraz bahsedeceğim.

Resimlerle çalışmak PhotoShop vb. programlarla daha kolaydır. Ancak resminizin üzerine ölçekli bir çizim yerleştirmeniz oldukça zor bir iştir. AutoCAD gibi milimetrik ölçeklerde çizim yapabilen bir programınız varsa, sorun halledilmiş demektir. Aslında dergimizin amacı gibi, paylaşmak esastır. Örneğin bir resim üzerinde fotomontaj yapacaksınız, bu durumda AutoCAD’i kullanmak biraz zor olabilir ve istediğiniz kesim yerlerini tam olarak yakalayamayabilirsiniz. Fakat resmin bazı yerlerine yay, çember, eşkenar bir beşgen veya dolgulu bir çizim eklemek istediğinizde, bu seferde PhotoShop’ta çalışmak zor olacaktır. İşte bu noktada yapacağımız işin hangi programa daha uygun olduğunu belirleyip, dosya paylaşımlarını kullanarak istediğimiz sonucu elde edebiliriz.

AutoCAD R14 sürümünden itibaren resim formatları üzerinde de artık ekleme, çıkarma, oynama vb. değişiklikler yapabiliyoruz. Konumuzda anlatacağım resimler örnek olması amacıyla tamamiyle AutoCAD kullanılarak yapılmıştır.

Bir çizime resim eklemek için AutoCAD *Insert *menüsünün altındaki *Raster Image *komutunu kullanacağız.

Command: \_image

Bu noktadan sonra karşınıza bir pencere açılacaktır. *Attach *butonuna basarak eklemek istediğiniz resmi seçin.

Insertion point <0,0>: Eklemek istediğiniz nokta (resmin sola alt köşesinin odaklanacağı nokta)

Base image size: Width: 1.00, Height: 0.75 <Unitless>

Scale factor <1>: 300 (Yukarıda görülen resmin boyutlarını ölçeklendirmek suretiyel kaç katını resminize eklemek istediğinizi belirtiyorsunuz. Burada Mouse kullanmak daha avantajlı olabilir.)

\*\* STRETCH \*\*

<Stretch to point>/Base point/Copy/Undo/eXit: (Eğer resmin boyutlarını beğenmediyseniz, *Stretch *komutunu kullanarak boyutunu değiştireilirsiniz.)

İlk resmimiz olan “Golden Gate” köprüsü çizime eklendi.

Command: \_image

İkinci resmim olan kartal resminide çizime eklemek için aynı yolları kullanıyorum. Daha sonra *Kartal’* ı köprü üzerine ekleyeceğim. Bakalım gerçekçi duruyor mu?

Insertion point <0,0>:

Base image size: Width: 1.00, Height: 0.75 <Unitless>

Scale factor <1>:

Bu resimde Kartal’ın oralı olmadığı anlaşılıyor.

Ancak Kartal resmi üzerinde biraz kırpma yapmam gerekiyor. Bunun için *Modify *menüsünün altındaki seçeneklerden önce *Object, *altından *Image Clip * seçeneğini belirliyorum.

Command: \_imageclip

Select image to clip: Other corner: (Resmimi sağdan sola seçme yüntemini kullanarak seçiyorum. Resmin üzerine tıklayarak seçim yapmak biraz zordur. Bu yüzden sağdan sola seçme yöntemini kullanmak daha akıllıca olur.

ON/OFF/Delete/<New boundary>:

ON: Kırpmayı etkinleştirir ve kırpılmış resmi bir önceki sınırlarıyla gösterir.

OFF: Kırpmayı kapatır ve resmin esas sınırlarını gösterir.

Delete: Kırpma sınırlarını kaldırır ve tüm resim görüntülenir.

New Boundary: Kırpma sınırlarını belirlememizi sağlayan seçenektir.

Polygonal/<Rectangular>: p (Kırpma sınırlarımı Polygon kullanarak yapacağım. Diktörtgen sınırlandırmasını kullanarak istediğim seçimi yapamam. Ancak resmin belirli bir bölgesini seçecekseniz, Rectangular seçimi kullanabilirsiniz.)

First point: Kırpma yapacağım ilk noktayı belirliyorum.

Undo/<Next point>:

Undo/<Next point>:

Close/Undo/<Next point>:

Close/Undo/<Next point>:

Close/Undo/<Next point>:

Close/Undo/<Next point>:

Close/Undo/<Next point>:

Close/Undo/<Next point>:

Close/Undo/<Next point>:

Close/Undo/<Next point>:

Close/Undo/<Next point>:

Close/Undo/<Next point>:

Close/Undo/<Next point>:

Close/Undo/<Next point>:

Close/Undo/<Next point>:

Close/Undo/<Next point>:

Close/Undo/<Next point>:

Close/Undo/<Next point>:

Close/Undo/<Next point>:

Close/Undo/<Next point>:

Close/Undo/<Next point>:

Close/Undo/<Next point>:

Close/Undo/<Next point>:

Close/Undo/<Next point>:

Close/Undo/<Next point>:

Close/Undo/<Next point>:

Close/Undo/<Next point>:

Close/Undo/<Next point>:

Close/Undo/<Next point>:

Close/Undo/<Next point>:

Close/Undo/<Next point>:

Close/Undo/<Next point>:

Close/Undo/<Next point>:

Close/Undo/<Next point>:

Close/Undo/<Next point>:

Close/Undo/<Next point>:

Close/Undo/<Next point>:

Close/Undo/<Next point>:

Close/Undo/<Next point>:

Close/Undo/<Next point>:

Close/Undo/<Next point>:

Close/Undo/<Next point>:

Close/Undo/<Next point>:

Close/Undo/<Next point>:

Close/Undo/<Next point>:

Close/Undo/<Next point>:

Close/Undo/<Next point>:

Close/Undo/<Next point>: c (polygon’u kapatıyorum)

Mouse’u kullanarak seçim yapacağım noktaları tıklıyorum. Dikkat edilmesi gereken nokta, çizdiğim polygonun dış kısmı atılacak ve iç kısmı görünür olacaktır. Polygonda kapatma komutu, komutu verdiğniz noktadan ilk noktaya çizilecek olan bir çizgidir. Bu sebeple *close *komutunu vermeden önce çizginin nereden geçeceğini saptamanız gerekir.

Kartal’ın kırpmak istediğim noktalarını kırptıktan sonra, seçili olan resmi *Move *komutunu kullanarak sağa kaydırıyorum. Şimdi Kartal oralı gibi duruyor mu? 

Düşündümde, bu köprünün ortasındaki dikdörtgen kısımlar, beşgen olsaymış daha iyi dururmuş gibi geldi bana. Birde şu köprüyü tutan çelik halatlara birkaç tane daha ekleyeyim de yıkılma riski ortadan kalksın. Tabi köprünün üzerine birde reklam asmak gerekecek. Boş durmasın…

Burası işin esprisi. Ancak lazım olduğu noktada daha gerçekçi çizimlerle resmin üzerine ekleme yapabilirsiniz.

Resimler üzerinde sizde değişiklikler yapabilirsiniz.

.dwg dosyasını indirmek için tıklayın…

**Yarın **yada az sonra ne olacağını bilmiyoruz. Bu nedenle elimizde olan zamanı iyi değerlendirmek zorundayız. Bugünlerin de geçeceğini unutmadan, gelecekte “ahlanmamak için” **şu anı boşa harcamamalıyız.**

alialan@mailcity.com

---
*Kaynak: `AUTOCAD DERS NOTLARI/resimekleme.doc` — Hakan — 2001*
