#!/usr/local/bin/perl

read (STDIN, $depo, $ENV{'CONTENT_LENGTH'});
@girdiler = split(/&/, $depo);

foreach $girdi (@girdiler) {
	($anahtar, $deger) = split (/=/, $girdi);
	$anahtar =~ tr/+/ /;
	$deger =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
	$deger =~ tr/+/ /;
	$deger =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
	
	$deger =~s/<!--(.|\n)*-->//g;
	
	if ($formveri{$anahtar}) {
		$formveri{$anahtar} .= ", $deger";
	} else {
		$formveri{$anahtar} = $deger;
	}
}

print "Content-type: text/html\n\n";
print "<meta http-equiv=\"content-type\" content=\"text/html; charset=ISO-8859-9\">\n";
print "<meta http-equiv=\"Content-Type\" content=\"text/html; charset=windows-1254\">\n";

foreach $anahtar (sort keys(%formveri)) {
	print "<P><B>$anahtar</B> alanına <B>$formveri{$anahtar} </B>değeri girildi.";
}

	
