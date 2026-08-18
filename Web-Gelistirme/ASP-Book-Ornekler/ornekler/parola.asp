<%@ LANGUAGE="VBSCRIPT" %>
<% 
Response.ExpiresAbsolute = Now() - 1 'Browser'ın sayfayı yedeklemesini önleyelim
FormParola = ucase(trim(request.form("FormParola")))
If FormParola <> "PAROLA" Then
%>
<HTML>
<HEAD>
<TITLE>ASP ILE PAROLA</TITLE>
<META http-equiv="content-type" content="text/html; charset=ISO-8859-9">
<META http-equiv="Content-Type" content="text/html; charset=windows-1254">
</HEAD>
<BODY bgcolor="#ccffff" text="black" link="navy" vlink="purple">
<DIV align="center">
<FORM action="parola.asp" method="POST">
<h2>Ana sayfaya girmek için parolayı yazınız (Mesela, PAROLA) ?</h2>
   <input type="password" name="FormParola" size="10"><br><br>
   <input type="submit" value="Girebilir Miyim?">
</form>
</div>
</body>
</html>
<% Else %>
Şimdi ana sayfaya girmiş oldunuz..
<% End If %>