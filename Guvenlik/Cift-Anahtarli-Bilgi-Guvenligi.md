# Cift Anahtarli Bilgi Guvenligi

teknik altyapı > çift anahtarlı bilgi güvenliği

**ÇİFT ANAHTARLI BİLGİ GÜVENLİĞİ**

Elektronik iletişim, günümüzde kağıt üzerinde yazı yazarak yapılan her türlü iletişimin yerine geçmeye adaydır. Çok uzak olmayan bir gelecekte kişi/kuruluş/toplumların, özel/kamusal/resmi haberleşmelerini elektronik iletişim ağları üzerinden yapabilmeleri açık ağlar üzerinden iletilen bilginin güvenliği ve güvenilirliğiyle yakından ilgilidir. Açık ağlarda bilgiyi tehdit eden unsurlar üç başlık altında toplanır:

Başkası dinleyebilir
Bilgi değiştirilebilir
Kimlik taklit edilebilir

Bilgi güvenliği bu tehditlerin ortadan kaldırılması ile sağlanır. Bunun için kriptografide önerilen yöntemler çift (açık) anahtarlı bilgi güvenliği yöntemleridir. Tipik kriptografi uygulamaları güvenli iletişim, kimlik tanımlama, kimlik doğrulamadır. Bu uygulamalar sayısal şifreleme ve sayısal imza ana başlıkları altında aşağıda özetlenmiştir. Daha komplike uygulamalar elektronik ticaret, elektronik kimlik belgeleme, güvenli e-posta, yeniden anahtar bulma ve bilgisayarlara güvenli erişim hakkı elde etme için geliştirilmiş sistemleri içerir. Her kullanıcıya biri gizli diğeri kamuya açık iki anahtarın verildiği, çift anahtarlı kriptografi sistemidir. Burada sözü edilen anahtar, kriptografi algoritmasının kullandığı uzun sayı dizisi anlamına gelmektedir. Anahtar çiftlerini üreten algoritmaların matematiksel özelliklerinden dolayı açık-gizli anahtar çiftleri her kişi için farklıdır, diğer bir deyişle her kullanıcının açık-gizli anahtar çifti yalnızca o kullanıcıya özeldir. Açık anahtar ile gizli anahtar arasında matematiksel bir bağ vardır. Bir kullanıcının açık anahtarıyla kilitlenen bir mesajı yalnız ve ancak ona ait gizli anahtar çözebilir. Aynı şekilde, herhangi bir kullanıcının gizli anahtarıyla attığı sayısal imzanın doğrulanabilmesi, yalnızca onun açık anahtarını kullanarak mümkün olabilir.

Gizli anahtar, adından da anlaşıldığı gibi kişinin kendisi dışında kimsenin bilmemesi gereken ve saklı tutması zorunlu olan gizli bir bilgidir. Gizli anahtar genelde kişinin bilgisayarında anahtar kelimeyi sadece kendisinin bildiği şifreli bir dosya içinde saklanır. Veya daha güvenli bir yöntem gizli anahtarın akıllı kart içinde şifreli saklanmasıdır. Açık anahtar kamuya açıktır, elektronik kimlik belgelerinin içinde diğer kişisel bilgilerle birlikte tutulur ve herkes birbirinin açık anahtarını e-kimliklerine ulaşmak süretiyle istediği zaman elde edebilir. Açık anahtarın içinde bulunduğu e-kimlikler kişinin bilgisayarında, bir kopyası da herkesin ulaşabildiği "dizin sunucu"larda tutulur. Kullanıcı dilerse e-kimlik belgesini (açık anahtarını) gizli anahtarıyla birlikte akıllı kartında da tutabilir. Böylece e-kimliğini yanında taşıyarak gerekli durumlarda farklı ortamlarda e-kimliğini kullanabilir (Şekil 1).

Açık anahtar bilgisiyle gizli anahtarın bulunabilmesi mümkün değildir. Çift anahtarlı kriptografide farklı algoritmalar ile şifreleme yapmak mümkündür. Kriptografide gizlilik, algoritmanın gizli tutulmasından degil, algoritmanın bazı matematiksel özelliklerinden dolayı şifrenin kırılmasının güçlüğünden ileri gelmektedir. Buradaki güçlük terimi, teknik olarak “hesaplanması pratik sınırlı sürelerde mümkün olmayan (örneğin, bilgisayarın yeteneklerinden bağımsız olarak her durumda en az 1000...0 yıl sürecek hesaplamalar)” anlamına gelir.

