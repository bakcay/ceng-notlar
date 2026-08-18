# Window 2000 Kurulum Adimlari

## **Windows 2000 için kurulum adımları:**

**UYARI:**** **Aşağıdaki adımlara geçmeden önce,** çalışan uygulamaları kapatın ve çalışmalarınızı kaydedin.******

**NOT:** Bir sürücü yükleyeceğiniz için, **sisteme “Administrative” yetkileri olan bir kullanıcı hesabıyla girmiş olmanız gereklidir**. Eğer bu özelliklere sahip olmayan bir kullanıcı hesabıyla sisteme girdiyseniz, sistemden çıkın ve sisteme “Administrative” yetkileri olan bir kullanıcı hesabıyla girin.

**NOT:** Sisteminize **daha önceden RASPPPOE ya da başka bir PPPoE client yazılımı yüklenmiş ise** kuruluma devam etmeden önce kurulu olan bu yazılımın sistemden kaldırılması gerekir.

**RASPPPoE.zip** dosyasını **C:\\Temp** dizini altına açın.

Masaüstündeki **“My Network Places”** simgesine sağ tıklayın ve **“Properties”** seçeneğini seçin.

Açılan **“N**etwork and Dial-up Connections” penceresinde **“View”** menüsünde **“Details”** seçeneğine tıklayın.

Bu pencerede bir ya da birden fazla **“Local Area Connection”** simgesi göreceksiniz. ADSL modeminizin bağlı olduğu network kartını seçin ve sağ tıklayıp **“Properties”** seçeneğini seçin.

**“Local Area Connection Properties”** penceresinde **“Install…”** tuşuna tıklayın.

**“Select Network Component Type”** penceresinde, **“Protocol”** seçin ve **“Add…”** tuşuna tıklayın. (Not: Bu işlemden sonra bir sonraki pencerenin açılması zaman alabilir).

**“Select Network Protocol”** penceresinde penceresinde **“Have Disk…”** tuşuna tıklayın.

**“Install From Disk”** penceresinde **C:\\Temp** yazın ve **“OK”** tuşuna basarak “PPP over Ethernet Protocol’ünün” kurulumunu başlatın. Kurulum sırasında ekrana “Digital Signature” ile ilgili mesaj pencereleri gelebilir. Bu pencerelerde **“Yes”** tuşuna basarak kuruluma devam edin.

**“Local Area Connection Properties”** penceresinde **“**Cancel**”** CLOSE tuşuna tıklayıp bu pencereyi kapatın.

Bağlantı oluşturmak için aşağıdaki adımları gerçekleştirin.

## **PPP over Ethernet Dial-up Bağlantı oluşturma:**

**“Start”** (Başlat) tuşuna tıklayın ve **“Run…’ı"** (Çalıştır…) seçip **“Run…”** (Çalıştır…) kutusunu ekrana getirin.

Bu kutuda **RASPPPOE** yazıp **“OK”** (Tamam) tuşuna basın.

Ekrana, üst kısmında **“Dial-Up Connection Setup”** yazan bir pencere gelecektir. Sisteminizde tek bir network kartı varsa, bu kart gri renkli olarak görünür. Eğer birden fazla network kartı varsa bu pencerede ADSL modeminizin bağlı olduğu network kartını seçin.

Yine aynı pencerenin altında yer alan **“Create a Dial-Up Connection for the selected Adapter”** tuşuna basın. Bu işlemden sonra masaüstünde **“Connection through *****Adapter Name*****”** isimli bir simge oluşturulmuş olacaktır.

**“Exit”** tuşuna basarak bu pencereyi kapatın.

Masaüstündeki bağlantı simgesine çift tıklayarak bağlantı penceresini açın. Bu pencerede ilgili yerlere **“kullanıcı adı”** ve **“şifrenizi”** girin.

**“Connect”** tuşuna basarak ADSL bağlantıyı başlatın.

---
*Kaynak: `WİNDOW 2000 KURULUM ADIMLARI/Windows 2000 için kurulum adımları.doc` — Administrator — 2004*
