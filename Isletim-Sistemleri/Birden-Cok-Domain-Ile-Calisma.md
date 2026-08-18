# Birden Çok Domain İle Çalişma

**Birden Çok Domain ile Çalışma**

Büyük bilgisayar ağlarında, ağ yönetimini bir domain ile çözmek mümkün olmayabilir. Farklı domain'ler bulunabilir ya da faklı network'te farklı birimler olabilir. Domain yönetim araçları (Server Manager; User Manager, NT Explorer vb) birden çok domain'i seçerek o domain'lerin de yönetimi sağlanır.

Birden çok domain ile çalışmanın temelleri.

Iki domain arasında bir güven ilişkisinin bulunması gerekir.

Bir domain'in kullanıcılarına izin verilerek diğer bir domain'e giriş yapmaları sağlanır

Bir domain'in kullanıcılarının diğer bir doman'in kaynaklarından yararlanması (erişmesi) sağlanır.

**Güven İlişkileri (Trust Relationships)**

Bir güven ilişkisi iki domain arasında kurulan bir bağlantıdır. Bu ilişkide bir domain diğer bir domain'e güvenerek kendi kaynaklarının diğer domain kullanıcıları tarafından kullanılmasına izin verir. Böylece bir domain'deki bir kullanıcı birden çok domain'e erişerek ağın bütün kaynaklarından yararlanmış olur. Güven ilişkileri domain düzeyinden daha fazla organizasyon düzeyinde (enterprise) bir network yönetimini sağlar.

Güven ilişkileri sayesinde iki domain, yönetilebilir tek bir birim haline gelir. Diğer bir deyişle merkezi yönetim sağlanır. Kullanıcı bakımından ise, kullanıcılar diğer domain'in kaynaklarını kullanabilirler. Kullanıcı önce domain'e logon olmalı ve daha önceden izin verilen kaynakları kullanabilirler.

**Domainler Arası İlişki******

Bütün güven ilişkileri iki domain arasında kurulur:

*· ****Bir yönlü*** ***güven.*** Sadece bir domain diğerine güvenir.

*· ****İki yönlü*** ***güven***. İki domain birbirine karşılıklı güvenir.

**Güvenen (Trusting) ve Güvenilen (Trusted) Domain'ler**

Bütün güven ilişkilerinde bir domain *güvenilen* diğeri *de güvenendir.***

***Güvenen (Trusting) Domain****.* Güvenen domain genellikle kaynakların yer aldığı domain'dir.

***Güvenilen (Trusted) Domain****.* Güvenilen domain ise güvenilen kullanıcıları belirtir.

Güvenilen ve güvenen domain kavramı kullanıcılar ve kaynakları belirtir. Güvenilen domain, uzak domain'deki kullanıcıları belirtir. Bu kullanıcılar izin verilen kaynakları kullanırlar.

Trusting (Güvenen) Trusted (Güvenilen)

-Kaynaklar- -Kullanıcılari-

Güvenen ve güvenilen terimleri kaynaklar ve kullanıcılar olarak düşünülmelidir. Kaynakların bulunduğu domain, kullanıcıların bulunduğu domain'e güvenir. Böylece uygun ilişkilerin düzenlenmesinin ardından, uzak domain'deki kullanıcılar güvenen domain'deki kaynakları kullanırlar.

Diğer domain'le bir yollu güvenin (one-way trust) düzenlenmesi o domain'e güvenilmesi anlamındadır.

*Güven ilişkilerini anlamanın en kolay yolu güven yönünü çizerek düşünmektir.*

**Güven İlişkisinin Planlanması**

Güven ilişkilerinin düzenlenmesi için planlama ve bilgiye gereksinim vardır. Güven ilişkilerinin düzenlenmesinde aşağıdaki faktörler göz önünde bulundurulmalıdır:

· Güven ilişkileri Windows NT Server domain'leri arasında kurulur.

