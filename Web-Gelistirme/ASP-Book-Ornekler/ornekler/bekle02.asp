<%@ LANGUAGE="VBSCRIPT" %>
<%
BEKLE_SURE = Request("BEKLE_SURE")
GONDER_URL = Request("GONDER_URL")
BEKLE_MESAJ = Request("BEKLE_MESAJ")
%>
<html>
<head>
<META http-equiv="content-type" content="text/html; charset=ISO-8859-9">
<META http-equiv="Content-Type" content="text/html; charset=windows-1254">

<meta http-equiv="Refresh" content="<% =BEKLE_SURE %>; URL=<% =GONDER_URL %>">
<title>ASP ile Bekletme</title>
</head>

<body color="#FFFFFF">

<font face="Arial"><p align = "center"><strong><% =BEKLE_MESAJ %></strong></p></font>

</body>
</html> 
