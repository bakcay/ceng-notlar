<% @LANGUAGE=VBscript %>
<html>
<head>
<title>Hoşgeldiniz!</title>
<meta http-equiv="content-type" content="text/html; charset=ISO-8859-9">
<meta http-equiv="Content-Type" content="text/html; charset=windows-1254">
</head>

<body>
<center>

<%
' Yazı tipi boyutunu tutacağımız bir değişken tanımlayalım
Dim fontBoyut 
%>

<%
' yazı tipi boyutunu 1'den 7'ye kadar değiştirelim
For fontBoyut = 1 To 7 
%>

<font size = <%=fontBoyut%>>
Hoşgeldiniz!<br>
<% Next %>

</center>

<h3>Bugün <% =WeekdayName(Weekday(Date)) %>, <% = Date %>.
Şu anda Server'da saat: <% = Time %>.<p>
</h3>
</body>
</html>

