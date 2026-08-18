# PIC 1 Ve PIC 2

PIC Microchip firmasinin 1994 yilinda ortaya çikardigi ‘Peripheral Interface Controller ‘ denen yani cevre birimleri kontrol eden bir islemcidir. Ilk üyesi de 16C54 artik piyasada yoktur. Amatörlerin kullanabilecegi çesitli tipte ve kapasitede PIC bulunmaktadir fakat ortak özellik 8 bit CMOS olmalaridir.

Bu yazimizda PIC ve programlama ile ilgili bilgiler verilmeyecektir, çünkü gazetemizde bu konu ile ilgili olarak TA2CBA'nin pek çok yazisi bulunmaktadir.

PIC konusu ile ilgilenenler, biraz bilgi sahibi olunca hakli olarak ögrendiklerini denemek isterler ve bunun için bir PIC programlayici edinmeleri gerekir, PIC programlayicilarin bir kismi çok pahali profesyonel cihazlardir, Kimi ise çok basit ve kullanissizdir. ‘ Easypic ‘ adini verdigimiz bu devre, PIC ile her yeni tanisanin kullandigi 16C84 ve 16F84 için tasarlanmistir.

16C84 ve 16F84 hemen hemen birbirinin ayni PIC lerdir. Tek fark bellek lerindeki EEPROM ve FLAS bellek olmalari (nerede ise ayni sey) ve data memory farkidir.

PIC assembly dilini bilen herkes bu iki PIC ile 35 komut kullanarak inanilmaz seyler basarabilir. Biraz gayret, merak ve niyet ile de bu is birkaç haftanizi alir.

EASYPIC tasarlanirken deneycilerin, hem programlamayi hem de denemeyi kolayca yapabilmeleri için, BREADBOARD kullanilacak sekilde dizayn edilmistir. Yani EASYPIC ‘i breadboard ‘ a takip gerekli voltaji verdikten sonra bir swiç yardimi ile program ve deneme modunu seçebilmektesiniz.

Easypic bacak çikislari kolaylik olsun diye sira ile dizayn edilmistir.

1-) RA0
2-) RA1
3-) RA2
4-) RA4
5-) RA5
6-) RB0
7-) RB1
8-) RB2
9-) RB3
10-)RB4
11-)RB5
12-)RB6
13-)RB7
14-)MCLR
15-)GND Devreye verilecek voltajin negatif baglantisi
16-)9-21 V Breadboard üzerinden devreye verilebilecek voltaj pozitif girisi
17-)+5 V Breadboard üzerinde gerekebilecek 5 volt için çikis

Bu PIC boardunu kullanmadan önce, PIC programi yazmak ve yüklemek için bir bilgisayara ihtiyacimiz olacak. Bu bilgisayarin eski olmasi, 386 – 486 olmasi hiç önemli degil is görür, yeter ki bir seri 9 pin konnektörlü çikis olsun.

PIC programlama için önce PIC Assembly yazabilecegimiz bir editor programi lazim bu neler olabilir.

1-) DOS‘ un EDIT‘i
2-) WINDOWS ‘un NOTEPAD‘,
3-) MPLAB‘in PSE‘si

En kolay olan DOS Edit ‘idir ve ben onu kullaniyorum. Bu editor programi ile PIC Assembly dili ile yazilmis komut paketini, sonu .ASM olacak sekilde kaydediniz.

Ikinci asamada, bu ASM dosyasini HEX file yapacak bir ASSEMLER gerekiyor MPLAB‘in içindeki MPASM bu is içindir.

MPASM çalistirilip daha önce yazilan ASM dosyasi pencereden seçilir ve gerekli ayarlar yapildiktan sonra çalistirilir. Yazdiginiz program dogru ise yasil renk görünür, bir yanlislik varsa kirmizi renk ve hatalari gösteren ERR dosyasi olusur.

Son asamada ise bu olusan HEX file‘i PIC'e yazdirmaktir. EASYPIC baglantisi kontrol edilip, programlama switch'inin çekili oldugu görülür ve yazma programi PICPROG çalistirilir gerekli ayarlar yapildiktan sonra PIC proramlanir. Daha sonra swic ileri itilerek deney gerçeklestirilir.

Tüm bunlarin aksamadan yapilabilmesi için, bilgisayar hardware'ini tekrar gözden geçirmeliyiz. Bize lazim olan 9 Pin çikisli bir seri porttur. Eski tip makinalarda bu portu mouse kullandigi için geriye 25 pin çikisli port kalmaktadir, bu nedenle ya bir 25 / 9 pin konnektör adaptörü kullanmaliyiz veya bilgisayar I/O karti üzerinden 2. Com port çikisina direk olarak 25 pin konnektörü çikarip 9 pin konnektör takmaliyiz. Mouse çikisina bir adaptör baglayip mouse'u 25 pin konnektöre kakmak ta mümkün olabilir.Tüm bunlar bilgisayarda nelerin olduguna ve hangi com portlarini kullandiklarina baglidir. Bize lazim olan port com 1 veya com2 portudur. Bu portlardan birini programlamak için kendimize ayirmaliyiz. Ps2 mouse kullanan makinalarda bu gerekli degildir orada 9 pin çikisi bos oldugu için böyle bir sorun olmaz. Özetle bilgisayardaki modem, mouse ve diger com kullanilicilari o sekilde ayarlamaliyiz ki ,bize programlamak için com 1 veya com 2 portu kalsin çikis 9 pin konnektörlü olsun.

Bilgisayarimizda bir Klasör altinda MPASM PICPROG bulunsun. Bu dosyalarin ve editör programinin masa üstümde de kisayollari olsun.

1-) Masaüstündeki MsDos'u açip EDIT komutu ile editöre girip programi yaziyoruz ve sonu ASM olacak sekilde kaydediyoruz.

2-) MPASM ile bu dosyayi bulup ayarlari yapip HEX file olusturuyoruz.

3-) PICPROG ile bu HEX dosyasini PIC'e yazdiriyoruz.

Daha sonra PIC programini breadboard üzerinde gerekli elemanlari yerlestirip deniyoruz.

16F84 programlama bacaklari olan RB6 ve RB7 bacaklari bir switch vasitasi ile devre disi birakilir aksi halde, breadbord üzerinde bu bacaklara eleman bagli iken, PIC in tekrar programlanamaz, switch bu durumu engeller.

---
*Kaynak: `PIC 1 ve PIC 2/PIC1.DOC`*
