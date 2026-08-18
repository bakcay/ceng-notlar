#!/usr/local/bin/perl

print "Content-type: text/html\n\n";
print "<meta http-equiv=\"content-type\" content=\"text/html; charset=ISO-8859-9\">\n";
print "<meta http-equiv=\"Content-Type\" content=\"text/html; charset=windows-1254\">\n";
print "<H3><CENTER>Teşekkürler</CENTER></H3>\n";

opendir (DIZIN, ".");
foreach $dosya_adi (sort (readdir(DIZIN))) {
	print "$dosya_adi\n";
	print "<BR>\n";
}
closedir(DIZIN);

