#!/usr/local/bin/perl
# isim-yas.pl
require 'cgi-lib.pl'

&ReadParse(*girdi);
print "Content-Type: text/html\r\n\r\n";
print "<HTML>\n";
print "<HEAD>\n";
print "<TITLE>ISIM-YAS</TITLE>\n";
print "<meta http-equiv=\"content-type\" content=\"text/html; charset=ISO-8859-9\">\n";
print "<meta http-equiv=\"Content-Type\" content=\"text/html; charset=windows-1254\">\n";
print "</HEAD>\n";
print "<BODY>\n";
print "<P>\n";
print "Merhaba, " . $girdi{'isim'} . ". Sen\n";
print $girdi{'yas'} . " yaşındasın.<p>\n";
print "</BODY>\n";
print "</HEAD>\n";
print "</HTML>\n";
