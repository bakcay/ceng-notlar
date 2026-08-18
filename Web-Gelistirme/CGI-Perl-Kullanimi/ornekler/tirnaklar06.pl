print "HTTP/1.0 200 OK\n";
print "Content-Type: text/html\n\n";

print "<HTML>\n";
print "<HEAD>\n";
print "<TITLE>MERHABA DÜNYA</TITLE>\n";
print "<meta http-equiv=\"content-type\" content=\"text/html; charset=ISO-8859-9\">\n";
print "<meta http-equiv=\"Content-Type\" content=\"text/html; charset=windows-1254\">\n";
print "</HEAD>\n";
print "<BODY>\n";
print "<H4>Tek tırnak çift tırnak farkı</H4>\n";

$Metin1 = 'Merhaba Dünya';
print qq/$Metin1..  Sana da merhaba ey ademoğlu!/;


print "</BODY>\n";
print "</HEAD>\n";
print "</HTML>\n";
 
