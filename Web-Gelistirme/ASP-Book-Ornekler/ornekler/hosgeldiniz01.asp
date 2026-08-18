<HTML>
<HEAD>
<TITLE>ASP ILE SAATE GÖRE SELAM</TITLE>
<META http-equiv="content-type" content="text/html; charset=ISO-8859-9">
<META http-equiv="Content-Type" content="text/html; charset=windows-1254">
</HEAD>
<BODY>
<H2>
<CENTER>
<%
If Hour(Now) <12 Then 
	Response.Write "Günaydın! "
ElseIf Hour(Now) >= 18 Then
	Response.Write "İyi akşamlar! "
Else
Response.Write "Tünaydın! "
End If
Response.Write "<BR>"
Response.Write "Site Onarım Sitesine Hoşgeldiniz"
%>
</CENTER>
</H2>
</BODY>
</HTML>