<% Option Explicit %>
<HTML>
<HEAD>
<TITLE>ASP ILE KLAOR - DOSYA KOLLEKSİYONU</TITLE>
<META http-equiv="content-type" content="text/html; charset=ISO-8859-9">
<META http-equiv="Content-Type" content="text/html; charset=windows-1254">
</HEAD>
<BODY>
<%
Dim DosyaSistemi, Surucu, Dosya, KokDizin, KokDosyalar, DosyaNesnesi
Dim SurucuHarfi
SurucuHarfi = "C:"
Set DosyaSistemi = CreateObject("Scripting.FileSystemObject")
Set Surucu = DosyaSistemi.GetDrive(SurucuHarfi)
Set KokDizin = Surucu.RootFolder
Set KokDosyalar = KokDizin.Files
For Each DosyaNesnesi In KokDosyalar
%>
<%=DosyaNesnesi.Name%><br>
<%
Next
%>
</BODY>
</HTML>
