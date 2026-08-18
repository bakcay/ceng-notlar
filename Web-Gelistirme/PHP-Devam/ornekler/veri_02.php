<?php

// Form doldurulduktan sonra program buradan başlıyor
if ( isset ( $HTTP_POST_VARS )) {

	$veri_yolu = mysql_connect("server", "root");
	if ( ! $veri_yolu ) die ("MySQL ile veri bağlantısı kurulamıyor!");
	mysql_select_db("veri" , $veri_yolu) or die ("Veritabanına ulaşılamıyor!" . mysql_error() );
	$ekle = mysql_query("INSERT INTO calisanlar ( adi , soyadi , adres , pozisyon ) VALUES ('$adi', '$soyadi', '$adres', '$pozisyon' )", $veri_yolu );

echo ("
	<HTML>
	<HEAD>
	<TITLE>PHP'de Veritabanı</TITLE>
	<meta http-equiv='content-type' content='text/html; charset=ISO-8859-9'>
	<meta http-equiv='Content-Type' content='text/html; charset=windows-1254'>

	<style>
	<!--

	a:link    { font-family: Verdana; font-size: 11px; font-weight: bold; text-decoration: none; color: #000000 }
	a:active  { font-family: Verdana; font-size: 11px; font-weight: bold; text-decoration: none; color: #ff0000 }
	a:visited { font-family: Verdana; font-size: 11px; font-weight: bold; text-decoration: none; color: #000080 }
	a:hover   { font-family: Verdana; font-size: 11px; font-weight: bold; text-decoration: underline; color: #ff0000 }

	td 
	{ 
	BACKGROUND-COLOR: #bbbbff;
	BORDER-BOTTOM: #000080 1px solid;
	BORDER-TOP: #0000ff 1px solid;
	BORDER-LEFT: #0000ff 1px solid;
	BORDER-RIGHT: #000080 1px solid;
	font-family: verdana;
	font-size: 11px; 
	font-weight: bold; 
	color: #0000ff
	CURSOR: arrow; 
	}

	.baslik 
	{
    BACKGROUND-COLOR: #0099ff;
    BORDER-BOTTOM: #003399 2px solid;
    BORDER-LEFT: #99ccff 2px solid;
    BORDER-RIGHT: #003399 2px solid;
    BORDER-TOP: #99ccff 2px solid;
    COLOR: white;
    FONT-FAMILY: Verdana, Arial, Helvetica, sans-serif;
    FONT-SIZE: 11px;
    FONT-WEIGHT: bold;
    HEIGHT: 20px;
    LETTER-SPACING: 0.2pt;
    LINE-HEIGHT: 10pt;
    MARGIN: 0px;
    PADDING-TOP: 1px;
    TEXT-DECORATION: none;
    TEXT-ALIGN: center
	}
	-->
	</style>
	</HEAD>
	<BODY>
	<p class='baslik'><FONT COLOR='#FFFFFF'><B>Üyelerimiz arasına siz de katıldınız</B></FONT></P>
	");

$sonuc = mysql_query("SELECT * FROM calisanlar", $veri_yolu);
echo ("<TABLE BORDER='0' BORDERCOLOR='blue' CELLSPACING='7' CELLPADDING='1'>\n");
echo ("
		<TR>
			<TD class='baslik'><FONT COLOR='#FFFFFF'><B>Uzmanın Adı</B></FONT></TD>
			<TD class='baslik'><FONT COLOR='#FFFFFF'><B>Çalıştığı Yer</B></FONT></TD>
			<TD class='baslik'><FONT COLOR='#FFFFFF'><B>Görevi</B></FONT></TD>
		</TR>
	\n");
while ($satir = mysql_fetch_row($sonuc)) {
	printf("<TR><TD ALIGN='left'>%s %s</TD><TD ALIGN='left'>%s</TD></TD><TD ALIGN='left'>%s</TD></TR>\n", $satir[1], $satir[2], $satir[3], $satir[4]);
	}
echo ("
		</TABLE>\n
		<p class='baslik'><FONT COLOR='#FFFFFF'><B>Teşekkür ederiz.</B></FONT></P>
		<A HREF='index.php'>Ana sayfaya dönmek için tıklayınız</A>
	
		");


}
// program ilk kez açılıyorsa buradan başlayacak

else {

echo ("
	<HTML>
	<HEAD>
	<TITLE>PHP'de Veritabanı</TITLE>
	<meta http-equiv='content-type' content='text/html; charset=ISO-8859-9'>
	<meta http-equiv='Content-Type' content='text/html; charset=windows-1254'>

	<style>
	<!--

	a:link    { font-family: Verdana; font-size: 11px; font-weight: bold; text-decoration: none; color: #000000 }
	a:active  { font-family: Verdana; font-size: 11px; font-weight: bold; text-decoration: none; color: #ff0000 }
	a:visited { font-family: Verdana; font-size: 11px; font-weight: bold; text-decoration: none; color: #000080 }
	a:hover   { font-family: Verdana; font-size: 11px; font-weight: bold; text-decoration: underline; color: #ff0000 }

	td 
	{ 
	BACKGROUND-COLOR: #bbbbff;
	BORDER-BOTTOM: #000080 1px solid;
	BORDER-TOP: #0000ff 1px solid;
	BORDER-LEFT: #0000ff 1px solid;
	BORDER-RIGHT: #000080 1px solid;
	font-family: verdana;
	font-size: 11px; 
	font-weight: bold; 
	color: #0000ff
	CURSOR: arrow; 
	}

	.baslik 
	{
    BACKGROUND-COLOR: #0099ff;
    BORDER-BOTTOM: #003399 2px solid;
    BORDER-LEFT: #99ccff 2px solid;
    BORDER-RIGHT: #003399 2px solid;
    BORDER-TOP: #99ccff 2px solid;
    COLOR: white;
    FONT-FAMILY: Verdana, Arial, Helvetica, sans-serif;
    FONT-SIZE: 11px;
    FONT-WEIGHT: bold;
    HEIGHT: 20px;
    LETTER-SPACING: 0.2pt;
    LINE-HEIGHT: 10pt;
    MARGIN: 0px;
    PADDING-TOP: 1px;
    TEXT-DECORATION: none;
    TEXT-ALIGN: center
	}
	-->
	</style>
	</HEAD>
	<BODY>
	<p class='baslik'><FONT COLOR='#FFFFFF'><B>Mevcut Üyelerimiz</B></FONT></P>
");

$veri_yolu = mysql_connect("server", "root");
mysql_select_db("veri", $veri_yolu);
$sonuc = mysql_query("SELECT * FROM calisanlar", $veri_yolu);
echo ("<TABLE BORDER='0' BORDERCOLOR='blue' CELLSPACING='7' CELLPADDING='1'>\n");
echo ("
		<TR>
			<TD class='baslik'><FONT COLOR='#FFFFFF'><B>Uzmanın Adı</B></FONT></TD>
			<TD class='baslik'><FONT COLOR='#FFFFFF'><B>Çalıştığı Yer</B></FONT></TD>
			<TD class='baslik'><FONT COLOR='#FFFFFF'><B>Görevi</B></FONT></TD>
		</TR>
	\n");
while ($satir = mysql_fetch_row($sonuc)) {
	printf("<TR><TD ALIGN='left'>%s %s</TD><TD ALIGN='left'>%s</TD></TD><TD ALIGN='left'>%s</TD></TR>\n", $satir[1], $satir[2], $satir[3], $satir[4]);
	}
echo ("

	</TABLE>\n
	<p></p>
	<p class='baslik'><FONT COLOR='#FFFFFF'><B>Siz de aramıza katılmak ister misiniz?</B></FONT></P>
	<FORM ACTION='$PHP_SELF' METHOD='POST'>
	<TABLE BORDER='0' BORDERCOLOR='blue' CELLSPACING='7' CELLPADDING='1'>
	<TR><TD class='baslik' ALIGN='left'>Adınız: </TD><TD ALIGN='left'><INPUT TYPE='TEXT' NAME='adi'></TD></TR>
	<TR><TD class='baslik' ALIGN='left'>Soyadınız: </TD><TD ALIGN='left'><INPUT TYPE='TEXT' NAME='soyadi'></TD></TR>
	<TR><TD class='baslik' ALIGN='left'>İş Yeriniz: </TD><TD ALIGN='left'><INPUT TYPE='TEXT' NAME='adres'></TD></TR>
	<TR><TD class='baslik'ALIGN='left'>Göreviniz: </TD><TD ALIGN='left'><INPUT TYPE='TEXT' NAME='pozisyon'></TD></TR>
	<TR><TD ALIGN='center'><INPUT TYPE='SUBMIT' VALUE='Defteri imzala!'></TD><TD ALIGN='center'><INPUT TYPE='RESET' VALUE='Tümünü sil!'></TD></TR>
	</TABLE>
	</FORM>
	</BODY>
	</HTML>
	");
} //else'in kapanan parantezi
?>