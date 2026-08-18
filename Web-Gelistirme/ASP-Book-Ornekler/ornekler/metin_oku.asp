<% Option Explicit %>
<HTML>
<HEAD>
<TITLE>ASP ILE DOSYADAN METİN OKUMA</TITLE>
<META http-equiv="content-type" content="text/html; charset=ISO-8859-9">
<META http-equiv="Content-Type" content="text/html; charset=windows-1254">
</HEAD>
<BODY>
<%
Dim DosyaSistemi, MetinDosyasi, Satir
Set DosyaSistemi = CreateObject("Scripting.FileSystemObject")
Set MetinDosyasi = DosyaSistemi.OpenTextFile("c:\yazi_deneme.txt",1, 0)
Do
Satir = MetinDosyasi.ReadLine
%>
<%=Satir%>
<%
Loop Until MetinDosyasi.AtEndOfStream
MetinDosyasi.Close
%>
</BODY>
</HTML>
