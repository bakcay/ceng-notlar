<% Option Explicit %>
<HTML>
<HEAD>
<TITLE>ASP ILE SÜRÜCÜ KOLLEKSIYONU</TITLE>
<META http-equiv="content-type" content="text/html; charset=ISO-8859-9">
<META http-equiv="Content-Type" content="text/html; charset=windows-1254">
</HEAD>
<BODY>
<%
Dim DosyaSistemi, Surucu, Suruculer
Set DosyaSistemi = CreateObject("Scripting.FileSystemObject")
Set Suruculer = DosyaSistemi.Drives
For Each Surucu In Suruculer
%>
<b>Sürücü:</b> <%=Surucu.DriveLetter%><br>
<% If Surucu.IsReady = True Then%>
<b>Disk Adı:</b> <%=Surucu.VolumeName%><br>
<b>Boş alan:</b> <%=Surucu.FreeSpace%><br>
<% Else %>
<i>Sürücü hazır değil!</i><br>
<%
End If
Next
%>
</BODY>
</HTML>
