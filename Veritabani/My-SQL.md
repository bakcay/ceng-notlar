# My SQL

**MySQL**

PHP web geliştiricileri genel olarak database tercihlerini çok rahat sql komutları yardımıyla kontrol edilebilen MySQL’den yana kullanılar. Özellikle PHP+MySQL+Apache üçlüsü performans olarak web sitelerinde performans isteyenler tarafından sıkça kullanılır. MySQL’i kullanabilmek için o an çalışıyor olması gerekir. Bunun için ms-dos komut isteminde c:\mysql\bin\ dizini altına inip orda şu komutu yazmalıyız.

```bash
:mysqld –standalone
```

Bu işlemden sonra mysql kullanıma hazır haldedir.

**MySQL'de Veritabanı işlemleri**

Ne kadar profesyonel olursanız olun, hazır yazılımlar kullanarak yapılan MySQL yönetimi hem daha hızlı hem de daha sıkıntısız olacaktır. PHP'yle geliştirilmiş olan PhpMyAdmin yazılımı kullanılarak tarayıcı penceresi içinden MySQL'le ilgili birçok işlemi gerçekleştirebilmek mümkündür. Pma’yi kullanabilmek için Apache ve Mysql çalışıyor olmalıdır.

**PhpMyAdmin'i Çalıştırma ve Tanıma**

PhpMyAdmin'i çalıştırmak için tek yapılması gereken, kurulum bölümünde anlatıldığı gibi sistemdeki Apache Web sunucusu üzerinden Web tarayıcısına http://localhost/pma/ adresini yazmaktır. Pma, güçlü bir SQL sorgulayıcısı olarak çalışabildiği gibi, veritabanı yönetimi ve bakım işlerinde de kullanılabilir. Pma'nın karşılama ekranında sol tarafta sistemde tanımlı olan veritabanlarının listesi, ortada da MySQL'in hafızadaki aktif işlemleri ve o anda yerine getirilen görevler yer alır. Sol menüde yer alan veritabanı isimleri, yeni kurulan bir MySQL kurulumu için sadece test ve mysql olarak görülecektir. Sol taraftan bu veritabanı isimlerine tıklanarak, veritabanı içinde yer alan tablolar ekranına ulaşılır. Aynı zamanda, sol tarafta da veritabanının altındaki tabloların isimleri belirecektir. Ortadaki pencerede yer alan metin alanına SQL cümlecikleri yazılarak, veritabanından Pma aracılığıyla sorgu gönderilerek cevaplarım aynı şekilde Pma'dan tarayıcı vasıtasıyla görmek de mümkündür. Sol menüdeki tablo isimlerine tıklanarak, tabloların içinde yer alan alanlar hakkında ayrıntılı bilgiye erişilebilir.

**PhpMyAdmin ile Database Oluşturma**

Pma’yi calıştırdığınızda karşınıza gelecek olan sağ frame’de yer alan create new database bölümüne oluşturulması istenilen database adı yazılarak create tuşuna basılarsa database oluşturulacaktır. Fiziksel olarak elimizde şu an bir database olmuş olacaktır.

**PhpMyAdmin ile Tablo Oluşturma**

Eğer database sorunsuz olarak oluşturulursa sağ frame’de karşımıza bir sql sorgu metin kutusu bir de manual olarak table oluşturmamıza yarayacak olan “Create new table on database ...” bölümü yer alacaktır. Eğer direkt sql olarak tablo oluşturulacak ise Create Table ile Run sql query bölümünden tablo oluşturmak mümkündür. Yada “Create new table on database...” yazan bölüme tablo adı ve kaç alandan oluşacağı yazılarak kaç alandan oluşacaksa belirtilerek wizard mantığı ile oluşturmak mümkündür.

Mesela run sql query bölümünde bir tablo oluşturalım.

```sql
CREATE TABLE isim (
ad VARCHAR (10) not null ,
soyad VARCHAR (10) not null ,
posta VARCHAR (50) not null
)
```

**“Your SQL-query has been executed successfully“ **şeklinde bir yanıt alınırsa tablo sorunsuz olarak oluşturulmuş demektir.

Eğer “Create new table on database “ bölümü secilirse burda tablo adı belirtilir kaç alan kullanılacak belirtilerek aynı tablo oluşturulabilir. Fakat sql cümlecikleri nispeten işimizi kolaylaştırır.

