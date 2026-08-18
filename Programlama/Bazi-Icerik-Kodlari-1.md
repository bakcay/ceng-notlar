# Bazi İçerik Kodlari

## **YAZDIĞINIZ SAYIDAKİ BANKNOT ADETLERİNİ VERİR**

```vbnet
Private Sub Command1_Click()
Dim i, j
Cls
i = Val(Text1.Text) 'text kutusuna yazılanı sayıya cevirir.'
j = Int(i / 10000000)
Print j; "tane 10000000 tl"
i = i Mod 10000000
j = Int(i / 5000000)
Print j; "tane 5000000 tl"
i = i Mod 5000000
j = Int(i / 1000000)
Print j; "tane 1000000 tl"
i = i Mod 1000000
j = Int(i / 500000)
Print j; "tane 500000 tl"
i = i Mod 500000
j = Int(i / 250000)
Print j; "tane 250000 tl"
i = i Mod 250000
j = Int(i / 100000)
Print j; "tane 100000 tl"
i = i Mod 100000
j = Int(i / 50000)
Print j; "tane 50000 tl"
i = i Mod 50000
j = Int(i / 10000)
Print j; "tane 10000 tl"
i = i Mod 10000
j = Int(i / 5000)
Print j; "tane 5000 tl"
i = i Mod 5000
Print "kalan"; i; "tl nin degeri yok"
End Sub
```

## **CD KAPAGINI AÇIP KAPAMAK**

```vbnet
Private Declare Function mciExecute Lib "winmm.dll" (ByVal lpstrCommand As String) As Long
Private Sub Command1_Click()
mciExecute ("Set CDAudio door Open")
End Sub

Private Sub Command2_Click()
mciExecute ("Set CDAudio door closed")
End Sub
```

## **EKRAN ÇÖZÜNÜRLÜK AYARI**

```vbnet
Private Sub Command1_Click()
Dim X As Integer, Y As Integer
With Screen
X = .Width / .TwipsPerPixelX
Y = .Height / .TwipsPerPixelY
End With
Label1.Caption = "Ekran Çözünürlüğü"
Label2.Caption = X & "x" & Y
End Sub
```

## **KAYAN YAZI**

