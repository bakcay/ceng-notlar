print "HTTP/1.0 200 OK\n";
print "Content-Type: text/html\n\n";

print "<HTML>\n";
print "<HEAD>\n";
print "<TITLE>CGI Cevre Degiskenleri</TITLE>\n";
print "<meta http-equiv=\"content-type\" content=\"text/html; charset=ISO-8859-9\">\n";
print "<meta http-equiv=\"Content-Type\" content=\"text/html; charset=windows-1254\">\n";
print "</HEAD>\n";
print "<BODY>\n";
print "<P>\n";
print "<H1>CGI Çevre Değişkenleri ve Değerleri</H1>\n";

foreach $env_var (keys %ENV) 
	{
	print "<B>$env_var</B> = $ENV{$env_var}<BR>\n";
	}

print "</BODY>\n";
print "</HEAD>\n";
print "</HTML>\n";
 