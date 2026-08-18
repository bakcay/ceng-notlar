<% @LANGUAGE=VBscript %>
<%
Option Explicit
Response.Expires = 0 
Dim strAdi, strSoyadi, strBilgi
If Request.ServerVariables("CONTENT_LENGTH") <> 0 Then
	strAdi = Trim(Request.Form("adi"))
	strSoyadi = Trim(Request.Form("soyadi"))
	strBilgi = Trim(Request.Form("mesaj"))
	strBilgi = Replace(strBilgi, vbcrlf, "<BR>" & vbcrlf)
%>
<html>
<head>
<title>Mini Form (Post)</title>
<meta http-equiv="content-type" content="text/html; charset=ISO-8859-9">
<meta http-equiv="Content-Type" content="text/html; charset=windows-1254">
</head>
<body>
Script'imize Form'dan bilgi ulaştı <BR><BR>
Gelen bilgiler:<BR>
Formu dolduran kişinin adı: <%= strAdi%> <BR><BR>
Formu dolduran kişinin Soyadı: <%= strSoyadi%> <BR><BR>
Mesaj: <%= strBilgi%> <BR><BR>
</body>
</html>
<%
Else
%>
<html>
<body>
Bize bilgi verir misiniz?<BR>
<FORM ACTION= "<%= Request.ServerVariables("SCRIPT_NAME") %>" METHOD="POST">
Adınız: <INPUT TYPE="Text" NAME="adi"><BR>
Soyadınız: <INPUT TYPE="Text" NAME="soyadi"><BR>
Mesajınız: <TEXTAREA NAME="mesaj">Mesajınızı buraya yazın!</TEXTAREA><BR>
<INPUT TYPE="Submit" NAME="Gönder" VALUE="Gönder">
</FORM>
</body>
</html>
<% End If %>
