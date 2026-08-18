<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<BASEFONT FACE="Tahoma">
<HTML>
<HEAD>
<TITLE>ORNEK FORM SONUCLARI</TITLE>
<META http-equiv="content-type" content="text/html; charset=ISO-8859-9">
<META http-equiv="Content-Type" content="text/html; charset=windows-1254">
</HEAD>
<BODY>
<%
dim FormTercihi
FormTercihi = Request.QueryString("HangiForm")
Select Case FormTercihi
Case 1
%>
Metin alanı sonuçları<P>
<TABLE BORDER=1 CELLPADDING=5 width=75%>
<TR><TD>Input/Text Alanı</TD><TD><B><%= Request.Form("MetinGir") %></B></TD></TR>
<TR><TD>Input/Passsword Alanı</TD><TD><B><%= Request.Form("ParolaAlani") %></B></TD></TR>
<TR><TD>TextArea Alanı</TD><TD><B><%= Request.Form("MetinAlani") %></B></TD></TR>
</TABLE>
<HR>
<%
Case 2
%>
Radyo Düğmesi ve İşaret Kutusu Sonuçları<P>
<TABLE BORDER=1 CELLPADDING=5 width=25%>
<TR><TD>Seçilen Radyo Düğmesi</TD><TD><B><%= Request.Form("Radyo") %></B></TD></TR>
<TR><TD>İşaretlenen Kutular</TD><TD><B><%
dim strIsaretlenen
	for each strIsaretlenen in Request.Form("IsaretKutusu")
	Response.Write strIsaretlenen & "<BR>"
	next
 %></B></TD></TR>
</TABLE>
<HR>
<%
Case 3
%>
Seçme Alanları sonuçları<P>
<TABLE BORDER=1 CELLPADDING=5 width=35%>
<TR><TD>Seçilen Liste Ögesi</TD><TD><B><%= Request("SecmeListesi") %></B></TD></TR>
<TR><TD>Seçilen Çoklu Liste Ögeleri</TD><TD><B><%
	for each strIsaretlenen in Request("CokluSecme")
	Response.Write strIsaretlenen & "<BR>"
	next
%></B></TD></TR>
</TABLE>
<HR>
<%
End Select
%>