Sağ frame’in en alt bölümünde yer alan “drop database” linki database silmek için kullanılır.

Tablo oluşturulurken kullanılan bazı alan türleri:

**Int:** Sayısal veri tipidir. Negatif ve pozitif değerler alabilir.

**Char(değer):** değer büyüklüğünde string ifade saklanabilecek tiptir.

**Varchar(değer):** değer büyüklüğünde string ifade saklanabilecek tiptir. Değişken boyutta olabilir.

**Date:** Tarih bilgisini tutan tiptir.

**Time:** Zaman bilgisini tutan tiptir.

**DateTime:** Tarih ve zaman bilgisini bir arada tutan tiptir.

**Timestamp:** O anki tarih ve saat bilgisini tutan tiptir.

**Enum(değer1,değer2,..,değerN):** Metin olarak aynı anda doğru olamayacak bilgileri depolar.

**Set(değer1,değer2,..,değerN):** Enum tipine benzer, ancak birden çok değeri aynı anda alabilir.

Bu alanlar dışında mevcut bazı tiplerde vardır. Fakat en sık kullanılan tipler bunlardır. Eğer bu tipleri incelemek isterseniz mysql manual’ini incelemeniz yeterli olacaktır.

Bir Database’nin Desenini Almak

Bir databasenin desenini almak demek o database’in başka yerde kullanılabilmesi için sql şekline tablolarının çevrilmesidir. İki şekilde alınabilir. Pma’da herhangi bir database’i sol frame’den seçip sağ frame’de “View dump (schema) of database” bölümünü kullanabiliriz. Burada 3 seçenek vardır.

Burada ;

Structure only: Sadece alanları ve tabloları tutar.

Structure and data: Hem alanları hemde alanlara kayıtlı verileri tutar.

Data only: Sadece tablolara kayıtlı alanları tutar.

Eğer herhangi birini secip sorunsuz şekilde çalışırsa karşımıza söyle bir görüntü gelir.

```sql
CREATE TABLE `isim` (
`ad` varchar(10) NOT NULL default '',
`soyad` varchar(10) NOT NULL default '',
`posta` varchar(50) NOT NULL default ''
) TYPE=MyISAM;
```

Eğer bunu herhangi bir text dosyasına kaydedip saklarsanız ilerde tekrar oluşturmaya gerek kalmadan direkt database oluşturulduktan sonra PhpMyAdmin’deki “Run sql query” bölümü kullanılarak tablo oluşturulabilir.

**SQL **

MySQL ile işlem yapabilmek için mutlaka ki sql dilini işimize yarayacak kadar bilmeliyiz. Bunun için çok sık kullanacağımız bazı sql deyimlerine burada değinmemiz gerekmektedir.

**Select Deyimi**

Bir tablodan kayıt çekmek için select deyimi kullanılır.

Kullanım şekli:

```sql
Select (alan adi) from (tablo adı);
```

Örnekler:

```sql
Select * from isim;
```

İsim adlı tablodaki tüm kayıtları çeker.

**Where Deyimi:**

Sql cümleciği içinde arama kriteri belirtmek için kullanılır.

Kullanım şekli:

```sql
DELETE [Alan Adi] FROM [Tablo Adı] WHERE [Seçilen Kriter]
SELECT [Alan Adi] FROM [Tablo Adı] WHERE [Seçilen Kriter]
UPDATE [Tablo Adi] SET [Yeni Değer] WHERE [Seçilen Kriter]
```

Örnekler:

```sql
Select * from isim where adi=’murat’;
```

adi=’murat’ olan kayitlari tablodan çeker.

```sql
Select * from dene where plaka>60;
```

Dene tablosundaki plaka alanı 60’dan büyük olan kayıtları çeker.

**Group By Deyimi:**

Tablodan çekilen kayıtları belli kriterlere göre sıralamak için kullanılır.

Kullanım şekli:

```sql
SELECT [Alan Adi] FROM [Tablo Adı] WHERE [Seçilen Kriter] Group By [Alan Adı];
```

Örnekler:

```sql
Select * from isim group by ad;
```

İsim adlı tablodaki tüm kayıtlar çekilir bu sırada ad alanına göre’de sıralanırlar.