```vbnet
Option Explicit

Private m_bDoEffect As Boolean

Private Declare Function timeGetTime Lib "winmm.dll" () As Long
Private Declare Function SetTextCharacterExtra Lib "gdi32" (ByVal hdc As Long, ByVal nCharExtra As Long) As Long
Private Type RECT
left As Long
tOp As Long
Right As Long
Bottom As Long
End Type
Private Declare Function OffsetRect Lib "user32" (lpRect As RECT, ByVal x As Long, ByVal y As Long) As Long
Private Declare Function SetTextColor Lib "gdi32" (ByVal hdc As Long, ByVal crColor As Long) As Long
Private Declare Function FillRect Lib "user32" (ByVal hdc As Long, lpRect As RECT, ByVal hBrush As Long) As Long
Private Declare Function CreateSolidBrush Lib "gdi32" (ByVal crColor As Long) As Long
Private Declare Function DeleteObject Lib "gdi32" (ByVal hObject As Long) As Long
Private Declare Function GetSysColor Lib "user32" (ByVal nIndex As Long) As Long
Private Const COLOR_BTNFACE = 15
Private Declare Function TextOut Lib "gdi32" Alias "TextOutA" (ByVal hdc As Long, ByVal x As Long, ByVal y As Long, ByVal lpString As String, ByVal nCount As Long) As Long
Private Declare Function DrawText Lib "user32" Alias "DrawTextA" (ByVal hdc As Long, ByVal lpStr As String, ByVal nCount As Long, lpRect As RECT, ByVal wFormat As Long) As Long
Private Const DT_BOTTOM = &H8
Private Const DT_CALCRECT = &H400
Private Const DT_CENTER = &H1
Private Const DT_CHARSTREAM = 4 ' Character-stream, PLP
Private Const DT_DISPFILE = 6 ' Display-file
Private Const DT_EXPANDTABS = &H40
Private Const DT_EXTERNALLEADING = &H200
Private Const DT_INTERNAL = &H1000
Private Const DT_LEFT = &H0
Private Const DT_METAFILE = 5 ' Metafile, VDM
Private Const DT_NOCLIP = &H100
Private Const DT_NOPREFIX = &H800
Private Const DT_PLOTTER = 0 ' Vector plotter
Private Const DT_RASCAMERA = 3 ' Raster camera
Private Const DT_RASDISPLAY = 1 ' Raster display
Private Const DT_RASPRINTER = 2 ' Raster printer
Private Const DT_RIGHT = &H2
Private Const DT_SINGLELINE = &H20
Private Const DT_TABSTOP = &H80
Private Const DT_TOP = &H0
Private Const DT_VCENTER = &H4
Private Const DT_WORDBREAK = &H10
Private Declare Function OleTranslateColor Lib "OLEPRO32.DLL" (ByVal OLE_COLOR As Long, ByVal HPALETTE As Long, pccolorref As Long) As Long
Private Const CLR_INVALID = -1
Private Sub TextEffect( _
ByVal sText As String, _
ByVal lX As Long, ByVal lY As Long, _
Optional ByVal bLoop As Boolean = False, _
Optional ByVal lStartSpacing As Long = 128, _
Optional ByVal lEndSpacing As Long = -1, _
Optional ByVal oColor As OLE_COLOR = vbWindowText _
)
Dim i As Long
Dim x As Long
Dim lLen As Long
Dim lHDC As Long
Dim hBrush As Long
Static tR As RECT
Dim iDir As Long
Dim bNotFirstTime As Boolean
Dim lTime As Long
Dim lIter As Long
Dim bSlowDown As Boolean
Dim lCOlor As Long
Dim bDoIt As Boolean

iDir = -1
i = lStartSpacing
tR.left = lX: tR.tOp = lY: tR.Right = lX: tR.Bottom = lY
OleTranslateColor oColor, 0, lCOlor

hBrush = CreateSolidBrush(GetSysColor(COLOR_BTNFACE))
lLen = Len(sText)
lHDC = Me.hdc
SetTextColor lHDC, lCOlor
bDoIt = True

Do While m_bDoEffect And bDoIt
lTime = timeGetTime
If (i < -3) And Not (bLoop) And Not (bSlowDown) Then
bSlowDown = True
iDir = 1
lIter = (i + 4)
End If
If (i > 128) Then iDir = -1
If Not (bLoop) And iDir = 1 Then
If (i = lEndSpacing) Then
' Stop
bDoIt = False
Else
lIter = lIter - 1
If (lIter <= 0) Then
i = i + iDir
lIter = (i + 4)
End If
End If
Else
i = i + iDir
End If
FillRect lHDC, tR, hBrush
x = 32 - (i * lLen)
SetTextCharacterExtra lHDC, i
DrawText lHDC, sText, lLen, tR, DT_CALCRECT
tR.Right = tR.Right + 4
If (tR.Right > Me.ScaleWidth \ Screen.TwipsPerPixelX) Then tR.Right = Me.ScaleWidth \ Screen.TwipsPerPixelX
DrawText lHDC, sText, lLen, tR, DT_LEFT
Me.Refresh
Do
DoEvents
Loop While (timeGetTime - lTime) < 20
Loop
DeleteObject hBrush

End Sub

Private Sub cmdOK_Click()
Unload Me
End Sub

Private Sub Form_Load()
Me.Show
Me.Refresh
If Not (m_bDoEffect) Then
Me.Cls
Me.Font.Size = 24
m_bDoEffect = True
TextEffect "VİSUAL BASIC TÜRK", 12, 12, , 128, 2, RGB(&H80, 0, 0)
If m_bDoEffect Then
Me.Font.Size = 14
TextEffect "ERDAL KOZAL -> erdalkozal5@hotmail.com", 36, 52, , 128, , vb3DShadow
End If
If m_bDoEffect Then
Me.Font.Name = "Tahoma"
Me.Font.Size = 8
Me.Font.Bold = False
TextEffect "ERDAL KOZAL VİSUAL BASIC TÜRK", 49, 86, , 128, 1
End If
If m_bDoEffect Then
TextEffect "TEŞEKKÜRLER.", 49, 100, , 128, 0
End If
m_bDoEffect = False
Else
m_bDoEffect = False
End If

End Sub

Private Sub Form_QueryUnload(Cancel As Integer, UnloadMode As Integer)
m_bDoEffect = False
End Sub
```

**KODU FORMA KOPYALAYIN VE AUTOREDRAW =TRUE OLSUN**

## **LİSTBOX EKLENTİ**

```vbnet
Option Explicit

Dim gerial As Boolean

Private Sub cmdEkle_Click()
If txtEkleme.Text <> "" Then ' eger txtekleme bos ise ekleme yapmasin
kombo.AddItem txtEkleme.Text
txtEkleme.Text = "" 'eklendikten sonra textbox'u temizle
End If
End Sub

Private Sub Form_Load()
'Burada item'lar ekleniyor
With kombo
.AddItem "cilek"
.AddItem "incir"
.AddItem "elma"
.AddItem "armut"
.AddItem "uzum"
.AddItem "karpuz"
.AddItem "seftali"
End With
End Sub

Private Sub kombo_KeyDown(basim As Integer, Shift As Integer)

If basim = vbKeyBack Or basim = vbKeyDelete Then
If kombo.Text <> "" Then
gerial = True
End If
End If

End Sub

Private Sub kombo_Change()

If gerial = True Or kombo.Text = "" Then
gerial = False
Exit Sub
End If

Dim i As Long
Dim nSel As Long

For i = 0 To kombo.ListCount - 1
If InStr(1, kombo.List(i), kombo.Text, _
vbTextCompare) = 1 Then
nSel = kombo.SelStart
kombo.Text = kombo.List(i)
kombo.SelStart = nSel
kombo.SelLength = Len(kombo.Text) - nSel
Exit For
End If
Next
End Sub
```

## **LİSTE KUTUSU**

