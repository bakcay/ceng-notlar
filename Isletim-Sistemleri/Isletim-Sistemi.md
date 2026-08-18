# İşletim Sistemi

İŞLETİM SİSTEMİ (MS-DOS)

(Microsoft dis Operaijen sistem)

MS-DOS işletim sistemi bıll bate tarafından PC-DOS ismi ile yazılmış microsoft firmasını kurduktan sonra MS-DOS olarak değiştirilmiştir. Devamlı değiştirilen MS-DOS işletim sistemi 10 versiyondan başlamış ve günümüzde 6.22 vesiyona ulaşmıştır. MS-DOS IBM uyumlu kişisel bilgisayarları çalışır hale getiren ve birbirlerinden farklı işlemler için hazırlanmış programlar zinciridir. Bu modüler programlar bilgisayarı çalışır hale gelmesini üç ana program ve işletim sistemine destek veren harici paket programlardan oluşur. MS-DOS işletim sisteminin, bilgisayarı çalışır hale getiren üç ana paket programı

10-SYS-MS-DOS, SYS

COMMAND.COM

10.SYS:Bellek giriş çıkış işlemlerini denetler.

MS-DOS-SYS: disk giriş çıkış işlemlerini denetler

COMMAND.COM: yapılacak çalışmalarda kullandığımız işletim sistemi dahili komutları içeren programlayıcı

BİLGİSAYARIN ÇALIŞIR HALE GELMESİ

Bilgisayar açıldığında ana bellek üzerindeki rom çipinde bulunan küçük bir program (BİOS) okunarak çalıştırılır. BİOS sırayla şu işlemleri yapar

1-Program önce ana belleğin durumunu kontrol eder.

2-Klavyenin bağlantısını kontrol eder. (keyboard Error) hata mesajıyla kullanıcıyı uyarır.

3-Ekranı kontrol ederek bir hata olup olmadığını kontrol eder.

4-A-Disket sürücüsünün çalışıp çalışmadığımı, sürücü kontrolünün normal olup olmadığına bakar.

5-bilgisayarın açıldığı manyetik ortamdan (sabit disk ve A sürücüsündeki disketten 1,0 SYS-MS-DOS-SYS okunarak belleğe alınarak çalıştırılır.

6-1,0 SYS çalışır çalışmaz gonkfin SYS programının olup olmadığına bakar varsa bellek yapısı ile ilgili komutları yerine getirir.

7-COMMEN,COM programı, belleğe yüklenerek çalıştırır.

8-COMMEN,COM çalışır çalışmaz AUTO EXEL BAT programının olup olmadığına bakar. Varsa tanımlanan komutlar sırayla yapılır.

9-Come: com :tarih ve saat bilgilerini görüntüleyerek değişiklik yapılmasını bekler.

KLAVYE:

FONKSİYON TUŞLARI:İşletim sisteminde komut satırından girilen komutlar geçici bellekte TEMPORARY MEMORY saklatılır. Bu komutların, tekrar belge edilmesi için, kullanılan ve klavyede F harfi ile numaralandırılmış tuşladır. F (veya sağ ok tuşu) geçici bellekteki bir önce verilen komutun karakterlerini birer, birer elde edilmesinde kullanılır. F2 geçici bellekteki bir önce verilen komutun belirli bir yerine kadar olan kısmını elde etmek için kullanılır.örneğin bir önce verilen komut makineyi kapat ise önce F2 tuşuna sonra “N” ye basılınca makin kısmını verir.

F3 Geçici bellekteki bir önce verilen komutun tamamını tekrar elde etmek için kullanılır. F4 Geçici bellekteki önce verilen komutun belirli bir yerinden sonrasını elde etmek için kullanırız. F5 hepsini silmek için kullanırız. ENTER: komut satırından henüz yazılmış satırı iptal eder. F6 (Come,com ) komutu veya EDLIN programı ile yazılan komutların yada bir metin yazılımının bittiğini belirten Z(EOF) End offile) (dosya sonu)

F7 Doskey com) isimli geçici bellek yapısını büyütme programı çalıştırılmışsa geçici bellekteki komutları numaralandırarak listeler

KISAYOL TUŞLARI

CTRL+S, CTRL+C, CTRL+BREAK, CTRL+SCROLLIOK, CTRL+Z, CTRL+P, CTRL+N, CTRL+N, CTRL+H, CTRL+ALT+DEL

