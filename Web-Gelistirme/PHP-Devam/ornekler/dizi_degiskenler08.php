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
	$ogrenciler = array (
		array ( adi => "Özbay", soyadi => "Altun", sinav1 =>"", sinav2 =>"", not =>""),
		array ( adi => "Muharrem", soyadi => "Taç", sinav1 =>"", sinav2 =>"", not =>""),
		array ( adi => "Hasan", soyadi => "Civelek", sinav1 =>"", sinav2 =>"", not =>""),
		array ( adi => "Şahika", soyadi => "Tabak", sinav1 =>"", sinav2 =>"", not =>""),
		);

// Buraya başka kodlar girecek

foreach ( $ogrenciler as $ogrenci ) {
	foreach ( $ogrenci as $anahtar => $deger ) {
		print ("$anahtar = $deger <br> ");
		}
	print ("<br>");
	}

?>
</H2>
</B>
</BODY>
</HTML>
