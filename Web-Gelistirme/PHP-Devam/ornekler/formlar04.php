<?php
if ( isset ( $HTTP_POST_VARS )) {

print ("<HTML>\n");
print ("<HEAD>\n");
print ("<TITLE>PHP'de Formlar</TITLE>\n");
print ("<meta http-equiv=\"content-type\" content=\"text/html; charset=ISO-8859-9\">\n");
print ("<meta http-equiv=\"Content-Type\" content=\"text/html; charset=windows-1254\">\n");
print ("</HEAD>\n");
print ("<BODY>\n");

	foreach ($HTTP_POST_VARS as $anahtar=>$deger ) {
		if ( gettype ($deger ) == "array" ) {
			print ("$anahtar == <br>\n");
			foreach ( $deger as  $yeni_degerler ) 
				print (".. $yeni_degerler<br>");
				}
		else {
		print ("<b>$anahtar = $deger <br>\n");
		}
	}
print ("</BODY>\n");
print ("</HTML>\n");

}

else {

print ("<HTML>\n");
print ("<HEAD>\n");
print ("<TITLE>PHP'de Formlar</TITLE>\n");
print ("<meta http-equiv=\"content-type\" content=\"text/html; charset=ISO-8859-9\">\n");
print ("<meta http-equiv=\"Content-Type\" content=\"text/html; charset=windows-1254\">\n");
print ("</HEAD>\n");
print ("<BODY>\n");
print ("<FORM ACTION=\"$PHP_SELF\" METHOD=\"POST\">\n");
print (" Adınız, Soyadınız: <INPUT TYPE=\"TEXT\" NAME=\"adi\">\n");
print ("<BR>\n");
print (" Elektronik Adresiniz: <INPUT TYPE=\"TEXT\" NAME=\"adres\">\n");
print ("<BR>\n");
print (" Hangi notunuzu öğrenmek istiyorsunuz? \n");
print ("<BR>\n");
print ("<SELECT NAME=\"hangi_not[]\" MULTIPLE>\n");
print ("<OPTION>Sınav 1 \n");
print ("<OPTION>Sınav 2 \n");
print ("<OPTION>Ortalama \n");
print ("</SELECT>\n");
print ("<BR>\n");
print ("<INPUT TYPE=\"SUBMIT\" VALUE=\"Gönder Gitsin!\"> <INPUT TYPE=\"RESET\" VALUE=\"Vazgeç, Gönderme!\">   \n");
print ("</FORM>\n");

print ("</BODY>\n");
print ("</HTML>\n");
}
?>