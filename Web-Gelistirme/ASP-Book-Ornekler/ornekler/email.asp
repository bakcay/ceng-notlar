<HTML>
<HEAD>
<TITLE>E-Mail Form’u</TITLE>
<META http-equiv="content-type" content="text/html; charset=ISO-8859-9">
<META http-equiv="Content-Type" content="text/html; charset=windows-1254"><%
If Not IsEmpty(Request.Form("Email")) Then
  strEmail = Request.Form("Email")  
  If dogruMu(strEmail) Then
	Response.Write strEmail & " adresini aldık; teşekkür ederiz.<BR>"
'	.....[BURAYA DIĞER KODLAR GİRECEK]........................
  Else     
    Response.Write strEmail & " adresi doğru görünmüyor.<BR>"
  End If
End If
%>
<FORM "Name="Email" Action="email.asp" Method="post">
Enter an email address: 
<INPUT Name="Email" Type=Text>
<BR>
<!- - Buraya formun diğer unsurları girecek - - >
<INPUT Type=Submit Value="Gönder">
</FORM>
<SCRIPT RUNAT=SERVER LANGUAGE=VBScript>
Function dogruMu (byval adres)
  AtIsareti=0             	'sayaç olarak kullanacağımız
  Nokta=0            	'değişkenleri sıfırlayalım
  dogruMu=false         	'Fonksiyonun değerini yanlış olarak belirleyelim
  KacKarakter=len(adres)    	'adresin boyutunu bir değişkene atayalım
  For i=1 to KacKarakter 	'döngüyü başlatalım
    karakter=mid(adres, i, 1) 	'sayacın gösterdiği karakteri alalım
    if karakter="@" then      	'@ işareti olup olmadığına bakalım
      AtIsareti=AtIsareti + 1  	'@ işareti ise sayacı bir arttıralım
    End If
    if karakter="." Then          'nokta işaretini arayalım
      Nokta=Nokta + 1    	'nokta ise nokta sayasını bir arttıralım
    End if
  Next                        	'bir sonraki karaktere geçelim
If AtIsareti=1 and Nokta >0 Then	'eğer en az bir @ ve nokta olduysa
dogruMu=true               	'Fonksiyonun değerini doğru yapalım
End If
End Function
</SCRIPT>
</HTML>
