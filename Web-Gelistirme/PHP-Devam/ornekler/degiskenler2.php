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
	$degisken  = "adi";
	$$degisken = "Şahika";
	print "$adi<br>";
	print $$degisken;
	print "<br>";
	print "${$degisken}<br>";
	print "${'adi'}<br>";
?>
</H2>
</B>
</BODY>
</HTML>
