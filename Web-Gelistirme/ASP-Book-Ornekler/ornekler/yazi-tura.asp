<% Option Explicit %>
<HTML>
<HEAD>
<TITLE>ASP ILE YAZI-TURA</TITLE>
<META http-equiv="content-type" content="text/html; charset=ISO-8859-9">
<META http-equiv="Content-Type" content="text/html; charset=windows-1254">
</HEAD>
<BODY>
<H2>
<CENTER>

<%
Dim ParaAt, Yazi, Tura, Atis
Randomize
Yazi = 0
Tura = 0
Atis = 0
Do While Tura < 3
	atis = Atis + 1
	ParaAt = Int(Rnd * 2) + 1
	If ParaAt = 1 Then
%>
Yazı!<P>
<%
		Yazi = Yazi + 1 
	Else
%>
Tura!<P>
<%
Tura = Tura + 1
	End If
Loop
%>
3 Tura getirebilmek için parayı <%=Atis%> kere atmak gerekti!
</HTML>
