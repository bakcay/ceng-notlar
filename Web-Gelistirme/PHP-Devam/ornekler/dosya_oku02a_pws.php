<HTML>
<HEAD>
<TITLE>PHP'de Dosya Okuma</TITLE>
<meta http-equiv=\"content-type\" content=\"text/html; charset=ISO-8859-9\">
<meta http-equiv=\"Content-Type\" content=\"text/html; charset=windows-1254\">
</HEAD>
<h2>
<?php
$dosya_adi = "/inetpub/wwwroot/bir_dosya.txt";
if ($dosya = (fopen ($dosya_adi , 'r') ) ) {
	print ("Dosya açıldı!<br>");
	}
	else {
	print ("Dosya açılamadı!");
	}
$dosya_boyut = filesize($dosya_adi);
$olcu = (int) ($dosya_boyut / 3 );
while ( ! feof ($dosya) ) {
	$paragraf = fread ( $dosya, $olcu) ;
	print ("$paragraf<br>");
	}
fclose ($dosya); 
?>

</h2>
</BODY>
</BODY>
</HTML>