<% Response.Buffer = True %>
<HTML>

<% mesaj = Server.URLEncode("Arzu ettiğiniz iş yapılıyor.. Lütfen bekleyiniz") %>
<% Response.Redirect ("bekle02.asp?BEKLE_SURE=3&BEKLE_MESAJ=" & mesaj & "&GONDER_URL=index.htm") %>

<HEAD>
<TITLE>ASP ILE BEKLETME 01</TITLE>
<META http-equiv="content-type" content="text/html; charset=ISO-8859-9">
<META http-equiv="Content-Type" content="text/html; charset=windows-1254">
</HEAD>
<BODY>
</BODY>
</HTML>