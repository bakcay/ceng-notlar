<%
'Randevular için gerekli bilgiyi randevu tablosundan al.
SQLRAND="SELECT randNO, randZaman FROM Randevu WHERE randDurum = 'SERBEST' ORDER BY randZaman"
set connrand = server.createobject("ADODB.Connection")
connrand.open "web"
set rand=connrand.execute(SQLRAND)
%>
<font face="arial" size="5">
<% do while not rand.eof

%>

<a href="rezerv.asp?siteNO=<%= siteNO %>&grafNO=<%= grafNO %>&turNO=<%= turNO %>&randNO=<%= rand(0) %>&randRayic=<%= bedel %>"><%= rand(1) %></a><br>
<%rand.movenext 
loop%>
</font>

<% connrand.close %>	
<% SET connrand = Nothing %>