**Order By Deyimi:**

Tablodan çekilen alanları sıralamak için kullanılır. Group by deyimi ile benzer yapıdadırlar.

Kullanım Şekli:

```sql
SELECT [Alan Adi] FROM [Tablo Adı] WHERE [Seçilen Kriter] Order By [Alan Adı];
```

Örnekler:

```sql
Select ad from isim order by ad;
```

İsim adlı tablodan ad alanı çekilerek gene ad alanına göre sıralanıyor.

**And ve Or Deyimleri:**

Where kalıbını kullanırken birden çok kritere göre cümle yazılması gereken durumlarda kullanılır.

Kullanım Şekli:

```sql
... where kriter1 and kriter2
... where kriter1 or kriter2
```

Örnekler

```sql
Select * from isim where adi=’ali’ and soyadi=’mehmet’;
```

İsim adlı tablodan adı ali ve soyadı mehmet olan tüm kayıtlar çekilir.

```sql
Select * from isim where adi=’ali’ or adi=’mehmet’;
```

İsim adlı tablodan adi ali veya mehmet olan tüm kayıtlar çekilir.

**Like Deyimi:**

Where kalıbı içerisinde kullanılan bu yapı bir alan içindeki kayıtlarda baş harfe veya belli yere kadar olan harf veya harflere göre arama yapmak gibi işlerde işimize yarayabilir.

Kullanım Şekli:

```sql
... where alan adı like kriter
```

Örnekler:

```sql
Select * from egg where renk like “%a?ı”;
```

Burada egg isimli tablodan renk alanına göre ilk başı önemli olmayan sonunda 3 harfinden ilki a sonraki önemli olmayan son harfi de ı olan tüm kayıtlar çekilir. Mesela “ayarı” gibi bir kayıt olsa bu kritere uyacaktır.

```sql
Select * from egg where renk like “be%”;
```

Burada egg isimli tablodan renk alanına göre ilk iki harfi be olan tüm kayıtlar çekilecektir.

**Insert Into Deyimi:**

Bir tabloya kayit eklemek için kullanılır.

Kullanım şekli:

```sql
Insert Into Tablo adı (alan1,alan2,..,alanN) values (‘değer1’, ‘değer2’,.., ‘değerN’);
```

Örnekler:

```sql
Insert Into isim (ad,soyad) values (‘ali’,’rizeli’);
```

İsim adlı tabloya sadece ad ve soyad alanlarına olmak üzere kayıt yapar.

```sql
Insert Into isim values (‘ali’,null,’ali@rizeli.com’);
```

Bu kullanım şeklinde alanlar belirtilmediğinden tüm alanların değeri belirtilmek zorundadır. Eğer girilecek alanlar belirtilmiş olsa idi boş kayıtlar belirtilmek zorunda kalmazdı.

**Update Deyimi**

Bir alanı güncellemek için kullanılır.

Kullanım şekli:

```sql
Update [Tablo Adı] Set alan=yeni deger Where aranan alan= alan değeri
```

Örnekler:

```sql
Update isim set ad=’murat’ where soy=’yüce’;
```

Soyadı yüce olan kayıtların adını murat yapar.

```sql
Update isim set posta=’a@b.net’ where ad=’murat’ or soy=‘yüce’;
```

Ad değeri murat veya soy değeri yüce olan kayıtların posta alanını a@b.net olarak günceller.

**Delete Deyimi**

Arama şartı belirtilen kayıtları siler.

Kullanım şekli:

```sql
Delete * From [tablo] where arama şartı;
```

Örnekler:

```sql
Delete * from isim where adi=’murat’;
```

Adi alani murat olan tüm kayitlari siler.

```sql
Delete * from isim where posta=null;
```

Posta alanı boş olan tüm kayıtları siler.

**MySQL ve PHP **

Yukarıda MySQL’i php’den bağımsız nasıl kullanabileceğimizi ve de MySQL ile PHP arasında bağlantıyı kuracak olan SQL’e birazda olsun değindik. Fakat genel manada yukarıdaki bilgiler yeterli olmayabilir. Bu durumda MySQL manual’i ve SQL referanslarına internetten ulaşabilir. Daha geniş bilgilere ulaşabilirsiniz. Şimdi mysql ile php arasındaki bağlantılar ve komutları görelim:

