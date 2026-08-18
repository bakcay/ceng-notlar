<%@ LANGUAGE="VBSCRIPT" %>
<% Option Explicit %>
<HTML>
<HEAD>
<TITLE>ASP SELECT DOLDURMA</TITLE>
<META http-equiv="content-type" content="text/html; charset=ISO-8859-9">
<META http-equiv="Content-Type" content="text/html; charset=windows-1254">
</HEAD>

<% 
' Değişkenleri tanımlayalım
Dim connVeriyolu, rsVeri, SQL
Set connVeriyolu = Server.CreateObject("ADODB.Connection")
SQL ="SELECT uyeAdi, uyeSoyadi FROM uyeler"
connVeriyolu.open "uyeler"
Set rsVeri=connVeriyolu.execute(SQL)
%>

<BODY>
Bu listeden bir üyenin adını seçiniz:
<SELECT NAME="AdSoyad">
<% Do While Not rsVeri.eof %>
<OPTION VALUE = "<%= rsVeri(0) & " " & rsVeri(1)%>"><%= rsVeri(0) & " " & rsVeri(1)%> 
</Option>
<%rsVeri.movenext 
loop%>
</select>
<% rsVeri.close %>	
</SELECT>
</BODY>
</HTML>
