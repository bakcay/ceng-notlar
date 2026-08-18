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
		$ogrenciler[] = "Özbay";
		$ogrenciler[] = "Muharrem";
		$ogrenciler[] = "Hasan";
		$ogrenciler[] = "Şahika";

// Buraya başka kodlar girecek

foreach ($ogrenciler as $ogrenci) {
	print ("$ogrenci<br>"); 
	}
?>

</H2>
</B>
</BODY>
</HTML>