**mysql_connect() deyimi(Databese bağlantısı)**

Php ile mysql ile bağlantıyı sağlayan komuttur. Kullanım şekli ise

```php
mysql_connect(“adres”,“kullanici”,”şifre”);
```

genel olarak mysql kurulduğunda kullanıcı tanımlanmamış ise tek kullanıcı vardır. Bu kullanıcı “root”dur. Ve şifresi boş geçilecektir. Adres bölümüne ise eğer kendi makinemizde kullanıyorsak localhost yazarız. Buna göre bağlantı için:

```php
mysql_connect(“localhost”,”root”,””);
```

şeklinde bir cümlecik eğer mysql çalışıyor ise bağlantı için yeterlidir.

**mysql_select_db() deyimi**

Eğer mysql ile bağlantı kurulmuş ise o an çalışılacak veritabanı adı belirtilme ve seçilmelidir. Bu işe için mysql_select_db(); komutu kullanılır. Kullanım şekli:

```php
mysql_select_db(“veritabanı adı”);
```

şeklindedir.

**PHP kullanarak mysql’e sorgu göndermek**

PHP'de MySQL'e sorgu göndermek için mysql_query() komutu kullanılır. Parantez içinde tırnak arasında sql sorgusu veya daha önce sql olarak hazırlanmış değişken yazılabilir. Örneğin:

```php
$sorgu=”select * from phpisbest”;
$islem=mysql_query($sorgu);
```

veya

```php
$islem=mysql_query(“select * from phpisbest”);
```

aynı işlemi yapar.

Kaç tane kayıt geldiğini öğrenmek için mysql_numrows() komutu kullanılır. Bu daha sonra sorgudan gelen kayıtları almak işimize yarayacaktır.

```php
$kac=mysql_numrows($islem);
```

yukarıdaki sorgudan kaç tane kayıt geldiğini bize verecektir. Eğer sorgudan gelen kayıtları değişkenlere almak istiyorsak bunun icinde mysql_result() komutu kullanılır. M

Mesela yukarıdaki sorgudan php ve asp diye iki alan geldiğini düşünelim burdan gelen tüm kayıtları ayrı ayrı iki değişkene aktaralım.

```php
$i=0;
while($i<$kac):
$asp[]=mysql_result($islem,$i,”asp”);
$php[]=mysql_result($islem,$i,”php”);
$i++;
endwhile;
```

Yukarıda $i değişkeni sorgudan gelen sonuçları alırken kullandığımız tampon değişkendir. Sırası ile her sıradaki asp ve php alanlarındaki kayıtlar $asp ve $php isimli iki dizi değişkene aktarıyor. Böylece mysql’de yer alan yaptığımız sorgu ile alakalı tüm kayıtlar artık php’nin içine aktarılmıştır. **Bunları ekrana dökmek için:**

```php
for($j=0;$j<$kac;$j++):
echo $asp[j].” “.$php[j].”<br>”;
endfor;
```

şeklinde kısa bir döngü kullanılabilir. Tabii ki bunu html kullanarak daha görsel hale getirmek mümkündür.

Php’den gelen değişkenleri de sorgularda kullanmamız mümkündür. Mesela $ad diye bir değişken gelecek ve bu değişkenin ad, soyad ve eposta bilgileri ekrana yazılacaktır. Kullanılan database isimler olsun isim adlı bir tablo kullanılsın. Örneğin aşağıda dökelim:

```php
<?
$host = “localhost”;
$user = “root”;
$pass = “”;
$database = “isimler”;
/* Daha dinamik bir program yapısı olması açısından bu şekilde tanımlamalar ile kullanmak ileride değişikliler yapıldığında işimizi kolaylaştıracaktır*/
mysql_connect($host,$user,$pass)
mysql_select_db($database);
$sorgu = “select ad,soyad,eposta from isim where ad=’$ad’”;
$islem = mysql_query($sorgu);
$kac = mysql_numrows($islem);
$i=0;
while($i<$kac):
$isim = mysql_result($islem,$i,”ad”);
$soyisim = mysql_result($islem,$i,”soyad”);
$posta = mysql_result($islem,$i,”eposta”);
echo”ad: $isim <br> soyad: $soyisim<br> eposta: $posta<br><br><br>”;
$i++;
endwhile;
?>
```

