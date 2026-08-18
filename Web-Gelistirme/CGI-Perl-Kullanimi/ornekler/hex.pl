print "HTTP/1.0 200 OK\n";
print "Content-Type: text/html\n\n";

print "<HTML>\n";
print "<HEAD>\n";
print "<TITLE>HEX</TITLE>\n";
print "<meta http-equiv=\"content-type\" content=\"text/html; charset=ISO-8859-9\">\n";
print "<meta http-equiv=\"Content-Type\" content=\"text/html; charset=windows-1254\">\n";
print "</HEAD>\n";
print "<BODY>\n";
print "<H4>Desimal - Heksadesimal Çevirmeni</H4>\n";

@Heksadesimal = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F');
for($i = 0; $i <= 255; $i++) {
	print sprintf("%3s", $i), "=", $Heksadesimal[int($i / 16)], $Heksadesimal[$i % 16], "  ";
	if(($i % 8) == 7) { 
	print "\n" 
	}
print "<br>\n";
}



print "</BODY>\n";
print "</HEAD>\n";
print "</HTML>\n";
 
