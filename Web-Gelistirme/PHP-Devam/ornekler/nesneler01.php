<HTML>
<HEAD>
<TITLE>PHP'de Nesneler</TITLE>
<meta http-equiv="content-type" content="text/html; charset=ISO-8859-9">
<meta http-equiv="Content-Type" content="text/html; charset=windows-1254">
</HEAD>
<BODY>
<B>
<H2>
<?php
class ogrenci {
// özellikleri tanımlayalım
	var $adi;
	var $soyadi;
	var $sinav1;
	var $sinav2;
	var $not;
// metodları tanımlayalım
	function adi_belirle ($n) {
		$this->adi = $n;
		}
	function soyadi_belirle ($n) {
		$this->soyadi = $n;
		}
	function sinav1_belirle ($n) {
		$this->sinav1 = $n;
		}
	function sinav2_belirle ($n) {
		$this->sinav2 = $n;
		}
	function not_hesapla() {
		$this->not = ($this->sinav1 + $this->sinav2)/2;
		print ($this->adi. " " . $this->soyadi . " için not ortalaması: ". $this->not);
		}
	}

//Buraya başka kodlar girecek

$ogr1 =  new ogrenci();
$ogr1 -> adi_belirle("Şahika"); 
$ogr1 -> soyadi_belirle("Tabak"); 
$ogr1 -> sinav1_belirle(7); 
$ogr1 -> sinav2_belirle(10); 
$ogr1 -> not_hesapla(); 

?>
</H2>
</B>
</BODY>
</HTML>