**MySQL’de hata kontrolü**

Kullanıcının MySQL'de oluşabilecek hataları PHP içinde fark edebilmesi için, PHP'de özel komutlar vardır. Bu komutlar sayesinde veritabanı sorgulamasında oluşan sonuçlar hata numarasıyla birlikte fark edilebilir. Hata gösterge komutları kullanılmadan PHP, MySQL'e dair hiçbir hata mesajı vermeden işleme devam eder.

```php
if (mysql_error())
{
echo ("MySQL hatası oluştu. Hata: ");
echo mysql_error() ;
}
```

Yukarıdaki PHP satırları mysql_error() komutunu kullanarak herhangi bir MySQL hatası oluştuğunda ekrana MySQL hatasının yazılmasını ve PHP yazılımcısının uyarılmasını sağlar.

Örnek Uygulama:

Web sitelerinde sık sık gördüğünüz şifreli giriş sayfalarından biri. Önce bir database oluşturmamız gerekiyor. Pma yardımıyla giris adlı bir veritabanı oluşturalım. Bundan sonra karşımıza gelen pencerede “run sql query” yazı kutusuna aşağıdaki sql’i paste edin.

```sql
CREATE TABLE `kisi` (
`kullanici` varchar(8) NOT NULL default '',
`sifre` varchar(8) NOT NULL default '',
`adi` varchar(20) NOT NULL default '',
`soyadi` varchar(15) NOT NULL default '',
`email` varchar(40) NOT NULL default '',
`cinsiyet` enum('e','k') NOT NULL default 'e',
`songiris` timestamp(14) NOT NULL,
`suan` enum('0','1') NOT NULL default '0'
) TYPE=MyISAM;
```

daha sonra dosyalarımızı sırasıyla dosyalarımız oluşturalım. İlk önce sabitlerin saklandığı sabit sayfası:

**sabit.php**

```php
<?
$server ="localhost";
$user ="root";
$pass ="";
$database ="giris";
?>
```

/*****************************************************************/

**index.php**

```php
<?
include "kontrol.php";
if($kontrol==1):
header("Location: sayfa.php");
else:
?>
<html>
<head>
<title>PHP&MySQL Giriş Sayfası</title>
<meta http-equiv="Content-Type" content="text/html; charset=">
</head>
<body bgcolor="#FFFFFF" text="#000000">
<SCRIPT>
function submitChange()
{
var theForm = document.giris;

if ( theForm.kullanici.value.length == 0 ) {
alert( 'Lütfen bir kullanıcı ismi giriniz!' );
theForm.kullanici.focus();
return;
}

if ( theForm.sifre.value.length == 0 ) {
alert( 'Lütfen şifre giriniz!' );
theForm.sifre.focus();
return;
}

theForm.submit();
}
</SCRIPT>
<center>
<b><font face="Verdana, Arial, Helvetica, sans-serif" size="2">Kullanıcı Girişi
</font></b>
<form name="giris" method="post" action="gir.php">
<table width="223" border="0" cellspacing="1" cellpadding="1">
<tr>
<td width="115"><font face="Verdana, Arial, Helvetica, sans-serif" size="2">Kullanıcı
Adı</font></td>
<td width="101"> <font face="Verdana, Arial, Helvetica, sans-serif" size="2">
<input type="text" name="kullanici" size="10" maxlength="8" value="<? echo $kullanici?>">
</font></td>
</tr>
<tr>
<td width="115"><font face="Verdana, Arial, Helvetica, sans-serif" size="2">Şifre</font></td>
<td width="101"> <font face="Verdana, Arial, Helvetica, sans-serif" size="2">
<input type="password" name="sifre" size="10" maxlength="8">
</font></td>
</tr>
</table>
<p>
<input type="button" onClick="submitChange()" value="Giriş" >
</p>
</form>
</center>
<br>
<br>
<br>
<center><a href=kaydet.php>Kullanıcı Kayıt</a></center>
</body>
</html>
<?
endif;
mysql_close()
?>
```

/*****************************************************************/

**kaydet.php**

