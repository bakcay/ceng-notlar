<%
'Grafik durumuyla ilgili bilgileri Grafik tablosundan al.
SQLGRAF="SELECT grafNO, grafDurum FROM Grafik"
set conngraf = server.createobject("ADODB.Connection")
conngraf.open "Web"
set graf=conngraf.execute(SQLGRAF)
%>
<select name="grafNO">
<% do while not graf.eof %>
<% 'Bu bilgilerle ziyaretçiye seçenek kutusu yap. %>
<Option value = "<%= graf(0) %>"><%= graf(1) %></Option>
<%graf.movenext 
loop%>
<% graf.close %>	
</select>

