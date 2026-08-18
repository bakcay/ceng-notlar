<HTML>
<HEAD>
<TITLE>HTTP ServerDegişkenleri Kolleksiyonu</TITLE>
<meta http-equiv="content-type" content="text/html; charset=ISO-8859-9">
<meta http-equiv="Content-Type" content="text/html; charset=windows-1254">
</HEAD>
<BODY BGCOLOR=white>
<CENTER>
<H2>HTTP Server Değişkenleri Kolleksiyonu</H2>
</CENTER>
<TABLE BORDER=1>
<TR><TD><B>Değişkenin adı</B></TD> <TD><B>Değeri</B></TD></TR>
<% For Each key in Request.ServerVariables %>
	<TR>
	<TD><% = key %></TD>
	<TD>
	<%If Request.ServerVariables(key) = "" Then
		Response.Write "&nbsp;" 
	Else		
		Response.Write Request.ServerVariables(key)
	End If
	Response.Write "</TD>"%>
	</TR>
<% Next %>
</TABLE>
<p>
Sizin Host'unuzun adı:<B> <%=Request.ServerVariables("HTTP_HOST")%></B>
</BODY>
</HTML>
