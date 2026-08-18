# PIC 1 Ve PIC 2

**Easypic devresinde Dikkat edilecek noktalar:**

Çok kolay bir devre oldugu için ,hersey gayet düzgün çalisir,fakat bilgisayar da hardware ve software hatasi olmamasi gerekmektedir.

Programlama için swich kendinize dogru çekilmelidir (Bu pozisyon swicth'in esas pozisyonudur)

Programlama bittiginde swicth ileri itilmelidir ki, RB6 RB7 bacaklari port tan ayrilip ,Breadbord ile baglansin.

PICPROG programlama programi eger iki pencere açmis ise,devre initialize olmaz ve program sasirir,bu nedenle Masa üstünde birden fazla PICPROG program penceresi olmamalidir.

PICRROG ile seçtiginiz herhangi bir HEX dosyasini,yüklerken XTAL osc. Tipini seçiniz. WDT yi ve CODE PROTEC'i isaretlemeyiniz, Deneme çalismalarinda bu kolaylik saglar.

Easypic voltajiile ilgili olarak : 9 volt pili takili tutup bradboard üzerinden daha yüksek voltaj (10V 12V gibi) verirseniz pil tükenmez.Pil portatif bir devre olsun diye düsünülmüstür.Mesela ögrenciler yaptiklari bir programi ögretmenin masasina götürüp gösterebilirler.

Bilgisayari açip devreye voltaji veriniz, port konnektörünü takiniz, Switch size dogru çekili iken PICPROG'u çalistiriniz, hex file seçip yükleyiniz.

Switch pozisyonunu degistirip deneyi gerçeklestiriniz.

PICPROG yükleme yaparken devreye müdahale etmeyiniz, PIC ile oynamayiniz.

PICPROG programi programlamanin bittigini gösterir, o durumda switch’ i ileri iterek deneyinizi gerceklestiriniz.

---
*Kaynak: `PIC 1 ve PIC 2/PIC2.DOC`*
