
<%@ Language = VBscript %>
<%

'DEGISKENLERI DEKLARE ET
Dim siteNO
Dim grafNO
Dim TurNO
Dim randNO
Dim randRayic
Dim adi
Dim soyadi
Dim email
Dim SQLINSERT
Dim connupdate
Dim SQLUPDATE
Dim URL
Dim simdi

' querystring yoluyla degiskenleri al.

siteNO=Request.Querystring("siteNO")
grafNO=Request.Querystring("grafNO")
turNO=Request.Querystring("turNO")
randNO=Request.Querystring("randNO")
randRayic=Request.Querystring("randRayic")
adi=Request.Querystring("adi")
soyadi=Request.Querystring("soyadi")
email=Request.Querystring("email")

'Yeni müsteri için SQL INSERT deyimi hazýrla.
 
SQLINSERT="INSERT INTO Musteriler (adi, soyadi, email, siteNO, grafNO, turNO) "
SQLINSERT=SQLINSERT & "VALUES ("
SQLINSERT=SQLINSERT & "'" & adi & "', "
SQLINSERT=SQLINSERT & "'" & soyadi & "', "
SQLINSERT=SQLINSERT & "'" & email & "', "
SQLINSERT=SQLINSERT & siteNO & ", "
SQLINSERT=SQLINSERT & grafNO & ", "
SQLINSERT=SQLINSERT & turNO & ") "

set connupdate = server.createobject("ADODB.Connection")
connupdate.open "web"
connupdate.execute(SQLINSERT)

'Randevunun kesinlestigi tarih ve saati al.

simdi =  FormatDateTime(now,vbLongDateTime)


SQLUPDATE="UPDATE Randevu SET " 
SQLUPDATE=SQLUPDATE & "email = '" & email & "', "
SQLUPDATE=SQLUPDATE & "randNezaman = '" & simdi & "', "
SQLUPDATE=SQLUPDATE & "randDurum = 'DOLU', "
SQLUPDATE=SQLUPDATE & "randRayic = " & randRayic 
SQLUPDATE=SQLUPDATE & " WHERE randNO =" & randNO

connupdate.execute(SQLUPDATE)
connupdate.close
SET connupdate = Nothing

'Randevunun kesinlestigini bildir.

URL="son.asp?adi=" & adi
Response.redirect (URL)

%>




<head>
<title></title>
</head>

