<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<%@ Language = VBscript %>
<%

'Degiskenleri tanımlayalım
Dim siteNO
Dim grafNO
Dim turNO
Dim randNO
Dim randRayic
Dim SQLZAMAN
Dim connzaman
Dim zaman
Dim randzaman

'Degiskenleri querystring yoluyla alalim

siteNO=Request.Querystring("siteNO")
grafNO=Request.Querystring("grafNO")
turNO=Request.Querystring("turNO")
randNO=Request.Querystring("randNO")
randRayic=Request.Querystring("randRayic")


'Randevu zamanini 
'birincil endekse göre al.
'Ve bunu randzaman degiskenine ver.

SQLZAMAN="SELECT randZaman FROM randevu "
SQLZAMAN=SQLZAMAN & "WHERE randNO=" & randNO

set connzaman = server.createobject("ADODB.Connection")
connzaman.open "Web"
set zaman=connzaman.execute(SQLZAMAN)
randzaman=zaman(0)
connzaman.close
%>

<HTML>
<HEAD>
<TITLE>Randevu Defteri</TITLE>
<META http-equiv="content-type" content="text/html; charset=ISO-8859-9">
<META http-equiv="Content-Type" content="text/html; charset=windows-1254">
</HEAD>

<BODY bgcolor=DarkOrange text="white"><br><br><br><br><br><center>
<table width="250"><tr><td>
<font face="arial" size="6">Lütfen elverişli randevu zamanı olan<font color="blue"><%= randzaman %></font> için rezervasyon yapmak üzere gerekli bilgileri giriniz.</font>
<p><font face="arial" size="4">
<% 'Müsteriden istedigi zamani ayirmak için bazi bilgiler almak zorundayiz
'bilinen unsurlari gizli degiskenlerle alabiliriz %>
<form action="guncelle.asp" method="get">
<input type="Hidden" name="siteNO" value="<%= siteNO %>">
<input type="Hidden" name="grafNO" value="<%= grafNO %>">
<input type="Hidden" name="turNO" value="<%= turNO %>">
<input type="Hidden" name="randNO" value="<%= randNO %>">
<input type="Hidden" name="randRayic" value="<%= randRayic %>">
<input type="Text" name="adi" size="20"><i>Adınız</i>
<p><input type="Text" name="soyadi" size="20"><i>Soyadınız </i>
<p><input type="Text" name="email" size="20"> <i>e-adresiniz</i>
<p><input type="Submit" value="Gönder">
</form>
</td></tr></table>
<p><p></center>
</BODY>
</HTML>