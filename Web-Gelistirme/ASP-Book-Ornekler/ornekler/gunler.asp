<HTML>
<HEAD>
<TITLE>ASP GÜNLERİ SAYMA</TITLE>
<META http-equiv="content-type" content="text/html; charset=ISO-8859-9">
<META http-equiv="Content-Type" content="text/html; charset=windows-1254">
</HEAD>
<BODY>
<H2>
<CENTER>
<%
Dim Gun 
Gun = Array("Pazartesi","Salı","Çarşamba","Perşembe","Cuma","Cumartesi","Pazar")
%>

<%
For sayac = 0 to 6
	Response.Write Gun(sayac)
	Response.Write "<BR>"
Next
%>
</CENTER>
</H2>
</BODY>
</HTML>

