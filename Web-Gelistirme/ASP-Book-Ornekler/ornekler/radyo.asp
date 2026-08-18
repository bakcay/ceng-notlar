<%@ LANGUAGE="VBSCRIPT" %>
<% Option Explicit %>
<HTML>
<HEAD>
<TITLE>ASP OPTION-RADIO DOLDURMA</TITLE>
<META http-equiv="content-type" content="text/html; charset=ISO-8859-9">
<META http-equiv="Content-Type" content="text/html; charset=windows-1254">
</HEAD>

<% 
' Değişkenleri tanımlayalım
Dim connVeriyolu, rsVeri, SQL
Set connVeriyolu = Server.CreateObject("ADODB.Connection")
SQL ="SELECT renk FROM renkler"
connVeriyolu.open "uyeler"
Set rsVeri=connVeriyolu.execute(SQL)
%>
<BODY>
<FORM><DIV ALIGN="center"><center><TABLE BORDER="0">
<TR>
<TD colspan="2" align="center"><h3>Renk</h3></TD>
</TR>
<% Do While Not rsVeri.eof %>
<TR><TD><INPUT TYPE="radio" VALUE="<%=rsVeri(0)%>" NAME="Radyo"></TD><TD><%=rsVeri(0)%></TD></TR>
<%rsVeri.movenext 
loop%>
</TABLE></CENTER></DIV>
</FORM>
</BODY>
</HTML>