· İlişki bir yönde mi olacak? Yoksa karşılıklı mı?

· Kullanıcıların yerinden çok kullanıcıların diğer önemlidir.

**Grup Stratejileri**

Güven ilişkileri domain'lerde yer alan yerel ve global gruplar yönetilmesinde yardımcı olurlar. Aynı bir domain'de olduğu gibi bir global grubun domain'deki yerel gruplara üye olmasıyla yerel haklardan yararlanan kitleler oluşturmak gibi; iki domain arasında da güven ilişkisi kurulduğunda güvenilen domain'deki global gruplar güvenen domain'deki bir yerel grubun üyesi olabilirler. Sonra güvenen domain'in yerel gruba verilen izin ile birlikte kaynakların kullanımı ya da sistemin yönetilmesi işlemleri güvenilen domain tarafından yapılır. Birden çok domain'in olduğu ortamda güven ilişkilerinin düzenlenmesinde aşağıdaki faktörler göz önünde bulundurulmalıdır.

Ne yapılacağına karar verilir.

· Network yönetimi (kullanıcı yaratma vb)

· Kaynak kullanımı için izin.

Olabildiğince mevcut yerel ve global gruplar kullanılır.

Güvenilen domain'in PDC'sinde

· Yeni bir kullanıcı ve global bir grup yaratılır.

· Istenilen kullanıcılar mevcut ya da yaratılan global gruba

Domain'de ya da güvenen domain'de

· Gereken bilgisayarda yerel grup yaratılır.

· Güvenilen domain'deki global grup yerel gruba eklenir.

· Yerel gruba gerekli izinler verilir.

*Global gruplar diğer bir domain'in kullanıcılarını ve gruplarını içeremezler.*

**Güven İlişkilerinin Düzenlenmesi**

Güven ilişkilerinin düzenlenmesinde iki anahtar adım vardır:

Güvenilen domain diğer domain'e güven için izin verir.

Güvenen domain güvenilen domain'i eklemelidir (add).

*Güven ilişkisinin kurulması aşamaları ters (garip) gelebilir. Şaşırılmasın. Önce güvenilecek domain, bana güvenebilirsin diye kendisine güvenecek olan domain'e izini verir (lütfeder). Sonra ona güvenecek olan domain güveni verir.*

Güven ilişkilerinin düzenlenmesi bir kullanıcı kayıdı yönetim işidir. Bu nedenle önce hangi domain'in kullanıcıları kullanılacaksa o domain (güvenilen) diğer domain'e (güvenecek) izin verir.

Güvenilen domain'e güvenen domain'in katılmasıyla güven ilişkileri tamamlanır. Bu işlemin ardından güvenilen domain'deki kullanıcılara güvenen domain'de izin verilebilir.

*Güven ilişkilerinin düzenlenmesine güvenen ya da güvenilen domain'den başlanabilir. İki domain'de kendi düzenlemelerini yerine getirmeden güven ilişkisi tamamlanamaz.*

Güven ilişkileri, *Administrator* tarafından yaratılır. Bu işlem için *User Manager for Domains* programı kullanılır. Buradan Policies menüsü ve ardından Trust Relationships seçilir.

Bazı durumlarda güven ilişkileri kurulamaz:

**Sorun****Çözüm**Güven ilişkisi oluşturulamıyorDomain'lerin PDC'leri çalışıyormu?Güvenilen kullanıcı adları kullanılamıyor.Güven ilişkisi yanlış yöndekurulmuş olabilir.

İlişki kurulmalı ve yeniden düzenlenmelidir.

**Tek-Taraflı Güven İlişkisini Düzenlenmesi**

Tek taraflı bir güven ilişkisinin düzenlenmesinde user Manager for Domains, ardından Poıicies menüsünden Trust Relationships seçilir.

Güven ilişkileri iletişim kutusunda iki kesim vardır:

