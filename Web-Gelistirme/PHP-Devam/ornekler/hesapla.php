<HTML>
<HEAD>
<TITLE>PHP'de Fonksiyon</TITLE>
<meta http-equiv="content-type" content="text/html; charset=ISO-8859-9">
<meta http-equiv="Content-Type" content="text/html; charset=windows-1254">
</HEAD>
<BODY>

<?php

function topla ($sayi1, $sayi2) {
	$sonuc = $sayi1 + $sayi2;
	return $sonuc;
	}
function cikart ($sayi1, $sayi2) {
	$sonuc = $sayi1 - $sayi2;
	return $sonuc;
	}
function carp ($sayi1, $sayi2) {
	$sonuc = $sayi1 * $sayi2;
	return $sonuc;
	}
function bol ($sayi1, $sayi2) {
	$sonuc = $sayi1 / $sayi2;
	return $sonuc;
	}


// Başka kodlar buraya girebilir

$sayi1 = 12;
$sayi2 = 5;

	print topla($sayi1, $sayi2);
	print ("<br>");
	print cikart($sayi1, $sayi2);
	print ("<br>");
	print carp($sayi1, $sayi2);
	print ("<br>");
	print bol($sayi1, $sayi2);
	print ("<br>");

?>

</BODY>
</HTML>