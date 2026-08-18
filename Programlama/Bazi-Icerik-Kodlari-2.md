# Bazi İçerik Kodlari

## **Text Box Nesnesinde Default Popop Menüler Açılmasın**

Bir kelime işlemci programı üzerinde uğraşıyorsunuz.Text Box nesnesine sağ tuşla tıklayınca Windows'a özgün menüler çıkıyor.Uğraştınız,uğraştınız yapamadınız.Aslında çözümü o kadar da zor değilmiş diğecek bir kod veriyoruz size...Proje için bir Text Box,birde adı "Popıp1" olan ve altmenülere sahip sizin kendi hazırladığınız menü.Eğer hata verirse hiç altmenüsü olmayan bir menü tasarlamışsınız demektir.Bu yüzden "Popup1"'in altmenülerini yapmayı unutmayınız.

```vbnet
Private Sub Text1_MouseDown(Button As Integer, _
Shift As Integer, X As Single, Y As Single)

If Button = 2 Then
Text1.Enabled = False
PopupMenu Popup1
Text1.Enabled = True
End If
End Sub
```

## **Status Bar'daki panelin özelliklerini değiştirmek**

Uygulama çalışırken status bar nesnesinde panel özelliklerini değiştirmek çok kolaydır.Aşağıda bir kaçını görebilirsiniz.Sadece önemli olan panelin INDEX numarasıdır.Değiştirme buna göre gerçekleşir.

```vbnet
StatusBar1.Panels(1).Text = "vbturk"
StatusBar1.Panels(1).ToolTipText = "vbturk"
```

## **Menülere Ayıraç Eklemek**

Bunu yapmak için tasarladığınız menünün başlığını "-" yapın(tırnaklar hariç).Adınıda istediğiniz bir şet yapın.

## **Yazının Kaç Karakter Olduğunu Bulma**

Bu olay için bize Len() fonksiyonu yetecektir.Aşağıdaki kod size yeter.

```vbnet
private sub form_load()
dim a,b
a="merhaba Len() fonksiyonu"
b=len(a)
call msgbox b
end sub
```

## **Formunuz İçin Güzel Kapanış**

Formlarınıza güzel bir kapanış eklemek isteyenlerinimiz vardır herhalde.Öyleyse aşağıdaki anlaşılır kodu kopyalayınız ve uygulamanıza yerleştiriniz.Program için bir adet Timer nesnesi gerekiyor.

```vbnet
Private sub form_load()
timer1.interval=50
timer1.enabled=false
end sub
Private Sub Timer1_Timer()
Form1.Width = Form1.Width - 30
Form1.Height = Form1.Height - 30
Form1.Top = Form1.Top + 50
Form1.Left = Form1.Left + 5
End Sub
Private Sub Form_Unload(Cancel As Integer)
timer1.enabled=true
End Sub
```

## **Randomize Sayı Üretmek**

Randomize sayı üretmek için rnd() fonksiyonu yeterlidir.Aşağıda çok basit bir kod var.

```vbnet
Private Sub Form_Load()
' 1 ile 10 arasında değişik bir tamsayı üretir
random = Int(Rnd * 10)
End Sub
```

## **Tüm Text Box Nesnelerinin İçeriğini Temizlemek**

Gelişmiş kelime işlemci programlarınızda kesinlikle arama olayının olması gerekir.Aşağıdaki kodu alın ve kopyalayın.Uygulama için bir RichTextBox nesnesi birde command button yeterli olur.

```vbnet
Private Sub Command1_Click()
dim x
ara=inputbox("Ara", "Bul", richtextbox1.seltext)
x=richtextbox1.find("bul",richtextbox1.selstart)
if x<0 then
msgbox x & "Aranan Kelime Bulunamadı"
end if
end sub
```

## **Denetim Masasını Açmak**

Programınızdan denetim masasına ulaşmanın en kısa yolu RunDLL dir.Kopyalayın yeter.

```vbnet
Private Sub Form_Load()
Shell ("rundll32.exe shell32.dll,Control_RunDLL")
End Sub
```

**Visual Basic'te "" işaretlerini yapabilmek**

Bilirsiniz bir değişkene yazı eklemek için "" işaretlerini kullanmak gerekir.ama öyle zamanlar gelirki "" işaretlerini değişkende kullanmak gerekir.Bunun için chr(34) yazmanız yeterlidir.Aşağıda daha iyi anlarsınız

