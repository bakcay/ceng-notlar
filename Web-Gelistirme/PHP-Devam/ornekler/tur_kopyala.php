<HTML>
<HEAD>
<TITLE>PHP'de Degisken Turleri Kopyalama (Casting)</TITLE>
<meta http-equiv="content-type" content="text/html; charset=ISO-8859-9">
<meta http-equiv="Content-Type" content="text/html; charset=windows-1254">
</HEAD>
<BODY>
<B>
<H2>
<?php
	$degisken  = 3.1418;
	print("Değişkenin  değeri : ");
	print "$degisken<br>";
	print("Türü : ");
	print gettype( $degisken ) ; //çift,ondalık/double
	print "<br>";
	print "<br>";

	print "İlk kopyalama işlemi: Alfanümerik/String:<br>";
	$kopya_degisken =  ( string ) $degisken; //alfanümerik/string
	print "Değeri : ";
	print "$kopya_degisken<br>";
	print("Türü : ");
	print gettype( $kopya_degisken ) ; //alfanümerik/string
	print "<br>";
	print "<br>";

	print "İkinci kopyalama işlemi: Tamsayı/Integer:<br>";
	$kopya_degisken =  ( integer ) $degisken; //Tamsayı/Integer
	print "Değeri : ";
	print "$kopya_degisken<br>";
	print("Türü : ");
	print gettype( $kopya_degisken ) ; //Tamsayı/Integer
	print "<br>";
	print "<br>";

	print "Üçüncü değiştirme işlemi: Ondalık/Double:<br>";
	$kopya_degisken =  ( double ) $degisken; //çift,ondalık/double
	print "Değeri : ";
	print "$kopya_degisken<br>";
	print("Türü : ");
	print gettype( $kopya_degisken ) ; //çift,ondalık/double
	print "<br>";
	print "<br>";

	print "Dördüncü kopyalama işlemi: Mantıksal/Boolean:<br>";
	$kopya_degisken =  ( boolean ) $degisken; // Mantıksal/Boolean
	print "Değeri : ";
	print "$kopya_degisken<br>";
	print("Türü : ");
	print gettype( $kopya_degisken ) ; // Mantıksal/Boolean
	print "<br>";
	print "<br>";

?>
</H2>
</B>
</BODY>
</HTML>