<HTML>
<TITLE>PHP ile Veri Örnegi</TITLE>
<meta http-equiv="content-type" content="text/html; charset=ISO-8859-9">
<meta http-equiv="Content-type" content="text/html; charset=windows-1254">
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
    CURSOR: hand;
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
<?php

$veri_yolu = mysql_connect("server", "root");
mysql_select_db("veri", $veri_yolu);
$sonuc = mysql_query("SELECT * FROM calisanlar", $veri_yolu);
echo ("<TABLE BORDER='0' BORDERCOLOR='blue' CELLSPACING='7' CELLPADDING='1'>\n");
echo ("
		<TR>
			<TD class='baslik'><FONT COLOR='#FFFFFF'><B>Uzmanın Adı:</B></FONT></TD>
			<TD class='baslik'><FONT COLOR='#FFFFFF'><B>Görevi:</B></FONT></TD>
		</TR>
	\n");
while ($satir = mysql_fetch_row($sonuc)) {
	printf("<TR><TD ALIGN='left'>%s %s</TD><TD ALIGN='left'>%s</TD></TR>\n", $satir[1], $satir[2], $satir[3]);
	}
echo ("</TABLE>\n");

?>

</BODY>
</HTML>