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

$Uzuuun_metin = <<"uzun_metin";
İnsanoğluna en çok güç veren unsurların başında sevilmek gelir.
Fakat kişinin sevildiğini kabul etmesi zordur;
hele herşeyin çıkara dayandığı çağımızda,
karşılıksız sevgiyi görünce tanımak, tanıyınca kabul etmek
hiç de kolay olmuyor.
--Immanuel L'Avanger
uzun_metin

print $Uzuuun_metin;


print "</BODY>\n";
print "</HEAD>\n";
print "</HTML>\n";
 
