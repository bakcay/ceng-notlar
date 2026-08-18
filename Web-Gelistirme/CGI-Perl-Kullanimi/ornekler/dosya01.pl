print "HTTP/1.0 200 OK\n";
print "Content-Type: text/html\n\n";

print "<HTML>\n";
print "<HEAD>\n";
print "<TITLE>Tekrarlama</TITLE>\n";
print "<meta http-equiv=\"content-type\" content=\"text/html; charset=ISO-8859-9\">\n";
print "<meta http-equiv=\"Content-Type\" content=\"text/html; charset=windows-1254\">\n";
print "</HEAD>\n";
print "<BODY>\n";
print "<H4>Dosya Aç</H4>\n";
print "<p>\n";
open (DOSYA, "ornek.txt") || &Hata;
$satir1 = <DOSYA>;
print $satir1;
print "<p>\n";
sub Hata {
print "Bir hata oldu; dosya açılmıyor. Ya bu dosya yok, ya da biz Perl’ü yazarken bir hata yaptık!\n";
print "Çok özür dileriz.. Şurayı tıklayın da bari başka bir tarafa gidin!\n";
print "<A HREF=\"baska_bir_taraf.htm\">Tıklayın!</A>\n";
exit
}
print "</BODY>\n";
print "</HEAD>\n";
print "</HTML>\n";
 
