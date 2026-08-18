<% @LANGUAGE = VBScript %>
<% 
Option Explicit 
Response.Buffer = True
Response.Expires = 60
%>
<HTML>
<HEAD>
<TITLE>ASP ILE ÇIKTI KONTROLU</TITLE>
<META http-equiv="content-type" content="text/html; charset=ISO-8859-9">
<META http-equiv="Content-Type" content="text/html; charset=windows-1254">
</HEAD>
<BODY>
Merhaba.. <BR>
Bakalım bu mesajı görecek misiniz?
<%
' Ama mesaj hızla değişiyor
Response.Clear
Response.Expires = 0
%>
<HTML>
<BODY>
Bu yazı Browser'a gidecek
<%
Response.Flush
%>
</BODY>
</HTML>
<%
Response.End
%>
Bu satır ise Browser'a hiç bir zaman gitmeyecek.