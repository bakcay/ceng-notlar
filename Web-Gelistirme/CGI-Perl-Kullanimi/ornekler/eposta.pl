#!/usr/bin/perl

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


&alandenetle;

sub alandenetle
{
     if($formveri{'ad'} eq "")
     {
          $ad_yok = 1;
     }
     if($formveri{'kent'} eq "")
     {
          $kent_yok = 1;
     }
     if($formveri{'ulke'} eq "Ülkeyi seçiniz")
     {
          $ulke_yok = 1;
     }
     if($formveri{'eposta'} eq "")
     {
          $eposta_yok = 1;
     }
} # alan denetimi sonu

     if($ad_yok || $kent_yok || $ulke_yok || $eposta_yok)
     {
          &hata;
          exit;
     }

     else

     {
          &epostayolla;
          &tesekkuret;
          &kaydet;
          exit;
     }


sub epostayolla
{
     $kime = "isim\@adres.com";
     open(MAIL, "|/usr/sbin/sendmail -t $kime") || die ("sendmail programýný bulamýyorum");
     print MAIL "Kimden: $formveri{'eposta'}\n";
     print MAIL "Kime: $kime\n";
     print MAIL "Konu: Ziyaretçi Formu\n\n";
     
     # Form bilgilerini kaydet
     print MAIL "Adý: $formveri{'ad'}\n";
     print MAIL "Kurum-Kuruluþ-Okul: $formveri{'kurum'}\n";
     print MAIL "Kent: $formveri{'kent'}\n";
     print MAIL "Ülke: $formveri{'ulke'}\n";
     print MAIL "E-Posta: $formveri{'eposta'}\n";
     print MAIL "Ýlgilendiði Hizmetler: $formveri{'hizmetler'}\n";
     print MAIL "Bilgi Ýstediði Konu: $formveri{'bilgi'}\n";
     print MAIL "Mesaj: $formveri{'mesaj'}\n";
     close(MAIL);     
}


sub hata
{
print "Content-type: text/html\n\n";
print "<HTML>\n";
print "<meta http-equiv=\"content-type\" content=\"text/html; charset=ISO-8859-9\">\n";
print "<meta http-equiv=\"Content-Type\" content=\"text/html; charset=windows-1254\">\n";
print "<BODY BGCOLOR=\"#FFFFFF\">\n";
print "<H3>\n";
print "Formda Eksiklikler Var\n";
print "</H3>\n";
print "<P>\n";
print "Bütün bilgileri doldurmadýnýz. Browser'ýn geri düðmesini týklayýn\n";
print "ve þu alanlarý tamamlayýn:\n\n";
print "<P>\n";
print "<B>\n";
     if($ad_yok)
     {
          print "Adýnýz\n";
          print "<BR>\n";
     }
     if($kent_yok)
     {
          print "Kent\n";
          print "<BR>\n";
     }
     if($ulke_yok)
     {
          print "Ülke\n";
          print "<BR>\n";
     }
     if($eposta_yok)
     {
          print "E-Posta Adresi\n";
          print "<BR>\n";
     }
     
     print "\n\n";
     print "</BODY>\n";
     print "</HTML>\n";

} 

# hata bitti

sub tesekkuret
{
print "Content-type: text/html\n\n";
print "<HTML>\n";
print "<meta http-equiv=\"content-type\" content=\"text/html; charset=ISO-8859-9\">\n";
print "<meta http-equiv=\"Content-Type\" content=\"text/html; charset=windows-1254\">\n";
print "<BODY BGCOLOR=\"#FFFFFF\">\n";
print "<H3>\n";
print "Teþekkür ederiz\n";
print "</H3>\n\n";
print "Verdiðiniz þu bilgiler ";
print $kime;
print " adresine gönderildi\n<P>\n";
print "Ad: $formveri{'ad'}<BR>";
print "Kurum-Kuruluþ-Okul: $formveri{'kurum'}<BR> ";
print "Kent: $formveri{'kent'}<BR>";
print "Ülke: $formveri{'ulke'}<BR>";
print "E-Posta Adresi: $formveri{'eposta'}<BR>";
print "Ýlgilendiðiniz Hizmetler: $formveri{'hizmetler'}<BR>";
print "Site Güncelleþtirildiðinde Bilgi: $formveri{'bilgi'}<BR>";
print "Mesaj: $formveri{'mesaj'}<BR>";
print "<P><BR>";
print "</BODY>\n</HTML><BR>";
}

sub kaydet
{
     open(CIKTI, ">>kayit_dosyasi.txt");
     print CIKTI $formveri{'ad'};
     print CIKTI "\t";
     print CIKTI $formveri{'kurum'};
     print CIKTI "\t";
     print CIKTI $formveri{'kent'};
     print CIKTI "\t";
     print CIKTI $formveri{'ulke'};
     print CIKTI "\t";
     print CIKTI $formveri{'eposta'};
     print CIKTI "\t";
     print CIKTI $formveri{'hizmetler'};
     print CIKTI "\t";
     print CIKTI $formveri{'bilgi'};
     print CIKTI "\t";
     print CIKTI $formveri{'mesaj'};
     print CIKTI "\n";
     close(CIKTI);
}

