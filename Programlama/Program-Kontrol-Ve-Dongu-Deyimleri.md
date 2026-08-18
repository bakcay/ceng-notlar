# Program Kontrol Ve Döngü Deyimleri

**8. BÖLÜM**

**PROGRAM KONTROL VE DÖNGÜ DEYİMLERİ**

**8.1. PROGRAM KONTROL DEYİMLERİ**

**8.1.1. IF Yapısı **

Programın akışını IF değimi ile birlikte verilen koşula bağlı olarak belirlenen veya ELSE, ELSEIF veya END IF değimleri ile oluşturulan işlem bloğuna geçmesini veya söz konusu program bloğunun işletilmeyip atlatılmasını sağlar.

** Yazılım :**

```vbnet
IF Şart THEN
Komutlar
ELSE
Komutlar
END IF
```

Şartın gerçekleşmesi durumunda THEN değiminden sonraki satır işletilir. Gerçekleşmemesi durumunda ise ELSE değiminden sonraki satırlar işletilir.

Tek satırda şart yazılırsa END IF değimi kullanılmaz.

```vbnet
IF Şart Komutlar THEN Komutlar
IF Şart Komutlar
```

**Örnek 8.1 : ** Girilen üç notun ortalamasını alıp, bu notların ortalamasına göre öğrencinin geçip veya kaldığını yazan programı yapınız?

```vbnet
Private Sub Form_Load()
Dim n1,n2,n3,ort
n1=val(InputBox(“1.Sınav Notunu Giriniz:”, “Sınav”);
n2=val(InputBox(“2.Sınav Notunu Giriniz:”, “Sınav”);
n3=val(InputBox(“3.Sınav Notunu Giriniz:”, “Sınav”);
ort=(n1+n2+n3)/3
IF (ort<50) Then
MsgBox(“Kaldınız” &ort)
Else
MsgBox(“Geçtiniz” &ort)
END IF
End Sub
```

**8.1.2. Select Case Yapısı **

İşlev bakımından IF değimine çok benzemektedir. Çok sayıda IF yapısı içi içe kullanıldığı zaman programın okunurluğu azalır ve programı izlemek zorlaşır. Bu gibi durumlarda Select Case yapısı kullanılır.

**Yazılım :**

```vbnet
Select Case Kontrol Değişkeni
Case ifade 1
......
Case ifade 2
.......
Case Else
.......
End Select
```

Genel yazılımdan anlaşılacağı gibi bloğu başlatan Select Case değiminden sonra yapılacak karşılaştırmalarda kullanılacak bir kontrol değişkeni bulunmaktadır. Eğer kontrol değişkeninin içeriği “ifade1” olarak verilen değerle aynı ise, birinci ifadenin içeriğini araştıran Case değiminden bir sonraki Case değimine kadar olan program satırları işletilir ve program akışı End Select değiminden sonraki satıra geçer.

**Örnek 8.2. : **Yukarıdaki örneği bu Select Case değimiyle yapalım.** **

```vbnet
Private Sub Form_Load()
Dim n1,n2,n3,ort
n1=val(InputBox(“1.Sınav Notunu Giriniz:”, “Sınav”);
n2=val(InputBox(“2.Sınav Notunu Giriniz:”, “Sınav”);
n3=val(InputBox(“3.Sınav Notunu Giriniz:”, “Sınav”);
ort=(n1+n2+n3)/3
Select Case ort
Case ort<50
MsgBox(“Kaldınız” &ort)
Case ort>50
MsgBox(“Geçtiniz” &ort)
End Select
End Sub
```

**Örnek 8.3 : **1-3 arasında girilen sayıyı bulan programı yapanız?

```vbnet
Private Sub Form_Load()
Dim sayi
sayi=val(InputBox(“1 ile 3 arasında bir sayı giriniz.”);
Select Case sayi
Case 1
MsgBox(“Girdiğiniz Sayı 1”)
Case 2
MsgBox(“Girdiğiniz Sayı 2” )
Case 3
MsgBox(“Girdiğiniz Sayı 3” )
End Select
End Sub
```

**8.1.3. IIF Yapısı**

Bir değişkenin değeri iki durumdan birine göre değer alırsa IF yapısı yerine IIF kullanılabilir. Bu yapı bize daha az satırla aynı işi yapabilmemizi sağlar.

**Yazılım :**

```vbnet
IFF (Şart; Doğru ise; yanlış ise)
```

**Örnek 8.4 : **

