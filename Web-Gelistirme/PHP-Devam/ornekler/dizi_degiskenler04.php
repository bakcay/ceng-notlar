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
		$ogrenciler[0] = "Emre";
		$ogrenciler[15] = "Özbay";

	print ("Dizideki 1'nci isim: $ogrenciler[0] <br>");
	print ("Dizideki 2'nci isim: $ogrenciler[1] <br>");
	print ("Dizideki 3'ünci isim: $ogrenciler[2] <br>");
	print ("Dizideki 4'üncü isim: $ogrenciler[3] <br>");
	print ("Dizideki 5'inci isim: $ogrenciler[4] <br>");
	print ("Dizideki 6'ncı isim: $ogrenciler[5] <br>");
	print ("..............<br>");
	print ("Dizideki 15'nci isim: $ogrenciler[15] <br>");
	
?>

</H2>
</B>
</BODY>
</HTML>