l. Trusted Domains (Güvenilen Domain) kutusunda *hangi domain’e güvenileceği* belirtilir.

2.Trusting Domain (Güvenen Domain) kutusu güvenilen domain tarafından doldurulur ve güvenen domain'i *bana kim güven vermiş* belirtir.

*İlişkinin daha kısa sürece kurulabilmesi için önce Trusting Domain tarafından güvene izin verilmesinin ardından Trusted Domains tarafının düzenlenmesi gerekir. Eğer tersi yapılırsa o zaman bu işlem (15 dakika kadar) süre alabilir.*

Önce güvenilmek istenen domain'in yöneticisi güven istediği domain’in adını *Trusingt Domain* iletişim kutusunda yazar. Bu işlemin ardından güvenen (güven verecek olan) domain güven vereceği domain’in adını *Trusted Domains* bölümüne yazar.

*Bu sıra ile düzenlenen güven ilişkilerinde güvenen domain yöneticisi güven ilişkisinin kurulduğu mesajını alır.*

Domain-ADomain-BPermitted to Trust this Domain:

Domain-BTrusted Domains:

Domain-A

**İki-Taraflı Bir Güven İlişkisi Düzenlenmesi**

İki taraflı bir domain ilişkisi düzenlemek iki tane bir taraflı güven ilişkisi düzenlemektir. Birinci güven ilişkisindeki güvenilen ve güvenen yerine ikinci ilişkide güvenen ve güvenilen olarak güven ilişkisi karşılıklı olarak kurulur.

Domain-ADomain-BTrusted Domains:

Domain-BTrusted Domains:

Domain-A

Domain-ADomain-BTrusting Domain:

Domain-BTrusting Domain:

Domain-A

İki taraflı ilişkinin yarısı kaldırıldığında diğer taraftan da yarısı otomatik olarak kalkar.

**Parola (Password) Verilmesi**

Güvenilen domain'in yöneticisi diğer domain'e güven izini verirken parola koyabilir. Bu işlemin yapılmasının ardından bu domain'e güven verecek olan domain'in yöneticisi bu parolayı girerek güven ilişkisini kurar.

**Güvenler Arasında İzinlerin Verilmesi**

İki domain arasında güven ilişkisi tesis edildikten sonra güvenen domain'de güvenilen taraftaki kullanıcıların kullanımı için izin verilir. Önce NT Explorer çalıştırılır ve paylaştırılacak dizin seçilir.

Daha sonra seçilen dizin üzerinde farenin sağ tuşuna basılarak Properties (Özellikler) seçilir.

Buradan Permissions (İzinler) diyalog kutusu ile seçilen dizin ve dosya için istenilen kullanıcı, kullanıcılar ya da gruplara istenilen izinler verilir. Bu düğmeye basılarak dizin ya da dosya üzerinde mevcut izinleri olan kullanıcı ve gruplar görülür.

Ardından Add düğmesi ile bu dizine erişim hakları vereceğimiz başka kullanıcılar ekleyebilir veya Remove ile seçilen kullanıcı veya kullanıcıları çıkartıp bu dizini (kaynağı) kullandırtmayabiliriz. Seçilen kullanıcıya, Type of Access kısmından, bu kaynağı kullanım haklarını belirleyebiliriz. Bu haklar yandaki resimde görülmektedir.

Bu erişim haklar aşağıda sıralanmıştır:

**No Access:** Erişim hakkı yok.

**List:** Dosyaların isimlerini listeler.

**Read:** Dosya içeriğini görebilir.

**Add:** İlave yapabilir.

**Add & Read:** İlave ve okuma yapabilir.

**Change:** Değişiklik yapabilir.

**Full Control:**

**Special Directory Access:**

**Special File Access:******

---
*Kaynak: `BİRDEN ÇOK DOMAİN İLE ÇALIŞMA/BIRDEN COK DOMAIN ILE CALISMA.doc` — BILGEM — 2004*
