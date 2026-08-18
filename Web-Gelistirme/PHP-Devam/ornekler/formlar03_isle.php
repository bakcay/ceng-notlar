<HTML>
<HEAD>
<TITLE>PHP'de Formlar</TITLE>
<meta http-equiv="content-type" content="text/html; charset=ISO-8859-9">
<meta http-equiv="Content-Type" content="text/html; charset=windows-1254">
</HEAD>
<BODY>

<?php

	foreach ($HTTP_GET_VARS as $anahtar=>$deger ) {
		print ("<b>$anahtar = $deger <br>\n");
	}
?>

</BODY>
</HTML>