```html
<html>
<head>
<title>Kullanıcı Kayıt Sayfası</title>
<meta http-equiv="Content-Type" content="text/html; charset=">
</head>

<body bgcolor="#FFFFFF" text="#000000">
<center>
<p><font face="Verdana, Arial, Helvetica, sans-serif" size="2"><b>Kullanıcı
Kayıt Sayfası</b></font></p>
<form name="form1" method="post" action="kayit.php">
<table width="337" border="0" cellspacing="1" cellpadding="1">
<tr valign="middle">
<td width="93">
<div align="right"><b><font face="Verdana, Arial, Helvetica, sans-serif" size="2">Lakap</font></b></div>
</td>
<td width="25">&nbsp; </td>
<td width="209"><font size="2">
<input type="text" name="kullanici" size="10" maxlength="8" value="<?echo $kullanici?>">
</font></td>
</tr>
<tr valign="middle">
<td width="93" height="2">
<div align="right"><b><font size="2" face="Verdana, Arial, Helvetica, sans-serif">Sifre</font></b></div>
</td>
<td width="25" height="2">&nbsp; </td>
<td width="209" height="2"><font size="2">
<input type="password" name="sifre1" size="10" maxlength="8">
</font></td>
</tr>
<tr valign="middle">
<td width="93" height="17">
<div align="right"><b><font size="2" face="Verdana, Arial, Helvetica, sans-serif">Tekrar</font></b></div>
</td>
<td width="25" height="17">&nbsp; </td>
<td width="209" height="17"><font size="2">
<input type="password" name="sifre2" size="10" maxlength="8">
</font></td>
</tr>
<tr valign="middle">
<td width="93">
<div align="right"><b><font size="2" face="Verdana, Arial, Helvetica, sans-serif">İsim</font></b></div>
</td>
<td width="25">&nbsp; </td>
<td width="209"><font size="2">
<input type="text" name="adi" size="25" maxlength="20" value="<?echo $adi?>">
</font></td>
</tr>
<tr valign="middle">
<td width="93">
<div align="right"><b><font size="2" face="Verdana, Arial, Helvetica, sans-serif">Soyisim</font></b></div>
</td>
<td width="25">&nbsp; </td>
<td width="209"><font size="2">
<input type="text" name="soyadi" size="25" maxlength="25" value="<?echo $soyadi?>">
</font></td>
</tr>
<tr valign="middle">
<td width="93">
<div align="right"><b><font size="2" face="Verdana, Arial, Helvetica, sans-serif">E-mail</font></b></div>
</td>
<td width="25">&nbsp; </td>
<td width="209"><font size="2">
<input type="text" name="email" size="30" maxlength="40" value="<?echo $email?>">
</font></td>
</tr>
<tr valign="middle">
<td width="93">
<div align="right"><b><font size="2" face="Verdana, Arial, Helvetica, sans-serif">Cinsiyet</font></b></div>
</td>
<td width="25">&nbsp; </td>
<td width="209"><font size="2"> <font face="Verdana, Arial, Helvetica, sans-serif">
<input type="radio" name="cinsiyet" value="e" <? if($cinsiyet=="e") echo checked?>>
Erkek<br>
<input type="radio" name="cinsiyet" value="k" <? if($cinsiyet=="k") echo checked?>>
Kız </font></font></td>
</tr>
</table>
<br>
<input type="submit" name="Submit" value="Submit">
<input type="reset" name="Submit2" value="Reset">
</form>
<p>&nbsp; </p>
</center>
</body>
</html>
```

/*****************************************************************/

**kayit.php**

```php
<?
include"sabit.php";

if (($sifre1==$sifre2) && ($kullanici) && ($adi) && ($soyadi) && ($email) && ($cinsiyet)):
mysql_connect($server,$user,$pass);
mysql_select_db($database);
$sorgu="SELECT kullanici from kisi";
$ids=mysql_query($sorgu);
$i=0;
while($i<mysql_numrows($ids)):
$id = mysql_result($ids,$i,"kullanici");
$i++;
if($kullanici==$id):
echo"<center>Kullanici adı mevcut</center>";
include "kaydet.php";
die();
endif;
endwhile;
$sorgu = "INSERT INTO kisi values ('$kullanici','$sifre1','$adi','$soyadi','$email','$cinsiyet','','0')";
mysql_query($sorgu);
mysql_close();
echo "<center>Kullanıcı Kaydı Tamamlandı</center><br>";
include "index.php";
else:
echo"<center>Lütfen tüm alanları doldurunuz!</center><br>";
include "kaydet.php";
endif;

?>
```

