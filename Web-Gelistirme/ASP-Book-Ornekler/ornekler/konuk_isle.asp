<% Option Explicit %>
<HTML>
<HEAD>
<TITLE>KONUK DEFTERI KAYIT</TITLE>
<META http-equiv="content-type" content="text/html; charset=ISO-8859-9">
<META http-equiv="Content-Type" content="text/html; charset=windows-1254">
</HEAD>
<BODY>
<h2>Verdiğiniz Bilgiler:</h2>
Adınız: <%=Request.Form("Adi")%><BR>
Soyadınız: <%=Request.Form("Soyadi")%><BR>
E-Posta Adresiniz: <%=Request.Form("Email")%><BR>
Düşünceleriniz: <%=Request.Form("Mesaj")%><BR>
<p>
<%
Dim DosyaSistemi, KonukDosyasi
Set DosyaSistemi = CreateObject("Scripting.FileSystemObject")
Set KonukDosyasi = DosyaSistemi.OpenTextFile("c:\inetpub\wwwroot\konuklar.txt",8, True)
KonukDosyasi.WriteLine Request.Form("Adi")
KonukDosyasi.WriteLine Request.Form("Soyadi")
KonukDosyasi.WriteLine Request.Form("Email")
KonukDosyasi.WriteLine Request.Form("Mesaj")
KonukDosyasi.Close
%>
<H3>Konuk Defterime kaydedildi. Çok teşekkür ederim.</H3>
<A HREF="konuk_oku.asp">Konuk Defterini Oku!</A>&nbsp;&nbsp;&nbsp;<A HREF="index.htm">Ana Sayfaya Dön!</A>
</BODY>
</HTML>