```vbnet
List1.AddItem "ERDAL"
List1.AddItem "KOZAL "

form loadda
Private Sub List1_Click()
Label2.Caption = List1.Text
Select Case List1.ListIndex
Case 0
Label1.Caption = "ERDAL KOZAL. "
Case 1
Label1.Caption = "KOZAL ERDAL. "
End Select
```

## ** FORM ORTALAMA**

```vbnet
Private Sub Form_Load()
formadı.Left = (Screen.Width - formadı.Width) / 2
formadı.Top = (Screen.Height - formadı.Height) / 2
```

## **RESİM AÇMAK**

```vbnet
'****************************************************
'Image Displayer Image nesnesini kullanarak resim
'formatlarını açmak için tasarlanmış
'bir programdır.Bu programda aynı zamanda
'Dirlistbox,Drivelistbox,Filelistbox
'nesnelerininde beraber kullanlmasıda
'gösterilmiştir.
'****************************************************
Private Sub dirList_Change()
filList.Path = dirList.Path
Text1.Text = dirList.Path
End Sub

Private Sub drvList_Change()
On Error GoTo hata
dirList.Path = drvList.Drive
Exit Sub
hata:
MsgBox "Lütfen CD veya Disketin cihaz içinde olduğuna emin olun ", vbCritical, "Ulaşım Hatası"
drvList.Drive = dirList.Path
Exit Sub
End Sub

Private Sub filList_Click()
Text1.Text = dirList.Path & "\" & filList.FileName
On Error GoTo hata
Image1.Picture = LoadPicture(Text1.Text)
Exit Sub
hata:
MsgBox "Lütfen Görüntülenebilecek bir öğe seçin", vbInformation, "UYARI"
End Sub

Private Sub Form_Load()
Text1.Text = drvList.Drive
End Sub
```

## **KLASİK SAAT FORMU**

```vbnet
Private Sub Form_Load()
Dim aci, i, t
AutoRedraw = True
Timer1.Interval = 1000 '1 aniye
Timer1.Interval = 10
ScaleMode = 3
For i = 0 To ScaleHeight
Line (0, i)-(ScaleWidth, i), i * 256
Next
ScaleMode = 1
Width = ScaleHeight 'form yüksekligi
Scale (-20, 20)-(20, -20)
t = "ERDAL KOZAL"
CurrentX = -TextWidth(t) / 2
CurrentY = -4
Print t
DrawWidth = 5
Circle (0, 0), 19, 65535
DrawWidth = 2
For aci = 0 To 360 Step 6
Line (18 * Cos(aci * 301415 / 180), 18 * Sin(aci * 3.1415 / 180))-(19 * Cos(aci * 3.1415 / 180), 19 * Sin(aci * 3.1415 / 180)), QBColor(5)
Next
DrawWidth = 4
For aci = 0 To 360 Step 6 * 5
Line (18 * Cos(aci * 3.1415 / 180), 18 * Sin(aci * 3.1415 / 180))-(19 * Cos(aci * 3.1415 / 180), 19 * Sin(aci * 3.1415 / 180)), QBColor(8)
Next
DrawMode = 7
--------
Private Sub Timer1_Timer()
Dim aci, saniye, dakika, saat, i
Static sx, sy, dx, dy, stx, sty
Caption = Time
DrawWidth = 2
Line (0, 0)-(sx, sy), QBColor(10)
saniye = Second(Time)
aci = -saniye * 6 + 90
sx = 18 * Cos(aci * 3.1415 / 180)
sy = 18 * Sin(aci * 3.1415 / 180)
Line (0, 0)-(sx, sy), QBColor(10)
DrawWidth = 3
Line (0, 0)-(dx, dy), QBColor(11)
dakika = Minute(Time)
aci = -dakika * 6 + 90
dx = 18 * Cos(aci * 3.1415 / 180)
dy = 18 * Sin(aci * 3.1415 / 180)
Line (0, 0)-(dx, dy), QBColor(11)
DrawWidth = 3
Line (0, 0)-(stx, sty), QBColor(12)
saat = Hour(Time)
aci = -saat * 30 + 90
stx = 12 * Cos(aci * 3.1415 / 180)
sty = 12 * Sin(aci * 3.1415 / 180)
Line (0, 0)-(stx, sty), QBColor(12)
If Minute(Time) = 0 Then Beep
--------
Private Sub Timer2_Timer()
Static sls
sls = (sls + 1) Mod 360
Dim aci
Dim sx, sy, dx, dy, stx, sty
DrawWidth = 1
aci = -sls * 3.6 + 90
sx = 3 * Cos(aci * 3.1415 / 180)
sy = 3 * Sin(aci * 3.1415 / 180)
Line (5, 5)-(5 + sx, 5 + sy), QBColor(10)
Line (-5, 5)-(-5 - sx, 5 - sy), QBColor(10)
```

## **FORMA ŞİFRE**

```vbnet
Private Sub Form_Load()
If InputBox("şifreyi giriniz") <> "erdal" Then
MsgBox ("şifreyi bilemediniz.bilgiler üzerinde degişiklik yapamazsınız.")
Text1.Locked = True
End If
End Sub
```

---
*Kaynak: `BAZI İÇERİK KODLARI/KODLAR/Kodlar1.doc` — mine — 2002*