```vbnet
Private Sub Form_Load()
Dim n1,n2,n3,ort,son
n1=val(InputBox(“1.Sınav Notunu Giriniz:”, “Sınav”);
n2=val(InputBox(“2.Sınav Notunu Giriniz:”, “Sınav”);
n3=val(InputBox(“3.Sınav Notunu Giriniz:”, “Sınav”);
ort=(n1+n2+n3)/3
son=IIF (ort<50, “geçtiniz”, “Kaldınız”)
MsgBox son
End Sub
```

**8.1.4. Choose Yapısı**

Bir değişkenin aldığı değer bir sayıya bağlı ise bu yapıyı kullanmak daha uygun olur.

**Yazılım:**

```vbnet
Sonuç= Choose(sayı, değer1, değer2, değer3, değer4,......,değerN)
```

**Örnek 8.5:**

```vbnet
gun=Choose(GunNo, “Pazar”, “Pazartesi”, “Salı”, “Çarşamba”, “Perşembe”, “Cuma”, “Cumartesi”)
```

**8.1.5. Switch Yapısı**

Birden fazla şartı aynı anda kontrol etmek için kullanılır.

**Yazılım :**

```vbnet
Sonuç=Switch(Şart1, Değer1, Şart2, Değer2,.......,ŞartN, DeğerN)
```

**8.2. DÖNGÜ DEYİMLERİ**

**8.2.1. For-Next Döngüsü**

For-Next döngüsü sayacın başlangıç değerinden başlayarak bitiş değerine kadar istenilen miktarda artırılarak blok içindeki konutları çalıştırır.

**Yazlım:**

```vbnet
For Sayac=BaşlangıçDeğeri to BitişDeğeri [Step Artırım]
Komutlar
Next
```

**Not: ** Artma değeri verilmezse artış miktarı 1 olarak alınır.** **

**Örnek 8.6 :** 1’den 10’a kadar olan sayıları toplayan programı yapınız?

```vbnet
Private Sub Form_Load()
Dim sayi,i
For i=1 to 10
sayi=sayi+i
Next
MsgBox sayi
End Sub
```

**8.2.2.While-Wend ve Do While- Loop Döngüsü**

Bir şart gerçekleştiği sürece çalışması gereken program bloklarında kullanılırlar.

**Yazılım:**

```vbnet
While Şart
Komutlar
Wend

Do While Şart
Komutlar
Loop
```

Yukarıdaki her iki komutta da şart gerçekleştiği sürece döngüde kalınır.

**Örnek 8.7: **Klavyeden girilen 10 öğrencinin notlarına göre sınıf ortalamasını hesaplayan programı yapınız.

```vbnet
Private Sub Form_Load ()
Dim not (10) As Integer
Dim t As Integer
i=1
Do While i < = 10
Not(i) = InputBox(Str(i) & ”. Öğrencinin Notu”)
t = t + not(i)
Loop
ort=t/10
MsgBox ort
End Sub
```

**8.2.3. Do Until – Loop Döngüsü **

Bu döngü yapısı diğerlerinden farklı olarak şart gerçekleşene kadar

çalışması gereken program bloklarında kullanılır.

**Yazılım :**

```vbnet
Do Until Şart
Komutlar
Loop
```

**8.2.4. Do-Loop While ve Do Loop Until Döngüsü**

Bu döngü yapılarının diğerlerinden tek farkı şart döngüye girerken değil de çıkarken kontrol edilir. Yani döngü içerisindeki komutlar en az bir kez çalışırlar.

**Yazılım :******

```vbnet
Do
Komutlar
Loop Until Şart

Do
Komutlar
Loop While Şart
```

**Döngü Kontrol İfadeleri**

**8.2.5.1. Exit Do **

Bu komut Do-Loop ve While Wend döngülerinden birinde bazı şartların gerçekleşmesi durumunda döngüden çıkmak için kullanılır.

**8.2.5.2. Exit For **

** **For-Next döngüsü tamamlanırken bazı şartlar gerçekleştiğinde döngüden çıkmaya yarar.

**8.2.5.3. Exit Sub ve Exit Function **

Exit Sub ve Exit Function değimleri alt program sonuna ulaşmadan alt programdan çıkmaya yarar.

**8.2.5.4. End**

** **Programı sona erdirir.

PAGE 1

PAGE 83

---
*Kaynak: `PROGRAM KONTROL VE DÖNGÜ DEYİMLERİ/PROGRAM KONTROL VE DÖNGÜ DEYİMLERİ.doc` — BAHADIR İŞLEYEN — 2004*
