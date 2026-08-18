<HTML>
<HEAD>
<TITLE>PHP'de Dosya Acma</TITLE>
<meta http-equiv=\"content-type\" content=\"text/html; charset=ISO-8859-9\">
<meta http-equiv=\"Content-Type\" content=\"text/html; charset=windows-1254\">
</HEAD>
<h2>
<?php

$dosya_dizin = "/wwwroot/mycgiserver.com/members/uNhM13Qnmlo9V3EcdRZPK6aZFtYZlJ3M/";
$dosya_url = "http://www.mycgiserver.com/~ocal/";

if ($dosya = (fopen ("$dosya_dizin/bir_dosya.txt" , 'r') ) ) {
	print ("Dosya açıldı!");
	}
	else {
	print ("Dosya açılamadı!");
	}

?>
</h2>
</BODY>
</BODY>
</HTML>