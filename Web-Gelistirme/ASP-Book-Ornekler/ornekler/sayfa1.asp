<% @Language = VBscript %>
<HTML>
<HEAD>
<TITLE>Web Sitesi Yapilir</TITLE>
<META http-equiv="content-type" content="text/html; charset=ISO-8859-9">
<META http-equiv="Content-Type" content="text/html; charset=windows-1254">
</HEAD>
<BODY bgcolor=darkorange text="white" language=Turkish>
<br><br><br><br><br><center><table width="250"><tr><td>
<font face="arial" size="6">Arzu ettiğiniz siteyi sür'atle oluşturabiliriz.<p>Önce
nasıl bir site istediğinizi ve grafik malzemenin durumunu belirtin?</font> </P>
</td></tr></table>
<p><p><table width="500">
<form action="sayfa2.asp" method="get">
<TBODY><tr><td width="500" align="middle">
<% 'Buraya bir harici include dosyası ekliyoruz %>            
<p><!--#include file="siteler.inc"-->
Kullanılacak grafik malzemenin durumu: <!--#include file="grafikler.inc"--><br>
<br><br><br><p><input type="submit" value="Gönder" align="left"></p>	
</td></tr></form></TBODY></table></center>
</BODY>
</HTML>