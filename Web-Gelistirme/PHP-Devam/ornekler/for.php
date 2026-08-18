<HTML>
<HEAD>
<TITLE>PHP'de Döngü</TITLE>
<meta http-equiv="content-type" content="text/html; charset=ISO-8859-9">
<meta http-equiv="Content-Type" content="text/html; charset=windows-1254">
</HEAD>
<BODY>

<?php
	$tekrar = 10;

	for ($sayac = 1; $sayac <= $tekrar ; $sayac++ ) {
	if ( $tekrar == 0 )
	break;
	print ("<font size= $sayac >");
	print ("<b><p>İyileri iyilikleri ile alkışlayınız!</b></p>");
	print ("</font>");
	}
?>

</BODY>
</HTML>