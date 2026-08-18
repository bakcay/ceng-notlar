<HTML>
<HEAD>
<TITLE>PHP'de Dosya Acma</TITLE>
<meta http-equiv=\"content-type\" content=\"text/html; charset=ISO-8859-9\">
<meta http-equiv=\"Content-Type\" content=\"text/html; charset=windows-1254\">
</HEAD>
<?php


$dizin_adi = "/wwwroot/mycgiserver.com/members/uNhM13Qnmlo9V3EcdRZPK6aZFtYZlJ3M/";
$dosya_url = "http://www.mycgiserver.com/~ocal";

$dizin = opendir ($dizin_adi);
print ("<H2>Bu dizindeki alt-dizinler:</H2>\n");
while ( gettype ( $bilgi =  readdir( $dizin ) ) != boolean ) {
		if ( is_dir( "$dizin_adi/$bilgi" ) ){
		print " [Dizin: ] " ;
		print ("<A href=\"$dosya_url/$bilgi\">$bilgi</A><br>\n");
	}
}
closedir ($dizin);

$dizin = opendir ($dizin_adi);
print ("<H2>Bu dizindeki Dosyalar:</H2>\n");
while ( gettype ( $bilgi =  readdir( $dizin ) ) != boolean ) {
		if ( is_dir( "$dizin_adi/$bilgi" ) ){
			continue; 
			}
		print ("<A href=\"$dosya_url/$bilgi\">$bilgi</A><br>\n");
}
closedir ($dizin);

?></BODY>
</BODY>
</HTML>