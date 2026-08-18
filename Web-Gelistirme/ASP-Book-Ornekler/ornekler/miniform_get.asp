<% @LANGUAGE=VBscript %>
<%
Option Explicit
Response.Expires = 0 
Dim strAdi, strSoyadi, hamBilgi, islenmisBilgi
If Request.ServerVariables("QUERY_STRING") <> "" Then
	strAdi = Trim(Request.QueryString("adi"))
	strSoyadi = Trim(Request.QueryString("soyadi"))
	hamBilgi = Trim(Request.QueryString("mesaj"))
	islenmisBilgi = Replace(hamBilgi, vbcrlf, "<BR>" & vbcrlf)
%>
<html>
<head>
<title>Mini Form (Get)</title>
<meta http-equiv="content-type" content="text/html; charset=ISO-8859-9">
<meta http-equiv="Content-Type" content="text/html; charset=windows-1254">
</head>
<body>
Script'imize Form'dan bilgi ulaştı <BR><BR>
Gelen bilgiler:<BR>
Formu dolduran kişinin adı: <%= strAdi%> <BR><BR>
Formu dolduran kişinin Soyadı: <%= strSoyadi%> <BR><BR>
Ham Bilgiler: <%= hamBilgi%> <BR><BR>
İşlenmiş Bilgiler: <%= islenmisBilgi%> <BR><BR>
"Query_String" olarak gelen bilgi:  <BR>
<%= Request.ServerVariables("QUERY_STRING")%>
</body>
</html>
<%
Else
%>
<html>
<body>
Bize bilgi verir misiniz?<BR>
<FORM ACTION= "<%= Request.ServerVariables("SCRIPT_NAME") %>" METHOD="GET">
Adınız: <INPUT TYPE="Text" NAME="adi"><BR>
Soyadınız: <INPUT TYPE="Text" NAME="soyadi"><BR>
Mesajınız: <TEXTAREA NAME="mesaj">Mesajınızı buraya yazın!</TEXTAREA><BR>
<INPUT TYPE="Submit" NAME="Gönder" VALUE="Gönder">
</FORM>
</body>
</html>
<% End If %>
