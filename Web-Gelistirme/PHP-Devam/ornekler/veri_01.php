<HTML>
<TITLE>PHP ile Veri Örnegi</TITLE>
<meta http-equiv="content-type" content="text/html; charset=ISO-8859-9">
<meta http-equiv="Content-type" content="text/html; charset=windows-1254">
</HEAD>
<BODY>
<?php

$veri_yolu = mysql_connect("server", "root");
if ( ! $veri_yolu ) die ("MySQL ile veri bağlantısı kurulamıyor!");
mysql_select_db("veri" , $veri_yolu) or die ("Veritabanına ulaşılamıyor!" . mysql_error() );
$sonuc = mysql_query("SELECT * FROM calisanlar",$veri_yolu);
	printf("Adı: %s<br>\n", mysql_result($sonuc,0,"adi"));
	printf("Soyadı: %s<br>\n", mysql_result($sonuc,0,"soyadi"));
	printf("Adresi: %s<br>\n", mysql_result($sonuc,0,"adres"));
	printf("Görevi: %s<br>\n", mysql_result($sonuc,0,"pozisyon"));
?>
</BODY>
</HTML>