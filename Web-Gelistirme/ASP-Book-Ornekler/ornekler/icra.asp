<%@ Language = VBscript %>
<%
'degiskenleri deklare edelim
Dim siteNO
Dim grafNO
Dim turNO
Dim randNO

Dim SQLSITETUTAR
Dim SQLGRAFTUTAR
Dim SQLTURTUTAR

Dim bedel
Dim turkatsayi
Dim grafkatsayi
Dim sitekatsayi

'querystring yoluyla degiskenleri alalim
siteNO=Request.Querystring("siteNO")
grafNO=Request.Querystring("grafNO")
turNO=Request.Querystring("turNO")
randNO=Request.Querystring("randNO")

'Bu müsterinin siteAdi ile siteNO degiskenlerini
'Site ölçüsü tablosu ile birlestirecegiz
 
SQLSITETUTAR="SELECT siteAdi, olcRayic FROM Siteler, Olcu "
SQLSITETUTAR=SQLSITETUTAR & "WHERE Siteler.olcNO = Olcu.olcNO and siteNO=" & siteNO

set conn = server.createobject("ADODB.Connection")
conn.open "web"
set sitetutar=conn.execute(SQLSITETUTAR)
siteadi=sitetutar(0)
sitekatsayi=sitetutar(1)

'Grafikin fiyata etkisi
SQLGRAFTUTAR="SELECT grafRayic, grafDurum FROM Grafik "
SQLGRAFTUTAR=SQLGRAFTUTAR & "WHERE grafNO=" & grafNO

set graftutar=conn.execute(SQLGRAFTUTAR)
grafkatsayi=graftutar(0)
grafdurum=graftutar(1)

'Türün fiyata etkisi
SQLTURTUTAR="SELECT turRayic, turAdi FROM Tur "
SQLTURTUTAR=SQLTURTUTAR & "WHERE turNO=" & turNO

set turtutar=conn.execute(SQLTURTUTAR)
turkatsayi=turtutar(0)
turadi=turtutar(1)
conn.close
SET conn = Nothing
bedel = 100 * turkatsayi * grafkatsayi * sitekatsayi
%>

<HTML>
<HEAD>
<TITLE>Web Tasarim Merkezi</TITLE>
<META http-equiv="content-type" content="text/html; charset=ISO-8859-9">
<META http-equiv="Content-Type" content="text/html; charset=windows-1254">
</HEAD>

<BODY bgcolor=DarkOrange text="white">
<br><br><br><br><br>
<center>
<table width="250"><tr>	<td>
<font face="arial" size="6">Çok güzel!<p>Grafik malzemesi <%= grafdurum %> olan <%= siteadi %> ve <%= turadi %> amaçlý bir Web sitesi, için ücret US$<%= bedel %> olacaktýr.</font></td></tr></table>
<br><br><br><br><table width="500"><tr>
<td width="150" valign="top"><font face="arial" size="5">Ýlk görüþme için iki saatlik randevu almanýz gerekir.</font>
<p><font face="arial" size="3">(Açýk olan randevu tarihi ve saatinden        beðendiðinizi týklayýnýz)</font></td>
<td width="50"></td>
<td width="300" valign="top"><!--#include file="rand.inc"--></td></tr></table>
</center>
</BODY>
</HTML>



