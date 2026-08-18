<%@ Language = VBscript %>
<%
'Değiskenleri tanımlayalım.
Dim siteNO
Dim grafNO
Dim SQLSITEADI
Dim connsiteadi
Dim siteadi

' Querystring ile formdan gelen değişkenleri alalım.
siteNO=Request.Querystring("siteNO")
grafNO=Request.Querystring("grafNO")

'Kullanmak istedigimiz site türünü 
'birincil endeksi kullanarak alalim.

SQLSITEADI="SELECT siteAdi FROM Siteler "
SQLSITEADI=SQLSITEADI & "WHERE siteNO= " & siteNO

set connsiteadi = server.createobject("ADODB.Connection")
connsiteadi.open "web"
set siteadi=connsiteadi.execute(SQLSITEADI)
%>
<HTML>
<HEAD>
<TITLE>Web Sitesi Üretim Merkezi</TITLE>
<META http-equiv="content-type" content="text/html; charset=ISO-8859-9">
<META http-equiv="Content-Type" content="text/html; charset=windows-1254">
</HEAD>

<BODY bgcolor=DarkOrange text="white"><br><br><br><br><br><center>
<table width="250"><tr><td>
<font face="arial" size="6">Arzu ettiğiniz <%= siteadi(0) %> sitesini tasarlamaya hazırız.
<p>Bu sitenin kullanım amacı hakkında bilgi verir misiniz?</font>
<form action="icra.asp" method="get">
<input type="Hidden" name="siteNO" value="<%= siteNO %>">
<input type="Hidden" name="grafNO" value="<%= grafNO %>">
<% 'Bu bilgilerle Tür tablosundan bilgi seç. %>
<!--#include file="turler.inc"--> &nbsp;
<input type="Submit" value="Gönder" align="LEFT">
</form></td></tr></table></center>
</BODY>
</HTML>