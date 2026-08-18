<% Option Explicit %>
<HTML>
<HEAD>
<TITLE>ASP ILE DOSYA SİLME</TITLE>
<META http-equiv="content-type" content="text/html; charset=ISO-8859-9">
<META http-equiv="Content-Type" content="text/html; charset=windows-1254">
</HEAD>
<BODY>
<%
Dim DosyaSistemi
Set DosyaSistemi = CreateObject("Scripting.FileSystemObject")
DosyaSistemi.DeleteFile "d:\Temp\*.*"
%>

<H2><CENTER>Bu Web sayfası sabit diskten dosya siler!!
<BR>
Şimdi D: sürücüsünde Temp dizinindeki bütün dosyaların silinmiş olması gerekir.!
<BR>
Lütfen bakar mısınız?</H2></CENTER>
</BODY>
</HTML>
