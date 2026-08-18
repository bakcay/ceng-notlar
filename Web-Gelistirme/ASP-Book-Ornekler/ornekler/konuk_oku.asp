<% Option Explicit %>
<HTML>
<HEAD>
<TITLE>KONUK DEFTERI OKUMA</TITLE>
<META http-equiv="content-type" content="text/html; charset=ISO-8859-9">
<META http-equiv="Content-Type" content="text/html; charset=windows-1254">
</HEAD>
<BODY>
<h2>Konuk Defterimde Yeralan Bilgiler:</h2>
Bugüne kadar konuk defterimi imzalayan bütün dostlarıma teşekkür ederim
<p>
<%
Dim DosyaSistemi, KonukDosyasi, Adi, Soyadi, Email, Mesaj
Set DosyaSistemi = CreateObject("Scripting.FileSystemObject")
Set KonukDosyasi = DosyaSistemi.OpenTextFile("c:\inetpub\wwwroot\konuklar.txt",1)
Do While Not KonukDosyasi.AtEndOfStream

Adi = KonukDosyasi.ReadLine
Soyadi = KonukDosyasi.ReadLine
Email = KonukDosyasi.ReadLine
Mesaj = KonukDosyasi.ReadLine
Response.Write Adi & "<BR>"
Response.Write Soyadi & "<BR>"
Response.Write Email & "<BR>"
Response.Write Mesaj & "<P>"
Loop
KonukDosyasi.Close
%>
<A HREF="index.htm">Ana Sayfaya Dön!</A>
</BODY>
</HTML>
