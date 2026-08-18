<HTML>
<HEAD>
<TITLE>PHP'de Dizin Islemleri</TITLE>
<meta http-equiv=\"content-type\" content=\"text/html; charset=ISO-8859-9\">
<meta http-equiv=\"Content-Type\" content=\"text/html; charset=windows-1254\">
</HEAD>
<?php
$dizin_adi = "./create";
$dizin = opendir ($dizin_adi);

while ( gettype ( $bilgi =  readdir( $dizin ) ) != boolean ) {
		if ( is_dir( "$dizin_adi/$bilgi" ) )
		print " (D) " ;
		print ("<A href=\"$dizin_adi/$bilgi\">$bilgi</A><br>\n");
	}

closedir ($dizin);

?>

</BODY>
</BODY>
</HTML>