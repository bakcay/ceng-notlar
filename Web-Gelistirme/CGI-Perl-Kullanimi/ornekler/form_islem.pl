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
open (EKLE, ">>form_bilgileri.txt");


foreach $anahtar (sort keys(%formveri)) {
if ($anahtar ne "Gonder") {
	print EKLE "$formveri{$anahtar}\t";
}
}
	print EKLE "\n";

close(EKLE);
	
print "Content-type: text/html\n\n";
print "<meta http-equiv=\"content-type\" content=\"text/html; charset=ISO-8859-9\">\n";
print "<meta http-equiv=\"Content-Type\" content=\"text/html; charset=windows-1254\">\n";
print "<H3><CENTER>Teşekkürler</CENTER></H3>\n";
print "<P>Sayın $formveri{Adi}\n";
print "<BR>$formveri{Adres} $formveri{Kod} \n";
print "<P>Sitemizi ziyaret ettiğiniz ve formumuzu doldurduğunuz için size teşekkür ederiz!\n";
print "<BR>Size<B> $formveri{Merak} </B>alanında daha iyi hizmet etmek için çaba göstereceğiz.\n";
print "<BR>Adınızı ve<B> $formveri{eposta} </B>şeklindeki elektronik adresinizi tanesi 250 bine kimseye satmayacağımıza söz veriyoruz.\n";
print "<P>Ana sayfamıza geri dönmek için burayı <A HREF=\"index.htm\">tıklayınız</A>.\n";