```vbnet
örnek="babam bana " & chr(34) & "Gel lan buraya" & chr(34) &" dedi"
```

## **Dosya Silmek**

Öyle durumlar gelirki Visual Basic'le bir dosya silmeniz gerekir.Gerektiğinde bir satırlık kod işinizi görecektir.

```vbnet
kill "c:\autoexec.bat"
```

## **Visual Basic 6'da Ses Dosyalarının Çalınması**

Programınızda *.wav formatındaki ses dosyalarını mı çalmak istiyorsunuz?Çok kolay.Bunu bir Windows Multimedia API'sı çözer.Yanlız Ses Dosyası Başka Bir Klasördeyse Klasörüde Belirtiniz.

```vbnet
'Formun Declarations Bölümüne
Private Declare Function sndPlaySound Lib "winmm.dll" Alias_
"sndPlaySoundA" (ByVal lpszSoundName As String, ByVal_
uFlags As Long) As Long
'Formun Ana Kısmına
private sub form_load()
sndPlaySound "ses.wav",0
end sub
```

## **Visual Basic'te Kes,Kopyala,Yapıştır,Tümünü Seç İşlemleri**

Visual Basic'te Bu işlemleri yapmak çok kolaydır.Clipboard nesnesi ve Len() fonksiyonu bu işlemleri yapmamızı sağlar.Sadece Bir İki İnce Ayrıntı Var.

```vbnet
With text1 'Tümünü Seç
.SetFocus '
.SelStart = 0 '
.SelLength = Len(text1.Text) '
End With
'------------------------------------------
Clipboard.Clear 'Kes
Clipboard.SetText text1.SelText '
'------------------------------------------
Clipboard.SetText text1.SelText 'kopyala
'------------------------------------------
text1.SelText = Clipboard.GetText 'yapıştır
```

**Text Box'da çok satır kullanma**

Text box'da çok satır kullanamamak hepimizi zor duruma düşürür değilmi.Bunu çözmek için bir satırlık kod olduğunu duyunca herhalde kafayı yiyorsunuzdur.Yemeyin ve aşağıdaki kodu inceleyin.

```vbnet
text1.multiline=true
```

**Komut Düğmesine Tuş Atamak**

Belki dikkat etmişsinizdir komut düğmelerinde cancel ve default özelliklerine. Bunlar fazla kullanılmayan,ama çok önemli öezlliklerdir.Aşağıdaki koddan görebilirsiniz.

```vbnet
' Enter tuşuna basıldığında command1 basılmış sayar
command1.default=true
'ESC tuşuna basıldığında command2 ye basılmış say
command2.cancel=true
```

## **Formu Ortalamak**

Formunuzu ortaya getirmek istiyorsanız 2 satırlık bir kod yazmanız gerekiyor.Kod çok açık:

```vbnet
Private Sub Form_Load()
Left = (Screen.Width - Width) \ 2
Top = (Screen.Height - Height) \ 2
End Sub
```

## **Boş Kodlara Son**

Hepimiz kodla bir nesnenin özelliklerini değiştiririz.Ama bu bazen çok seviyeye çıktığında boşuna nesneyi onlarca kez kullanmak gerekmez.Aşağıyı incelerseni With fonksiyonunun ne kadar yararlı olduğunu öğrenirsiniz.

```vbnet
'önceki hal
command1.default=true
command1.height=124
command1.style=1
command1.mousepointer=2
-----------------------
'sonraki hal
with command1
.default=true
.height=124
.style=1
.mousepointer=2
end with
'Ne kadarda kolaymış değilmi?
```

**Şifreli Text Box'lar**

Bir çoğumuz ya internet sitelerinde yada bazı programlarda ***** karakterleri ile gizlenmiş kutucuklar görmüşüzdür.Bunları Visual Basic'te kullanmakta çok kolaydır.Sadece textbox nesnesinin passwordchar özelliğine "*" işaretini koyunuz(tırnaklar hariç).Eğer başka bir karakter koymak istiyorsanız tek haneli bir karakter girebilirsiniz.

```vbnet
Text1.PasswordChar = "*"
```

## **Dominant Pencereler**

Bazı pencereler hep üstte kalmayı başarabiliyorlar. Bunu yapmak da çok kolay. Sizlere bununla ilgili çok kısa bir kod hazırladım. Başrolde SetWindowsPos API si yer alıyor.Nefesleri kesecek bu projeyi hep beraber kullanalım.

