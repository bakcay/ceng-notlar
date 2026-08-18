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
Select Case Hour(Now)
	Case 0,1,2,3,4,5,6,7,8,9,10,11
	Response.Write "Günaydın!"
	Case 12,13,14,15,16,17
	Response.Write "Tünaydın"
	Case Else
	Response.Write "İyi Akşamlar!"
End Select
Response.Write "<BR>"
Response.Write "Site Onarım Sitesine Hoşgeldiniz"
%>
</CENTER>
</H2>
</BODY>
</HTML>