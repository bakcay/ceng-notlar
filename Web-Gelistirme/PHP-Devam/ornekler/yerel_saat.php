<HTML>
<HEAD>
<TITLE>PHP'de Yerel saat</TITLE>
<meta http-equiv="content-type" content="text/html; charset=ISO-8859-9">
<meta http-equiv="Content-Type" content="text/html; charset=windows-1254">
</HEAD>
<BODY>


<?php 
setlocale ("LC_TIME", "TR");
print (strftime ("Türkçe bugün günlerden: %A "));
?>

</BODY>
</HTML>