```vbnet
'Bu kodu tamamen kopyala-yapıştır yapın...
'Formun kod kısmına aynen ekleyin bakalım n'olcak ?
Const HWND_TOPMOST = -1 ' Hep üstte tutan değişken değer
Const HWND_NOTOPMOST = -2 ' Hep üstte özelliğini yok eden değişken değer...
Const SWP_NOSIZE = &H1 ' Formun boyutlarını değiştirilmez yapar...
Const SWP_NOMOVE = &H2 ' Formu taşınmaz yapar...
Const SWP_NOACTIVATE = &H10 ' Form Aktif yapılmaz...
Const SWP_SHOWWINDOW = &H40 ' Pencere Görünür Yapılır...
Private Declare Sub SetWindowPos Lib "User32" (ByVal hWnd As Long, ByVal hWndInsertAfter As Long, _
ByVal X As Long, ByVal Y As Long, ByVal cx As Long, ByVal cy As Long, ByVal wFlags As Long)

' Form Her Aktif Olduğunda su üstüne çıkıyor :-)
Private Sub Form_Activate()
' vbturk
' http://www.xx.com

SetWindowPos Me.hWnd, HWND_TOPMOST, 0, 0, 0, 0, SWP_NOACTIVATE _
Or SWP_SHOWWINDOW Or SWP_NOMOVE Or SWP_NOSIZE

End Sub
```

## **Yuvarlak Pencereler**

API üstüne API ile karşınızda olmaya devam ediyoruz. Sizleri API ye boğmaya karar vermiş biri olarak şimdi de YUVARLAK Bir Form Nasıl Oluşturulur tüm sırları ile beraber sunuyorum. Hiç bir yerde bulamayacağınız çok özel pozları ile karşınızda CreateEllipticRgn ve sevgilisi SetEllipticRgn nun bu pozlar karşısında şok etkisi yaratacak açıklamaları...

```vbnet
'Komple Formun kod bölümüne ekleyin(kopyala-yapıştır) :-)
'API tanımlamaları yapılıyor...

Private Declare Function CreateEllipticRgn Lib "gdi32" (ByVal X1 As Long, ByVal Y1 As Long, _
ByVal X2 As Long, ByVal Y2 As Long) As Long

Private Declare Function SetWindowRgn Lib "user32" (ByVal hWnd As Long, ByVal hRgn As Long, _
ByVal bRedraw As Long) As Long

'Pencere yüklenirkene formu yuvarlatıyoruz...
Private Sub Form_Load()
Dim hr&, dl&
Dim usew&, useh&
usew& = Me.Width / Screen.TwipsPerPixelX
useh& = Me.Height / Screen.TwipsPerPixelY
' Oluşturuluyor...
hr& = CreateEllipticRgn(0, 0, usew, useh)
' Gösteriliyor...
dl& = SetWindowRgn(Me.hWnd, hr, True)
End Sub
```

## **Delikli Nane :-)**

Vallahi denecek başka bir şey yok. O pozlardan sonra kim olsa
delerdi bi' tarafını :-).

Her ne ise ! Bu API yi zaten biliyorsunuz. Yuvarlak bir form
oluşturmuştuk şimdi de içi delik bir form oluşturuyoruz. Esasında
amacım simit şeklinde bir form oluşturmaktı ama başaramadım.
Başarırsam ileride sizlere duyururum. Bu arada siz yaparsanız da
bana yollamaktan çekinmeyin...

Alın aşağıdaki kodu aynen kopyala-yapıştır yapın. Bu arada amman
dikkat bunu VB farketmesin yoksa Windows' unuz çökebilir.
Çok kızar! Acayip karşıdır kopyalamaya..

