#!/usr/local/bin/perl

print "Content-type: text/html\n\n";
print "<meta http-equiv=\"content-type\" content=\"text/html; charset=ISO-8859-9\">\n";
print "<meta http-equiv=\"Content-Type\" content=\"text/html; charset=windows-1254\">\n";
print "<H3><CENTER>Dizindeki dosyalar</CENTER></H3>\n";

opendir (DIZIN, ".");
while($dosya_adi = readdir(DIZIN)) {
	if ($dosya_adi =~ /^\w*.htm/){
	push(@dosyalar, $dosya_adi);
	print "<A HREF=\"$dosya_adi\"> $dosya_adi </A>\n";
	print "<BR>\n";

	}
}
closedir(DIZIN);