KULLANILAN DİĞER YARDIMCI TUŞLAR

ESC, TAB, CAPS LOCK, SHİFT, CTRL, ALT, SPACE BAR, ENTER, BACK SPACE, DELETE, COME, END, PAGEUT, PRİNT SCTEEN, INSERT, SCROLL LOCK, PAUSE, NUMLOCK,

YAZILIM TANIMLARINDA KULLANILAN İFADELER

Program adı:bir işlem yaptırmak amacıyla yazılmış programlara verilen isimdir. En az bir en fazla 8 karakter uzunluğunda olabilir.

Program uzantısı: program adından sonra nokta ile paragraf özelliğini belirtmek amacıyla verilen tanımdır.en fazla 3 karakter uzunluğunda olabilir. Hemen çalıştırılabilir. Küçük uzantılarıdır.

COM: Belirli bir işlem yapmak için hazırlanmış komut programlarına verilen uzantı BAT: kullanıcı tarafından hazırlanan toplu işlem komut dosyalarına verilen uzantı

EXE:belirli bir işlem yapmak için hazırlanmış, çalıştırılabilir durumda olan programlara verilen uzantı.

MS-DOS KOMUTLARI

Dahili komutlar: Comand com dosyası içinde yer alan kullanılması için başka sistem kütüklerine gereksinim duyan komutlar dahili komutlarıdır

Harici komutlar: kullanılabilmeleri için sistem kütüklerinin yanında başka kütüklere de ihtiyaç duyulan komutlar harici komutlarıdır.

DAHİLİ KOMUTLAR:

Break=program durdurma

Buffers

Call

Cd(chdır)=drectory değiştirme

Chep

Cls=Ekran silme

Coppy=dosya kopyalama

Ctty=Standart giriş çıkış komutları

Date=Tarih gösterme değiştirme

Del(Frase)=Dosya silme

Exit

Fcbs

Files

Format=Disketi MS-DOS Hazır hale getirme

Goto

If

Include

Instail

Lastdrive

Pause

Prompt=komut uyarısını değiştirme

Rd(Rmdır)=Director silme

Rem

Ren (Rename)=Dosya ismi değiştirme

Set=Hafızaya karakter dizisi yerleştirme

Shellf

Shift

Stacks

Submeny

Devıce

Devicetlingh

Dır=Dosya listesi

Drıvparm

Eacho

Dos

Md(mkdır)=directory açma

Menucolor

Menudefaults

Numlock

Path=Komut arama yolu ayarlama

Swıtches

Tıme

Type=Bir metin dosyasını içeriğini görme

Ver=MS-DOS Versiyon numarasını gösterir

Verıfy=Dosya kontrolü

Vol =Disketi veya seri nosunu gösterme HARICİ komutlar

Append=Veri dosyaları için arama yolu ayarlama

Attrib=dosya niteliklerini görüntüleme ve ayarlama

Chkdisk

Choice

Command=komut işlemlerini başlatma

Dbisboce

Debus

Detreg

Deltree

Diskcomp=Disket karşılaştırma

Diskcoyp=disket kopyalama

Doskey

Dosswap

Edit

Fasthelp

Fastopen =zaman azaltma

Fc=dosya karşılaştırma

Fdisk=harddiski hazırlama

Find=Veri arama

Format=Diski-Disketi MS-DOS a hazır hale getirme

Graphics=renkli veya grafik monitör adaptörü kullanımında printer üzerinde grafik görüntü ekranı çizilmesi

Help

Interınk

Intersur

Keyb=klavye programı yükleme

Keyms

Label=disk etiketi yaratma-değiştirme

Loadfix

Mem:=hafızaya gösterme

Memmaker

Mode=mod değiştirme

More=ekran görüntüsü

Move

Mscdex

Msd

Mnav

Mnantsr

Mnbackup

Mwundel

Nisfune

Park

Power

Print

Gbasic

Replace=dosya yenileme

Restore

Scandisk

Setver

Share

Sizer

Smartdrv

Smartmon

sort

substr=bir sürücü harfi ile drectory arasında bağlantı

sys=Sistem dosyalarının hard diske transferi

tree=drectory listesi

undelete

unformat

v.safe

xcopy=Dosya kopyalama

---
*Kaynak: `İŞLETİM SİSTEMİ/İŞLETİM SİSTEMİ.doc` — Çağrı Kıroğlu — 2004*
