<%
'Siteler tablosundan siteAdi sütunundaki bilgileri al.
SQLSITE="SELECT siteAdi, siteNO FROM Siteler"
set connsite = server.createobject("ADODB.Connection")
connsite.open "web"
set siteler=connsite.execute(SQLSITE)
%>
<select name="siteNO">
	<% 'Listedeki her kayit için su isi yap. %>
	<% do while not siteler.eof %>
		<Option value = "<%= siteler(1) %>"><%= siteler(0) %></Option>
	<%siteler.movenext 
	loop%>
</select>
<% siteler.close %>	

