<HTML>
<HEAD>
<TITLE>PHP'de Degiskenler</TITLE>
<meta http-equiv="content-type" content="text/html; charset=ISO-8859-9">
<meta http-equiv="Content-Type" content="text/html; charset=windows-1254">
</HEAD>
<BODY>
<B>
<H2>
<?php
	$adi = "Şahika";
	print $adi;

	print "</h2>";
	print "<h2>";

	$soyadi = "Tabak";
	$birsey = "soyadi";
	print $$birsey;

?>
</H2>
</B>
</BODY>
</HTML>