/*****************************************************************/

**gir.php**

```php
<?
if( $kullanici && $sifre ):
include "sabit.php";

mysql_connect($server,$user,$pass);
mysql_select_db($database);

$sorgu="select * from kisi where kullanici='$kullanici'";
$bul=mysql_query($sorgu);
$sayi=mysql_numrows($bul);
if ( $sayi == 0 ):
$hata=2;
mysql_close();
include "hata.php";
die();
endif;
if ($sayi == 1 ):
$el=mysql_result($bul,0,sifre);
if ( $el != $sifre ):
$hata=1;
mysql_close();
include "hata.php";
die();
endif;
if ( $el == $sifre ):
setcookie("kim","$kullanici");
$sorgu1="update kisi set suan='1' where kullanici='$kullanici'";
mysql_query($sorgu1);
mysql_close();
@header ("Location: sayfa.php");
endif;
endif;
else:
@header("Location: sayfa.php");
endif;
?>
```

/*****************************************************************/

**logout.php**

```php
<?
if( $kullanici && $sifre ):
include "sabit.php";

mysql_connect($server,$user,$pass);
mysql_select_db($database);

$sorgu="select * from kisi where kullanici='$kullanici'";
$bul=mysql_query($sorgu);
$sayi=mysql_numrows($bul);
if ( $sayi == 0 ):
$hata=2;
mysql_close();
include "hata.php";
die();
endif;
if ($sayi == 1 ):
$el=mysql_result($bul,0,sifre);
if ( $el != $sifre ):
$hata=1;
mysql_close();
include "hata.php";
die();
endif;
if ( $el == $sifre ):
setcookie("kim","$kullanici");
$sorgu1="update kisi set suan='1' where kullanici='$kullanici'";
mysql_query($sorgu1);
mysql_close();
@header ("Location: sayfa.php");
endif;
endif;
else:
@header("Location: sayfa.php");
endif;
?>
```

/*****************************************************************/

**sayfa.php**

```php
<?
include "kontrol.php";
if ( $kontrol == 1 ):
echo "<center>Gizli bölüm</center>";
echo "<br><br><a href=logout.php><center>logout</center></a>";
echo "<br><a href=sil.php><center>sil</center></a>";
else:
include "hata.php";
endif;
mysql_close()
?>
```

/*****************************************************************/

**sil.php**

```php
<?
include "kontrol.php";
if ( $kontrol == 1 ):
echo $ok;
$sorgu="delete from kisi where kullanici='$ok'";
$islem=mysql_query($sorgu);
echo "<center>İşlem Tamamlandı</center>";
echo "<br><br><center><a href=index.php>Ana Sayfa</a></center>";
else:
include "hata.php";
endif;
mysql_close()
?>
```

/*****************************************************************/

**kontrol.php**

```php
<?
include"sabit.php";

$ok = $HTTP_COOKIE_VARS["kim"];
$hata = 3;

mysql_connect($server,$user,$pass);
mysql_select_db($database);

$sorgu = "select * from kisi where kullanici='$ok' and suan='1'";
$bul = mysql_query($sorgu);
$dogru = mysql_numrows($bul);
if ($dogru == 1):
$kontrol = 1;
else:
$kontrol = 0;
endif;
?>
```

/*****************************************************************/

**hata.php**

```php
<?
if($hata==1):
echo"<Center><Font Face=Verdana Size=1 Color=Red><b>Hatalı Şifre...</b></font></center><br><br>";
include "index.php";
exit ;
endif ;
if($hata==2):
echo"<Center><Font Face=Verdana Size=1 Color=Red><b>Kullanıcı Kayıtlı Değil...</b></font></center><br><br>";
include "index.php";
exit ;
endif ;
if($hata==3):
echo"<Center><Font Face=Verdana Size=1 Color=Red><b>Login olmalısın...</b></font></center><br><br>";
include "index.php";
exit ;
endif ;
if(!($hata) or ($hata<1 or $hata>3)):
echo"<Center><Font Face=Verdana Size=1 Color=Red><b>Hata...</b></font></center><br><br>";
include "index.php";
exit ;
endif ;
?>
```

---
*Kaynak: `MY SQL/MY SQL.doc` — Murat Yüce — 2004*
