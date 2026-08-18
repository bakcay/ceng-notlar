<% Option Explicit %>
<HTML>
<HEAD>
<TITLE>ASP ILE DOSYA YAZMA</TITLE>
<META http-equiv="content-type" content="text/html; charset=ISO-8859-9">
<META http-equiv="Content-Type" content="text/html; charset=windows-1254">
</HEAD>
<BODY>
<%
Dim YaziFSO, yaz
Set YaziFSO = CreateObject("Scripting.FileSystemObject")
Set yaz = YaziFSO.CreateTextFile("c:\yazi_deneme.txt",True)
yaz.WriteLine("Bu bir denemedir.")
yaz.Close
%>
<H2><CENTER>Bu Web sayfası sabit diske yazı yazdırır!!
<BR>
Şimdi C: sürücüsünde yazi_deneme.txt adlı bir dosya olması gerekir!
<BR>
Lütfen bakar mısınız?</H2></CENTER>
</BODY>
</HTML>
