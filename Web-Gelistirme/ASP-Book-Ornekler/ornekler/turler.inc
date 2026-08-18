<%
'Türler tablosundan bilgi seçmek ve müsteriye sunmak için.

SQLTUR="SELECT turNO, turAdi FROM Tur"
set conntur = server.createobject("ADODB.Connection")
conntur.open "web"
set tur=conntur.execute(SQLTUR)
%>
<select name="turNO">
<% 'Listedeki bütün seçenekleri al.%>

<% do while not tur.eof %>
<Option value = "<%= tur(0) %>"><%= tur(1) %></Option>
<%tur.movenext 
loop%>
<% tur.close %>	
</select>

