# Bazi İçerik Kodlari

**Merhabalar.Projeler sayfamızda 1. projemizin kodları aşagıdaki gibidir.******

**Aynen kes yapıştır tekniğiyle yeni yarattığınız projeye kopyalayın.******

**Gerekli butonları yerlerine yerleştirdikten sonra yazılımınız hazırdır.******

**(Amaç test kitapcığı hazırlayabileceğiniz bir proje oluşturmak)******

**>****command3D2 ****<****command3D1 ****Tamam****command1 ****Cıkış****command3******

**label1****=label3 ****label1****=label1 ****label2****=label2 ****label2****=label5******

**-----------------------------------------------------------------------------------------------------------------------------------------------------------******

```vbnet
Dim Sonuc, yanlis, kalan, answer1, answer2
Dim cevap(1 To 14)
Dim secenek(1 To 14, 1 To 14)
Dim soru_no
Dim user_cevap(0 To 14)
Dim cevap_index

Sub Command1_Click()
If user_cevap(soru_no - 1) = "" Then
If cevap_index = "" Then cevap_index = 0
Select Case cevap_index
Case 0: answer2 = "A"
Case 1: answer2 = "B"
Case 2: answer2 = "C"
Case 3: answer2 = "D"
End Select

user_cevap(soru_no - 1) = answer2

If user_cevap(soru_no - 1) = cevap(soru_no) Then
Sonuc = Sonuc + 1
Label1.Caption = "Dogru Adet= " + Str(Sonuc)
Else
yanlis = yanlis + 1
Label2.Caption = "Yanlis Adet= " + Str(yanlis)
End If
kalan = (14 - Sonuc - yanlis)
Label5.Caption = "Kalan Soru=" + Str(kalan)
Else
Select Case user_cevap(soru_no - 1)
Case "A": answer1 = 0
Case "B": answer1 = 1
Case "C": answer1 = 2
Case "D": answer1 = 3
Case Else: answer1 = 0
End Select
Option1(answer1).Value = True
End If
End Sub

Sub Command3_Click()
End
End Sub

Sub Command3D1_Click()
soru_no = soru_no - 1
Label3.Caption = "Soru Nosu= " + Str(soru_no)
Select Case soru_no
Case 1
Command3d1.Enabled = False
Command3d2.Enabled = True
Label4(0).Visible = True
Label4(1).Visible = False
Label4(2).Visible = False
Label4(3).Visible = False
Label4(4).Visible = False
Label4(5).Visible = False
Label4(6).Visible = False
Label4(7).Visible = False
Label4(8).Visible = False
Label4(9).Visible = False
Label4(10).Visible = False
Label4(11).Visible = False
Label4(12).Visible = False
Label4(13).Visible = False
Option1(0).Caption = secenek(soru_no, 1)
Option1(1).Caption = secenek(soru_no, 2)
Option1(2).Caption = secenek(soru_no, 3)
Option1(3).Caption = secenek(soru_no, 4)
Case 2
Label4(0).Visible = False
Label4(1).Visible = True
Label4(2).Visible = False
Label4(3).Visible = False
Label4(4).Visible = False
Label4(5).Visible = False
Label4(6).Visible = False
Label4(7).Visible = False
Label4(8).Visible = False
Label4(9).Visible = False
Label4(10).Visible = False
Label4(11).Visible = False
Label4(12).Visible = False
Label4(13).Visible = False
Option1(0).Caption = secenek(soru_no, 1)
Option1(1).Caption = secenek(soru_no, 2)
Option1(2).Caption = secenek(soru_no, 3)
Option1(3).Caption = secenek(soru_no, 4)
Command3d1.Enabled = True
Command3d2.Enabled = True

Case 3
Label4(0).Visible = False
Label4(1).Visible = False
Label4(2).Visible = True
Label4(3).Visible = False
Label4(4).Visible = False
Label4(5).Visible = False
Label4(6).Visible = False
Label4(7).Visible = False
Label4(8).Visible = False
Label4(9).Visible = False
Label4(10).Visible = False
Label4(11).Visible = False
Label4(12).Visible = False
Label4(13).Visible = False
Option1(0).Caption = secenek(soru_no, 1)
Option1(1).Caption = secenek(soru_no, 2)
Option1(2).Caption = secenek(soru_no, 3)
Option1(3).Caption = secenek(soru_no, 4)
Command3d1.Enabled = True
Command3d2.Enabled = True

Case 4
Label4(0).Visible = False
Label4(1).Visible = False
Label4(2).Visible = False
Label4(3).Visible = True
Label4(4).Visible = False
Label4(5).Visible = False
Label4(6).Visible = False
Label4(7).Visible = False
Label4(8).Visible = False
Label4(9).Visible = False
Label4(10).Visible = False
Label4(11).Visible = False
Label4(12).Visible = False
Label4(13).Visible = False
Option1(0).Caption = secenek(soru_no, 1)
Option1(1).Caption = secenek(soru_no, 2)
Option1(2).Caption = secenek(soru_no, 3)
Option1(3).Caption = secenek(soru_no, 4)
Command3d1.Enabled = True
Command3d2.Enabled = True

Case 5
Label4(0).Visible = False
Label4(1).Visible = False
Label4(2).Visible = False
Label4(3).Visible = False
Label4(4).Visible = True
Label4(5).Visible = False
Label4(6).Visible = False
Label4(7).Visible = False
Label4(8).Visible = False
Label4(9).Visible = False
Label4(10).Visible = False
Label4(11).Visible = False
Label4(12).Visible = False
Label4(13).Visible = False
Option1(0).Caption = secenek(soru_no, 1)
Option1(1).Caption = secenek(soru_no, 2)
Option1(2).Caption = secenek(soru_no, 3)
Option1(3).Caption = secenek(soru_no, 4)

Command3d1.Enabled = True
Command3d2.Enabled = True

Case 6
Label4(0).Visible = False
Label4(1).Visible = False
Label4(2).Visible = False
Label4(3).Visible = False
Label4(4).Visible = False
Label4(5).Visible = True
Label4(6).Visible = False
Label4(7).Visible = False
Label4(8).Visible = False
Label4(9).Visible = False
Label4(10).Visible = False
Label4(11).Visible = False
Label4(12).Visible = False
Label4(13).Visible = False
Option1(0).Caption = secenek(soru_no, 1)
Option1(1).Caption = secenek(soru_no, 2)
Option1(2).Caption = secenek(soru_no, 3)
Option1(3).Caption = secenek(soru_no, 4)

Command3d1.Enabled = True
Command3d2.Enabled = True

Case 7
Label4(0).Visible = False
Label4(1).Visible = False
Label4(2).Visible = False
Label4(3).Visible = False
Label4(4).Visible = False
Label4(5).Visible = False
Label4(6).Visible = True
Label4(7).Visible = False
Label4(8).Visible = False
Label4(9).Visible = False
Label4(10).Visible = False
Label4(11).Visible = False
Label4(12).Visible = False
Label4(13).Visible = False
Option1(0).Caption = secenek(soru_no, 1)
Option1(1).Caption = secenek(soru_no, 2)
Option1(2).Caption = secenek(soru_no, 3)
Option1(3).Caption = secenek(soru_no, 4)

Command3d1.Enabled = True
Command3d2.Enabled = True

Case 8
Label4(0).Visible = False
Label4(1).Visible = False
Label4(2).Visible = False
Label4(3).Visible = False
Label4(4).Visible = False
Label4(5).Visible = False
Label4(6).Visible = False
Label4(7).Visible = True
Label4(8).Visible = False
Label4(9).Visible = False
Label4(10).Visible = False
Label4(11).Visible = False
Label4(12).Visible = False
Label4(13).Visible = False
Option1(0).Caption = secenek(soru_no, 1)
Option1(1).Caption = secenek(soru_no, 2)
Option1(2).Caption = secenek(soru_no, 3)
Option1(3).Caption = secenek(soru_no, 4)

Command3d1.Enabled = True
Command3d2.Enabled = False

Case 9
Label4(0).Visible = False
Label4(1).Visible = False
Label4(2).Visible = False
Label4(3).Visible = False
Label4(4).Visible = False
Label4(5).Visible = False
Label4(6).Visible = False
Label4(7).Visible = False
Label4(8).Visible = True
Label4(9).Visible = False
Label4(10).Visible = False
Label4(11).Visible = False
Label4(12).Visible = False
Label4(13).Visible = False
Option1(0).Caption = secenek(soru_no, 1)
Option1(1).Caption = secenek(soru_no, 2)
Option1(2).Caption = secenek(soru_no, 3)
Option1(3).Caption = secenek(soru_no, 4)

Command3d1.Enabled = True
Command3d2.Enabled = True

Case 10
Label4(0).Visible = False
Label4(1).Visible = False
Label4(2).Visible = False
Label4(3).Visible = False
Label4(4).Visible = False
Label4(5).Visible = False
Label4(6).Visible = False
Label4(7).Visible = False
Label4(8).Visible = False
Label4(9).Visible = True
Label4(10).Visible = False
Label4(11).Visible = False
Label4(12).Visible = False
Label4(13).Visible = False
Option1(0).Caption = secenek(soru_no, 1)
Option1(1).Caption = secenek(soru_no, 2)
Option1(2).Caption = secenek(soru_no, 3)
Option1(3).Caption = secenek(soru_no, 4)

Command3d1.Enabled = True
Command3d2.Enabled = True

Case 11
Label4(0).Visible = False
Label4(1).Visible = False
Label4(2).Visible = False
Label4(3).Visible = False
Label4(4).Visible = False
Label4(5).Visible = False
Label4(6).Visible = False
Label4(7).Visible = False
Label4(8).Visible = False
Label4(9).Visible = False
Label4(10).Visible = True
Label4(11).Visible = False
Label4(12).Visible = False
Label4(13).Visible = False
Option1(0).Caption = secenek(soru_no, 1)
Option1(1).Caption = secenek(soru_no, 2)
Option1(2).Caption = secenek(soru_no, 3)
Option1(3).Caption = secenek(soru_no, 4)

Command3d1.Enabled = True
Command3d2.Enabled = True

Case 12
Label4(0).Visible = False
Label4(1).Visible = False
Label4(2).Visible = False
Label4(3).Visible = False
Label4(4).Visible = False
Label4(5).Visible = False
Label4(6).Visible = False
Label4(7).Visible = False
Label4(8).Visible = False
Label4(9).Visible = False
Label4(10).Visible = False
Label4(11).Visible = True
Label4(12).Visible = False
Label4(13).Visible = False
Option1(0).Caption = secenek(soru_no, 1)
Option1(1).Caption = secenek(soru_no, 2)
Option1(2).Caption = secenek(soru_no, 3)
Option1(3).Caption = secenek(soru_no, 4)

Command3d1.Enabled = True
Command3d2.Enabled = True

Case 13
Label4(0).Visible = False
Label4(1).Visible = False
Label4(2).Visible = False
Label4(3).Visible = False
Label4(4).Visible = False
Label4(5).Visible = False
Label4(6).Visible = False
Label4(7).Visible = False
Label4(8).Visible = False
Label4(9).Visible = False
Label4(10).Visible = False
Label4(11).Visible = False
Label4(12).Visible = True
Label4(13).Visible = False
Option1(0).Caption = secenek(soru_no, 1)
Option1(1).Caption = secenek(soru_no, 2)
Option1(2).Caption = secenek(soru_no, 3)
Option1(3).Caption = secenek(soru_no, 4)

Command3d1.Enabled = True
Command3d2.Enabled = True

Case 14
Label4(0).Visible = False
Label4(1).Visible = False
Label4(2).Visible = False
Label4(3).Visible = False
Label4(4).Visible = False
Label4(5).Visible = False
Label4(6).Visible = False
Label4(7).Visible = False
Label4(8).Visible = False
Label4(9).Visible = False
Label4(10).Visible = False
Label4(11).Visible = False
Label4(12).Visible = False
Label4(13).Visible = True
Option1(0).Caption = secenek(soru_no, 1)
Option1(1).Caption = secenek(soru_no, 2)
Option1(2).Caption = secenek(soru_no, 3)
Option1(3).Caption = secenek(soru_no, 4)

Command3d1.Enabled = True
Command3d2.Enabled = False
Case Else: soru_no = 1
End Select

cevap_index = user_cevap(soru_no - 1)
Select Case cevap_index
Case "A": cevap_index = 0
Option1(cevap_index).Value = False
Case "B": cevap_index = 1
Option1(cevap_index).Value = False
Case "C": cevap_index = 2
Option1(cevap_index).Value = False
Case "D": cevap_index = 3
Option1(cevap_index).Value = False
Case Else:
Option1(0).Value = False
Option1(1).Value = False
Option1(2).Value = False
Option1(3).Value = False

End Select
End Sub

Sub Command3D2_Click()
soru_no = soru_no + 1
Label3.Caption = "Soru Nosu= " + Str(soru_no)
Select Case soru_no
Case 1
Command3d1.Enabled = False
Command3d2.Enabled = True
Label4(0).Visible = True
Label4(1).Visible = False
Label4(2).Visible = False
Label4(3).Visible = False
Label4(4).Visible = False
Label4(5).Visible = False
Label4(6).Visible = False
Label4(7).Visible = False
Label4(8).Visible = False
Label4(9).Visible = False
Label4(10).Visible = False
Label4(11).Visible = False
Label4(12).Visible = False
Label4(13).Visible = False
Option1(0).Caption = secenek(soru_no, 1)
Option1(1).Caption = secenek(soru_no, 2)
Option1(2).Caption = secenek(soru_no, 3)
Option1(3).Caption = secenek(soru_no, 4)
Case 2
Label4(0).Visible = False
Label4(1).Visible = True
Label4(2).Visible = False
Label4(3).Visible = False
Label4(4).Visible = False
Label4(5).Visible = False
Label4(6).Visible = False
Label4(7).Visible = False
Label4(8).Visible = False
Label4(9).Visible = False
Label4(10).Visible = False
Label4(11).Visible = False
Label4(12).Visible = False
Label4(13).Visible = False
Option1(0).Caption = secenek(soru_no, 1)
Option1(1).Caption = secenek(soru_no, 2)
Option1(2).Caption = secenek(soru_no, 3)
Option1(3).Caption = secenek(soru_no, 4)
Command3d1.Enabled = True
Command3d2.Enabled = True

Case 3
Label4(0).Visible = False
Label4(1).Visible = False
Label4(2).Visible = True
Label4(3).Visible = False
Label4(4).Visible = False
Label4(5).Visible = False
Label4(6).Visible = False
Label4(7).Visible = False
Label4(8).Visible = False
Label4(9).Visible = False
Label4(10).Visible = False
Label4(11).Visible = False
Label4(12).Visible = False
Label4(13).Visible = False
Option1(0).Caption = secenek(soru_no, 1)
Option1(1).Caption = secenek(soru_no, 2)
Option1(2).Caption = secenek(soru_no, 3)
Option1(3).Caption = secenek(soru_no, 4)
Command3d1.Enabled = True
Command3d2.Enabled = True

Case 4
Label4(0).Visible = False
Label4(1).Visible = False
Label4(2).Visible = False
Label4(3).Visible = True
Label4(4).Visible = False
Label4(5).Visible = False
Label4(6).Visible = False
Label4(7).Visible = False
Label4(8).Visible = False
Label4(9).Visible = False
Label4(10).Visible = False
Label4(11).Visible = False
Label4(12).Visible = False
Label4(13).Visible = False
Option1(0).Caption = secenek(soru_no, 1)
Option1(1).Caption = secenek(soru_no, 2)
Option1(2).Caption = secenek(soru_no, 3)
Option1(3).Caption = secenek(soru_no, 4)
Command3d1.Enabled = True
Command3d2.Enabled = True

Case 5
Label4(0).Visible = False
Label4(1).Visible = False
Label4(2).Visible = False
Label4(3).Visible = False
Label4(4).Visible = True
Label4(5).Visible = False
Label4(6).Visible = False
Label4(7).Visible = False
Label4(8).Visible = False
Label4(9).Visible = False
Label4(10).Visible = False
Label4(11).Visible = False
Label4(12).Visible = False
Label4(13).Visible = False
Option1(0).Caption = secenek(soru_no, 1)
Option1(1).Caption = secenek(soru_no, 2)
Option1(2).Caption = secenek(soru_no, 3)
Option1(3).Caption = secenek(soru_no, 4)
Command3d1.Enabled = True
Command3d2.Enabled = True

Case 6
Label4(0).Visible = False
Label4(1).Visible = False
Label4(2).Visible = False
Label4(3).Visible = False
Label4(4).Visible = False
Label4(5).Visible = True
Label4(6).Visible = False
Label4(7).Visible = False
Label4(8).Visible = False
Label4(9).Visible = False
Label4(10).Visible = False
Label4(11).Visible = False
Label4(12).Visible = False
Label4(13).Visible = False
Option1(0).Caption = secenek(soru_no, 1)
Option1(1).Caption = secenek(soru_no, 2)
Option1(2).Caption = secenek(soru_no, 3)
Option1(3).Caption = secenek(soru_no, 4)
Command3d1.Enabled = True
Command3d2.Enabled = True

Case 7
Label4(0).Visible = False
Label4(1).Visible = False
Label4(2).Visible = False
Label4(3).Visible = False
Label4(4).Visible = False
Label4(5).Visible = False
Label4(6).Visible = True
Label4(7).Visible = False
Label4(8).Visible = False
Label4(9).Visible = False
Label4(10).Visible = False
Label4(11).Visible = False
Label4(12).Visible = False
Label4(13).Visible = False
Option1(0).Caption = secenek(soru_no, 1)
Option1(1).Caption = secenek(soru_no, 2)
Option1(2).Caption = secenek(soru_no, 3)
Option1(3).Caption = secenek(soru_no, 4)
Command3d1.Enabled = True
Command3d2.Enabled = True

Case 8
Label4(0).Visible = False
Label4(1).Visible = False
Label4(2).Visible = False
Label4(3).Visible = False
Label4(4).Visible = False
Label4(5).Visible = False
Label4(6).Visible = False
Label4(7).Visible = True
Label4(8).Visible = False
Label4(9).Visible = False
Label4(10).Visible = False
Label4(11).Visible = False
Label4(12).Visible = False
Label4(13).Visible = False
Option1(0).Caption = secenek(soru_no, 1)
Option1(1).Caption = secenek(soru_no, 2)
Option1(2).Caption = secenek(soru_no, 3)
Option1(3).Caption = secenek(soru_no, 4)
Command3d1.Enabled = True
Command3d2.Enabled = True

Case 9
Label4(0).Visible = False
Label4(1).Visible = False
Label4(2).Visible = False
Label4(3).Visible = False
Label4(4).Visible = False
Label4(5).Visible = False
Label4(6).Visible = False
Label4(7).Visible = False
Label4(8).Visible = True
Label4(9).Visible = False
Label4(10).Visible = False
Label4(11).Visible = False
Label4(12).Visible = False
Label4(13).Visible = False
Option1(0).Caption = secenek(soru_no, 1)
Option1(1).Caption = secenek(soru_no, 2)
Option1(2).Caption = secenek(soru_no, 3)
Option1(3).Caption = secenek(soru_no, 4)
Command3d1.Enabled = True
Command3d2.Enabled = True

Case 10
Label4(0).Visible = False
Label4(1).Visible = False
Label4(2).Visible = False
Label4(3).Visible = False
Label4(4).Visible = False
Label4(5).Visible = False
Label4(6).Visible = False
Label4(7).Visible = False
Label4(8).Visible = False
Label4(9).Visible = True
Label4(10).Visible = False
Label4(11).Visible = False
Label4(12).Visible = False
Label4(13).Visible = False
Option1(0).Caption = secenek(soru_no, 1)
Option1(1).Caption = secenek(soru_no, 2)
Option1(2).Caption = secenek(soru_no, 3)
Option1(3).Caption = secenek(soru_no, 4)
Command3d1.Enabled = True
Command3d2.Enabled = True

Case 11
Label4(0).Visible = False
Label4(1).Visible = False
Label4(2).Visible = False
Label4(3).Visible = False
Label4(4).Visible = False
Label4(5).Visible = False
Label4(6).Visible = False
Label4(7).Visible = False
Label4(8).Visible = False
Label4(9).Visible = False
Label4(10).Visible = True
Label4(11).Visible = False
Label4(12).Visible = False
Label4(13).Visible = False
Option1(0).Caption = secenek(soru_no, 1)
Option1(1).Caption = secenek(soru_no, 2)
Option1(2).Caption = secenek(soru_no, 3)
Option1(3).Caption = secenek(soru_no, 4)
Command3d1.Enabled = True
Command3d2.Enabled = True

Case 12
Label4(0).Visible = False
Label4(1).Visible = False
Label4(2).Visible = False
Label4(3).Visible = False
Label4(4).Visible = False
Label4(5).Visible = False
Label4(6).Visible = False
Label4(7).Visible = False
Label4(8).Visible = False
Label4(9).Visible = False
Label4(10).Visible = False
Label4(11).Visible = True
Label4(12).Visible = False
Label4(13).Visible = False
Option1(0).Caption = secenek(soru_no, 1)
Option1(1).Caption = secenek(soru_no, 2)
Option1(2).Caption = secenek(soru_no, 3)
Option1(3).Caption = secenek(soru_no, 4)
Command3d1.Enabled = True
Command3d2.Enabled = True

Case 13
Label4(0).Visible = False
Label4(1).Visible = False
Label4(2).Visible = False
Label4(3).Visible = False
Label4(4).Visible = False
Label4(5).Visible = False
Label4(6).Visible = False
Label4(7).Visible = False
Label4(8).Visible = False
Label4(9).Visible = False
Label4(10).Visible = False
Label4(11).Visible = False
Label4(12).Visible = True
Label4(13).Visible = False
Option1(0).Caption = secenek(soru_no, 1)
Option1(1).Caption = secenek(soru_no, 2)
Option1(2).Caption = secenek(soru_no, 3)
Option1(3).Caption = secenek(soru_no, 4)
Command3d1.Enabled = True
Command3d2.Enabled = True

Case 14
Label4(0).Visible = False
Label4(1).Visible = False
Label4(2).Visible = False
Label4(3).Visible = False
Label4(4).Visible = False
Label4(5).Visible = False
Label4(6).Visible = False
Label4(7).Visible = False
Label4(8).Visible = False
Label4(9).Visible = False
Label4(10).Visible = False
Label4(11).Visible = False
Label4(12).Visible = False
Label4(13).Visible = True
Option1(0).Caption = secenek(soru_no, 1)
Option1(1).Caption = secenek(soru_no, 2)
Option1(2).Caption = secenek(soru_no, 3)
Option1(3).Caption = secenek(soru_no, 4)
Command3d1.Enabled = True
Command3d2.Enabled = False

Command3d2.Enabled = False
Case Else: soru_no = 14
End Select
cevap_index = user_cevap(soru_no - 1)
Select Case cevap_index
Case "A": cevap_index = 0
Option1(cevap_index).Value = False
Case "B": cevap_index = 1
Option1(cevap_index).Value = False
Case "C": cevap_index = 2
Option1(cevap_index).Value = False
Case "D": cevap_index = 3
Option1(cevap_index).Value = False
Case Else:
Option1(0).Value = False
Option1(1).Value = False
Option1(2).Value = False
Option1(3).Value = False

End Select
End Sub

Sub Form_Load()
Label1.Caption = "Dogru Adet= 0"
Label2.Caption = "Yanlis Adet= 0"
Label3.Caption = "Soru Nosu= 1"
Label5.Caption = "Kalan Soru= 14"
Label4(0).Visible = True
Label4(1).Visible = False
Label4(2).Visible = False
Label4(3).Visible = False
Label4(4).Visible = False
Label4(5).Visible = False
Label4(6).Visible = False
Label4(7).Visible = False
Label4(8).Visible = False
Label4(9).Visible = False
Label4(10).Visible = False
Label4(11).Visible = False
Label4(12).Visible = False
Label4(13).Visible = False
Command3d1.Enabled = False
secenek(1, 1) = "Ankara"
secenek(1, 2) = "Istanbul"
secenek(1, 3) = "Van"
secenek(1, 4) = "Manisa"

secenek(2, 1) = "Türkiye"
secenek(2, 2) = "Balikesir"
secenek(2, 3) = "Van"
secenek(2, 4) = "Ankara"

secenek(3, 1) = "Bursa"
secenek(3, 2) = "Ankara"
secenek(3, 3) = "Van"
secenek(3, 4) = "Manisa"

secenek(4, 1) = "Bursa"
secenek(4, 2) = "Ankara"
secenek(4, 3) = "Van"
secenek(4, 4) = "Manisa"

secenek(5, 1) = "Marmara"
secenek(5, 2) = "Ic Anadolu"
secenek(5, 3) = "Akdeniz"
secenek(5, 4) = "Karadeniz"

secenek(6, 1) = "ERDAL"
secenek(6, 2) = "Ic Anadolu"
secenek(6, 3) = "Akdeniz"
secenek(6, 4) = "Karadeniz"

secenek(7, 1) = "CANAN"
secenek(7, 2) = "Ic Anadolu"
secenek(7, 3) = "Akdeniz"
secenek(7, 4) = "Karadeniz"

secenek(8, 1) = "DİLARA"
secenek(8, 2) = "Ic Anadolu"
secenek(8, 3) = "Akdeniz"
secenek(8, 4) = "Karadeniz"

secenek(9, 1) = "DOKUZ"
secenek(9, 2) = "Ic Anadolu"
secenek(9, 3) = "Akdeniz"
secenek(9, 4) = "Karadeniz"

secenek(10, 1) = "ON"
secenek(10, 2) = "Ic Anadolu"
secenek(10, 3) = "Akdeniz"
secenek(10, 4) = "Karadeniz"

secenek(11, 1) = "ONBİR"
secenek(11, 2) = "Ic Anadolu"
secenek(11, 3) = "Akdeniz"
secenek(11, 4) = "Karadeniz"

secenek(12, 1) = "ONİKİ"
secenek(12, 2) = "Ic Anadolu"
secenek(12, 3) = "Akdeniz"
secenek(12, 4) = "Karadeniz"

secenek(13, 1) = "ONÜÇ"
secenek(13, 2) = "Ic Anadolu"
secenek(13, 3) = "Akdeniz"
secenek(13, 4) = "Karadeniz"

secenek(14, 1) = "ONDÖRT"
secenek(14, 2) = "Ic Anadolu"
secenek(14, 3) = "Akdeniz"
secenek(14, 4) = "Karadeniz"

Option1(0).Caption = secenek(1, 1)
Option1(1).Caption = secenek(1, 2)
Option1(2).Caption = secenek(1, 3)
Option1(3).Caption = secenek(1, 4)

cevap(1) = "A"
cevap(2) = "B"
cevap(3) = "C"
cevap(4) = "D"
cevap(5) = "A"
cevap(6) = "B"
cevap(7) = "C"
cevap(8) = "D"
cevap(9) = "A"
cevap(10) = "B"
cevap(11) = "C"
cevap(12) = "D"
cevap(13) = "A"
cevap(14) = "B"
soru_no = 1
user_cevap(1) = ""
user_cevap(2) = ""
user_cevap(3) = ""
user_cevap(4) = ""
user_cevap(0) = ""

End Sub

Sub Option1_Click(Index As Integer)
cevap_index = Index
End Sub
```

---
*Kaynak: `BAZI İÇERİK KODLARI/KODLAR/Kodlar3.doc` — mine — 2002*