```vbnet
Private Declare Function CreateRectRgn Lib "gdi32" (ByVal X1 As Long, ByVal Y1 As Long, ByVal X2 As Long, ByVal Y2 As Long) As Long
Private Declare Function CreateEllipticRgn Lib "gdi32" (ByVal X1 As Long, ByVal Y1 As Long, ByVal X2 As Long, ByVal Y2 AsLong) As Long
Private Declare Function CombineRgn Lib "gdi32" (ByVal hDestRgn As Long, ByVal hSrcRgn1 As Long, ByVal hSrcRgn2 As Long, ByVal nCombineMode As Long) As Long
Private Declare Function SetWindowRgn Lib "user32" (ByVal hWnd As Long, ByVal hRgn As Long, ByVal bRedraw As Long) As Long

'Form her değiştiğinde uygulanacak.
Private Sub Form_Resize()
Const RGN_DIFF = 4
' VB#Türk Progreamlama Grubu
' http://vbturk.cjb.net
Dim outer_rgn As Long
Dim inner_rgn As Long
Dim combined_rgn As Long
Dim wid As Single
Dim hgt As Single
Dim border_width As Single
Dim title_height As Single

'Eğer pencere simge durumunda ise işlem sonlandırılıyor.
If WindowState = vbMinimized Then Exit Sub

' Yuvarlaklar oluşturuluyor...
wid = ScaleX(Width, vbTwips, vbPixels)
hgt = ScaleY(Height, vbTwips, vbPixels)
outer_rgn = CreateRectRgn(0, 0, wid, hgt)

border_width = (wid - ScaleWidth) / 2
title_height = hgt - border_width - ScaleHeight
inner_rgn = CreateEllipticRgn( _
border_width + ScaleWidth * 0.1, _
title_height + ScaleHeight * 0.1, _
ScaleWidth * 0.9, ScaleHeight * 0.9)

' İç ile dış eşleştiriliyor...
combined_rgn = CreateRectRgn(0, 0, 0, 0)
CombineRgn combined_rgn, outer_rgn, _
inner_rgn, RGN_DIFF

' Pencere gösteriliyor...
SetWindowRgn hWnd, combined_rgn, True
End Sub
```

## **Sürüm Sürüm Süründürün**

İşte sizlere bir güzellik daha !
İllaki de Windows Pencerelerinin başlık çubuğunu mu kullanmak zorundasın sanki ? Hayır !
O halde aşağıdaki ReleaseCapture API si ile sizler de herhangi bir nesneye tıklayarak
formu istediğiniz yere sürükleyebilirsiniz. Bu nesne ister bir resim, ister bir düğme
isterse de formun herhangi bir boş alanı olabilir. Gerisi size kalmış...

```vbnet
'Formun Kod Bölümüne ekleyiniz...

Private Declare Function SendMessage Lib "User32" Alias "SendMessageA" (ByVal hWnd As Long, ByVal wMsg As Long, ByVal wParam As Long, lParam As Any) As Long
Private Declare Sub ReleaseCapture Lib "User32" ()

Const WM_NCLBUTTONDOWN = &HA1
Const HTCAPTION = 2
Private Sub Form_MouseMove(Button As Integer, Shift As Integer, X As Single, Y As Single)
' VB#Türk Programlama Grubu
' http://vbturk.cjb.net/
Dim lngReturnValue As Long
If Button = 1 Then
'Pencere Yakalanıyor
Call ReleaseCapture
' Forma mesaj yollanıyor
lngReturnValue = SendMessage(Me.hWnd, WM_NCLBUTTONDOWN, HTCAPTION, 0&)
End If
End Sub
Private Sub Form_Paint()
FontSize = 12
Me.Print "Formu taşımak için herhangi bir yere tıklayarak sürükleyiniz."
End Sub
```

## **Boyut**

Bir Pencerenin o anki durumunun ne olduğunu öğrenmeniz gerekebilir.
Diyelimki, projenizin sadece Pencere açıkken çalışmasını isteyebilirsiniz.

Bunu yapmak için de sizlere ISICONIC adlı bir WinAPI den bahsedeceğim.
Bu WinAPI yardımıyla eğer bir pencere simge durumuna küçültülmüş ise
anlayabiliyoruz.

Bu da sizlere bir takım alanlarda işe yarar bir dipnot olarak bu sayfalarda
kalsın.

```vbnet
'Projeye 1 tane Timer Nesnesi Ekleyiniz..
Private Declare Function IsIconic Lib "user32" _
(ByVal hwnd As Long) As Long

Private Sub Form_Load()
'VB#Türk Programalam Grubu
'http://vbturk.cjb.net
Timer1.Interval = 100
Timer1.Enabled = True
End Sub
Private Sub Timer1_Timer()
Dim Durum As Boolean
'Formun Durumu Nedir ?
Durum = IsIconic(Me.hwnd)
'Formun Durumu Başlık Olarak Atanıyor.
If Durum <> False Then
Me.Caption = "Simge !!"
Else
Me.Caption = "Pencere !!"
End If
End Sub
```

---
*Kaynak: `BAZI İÇERİK KODLARI/KODLAR/Kodlar2.doc` — mine — 2002*
