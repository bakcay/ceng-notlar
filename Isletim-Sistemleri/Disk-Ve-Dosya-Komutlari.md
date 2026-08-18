# Disk Ve Dosya Komutlari

Disk Ve Dosya Komutlar

Disk üzerinde işlem yapan komutları kullanırken hata ayıklama kodları kullanmak gereklidir. Aksi takdirde olmayan bir dizin veya dosya üzerinde işlem yapmaya kalktığınızda program hat verecek ve çalışması sona erecektir. Var olduğunu kabul edip hata ayıklama kodu koymadığınız durumlarda, kullanıcının onu silmiş olabileceği veya değiştirmiş olabileceği ve diğer durumları da düşünerek hata ayıklama komutlarını kullanmanız programınızın sağlıklı çalışması açısından iyi olacaktır. Örneğin kullanıcıdan disket sürücüye takmamışsa program hata verip sona erer. Halbuki hat kontrol edilmiş olsa bu durum ortadan kalkacaktır.

Bu komutu kullanırken aşağıdakine benzer bir yapı kullanılabilir.

On Load Error Goto Hata "hata olursa HATA isimli yere git.

Disk komutu "Hataoluşturabilecek komut

Exit Sub "Hata olmazsa aşağı devam etme

Hata:"HATA isimli yer

Msgbox("Hata") "hata Mesaj

Exit Sub Alt programdan çık

Bu yapıda, bir hata oluştuğunda hata kullanıcıya bildirilir ve program çalışmaya devam eder.

## **ChDrive**

Aktif sürücüyü değiştirir.

**Sürücü harfi:G**eçilmek istenen sürücünün baş harfini içeren string değerdir. Stringin içeriği bir karakterden fazla ise ilk harf dikkate alınır.

On Load Error GoTo hata

**ChDrive **“A” ‘A sürücüsüne

Exit Sub

Hata:

MsgBox (“Disket sürücüye erişilemedi : “ & Error)

Exit Sub

## **ChDir **

**ChDir Dizin **

Aktif dizini değiştirmeye yarar.

On Load Error GoTo hata

ChDir “c:\\windows”Aktif dizini Windows dizini yap.

Exit Sub

Hata:

MsgBox (“Dizine erişilemedi: “ & Error)

Exit Sub

VB’deki komutların dosya isimlerinde yo kullanılmazsa, aktif sürücü ve dizinde arnır.

## MkDir

**MkDir Dizin Adı**

Dizin oluşturmak için bu komut kullanılır.**DizinAdı** isimli dizini oluşturur.

On Load Error GoTo hata

RmDir “c:\\windos \\yedek” ‘Windows dizinindeki yedek dizinini aç

Exit Sub

Hata:

MsgBox (“ Dizin oluşturulamadı : “ & Error)

Exit Sub

## RmDir

**RmDir Dizin Adı**

İsmi verilen dizini siler. İsmi verilen dizinin alt dizinlerinin bulunması ve boş olması gerekir.

On Load Error GoTo hata

RmDir “c:\\windos \\yedek” ‘Windows dizinindeki yedek dizinini sil

Exit Sub

Hata:

MsgBox (“ Dizin oluşturulamadı : “ & Error)

Exit Sub

## Kill

**Kill Dosya Adı**

İsmi verilen dosyayı siler.

On Load Error GoTo hata

Kill “c:\\windos \\\*.tmp ‘Windows dizinindeki TMP dosyaları sil

Exit Sub

Hata:

MsgBox (“ Dizin Silinemedi : “ & Error)

Exit Sub

## Name

**Name Ad As Yeni Ad**

Verilen dosyanın ismini değiştirir.

Name “Eski.Doc” As “Yeni.Doc” satırı ile Eski.Doc ismi Yeni.Doc olarak değiştirilmiştir.

On Load Error GoTo hata

Dim eski, yeni

Eski=InputBox(“İsmi değiştirilecek dosya”)

Yeni=InputBox(“Yeni Adı”)

Name eski As yeni

Exit Sub

Hata:

MsgBox (“İsim Değiştirilemedi: “ & Error)

Exit Sub

## CurDir

**CurDir \[ Sürücü Harfi \]**

ChDir komutunun aktif dizini değiştirildiğini biliyorsunuz. Bu komut ise aktif dizini öğrenmenize yarar.

Sürücü harfi kullanılmazsa aktif sürücüdeki aktif dizi bildirir. Sürücü harfi verilirse verilen sürücüdeki aktif bildirir.

Print CurDir Print CurDir “A”

## **File Copy**

**FileCopy kaynak dosya, HedefDosya**

Bu komut DOS’un Copy komutu kadar gelişmiş olmasa da bir dosyayı bir yerden, başka bir yere kopyalamamızı sağlar.

Kaynak Dosya :Kopyalanacak Dosyanın yeri ve dosyanın adı.

Hedef Dosya :Kopyalanacak Dosyanın yeni yeri ve adı.

Dosya adı, sürücü ismi ve yol içerebilir ancak joker karakter dediğimiz ?,\* gibi karekterleri içeremez. Bu da, bu komutu kullanarak bir seferde sadece bir dosya kopyalayabilirsiniz demektir.

FileCopy “\\Windows\\Win.Com” , “\\Dos\\Win.Com”

Dikkat ederseniz Dos’un Copy komutundan farklı olarak, hedef olarak yolu ve dosyanın ismini vermeniz gerekir.

## **File Len**

**FileLen(Dosya Adı)**

İsmi verilen dosyanın boyutunu byte olarak bildirir. Bu dosya adına sürücü ve yol ismi de verilebilir.

| Print “Win.Com dosyasının boyu”;FileLen (“\\Wimdows\\ Win.Com”) |
| --- |

## **FileDateTime**

**FileDateTime(DosyaAdı)**

Dosyanın tarih ve saatini verir.

Geri dönen değer “ Tarih saat” formatındadır.

## **GetAttr**

**GetAttr(DosyaAdı)******

Dosyanın attributesini öğrenmeye yarar.

Geri dönen değer aşağıdaki sayılarla And işlemine tabi tutularak o özelliğin bulunup bulunmadığı öğrenilir.

**Anlamı Sembolik Sayısal Değer**

Yalnız okunabilir dosya(Read Only) VbReadOnly 1

Gizli Dosya(Hidden) VbHidden 2** **

System Dosyası VbSystem 4

Volumetkisi VbVolume 8

Dizin VbDirectory 16

Arşiv dosyası VbArchive 32

Normal VbNormal 0

Alias İsim VBAlias 64

Dim attr

Attr=GetAttr (“\\windows\\win.com”)

Print”win.com”;

İf Attr And 1 Then print “R”;

İf Attr And 2 Then print “H”;
İf Attr And 4 Then print “S”;
İf Attr And 32Then print “A”;

---
*Kaynak: `DISK VE DOSYA KOMUTLARI/DISK VE DOSYA KOMUTLARI.doc` — Bilgisayar Bölümü — 2004*
