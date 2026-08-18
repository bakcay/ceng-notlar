<% @LANGUAGE=VBscript %>
<%
Option Explicit
Response.Expires = 0 
Dim serverTarih, kalanGun
serverTarih = Date
' aşağıdaki satırda işaretler arasındaki yere kendi doğum gününüzün tarihini yazın
kalanGun = DateDiff("d",Date,#5/7/2000#)
%>
<html>
<head>
<title>Dogum Günü Hesabı!</title>
<meta http-equiv="content-type" content="text/html; charset=ISO-8859-9">
<meta http-equiv="Content-Type" content="text/html; charset=windows-1254">
</head>

<body>
<h3>
<center>
<p>Selam:</p>
<p>Şu anda tarih: <%=serverTarih%></p>
<%
If kalanGun > 0 Then
	Response.Write "Doğum gününüze " & kalanGun & " gün var." & VbCrLf
ElseIf kalanGun < 0 Then
	Response.Write "Doğum gününüz " & kalanGun & " geçmiş buluyor." & VbCrLf
Else
	Response.Write "<b>Doğum gününüz kutlu olsun!</b>" & VbCrLf
End If
%>
</center>
</h3>
</body>
</html>

