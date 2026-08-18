<HTML>
<HEAD>
<TITLE>PHP'de Formlar</TITLE>
<meta http-equiv="content-type" content="text/html; charset=ISO-8859-9">
<meta http-equiv="Content-Type" content="text/html; charset=windows-1254">
</HEAD>
<BODY>

<?php

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
?>

</BODY>
</HTML>