**Sayısal Şifreleme**
Şifreleme açık ağlardan gönderilen bilginin başkaları tarafından görülmesinin (dinlenmesinin) istenmedigi, diğer bir deyişle yukarıda sözü edilen tehditlerin 1. şıkkında belirtilen durumun engellenmesi istendigi zaman yapılır. Bunun için çift anahtarlı bir kriptografik algoritma kullanılabilir. Buna göre, mesajı gönderen taraf:
Gönderilen bilginin sayısal içeriğini,
Mesajı alacak tarafın açık anahtarını,
sayısal şifrelemede kullanır.
Mesajı alan taraf da, şifreli mesajı çözmek için şunlara gereksinim duyar:
Şifreli mesajın sayısal içeriği,
Kendisinin gizli anahtarı.(Şekil 2)

Burada dikkat edilecek olursa, şifreli mesajın üçüncü taraflar tarafından dinlenebilmesi ancak “gizli anahtara” sahip olmaları ya da şifreli mesajı matematiksel yollarla deşifre etmeye çalışmaları ile mümkün olabilir. “Güvenlik açısından iyi bir şifreleme” algoritması, gizli anahtar olmadan şifreli mesajı deşifre etmeye imkan tanımıyan bir algoritmadır.

**Sayısal İmza**
Sayısal imza elektronik mesaja eklenmiş bilgidir. Çift anahtarlı bir kriptografik algoritmayla hazırlanan sayısal imza, hem gönderilen bilginin sayısal içeriğinin değiştirilmediğinin hem de gönderen tarafın kimliğinin ispatlanması, diğer bir deyişle yukarıda bahsedilen 2. ve 3. şıktaki tehditlerin engellenmesi için atılır ve şunlara bağlı olarak oluşturulur:
Gönderilecek mesajdan üretilen “mesaj özetinin” sayısal içeriği,
Gönderen tarafın kendi gizli anahtarı.

Sayısal imzanın doğruluğunu kanıtlamak için mesaji alan taraf şunları kullanır:
Kendisine gelen mesajin ve sayısal imzanın sayısal içeriği,
Gönderen tarafın açık anahtarı. (Şekil 3)

“Mesaj özeti”, gönderilecek mesajdan matematiksel yollarla üretilen sabit uzunlukta sayısal bilgidir. Bu işlem “hash” fonksiyonu olarak bilinir. Hash fonksiyonu bir kaç özelliği sağlar:
Mesaj özeti anlamsız bir bilgidir.
Hash fonksiyonu geri dönüşümü olmayan bir fonksiyondur. Diğer bir deyişle, herhangi bir mesajın özetine bakarak mesajın kendisini elde etmek mümkün değildir.
Aynı özeti veren herhangi iki farklı mesaj bulmak da mümkün değildir.

Böylelikle, her mesajın farklı bir özeti olması ve dolayısıyla mesajda yapılacak en ufak bir değişikliğin imzayı geçersiz kılması sağlanmış olur. Sayısal imzalamada son adım, mesaj özetinin gönderen tarafın gizli anahtarıyla şifrelenmesidir. Sayısal imza mesaja eklenir ve mesaj ile birlikte alıcıya gönderilir. Alıcının imzanın geçerliliğini kontrol etmesi iki adımda gerçekleşir. Alıcı sayısal imzayı karşı tarafın açık anahtarı ile çözerek varsayılan mesaj özetini elde eder. Diğer yanda mesajın tekrar özetini çıkarır. Son olarak bu iki özeti karşılaştırır. Bu özetlerin tıpatıp aynı olması, imzanın doğruluğunu gösterir.(Şekil 3)

---
*Kaynak: `CIFT ANAHTARLI BILGI GUVENLIGI/CIFT ANAHTARLI BILGI GUVENLIGI.doc` — Internet1 — 2004*
