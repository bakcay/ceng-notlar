# Mikrokontrolör Ve Çalişma Esaslari

**68HC11 - 8051 MİKROKONTROLÖR VE ÇALIŞMA ESASLARI**

**68HC11 MİKROKONTROLÖR:**

68HC11 önceki 68xx (6801, 6805, 6809)’lara benzer komut setiyle Motrola’nın 8-bit veri , 16-bit adres mikrokonrolörüdür. Yeterli çeşitlilikte 68HC11 üretilmiştir, EEPROM/OTPROM, RAM, dijital I/O, zamanlayıcı (timers), A/D dönüştürücü (converter), PWM jeneratör, ve senkron/asenkron iletişim kanalları (RS232 ve SPI). Tipik akım çekme 10mA den az.

**Mimari**

68HC11 düşük güç tüketimi ve yüksek performanslı işlemlerde 4 MHz’in üzerinde yol (bus) frekansı ile optimumdur. CPU’nun iki tane 8-bit akümülatörü (A&B) vardır. İki tane 16-bit indeks (X&Y) kaydedicisi vardır , bunlar belleğin herhangi bir yerini indekslemeyi sağlar. İki tane indeks kaydedicisine sahip olması 68HC11’in veri işlemede çok iyi olmasını sağlar. 8-bit işlemci olmasına rağmen 68HC11 bazı 16-bit komutlara da sahiptir (add, subtract, 16 \* 16 divide, 8 \* 8 multiply, shift, ve rotates). 16-bit yığın göstericisi ve yığın işlemeyi sağlayan komutları vardır. Tipik olarak çoklu adres ve veri yolu vardır.

Diğer özellikleri:

• Etkili bit işleme komutları

• 6 etkili adres modu (Immediate, Extended, Indexed, Inherent and Relative)

• Etkili koruma DUR ve BEKLE modu

• Bellek haritalama I/O ve özel fonksiyonlar

**Bellek**

M68HC11 ailesi mikrokontrolör bellek teknolojisinde liderdir. Hatta, 68HC711E9 EPROM ve EEPROM teknolojilerini aynı çipte birleştiren ilk araçtır. Birçok uygulamada, M68HC11 maske programlı ROM veya kullanıcı tarafından programlanabilir. EPROM’la birlikte tek çipli çözüm sunar.

M68HC11 ailesinin RAM’i tam statik bir tasarım içerir ve içindekiler işlemci inaktif durumdayken bile muhafaza edilir.

M68HC11 araçlarının tek zamanlı programlanabilir (OTP) ve pencereli EPROM versiyonları küçük hacimli prototipler için ve geliştirme amacıyla ekonomik, kullanıcı tarafından programlanabilir bir ROM imkanı sunar. Güvenli EPROM araçları, kodun tehlikede olduğu uygulamalar için de elverişlidir.

M68HC11’in EEPROM’u gerekli kalibrasyon, tanı ve güvenlik bilgisinin emniyetli bir şekilde saklanması için idealdir.

Bazı araçlardaki 4 kanallı Doğrudan Belleğe Erişim (DMA) birimi iki bellek bloğu arasında (genişletilmiş moddaki dıştan eşlenmiş bellek dahil), kaydediciler arasında veya kaydediciler ve bellek arasında hızlı veri transferi sağlar.

**Zamanlayıcı (Timer)**

Endüstri standartlarına sahip M68HC11 zamanlayıcısı esneklik, performans ve kullanım kolaylığı sağlar. Sistemin tabanında serbest hareketli 16-bit sayaç ve programlanabilir ön ölçekleyici, aşırı akış kesici ve ayrı fonksiyon kesici bulunur. M68HC11 zamanlayıcısının diğer özellikleri:

Sabit periyodik oran kesmeleri

Düzgün Bilgisayar İşlemlerinde (COP) yazılım başarısızlıklarına karşı gösterim

Dış olay sayıcı veya kontrollü zaman akümülasyonu için pals akümülatörü

Altı kanal ve 16-bit PWM çıkış sağlayan opsiyonel PWM

İleri zamanlama opsiyonları için opsiyonel olay sayaç sistemi

Çoklu giriş tutma fonksiyonları ve çoklu çıkış karşılaştırmaları

Ayrıca zamanlama yoğunluklu uygulamalar için zamanlayıcı alt sistemleri de bulunur, bunların her biri aşağıdakiler dahil, özgün aile üyelerinin sahip olduğu ek özelliklerle desteklenmektedir:

Giriş Tutma

Çıkış Karşılaştırma

Gerçek Zamanlı Kesme

Pals Akümülatörü

Koruma (Watchdog) fonksiyonu

**A/D Dönüştürücü**

8-12 kanal ve 8-10 bit çözünülürlük arasında A/D sistemleri mevcuttur. A/D tek veya sürekli dönüştürme modları temin etmek amacıyla yazılımla programlanabilirdir. M68HC11 ailesinde ayrıca arttırılmış değişkenlik için D/A dönüştürme bulunur.

**Seri İletişim Arabirimi (SCI)**

SCI’de eksiksiz çift yönlü Evrensel Asenkron Alıcı/İletici sistemi bulunur, bu sistem mikrokontrolör ve PC arası bağlantı için veya geniş alana dağılmış mikrokontrolörleri bağlamak üzere seri iletişim kurmak için sıfıra dönmeme (NRZ) formatı kullanır. SCI aracılığıyla, kurulu besleme arabirimi, devre içi programlama sağlar ve uygulamanızın tanısal ve test işlemlerini kolaylaştırır.

Veri formatı\_ 1 Start, 8 veya 9 veri ve bir stop bit

Veri oranı\_ 150-312500 Baud (312500 4 MHz E saat)

**Seri Yan Arabirim (SPI) **

SPI, \_ çoklu master sisteminde işlemciler arası iletişim sağlar. Senkronize seri iletişimler CLK, DATA IN, DATA OUT ve opsiyonel çipleri bir araya getirir. Ayrıca özgün SPI araçları kullanıldığında, I/O’yu SPI ve standart lojik araçları (yani 74HC595 ve 74HC165) kullanarak genişletmek çok kolaydır. SPI ayrıca mikrokontrolör ve aşağıdaki yan araçlar arasında senkronize iletişim de sağlar:

Kaydırma kaydedici

Likit kristal ekran (LCD) sürücüleri

Analog/Dijital dönüştürücü

Diğer Mikroişlemciler

**Pals Genişliği Modülasyonu**

M68HC11 ailesinde bir dizi uygulamayı desteklemek üzere Pals Genişliği Modülasyonu (PWM) seçenekleri mevcuttur. Programlanabilir oranlarda sürekli dalga formları ve 0’dan %100’e kadar yazılım seçimli iş çevrimleri yaratmak için 6’ya kadar PWM kanalı seçilebilir.

**MC68HC11 Ailesi **

**HC11 A Serisi**
8K ROM (A8), Romsuz (ROMless) (A0,A1), 256 RAM, 512 EEPROM (A1,A8), SPI, SCI, 3 IC 5 OC, 8 kanal 8 bit A/D.

**HC11 C0**
AT&T ile beraber iyi ve yeni bir aygıt geliştirildi. ROMless, 256K’nın üzerinde bellek alanını anahtarlamayı (switching) amaçlayan pano üstü (on board) küme . Tamamen bağımsız arayüz – pano üstü çip seçme, Okuma sağlayan ve Yazma sağlayan sinyaller çip üstüne alındı. 256 RAM, 8 kanal 8 bit A/D.

**HC11 D Serisi**
HC11 Ailesinin küçültülmüş ve düşük maliyetli bir üyesi. ROMless D0, 4K ROM (D3), 4K EPROM (711D3) -A-D veya EEPROM'suz. Yine standart zamanlayıcı ve seri portlara sahip.

**HC11 E Serisi**
Aynı A serisi gibi 512 bayt RAM ve 512 EEPROM (E2 için 2048) ‘lardan hariç tutulur. Pim uyumlu, tek farkı tek zamanlı (one timer) pim (PA4). Üstelik bir EPROM aygıtı ve geniş bir belleği vardır - HC711E9 (12K OTP), HC711E20 (20K OTP).

**HC11 F Serisi**
ROMless, çoklu olmayan adres /veri yolu 4 çip seçme ile üretilmiş. 1K RAM, 512 bayt EEPROM Diğerleri aynı E serisi gibi.

**HC11 G Serisi**
16K ROM/EPROM, çoklu olmayan adres/veri yolu, 512 RAM, 4 kanal PWM, 10 Bit A/D dönüştürücü, 2 ayrı 16 bit zamanlayıcı.

**HC11 K4**
24K ROM/EPROM, 1Mb adreslemede kullanılan çip üstü bellek alanı. Çoklu olmayan adres ve veri yolu. 4 programlanabilir çip seçme, 8 kanal 8 bit A/D. 4 kanal PWM, 768 bayt RAM.

**HC11 L6**
68HC11L6, 68HC11E9 ‘ ın temeline dayanır. 16K ROM, ilave olarak yönsüz port. Bu tamamen statik bir dizayn, dc frekansın altındaki işlemlere izin verir .

**HC11 M Serisi**
Geniş bellek modülleri, 16 bit matematik işlemci (math coprocessor), 4 kanallı DMA.

**HC11 P Serisi**
Programlanabilir PLL ,temel saat devresi, fazlaca 1/0 pimleri, geniş bellek ve 3 SCI port.

(Bkz http://www.hc11.demon.nl/thrsim11/68hc11/ )

**PRIVATEM68HC11 Ailesi**

**68HC11 8-bit Mikrokontrolörler******

PRIVATE**Ürün****ROM******

(KBytes)**RAM******

(Bytes)**EPROM/OTP******

(Kbytes)**EEPROM******

(Bytes)**Zamnlayıcı(Timer)****Serial****A/D****PWM**

**Operating Voltage******

(V)**Bus Frequency******

**(Max)******

(MHz)

68HC11D0-192--16-Bit, 3/4IC, 4/5OC, RTI, pulse accumulatorSCI, SPI--3.0, 5.03

68HC11D34192--16-Bit, 3/4IC, 4/5OC, RTI, pulse accumulatorSCI, SPI--3.0, 5.03

68HC11E0-512--16-Bit, 3/4IC, 4/5OC, RTI, pulse accumulatorSCI, SPI8-CH 8-Bit--3

68HC11E1-512-51216-Bit, 3/4IC, 4/5OC, RTI, pulse accumulatorSCI, SPI8-CH 8-Bit-3.0, 5.03

68HC11E912512-51216-Bit, 3/4IC, 4/5OC, RTI, pulse accumulatorSCI, SPI8-CH 8-Bit-3.0, 5.03

68HC11E2020768-51216-Bit, 3/4IC, 4/5OC, RTI, pulse accumulatorSCI, SPI8-CH 8-Bit-53

68HC11F1-1-51216-Bit, 3/4IC, 4/5OC, RTI, pulse accumulatorSCI SPI8-CH 8-Bit-3.0, 5.05

68HC11FC0-1--16-Bit, 3/4IC, 4/5OC, RTI, pulse accumulatorSCI SPI--56

68HC11K0-768--16-Bit, 3/4IC, 4/5OC, RTI, pulse accumulatorSCI+ SPI8-CH 8-Bit4-CH 8-Bit or 2-CH 16-Bit3.0, 5.04

69HC11K1-768-64016-Bit, 3/4IC, 4/5OC, RTI, pulse accumulatorSCI+ SPI8-CH 8-Bit4-CH 8-Bit or 2-CH 16-Bit3.0, 5.04

68HC11K424768-64016-Bit, 3/4IC, 4/5OC, RTI, pulse accumulatorSCI+ SPI8-CH 8-Bit4-CH 8-Bit or 2-CH 16-Bit3.0, 5.04

68HC11KS2-13264016-Bit, 3/4IC, 4/5OC, RTI, pulse accumulatorSCI+ SPI8-CH 8-Bit-54

68HC11KW1-768-64016-Bit, 3/4IC, 4/5OC, RTI, pulse accumulatorSCI+ SPI10-CH 10-Bit4-CH 8-Bit or 2-CH 16-Bit54

68HC11P1-1-64016-Bit, 3/4IC, 4/5OC, RTI, pulse accumulatorTriple SCI SPI8-CH 8-Bit4-CH 8-Bit or 2-CH 16-Bit54

68HC11P2321-64016-Bit, 3/4IC, 4/5OC, RTI, pulse accumulatorTriple SCI SPI8-CH 8-Bit4-CH 8-Bit or 2-CH 16-Bit54

68HC711D3-1924-16-Bit, 3/4IC, 4/5OC, RTI, pulse accumulatorSCI SPI--53

68HC711E9-5121251216-Bit, 3/4IC, 4/5OC, RTI, pulse accumulatorSCI SPI8-CH 8-Bit-54

68HC711E20-7682051216-Bit, 3/4IC, 4/5OC, RTI, pulse accumulatorSCI SPI8-CH 8-Bit-54

68HC711KS2-13264016-Bit, 3/4IC, 4/5OC, RTI, pulse accumulatorSCI+ SPI8-CH 8-Bit-54

(Bkz http://www.motorola.com)

**Komut Seti**

Komut seti listesinde bütün geçerli opcode’lar ve komutların yerini tutan ayrıntılar vardır. Makine dili ve assembly dili programlayıcılarına başlıca yardımdır. Komut seti listesindeki komutlar isimlerine göre alfabetik sıralanmışlardır.

Kaydedici (register) a = 8 bit

Kaydedici (register) b = 8 bit

Kaydedici (register) d = 16 bit (a = MSB, b = LSB)

Kaydedici (register) x = 16 bit

Kaydedici (register) y = 16 bit

notlar:

- değişim yok

x veriye göre güncellenir

0 0 ‘a kur

1 1 ‘e kur

3 c|=(msn>9)

4 b biti oldukça önemli .

5 Kesme olduğunda kur. Eğer önceden kurulmuşsa,

maskelenemeyen bir kesme bekleme durumundan çıkmak ister.

addressing modes flags

instruct. immed direct ind,x ind,y extend inherent explanation h i n z v c

----------------------------------------------------------------------------------------------

aba -- - - -- - - -- - - -- - - -- - - 1b 1 1 a+=b x - x x x x

abx -- - - -- - - -- - - -- - - -- - - 3a 1 1 x+=(uc)b - - - - - -

aby -- - - -- - - -- - - -- - - -- - - 183a 1 1 y+=(uc)b - - - - - -

adca 89 2 2 99 3 2 a9 4 2 18a9 4 2 b9 4 3 -- - - a+=m+c x - x x x x

adcb c9 2 2 d9 3 2 e9 4 2 18e9 4 2 f9 4 3 -- - - b+=m+c x - x x x x

adda 8b 2 2 9b 3 2 ab 4 2 18ab 4 2 bb 4 3 -- - - a+=m x - x x x x

addb cb 2 2 db 3 2 eb 4 2 18eb 4 2 fb 4 3 -- - - b+=m x - x x x x

addd c3 3 3 d3 4 2 e3 5 2 18e3 5 2 f3 5 3 -- - - d+=m - - x x x x

anda 84 2 2 94 3 2 a4 4 2 18a4 4 2 b4 4 3 -- - - a&=m - - x x 0 -

andb c4 2 2 d4 3 2 e4 4 2 18e4 4 2 f4 4 3 -- - - b&=m - - x x 0 -

asl -- - - -- - - 68 6 2 1868 6 2 78 6 3 -- - - m<<=1 - - x x x x

asla -- - - -- - - -- - - -- - - -- - - 48 1 1 a<<=1 - - x x x x

aslb -- - - -- - - -- - - -- - - -- - - 58 1 1 b<<=1 - - x x x x

asld -- - - -- - - -- - - -- - - -- - - 05 1 1 d<<=1 - - x x x x

asr -- - - -- - - 67 6 2 1867 6 2 77 6 3 -- - - (i)m>>=1 - - x x x x

asra -- - - -- - - -- - - -- - - -- - - 47 1 1 (i)a>>=1 - - x x x x

asrb -- - - -- - - -- - - -- - - -- - - 57 1 1 (i)b>>=1 - - x x x x

bcc 24 3 2 -- - - -- - - -- - - -- - - -- - - bra(cc) - - - - - -

bclr -- - - 15 6 3 1d 7 3 181d 7 3 -- - - -- - - m&=im - - x x 0 -

bcs 25 3 2 -- - - -- - - -- - - -- - - -- - - bra(cs) - - - - - -

beq 27 3 2 -- - - -- - - -- - - -- - - -- - - bra(eq) - - - - - -

bge 2c 3 2 -- - - -- - - -- - - -- - - -- - - bra(ge) - - - - - -

bgt 2e 3 2 -- - - -- - - -- - - -- - - -- - - bra(gt) - - - - - -

bhi 22 3 2 -- - - -- - - -- - - -- - - -- - - bra(hi) - - - - - -

bhs 24 3 2 -- - - -- - - -- - - -- - - -- - - bra(hs) - - - - - -

bita 85 2 2 95 3 2 a5 4 2 18a5 4 2 b5 4 3 -- - - a&m - - x x 0 -

bitb c5 2 2 d5 3 2 e5 4 2 18e5 4 2 f5 4 3 -- - - b&m - - x x 0 -

ble 2f 3 2 -- - - -- - - -- - - -- - - -- - - bra(le) - - - - - -

blo 25 3 2 -- - - -- - - -- - - -- - - -- - - bra(lo) - - - - - -

bls 23 3 2 -- - - -- - - -- - - -- - - -- - - bra(ls) - - - - - -

blt 2d 3 2 -- - - -- - - -- - - -- - - -- - - bra(lt) - - - - - -

bmi 2b 3 2 -- - - -- - - -- - - -- - - -- - - bra(mi) - - - - - -

bne 26 3 2 -- - - -- - - -- - - -- - - -- - - bra(ne) - - - - - -

bpl 2a 3 2 -- - - -- - - -- - - -- - - -- - - bra(pl) - - - - - -

bra 20 3 2 -- - - -- - - -- - - -- - - -- - - bra - - - - - -

brclr -- - - 13 6 4 1f 7 4 181f 7 4 -- - - -- - - bra(!(m&im)) - - x x 0 -

brn 21 3 2 -- - - -- - - -- - - -- - - -- - - bra( 0) - - - - - -

brset -- - - 12 6 4 1e 7 3 181e 7 3 -- - - -- - - bra(!(/m&im)) - - x x 0 -

bset -- - - 14 6 3 1c 7 3 181c 7 3 -- - - -- - - m|=im - - x x 0 -

bsr 8d 5 2 -- - - -- - - -- - - -- - - -- - - bsr - - - - - -

bvc 28 3 2 -- - - -- - - -- - - -- - - -- - - bra(vc) - - - - - -

bvs 29 3 2 -- - - -- - - -- - - -- - - -- - - bra(vs) - - - - - -

cba -- - - -- - - -- - - -- - - -- - - 11 1 1 a-b - - x x x x

clc -- - - -- - - -- - - -- - - -- - - 0c 1 1 c=0 - - - - - 0

cli -- - - -- - - -- - - -- - - -- - - 0e 1 1 i=0 - 0 - - - -

clr -- - - -- - - 6f 5 2 186f 5 2 7f 5 3 -- - - m=0 - - x x 0 0

clra -- - - -- - - -- - - -- - - -- - - 4f 1 1 a=0 - - x x 0 0

clrb -- - - -- - - -- - - -- - - -- - - 5f 1 1 b=0 - - x x 0 0

clv -- - - -- - - -- - - -- - - -- - - 0a 1 1 v=0 - - - - 0 -

cmpa 81 2 2 91 3 2 a1 4 2 18a1 4 2 b1 4 3 -- - - a-m - - x x x x

cmpb c1 2 2 d1 3 2 e1 4 2 18e1 4 2 f1 4 3 -- - - b-m - - x x x x

com -- - - -- - - 63 6 2 1863 6 2 73 6 3 -- - - m=~m - - x x 0 1

coma -- - - -- - - -- - - -- - - -- - - 43 1 1 a=~a - - x x 0 1

comb -- - - -- - - -- - - -- - - -- - - 53 1 1 b=~b - - x x 0 1

cpd 1a83 5 4 1a93 6 3 1ab3 7 4 cdb3 7 4 1aa3 7 3 -- - - d-m - - x x x x

cpx 8c 3 3 9c 4 2 ac 5 2 18ac 5 2 bc 5 3 -- - - x-m - - x x x x

cpy 188c 3 3 189c 4 2 18ac 5 2 1aac 5 2 18bc 5 3 -- - - x-m - - x x x x

daa -- - - -- - - -- - - -- - - -- - - 19 2 1 a=da(a) - - x x x 3

dec -- - - -- - - 6a 6 2 6a 6 2 7a 6 3 -- - - m-=1 - - x x x -

deca -- - - -- - - -- - - -- - - -- - - 4a 1 1 a-=1 - - x x x -

decb -- - - -- - - -- - - -- - - -- - - 5a 1 1 b-=1 - - x x x -

des -- - - -- - - -- - - -- - - -- - - 34 1 1 s-=1 - - - - - -

dex -- - - -- - - -- - - -- - - -- - - 09 1 1 x-=1 - - - x - -

eim -- - - 75 6 3 65 7 3 1865 7 3 -- - - -- - - m^=im - - x x 0 -

eora 88 2 2 98 3 2 a8 4 2 18a8 4 2 b8 4 3 -- - - a^=m - - x x 0 -

eorb c8 2 2 d8 3 2 e8 4 2 18e8 4 2 f8 4 3 -- - - b^=m - - x x 0 -

inc -- - - -- - - 6c 6 2 186c 6 2 7c 6 3 -- - - m+=1 - - x x x -

inca -- - - -- - - -- - - -- - - -- - - 4c 1 1 a+=1 - - x x x -

incb -- - - -- - - -- - - -- - - -- - - 5c 1 1 b+=1 - - x x x -

ins -- - - -- - - -- - - -- - - -- - - 31 1 1 s+=1 - - - - - -

inx -- - - -- - - -- - - -- - - -- - - 08 1 1 x+=1 - - - x - -

jmp -- - - -- - - 6e 3 2 186e 3 2 7e 3 3 -- - - jmp - - - - - -

jsr -- - - 9d 5 2 ad 5 2 18ad 5 2 bd 6 3 -- - - jsr - - - - - -

ldaa 86 2 2 96 3 2 a6 4 2 18a6 4 2 b6 4 3 -- - - a=m - - x x 0 -

ldab c6 2 2 d6 3 2 e6 4 2 18e6 4 2 f6 4 3 -- - - b=m - - x x 0 -

ldd cc 3 3 dc 4 2 ec 5 2 18ec 5 2 fc 5 3 -- - - d=m - - x x 0 -

lds 8e 3 3 9e 4 2 ae 5 2 18ae 5 2 be 5 3 -- - - s=m - - x x 0 -

ldx ce 3 3 de 4 2 ee 5 2 18ee 5 2 fe 5 3 -- - - x=m - - x x 0 -

lsr -- - - -- - - 64 6 2 1864 6 2 74 6 3 -- - - (u)m>>=1 - - x x x x

lsra -- - - -- - - -- - - -- - - -- - - 44 1 1 (u)a>>=1 - - x x x x

lsrb -- - - -- - - -- - - -- - - -- - - 54 1 1 (u)b>>=1 - - x x x x

lsrd -- - - -- - - -- - - -- - - -- - - 04 1 1 (u)d>>=1 - - x x x x

mul -- - - -- - - -- - - -- - - -- - - 3d 7 1 d=a\*b - - - - - 4

neg -- - - -- - - 60 6 2 1860 6 2 70 6 3 -- - - m=-m - - x x x x

nega -- - - -- - - -- - - -- - - -- - - 40 1 1 a=-a - - x x x x

negb -- - - -- - - -- - - -- - - -- - - 50 1 1 b=-b - - x x x x

nop -- - - -- - - -- - - -- - - -- - - 01 1 1 nop - - - - - -

oim -- - - 72 6 3 62 7 3 1862 7 3 -- - - -- - - m|=im - - x x 0 -

oraa 8a 2 2 9a 3 2 aa 4 2 18aa 4 2 ba 4 3 -- - - a|=m - - x x 0 -

orab ca 2 2 da 3 2 ea 4 2 18ea 4 2 fa 4 3 -- - - b|=m - - x x 0 -

psha -- - - -- - - -- - - -- - - -- - - 36 4 1 \*s--=a - - - - - -

pshb -- - - -- - - -- - - -- - - -- - - 37 4 1 \*s--=b - - - - - -

pshx -- - - -- - - -- - - -- - - -- - - 3c 5 1 \*s--=x - - - - - -

pula -- - - -- - - -- - - -- - - -- - - 32 3 1 a=\*++s - - - - - -

pulb -- - - -- - - -- - - -- - - -- - - 33 3 1 b=\*++s - - - - - -

pulx -- - - -- - - -- - - -- - - -- - - 38 4 1 x=\*++s - - - - - -

rol -- - - -- - - 69 6 2 1869 6 2 79 6 3 -- - - m=rol(m) - - x x x x

rola -- - - -- - - -- - - -- - - -- - - 49 1 1 a=rol(a) - - x x x x

rolb -- - - -- - - -- - - -- - - -- - - 59 1 1 b=rol(b) - - x x x x

ror -- - - -- - - 66 6 2 1866 6 2 76 6 3 -- - - m=ror(m) - - x x x x

rora -- - - -- - - -- - - -- - - -- - - 46 1 1 a=ror(a) - - x x x x

rorb -- - - -- - - -- - - -- - - -- - - 56 1 1 b=ror(b) - - x x x x

rti -- - - -- - - -- - - -- - - -- - - 3b a 1 rti x x x x x x

rts -- - - -- - - -- - - -- - - -- - - 39 5 1 rts - - - - - -

sba -- - - -- - - -- - - -- - - -- - - 10 1 1 a-=b - - x x x x

sbca 82 2 2 92 3 2 a2 4 2 18a2 4 2 b2 4 3 -- - - a-=m+c - - x x x x

sbcb c2 2 2 d2 3 2 e2 4 2 18e2 4 2 f2 4 3 -- - - b-=m+c - - x x x x

sec -- - - -- - - -- - - -- - - -- - - 0d 1 1 c=1 - - - - - 1

sei -- - - -- - - -- - - -- - - -- - - 0f 1 1 i=1 - 1 - - - -

sev -- - - -- - - -- - - -- - - -- - - 0b 1 1 v=1 - - - - 1 -

slp -- - - -- - - -- - - -- - - -- - - 1a 4 1 sleep - - - - - -

staa -- - - 97 3 2 a7 4 2 18a7 4 2 b7 4 3 -- - - m=a - - x x 0 -

stab -- - - d7 3 2 e7 4 2 18e7 4 2 f7 4 3 -- - - m=b - - x x 0 -

std -- - - dd 4 2 ed 5 2 18ed 5 2 fd 5 3 -- - - m=d - - x x 0 -

sts -- - - 9f 4 2 af 5 2 18af 5 2 bf 5 3 -- - - m=s - - x x 0 -

stx -- - - df 4 2 ef 5 2 18ef 5 2 ff 5 3 -- - - m=x - - x x 0 -

suba 80 2 2 90 3 2 a0 4 2 18a0 4 2 b0 4 3 -- - - a-=m - - x x x x

subb c0 2 2 d0 3 2 e0 4 2 18e0 4 2 f0 4 3 -- - - b-=m - - x x x x

subd 83 3 3 93 4 2 a3 5 2 18a3 5 2 b3 5 3 -- - - d-=m - - x x x x

swi -- - - -- - - -- - - -- - - -- - - 3f c 1 swi - 1 - - - -

tab -- - - -- - - -- - - -- - - -- - - 16 1 1 b=a - - x x 0 -

tap -- - - -- - - -- - - -- - - -- - - 06 1 1 ccr=a x x x x x x

tba -- - - -- - - -- - - -- - - -- - - 17 1 1 a=b - - x x 0 -

tim -- - - 7b 4 3 6b 5 3 186b 5 3 -- - - -- - - m-im - - x x 0 -

tpa -- - - -- - - -- - - -- - - -- - - 07 1 1 a=ccr - - - - - -

tst -- - - -- - - 6d 4 2 186d 4 2 7d 4 3 -- - - m-0 - - x x 0 0

tsta -- - - -- - - -- - - -- - - -- - - 4d 1 1 a-0 - - x x 0 0

tstb -- - - -- - - -- - - -- - - -- - - 5d 1 1 b-0 - - x x 0 0

tsx -- - - -- - - -- - - -- - - -- - - 30 1 1 x=s+1 - - - - - -

txs -- - - -- - - -- - - -- - - -- - - 35 1 1 s=x-1 - - - - - -

wai -- - - -- - - -- - - -- - - -- - - 3e 9 1 wait - 5 - - - -

xgdx -- - - -- - - -- - - -- - - -- - - 18 2 1 exg(d,x) - - - - - -

PRIVATE "TYPE=PICT;ALT=CPU-registers"**CPU Kaydedicileri:**

MC68HC11 iki tane 8-bit akümülatöre (A ve B) sahiptir, bir 16-bit akümülatör (D) A ve B ile biçimlendirilir; A’nın yeri MSB ve B’nin yeri LSB’dir. Bu mikrokontrolör iki tanede 16-bit indeks kaydediciye sahiptir. İsimleri X ve Y. Bir 16-bit yığın göstericisi (SP) ve 16 bit program sayıcısı (programcounter -PC) vardır . Şartlı-kod-kaydedici veya bayrak-kaydedici, 8 bayrağa sahiptir

DUR engelleyici (S)

X- kesme (interrupt )(X)

Bit-3 ‘ten yarım elde (H)

I- kesme (interrupt) (I)

Negatif (Negative) (N)

Sıfır (Zero) (Z)

İkinci tamamlayıcı taşma hatası (V)

Daha önemli bitten elde (C)

(Bkz http://www.hc11.demon.nl/thrsim11/68hc11/)

**M68HC11 Kullanımında Karşılaşılan Bazı Problemler ve Çözüm Önerileri:**

Programlama veya hedef uygulamalarda kullanım sırasında M68HC11 pencereli Eprom araçlarıyla problem yaşıyorsanız, bu problemler, hizalama problemlerinden kaynaklanıyor olabilir. Bu araçlardaki uçlar (FS ambalaj mührüyle tanımlanır) plastik uçlu çip kuryelerinde ambalajlanmış benzer EPROM araçlarındakilerden (FN ambalaj mührüyle tanımlanan) daha esnektir. Bu ek esneklik, parçaların çoğunlukla elle tutulduğu uygulamalarda problemlere yol açabilir.

**Semptomlar**

Arıza semptomlarına şunlar dahildir:

\* Araçlar ticari EPROM programlayıcılarda düzgün programlama yapmazlar. EEPROM ve/veya EPROM Motorola M68HC11 değerlendirme ve programlayıcı pano(board) ürünlerinde programlama yapmaz.

\* Sıfır eklenti güçlü (ZIF) soketleri içeren hedef sistemlerde araçlar düzgün çalışmaz.

\* Seri iletişim arabirimi (SCI) hedef sistemlerde düzgün çalışmaz, fakat geliştirme araçlarında çalışır.

\* Uygun şekilde konfigüre edilmiş hedef sistemler özel besleme modunda çalışmaz.

**Araç Talimatları**

Bu EPROM araçları pencereli seramik uçlu çip kurye taşıma ambalajlarında mevcuttur.

MC68HC711D3FS

MC68HC711E9FS

MC68HC711E20FS

MC68HC711G5FS

MC68HC711K4FS

MC68HC711KA4FS

MC68HC711KA2FS

MC68HC711L6FS

MC68HC711N4FS

Bu araçlarla ve Motorola’nın benzer şekilde ambalajladığı diğer araçları kullanırken şu talimatlara uyunuz:

\* Bu parçaları tutarken, uçlarına dokunmamaya dikkat edin. Uygun bir tutuş sayesinde sadece uçları eğme riski en aza indirilmekle kalmaz, ayrıca elektrostatik boşalma riskinden gelebilecek zarar olasılığı da azalır.

NOT: Herhangi hassas elektronik parçaları tutarken uygun şekilde topraklama yapılması gereklidir.

Sıfır eklenti gücü soketli, seramik uçlu çip kurye araçları (Yamaichi ve Plastronics’in ürettikleri gibi) kullanırken, soketlerin parçalar yukarıdan aşağıya doğru eklenmiş şekilde kullanılabilmesi için devreyi düzenlemeye çalışın. Bu şekildeki montaj soketlerinin çeşitli avantajları vardır.

- Herhangi iki ucun birlikte sıkıştırılıp kısa devre yapmasını önlersiniz. MC68HC11’in bazı versiyonlarında, uçlu çip kurye ambalajının köşelerinde veya köşelerine yakın yerlere takılmış PDO/RxD ve PD1/TxD pimleri bulunur. Bu parçalar sıfır eklenti güçlü soketlere uygun şekilde oturtulmazsa, PDO/RxD ve PD1/TxD pimleri birlikte sıkıştırılabilir.

- Araçlarınızı aşağıdan yukarıya doğru eklemek çipin uçlarının karşılık gelen soketlerle temasta olmadığını görmenizi sağlar. Bu bağlantıları kontrol etmek için süreklilik testi uygulanabilir. EEPROM veya EPROM araçlarının programlanmasında yaşanan zorlukların nedeni budur. EEPROM ve EPROM programlamayı destekleyen birçok pano, RxD ve TxD pimlerine hatalı soket bağlantılarının kendilerini araç programlama hatası gibi gösterdiği özel besleme modunda bu şekilde tepki verir.

- Yukarıdan aşağıya doğru eklendiğinde, araçlarınızdaki uçlar sıfır eklenti güçlü soketlerin ucuyla daha iyi temas kuracak ve soketinizin ömrünü uzatacaktır.

Tasarım yaparken, aracın sökülmesi için çip ayırıcı gerektiren soketler kullanmaya dikkat edin. MC68HC11’in söküleceği uygulamalarda, sıfır eklenti güçlü soket kullanılması uygun olmakla birlikte, yarı kalıcı soketler (AMP’ninkiler gibi) daha fazla güvenilirlik sunar. Bu soketler, uçları bir aracın uçlarıyla temas etmeye zorlanacak şekilde dizayn edilmiştir. Her zaman bu soketlerin parçalarını kullanın. Başka şekilde sökmeye çalışmak çipin uçlarını eğebilir veya zarar verebilir.

\* Seramik MC68HC11 araçlarındaki uçların eğilmiş olduğunu görürseniz, bunları dikkatlice düzeltebilirsiniz.

NOT: Bunu yaparken topraklama yapın.

Ucun J-şeklindeki kısmı altından sağlam bir dikiş iğnesi geçirin. İnce bir iğne kullanıyorsanız, yukarıya doğru eğilmede biraz dirençle karşılaşabilirsiniz. Bunu uçlu çip taşıma paketinin her tarafına uygulayın. Belli uçlar temas etmiyorsa, medikal tahlil sondası kullanabilirsiniz. Bu, saplı ve uzun ince bir pimdir, fakat yukarıya doğru eğilirken uçlara daha fazla basınç uygulamanızı sağlar.

**Alternatifler**

Mümkünse, MC68HC11’in tek zamanlı programlanabilir versiyonlarını kullanın. MC68HC11’in birçok versiyonu plastik uçlu çip taşıyıcı tek zamanlı programlanabilir paketler içinde sunulur (FN paket mührünü taşır). Belirtildiği üzere, PLCC paketinde seramik paketten daha güçlü uçlar vardır ve kodun son uygulamasını muhafaza edebileceğiniz uygulamalarda tek zamanlı programlanabilir araçlar kullanmak ekonomik olacaktır.

Aracınızda sık sık değişiklik yapmak istiyorsanız, EPROM tabanlı HC11 aracı yerine soketli bir FLASH EPROM veya EPROM ve ROM’suz HC11 aracı kullanmak daha uygun olacaktır. Tek çipli uygulamalar daha çok entegrasyon sağlamasına ve daha az yer kaplamasına rağmen, HC11’i sabit olarak soketlerle bağlar ve soketi ayırırsanız güvenilirlik artacaktır.

(Bkz Motorola Semiconductor Engineering Bulletin, By John Bodnar **Austin, Texas)**

**8051 MİKROKONTROLÖR:******

Bir mikrokontrolör tek-çip bilgisayardır. Bütünleşmiş bir devredir, yani işlemci ve ikincil gerekler (kod ve veri belleği, paralel ve seri portlar, zamanlayıcı, sayıcı ve kesme mantığı gibi). Mikrokontrolörler iç kontrollerde daima kullanılırlar. İç kontrol bilgisayar sistemleri ile ilgilidir. Bunlar fiziksel olarak monitör ve kontrol aygıtlarının içine yerleştirilirler. Bunların çeşitleri özel uygulamalar-spesifik yazılımlar içiren iç kontrollerdir. Endüstriyel veya ticari uygulamalar için ROM içinde kod alanı vardır. 8051 dahili ROM ve RAM’a sahiptir. Ticari uygulamalar geliştirmede 8051 tek-çip modunda çalışılabilir.

Intel’in 8-bit MCS 51 mikrokontrolör ailesi iç kontrol için bir sanayi standardı haline gelmiştir. Mimari kontrol merkezli uygulamalar için optimum hale getirilmiştir. Intel, pano(board)-içi EPROM ve ROM bellek ve sadece CPU için değişik versiyonlarda bir dizi 8-bit mikrokontrolör sunmaktadır. Sonuç olarak, Intel size özgün uygulama ihtiyaçlarınızı karşılamanız için, EPROM, tek zamanlı programlanabilir (OTP) ROMsuz (ROMless) ve ROM-tabanlı (ROM-based) mikrokontrolör sunmaktadır. HMOS 8051 ailesi ekonomik açıdan hassas tasarımlar için kullanılırken, Intel’in kendini kanıtlamış CHMOS teknolojisini kullanan 8051 ailesi daha düşük güç, daha yüksek entegrasyon ve daha yüksek performans sağlamaktadır.

| **Özellikler** | **Faydaları** |
| --- | --- |
| Sonuç kontrolü için 8-bit CPU uyumluluğu | **Hızlı ve verimli.** Sonuç kontrol dizaynı. |
| Boolean işlemleri | **Kolaylık.** |
| Çip üzerinde bellek (32K ve üzeri) | **Çözünme.** Tek-çip dizaynı olanaklı kılar. |
| Çip üzerinde ikincil (zamanlayıcı-sayıcı, seri portlar, PCA vb.) | **Yüksek bütünleşme.** Düşük maliyet ve I/O portlarını, küçük-çip sayıcı dizaynını olanaklı kılar. |

(Bkz http://www.intel.com)

8051 255 komutlu akümülatör tabanlı bir tasarımdır. Temel bir komut çevrimi 12 saat alır (bazılarında 4). CPU’da metin anahtarlamak üzere çip üzerindeki ram’da 8-bitlik sekiz kaydedici bankasına sahiptir. Bu kaydediciler 8051’in 128 baytlık ram’i dahilinde bit çalıştırma alanı ve genel kayıt ram’i boyunca bulunurlar. Kaydedici, çip üstü ram adresi için 8 bitlik veya 16 bitlik veri gösterici (pointer) kaydedicisi (dptr) gerektirir; orijinal 8051’de sadece bir dptr bulunur; Atmel, Dallas ve Philips’in mikrokontrolörlerinde iki dptr bulunur; infineon’da 8 tane vardır.

• 8051 MCS Mikrokontrolör ailesinin çekirdek üyesidir.

• Tek-çip mikrobilgisayar

•İç RAM ve ROM/EPROM

•I/O Portları

•Paralel portlar (8-bit transfer edilir)

•Seri port (bit-bit)

•Intel tarafından dizayn edilmiştir fakat farklı fabrikalarda değişiklik gösterir.

•8-bit makinedir, çünkü “veri genişliği” =”Acc. genişliği” =8-bit

• Diğer birçok kaydedicisi 8-bittir. PC, veri göstericisi (DPTR), zamanlayıcı kaydedicisi 16-bittir, fakat bunlar iki 8-bitlik kaydediciden yapılır.

**Bellek Organizasyonu:**

Çoğunlukla bir CPU bellek ünitesine üç farklı bağlantı sağlar. Bunlar;

•Veri yolu (Data Bus) (okuma/yazma – doğrusal olmayan)

•Adres yolu (address Bus) (adresleri bellek alanına gönderir – tek yönlü)

•Kontrol yolu (Control Bus) (okuma/yazma sinyallerini bellek ünitesine gönderir)

•Veri yolundaki bitlerin sayısı CPU’nun ve bellek ünitesinin veri genişliğidir. 8051, veri genişliği 8-bittir.

•Adres yolundaki bitlerin maksimum sayısı CPU’nun adres alanıdır. Bununla birlikte eğer asıl bellek CPU’yu maksimumdan az kullanıyorsa burada az sayıda bit olabilir.

8051’in veri belleği ve program belleği farklıdır. Bu “Harvard Mimarisi” nin karakteristiğidir. Komutlar ve programlar program belleğine yüklenir. Veri belleğine yüklenmiş olan veriler bu komutlarla işlenirler. Program ve veri bellekleri için farklı kontrol sinyalleri vardır. Fakat veri ve adres yolu çokludur.

**Program Belleği: **8051 program belleği harici ( 8051 çipi üstünde değil), dahili (8051 çipi üstünde, 4K kapasiteli) Veya ikisi birden olabilir. Toplam adres alanı 16-bittir. Bu nedenle 64K’nı üzerinde program belleğine sahip olabiriz.. EPROM/ROM ‘lar program belleği gibi kullanılabilir.

**Veri Belleği: **8051’ de iki farklı veri belleği vardır. Bir tanesi dahili ve diğeri harici. Dahili veri belleği çip üzerinde. Harici veri belleği çipten ayrı. Bunlar için farklı adres alanları, farklı kontrol sinyalleri ve özellikle farklı komutları var. RAM ‘ler data belleği gibi kullanılırlar. Dahili veri belleğinin adres alanı 8-bittir. Bu nedenle 256 adreslenebilir bayta sahip olabiliriz. Fakat 8051 bu alanın tamamını kullanmaz. Kullanılan adres alanları 21 adreslenebilir SFRs + 32 genel amaçlı kaydedici + 96 bayt RAM için= 149

adres. Harici veri bellek adres alanı 16- bittir. Bu neden 64K’nın üzerinde adrese (bayt) sahibiz.

8051 ayrıntılı adres alanı aşağıdaki gibi:

**Dahili Bellek Organizasyonu:**

İlk olarak 8-bit dahili veri belleği adres alanını anlatacağız. Yani 256 adreslenebilir bayt var. Üstelik dahili veri belleğinde bazı adreslenebilen “bitler” de var. Bu “bit adres alanı” bayt adres alanından farklıdır. Bit adres alanı 8-bittir, yani dahili veri belleğinde 256 adreslenebilir bit vardır.

**Alt 128 bayt:******

• Bayt adresleri 00H-7FH

• Doğrusal ve doğrusal olmayan adresleme yolu ile erişilebilir.

• 4 küme içinde 32 genel amaçlı kaydedici (her küme için 8 kaydedici, R0-R7) vardır. Adresler 00H-0FH arasındaki alanlardadır. Bir devirde sadece bir küme aktif durumdadır ve kaydedicileri (R0, R1, R2,......,R7) açıkça belirttiğiniz zaman, bu kaydediciyi aktif olan kümeye yönlendirebilirsiniz. PSW ‘deki iki bit kullanılarak aktif küme seçimi yapılır. Kurulu küme 00’dır.

23=8 aktif kaydedicimiz olduğu sürece, 3 bit genel amaçlı kaydedicileri komutlarla ilişkilendirmek için yeterlidir.

• Bir “bit adreslenebilir bellek” (16 bayt/128 bit) vardır. Bayt adresleri 20H-2FH arasındadır. Bit adresleri 00H-7FH arasındadır. Bit ve bayt adresleri üst üste binmesine rağmen, bit ve bayt için farklı komutlar olduğundan dolayı bu problem değildir. Örneğin “MOV A, 21H” bayt komutu, “MOV C, 6FH” ise bit komutudur.

• Bir genel amaçlı RAM(80 bayt) vardır. Bayt adresleri 30H-7FH arasındadır. Belleğin bu kısmı bit olarak adreslenemez.

**Üst 128 bayt: **

• Bayt adresleri 80H-FFH

• Doğrudan adresleme yolu ile erişilebilir.

• Dahili veri belleğinin bu kısmında SFRler vardır ve sadece 21 tanedir. 128-21=107 yer kullanılmaz.

• Bazı SFRler bit olarak adreslenebilir.

• SFRleri ezberlemenize gerek yoktur, program içinde adres gibi onların sözcüklerinin baş harflerinden oluşan sözcükleri (acronyms) kullanabilirsiniz. Örneğin Port 1 kaydedicisinin içeriğini akümülatöre aktarırken, basitçe “MOV A, P1” kullanabilirsiniz. Assembler P1 (90H)’in adresini programı derlerken otomatik olarak yerleştirir.

• SFR bitlerinin yerini belirtmek için kaydedici ve bit numaraları arasını nokta (.) koyabilirsiniz. B kaydedicisinin 3. Bitinin tamamlayıcısı yerine “CPL B.3” yazabilirsiniz. Assembler B.3 (F3H) adresini yerine otomatik olarak yerleştirir.

Unutmayın ki LSB biti kaydedicide 0, MSB ise 7’dir.

**SFRler:**

P0, P1, P3, P3: Paralel port kaydedicileri, herbiri 8-bit. Portlardan gelen ve portlara gönderilen verileri içerirler. P0 ve P2 harici program ve veri belleği için adres ve veri yolu gibi kullanılırlar. P3 bazı özel sinyalleri seri portlara taşır, zamanlayıcı/sayıcı, harici veri belleği erişimi ve kesme girişleri.

**IE: **Kesme olanağı sağlayan kaydedicidir. Bu kaydedicinin içindeki bitler kesmeye olanak sağlayan/sağlamayan bitlerdir.

**IP: **Kesme üstünlük kaydedicisi. 8051 kaydedicileri için iki üstünlük düzeyi vardır. Kaydedicinin içindeki bu bitler her kesmenin üstünlük düzeyini belirlemede kullanılırlar.

**Acc: **Akümülatör.

**B: **B kaydedicisi. B kaydedicisi bölme ve çarpma için kullanılır.

**PSW: **Program durum word’ü. PSW birkaç durum biti içerir, bunlar CPU’nun akım durumunu gösterir.

**SP: **Yığın göetericisi. Bu 8-bit kaydedici yığının en üüstünü tutar.

**DPTR: **Veri göstericisi. 16-bit kaydedicidir ve iki 8-bit kaydediciden (DPL ve DPH) meydana gelir.

DPTR harici veri belleği erişimi için kullanılan adres kaydedicidir.

**SCON, SBUF: **Seri port kontrolü ve seri port tampon kaydedicisidir.

**TCON, TMOD, TH0, TH1, TH2, TL1: **Zamanlayıcı kontrolü, zamanlayıcı mod kaydedicisi ve iki

16-bit zamanlayıcı/sayıcı (herbiri iki 8-bit kaydediciden meydana gelir).

**Program Belleği:** Program veri belleği alanı 16-bittir ve 64K’nın üzerinde program belleği vardır.

Program belleği harici, dahili veya ikisi birden olabilir. Dahili program belleği 4k’ya sınırlandırılır. Adres alanı dahili ve harici program belleği arasında paylaşılır.

Sadece Dahili Harici ve Dahili Sadece Harici

**Adresleme Modları:**

**Doğrudan Adresleme: **Doğrudan adreslemede işlenenler 8-bit adres alanı olarak komutlara belirtilirler. Sadece dahili veri belleği doğrudan adresleme yapabilir.

**Dolaylı Adresleme:** Dolaylı adreslemede işlenenler adres içeren bir kaydedici olarak komutlara belirtilir. Dahili ve harici veri belleklerinde dolaylı adresleme (SFRler’de dolaylı adresleme yapılmaz) yapılabilir. Adres kaydedicileri için 8-bit adresler sadece seçilmiş kümede R0 veya R1 de yada yığın göstericisinde olabilir.

**Kaydedici-Özel Komutları: **Bazı komutlar belirli kaydedicilerle kullanılırlar. Örneğin, bazı komutlar daima akümülatör üzerinde işlem görür, yani adres baytına ihtiyaç yoktur. Opcode kendiliğinden halleder.

**Kaydedici Adresleme: **Kaydedici kümelerinin, içerdiği R0 R7 arasındaki kaydedicilere belirli komutlarla erişebilir, yani komutların içerdiği 3-bit kaydedici belirtme opcode’u ile erişebilirler. Komutları adres baytından kurtaran bu moddan beri kaydedicilere bu kodları içerme yolu ile erişirler. Komut işlendiği zaman seçilmiş kümenin 8 kaydedicisinden birine erişilir.

**Veri Tanımlı Adresleme: **Aslında bu bir adresleme modu değildir, çünkü komutlara bir adres belirtilmez. Burada komutlara bir sabit belirtilir.

“#” sembolü assembly komutlarında yer alan bu sabit değerlerinin önünde yer alır. Bu sabit ondalık numara, onaltılık numara, ikilik numara yada karakter olabilir.

(Bkz 8051 Architecture and Addressing Modes, Dr. Albert Levi)

**8051 KOMUT (INSTRUCTION) SETİ **

Bütün Komutlar Alfabetik Sırada:

| PRIVATEACALL addr11DIV ABLJMP addr16RETI |
| --- |

| ADD A,<src>DJNZ <byte>,<rel8>MOV <dest>,<src>RL A |
| --- |

| ADDC A,<src>INC <byte>MOV DPTR,#data16RLC A |
| --- |

| AJMP addr11INC DPTRMOV bit,bitRR A |
| --- |

| ANL <dest>,<src>JB bit,rel8MOVC A,@A+<base>RRC A |
| --- |

| ANL <bit>JBC bit,rel8MOVX <dest>,<src>SETB bit |
| --- |

| CJNE <dest>,<src>,rel8JC rel8MUL ABSJMP rel8 |
| --- |

| CLR AJMP @A+DPTRNOPSUBB A,<src> |
| --- |

| CLR bitJNB bit,rel8ORL <dest>,<src>SWAP A |
| --- |

| CPL AJNC rel8ORL C,bitXCH A,<byte> |
| --- |

| CPL bitJNZ rel8POP directXCHD A,@Ri |
| --- |

| DA AJZ rel8PUSH directXRL <dest>,<src> |
| --- |

DEC <byte>LCALL addr16RET

.

(Bkz http://.www.rehn.org/YAM51/51set/instruction.shtml)

**Standart 8051/52 CPU Kaydedicileri:**

| SEMBOL | İSİM | ADRES | Reset – Değeri |
| --- | --- | --- | --- |
| ACC \* | Akümülatör (Accumulator) | E0 | 0000 0000 (00) |
| B \* | B Kaydedicisi (B Register) | F0 | 0000 0000 (00) |
| PSW \* | Program Durum Word (PSW) | D0 | 0000 0000 (00) |
| SP | Yığın Gösrerici (Stack Pointer) | 81 | 0000 0111 (07) |
| DPL | Düşük Byte Dptr | 82 | 0000 0000 (00) |
| DPH | Yüksek Byte Dptr | 83 | 0000 0000 (00) |
| P0 \* | Port 0 | 80 | 1111 1111 (FF) |
| P1 \* | Port 1 | 90 | 1111 1111 (FF) |
| P2 \* | Port 2 | A0 | 1111 1111 (FF) |
| P3 \* | Port 3 | B0 | 1111 1111 (FF) |
| IP \* | Kesme Hakkı Kontrolü (IPC) | B8 | xxx0 0000 (?0) |
| IE \* | Kesme Yetkilendirme Kontrolü (IEC) | A8 | 0xx0 0000 (?0) |
| TMOD \* | Zamanlayıcı/Sayıcı Yöntem Kontrolü | 89 | 0000 0000 (00) |
| TCON \* | Zamanlayıcı/Sayıcı Kontrolü | 88 | 0000 0000 (00) |
| T2CON \*^ | Zamanlayıcı/Sayıcı 2 Kontrolü | C8 | 0000 0000 (00) |
| TH0 | Zamanlayıcı/Sayıcı 0 Yüksek Byte | 8C | 0000 0000 (00) |
| TL0 | Zamanlayıcı/Sayıcı 0 Düşük Byte | 8A | 0000 0000 (00) |
| TH1 | Zamanlayıcı/Sayıcı 1 Yüksek Byte | 8D | 0000 0000 (00) |
| TL1 | Zamanlayıcı/Sayıcı 1 Düşük Byte | 8B | 0000 0000 (00) 0000 0000 (00) |
| TH2^ | Zamanlayıcı/Sayıcı 2 Yüksek Byte | CD | 0000 0000 (00) |
| TL2^ | Zamanlayıcı/Sayıcı 2 Düşük Byte | CC | 0000 0000 (00) |
| RCAP2H^ | Z/S 2 Tutan Kaydedici Yüksek Byte | CB | 0000 0000 (00) |
| PCAP2L^ | Z/S 2 Tutan Kaydedici Düşük Byte | CA | 0000 0000 (00) |
| SCON | Seri Control (Serial Control) | 98 | 0000 0000 (00) |
| SBUF | Seri Veri Tamponu | 99 | xxxx xxxx (??) |
| PCON | Güç Kontrolü | 87 | 0xxx 0000 (?0) |

Tanımlama:
^ = 80C52
\* = Bit adreslenebilir
x = Bilinmeyen durum

(Bkz http://www.rehn.org/YAM51/51set/regs.shtml)

**Paketleme**

Paketleme seçenekleri arasında

Plastik Uçlu Çip Kurye (PLCC)

Plastik İkili Hat İçi (P-DIP)

Plastik Dörtlü Düz Paket (PQFP)

Pencereli CERDIP bulunur.

**Yeni Ürünler**

Intel 8xC51RA/RB/RC, MCS51 mikrokontrolör mimarisi tabanlı yeni genişletilmiş RAM mikrokontrolör dizisine aittir. 8xC51RA/RB/RC mevcut MCS 51 mikrokontrolörlerle kod ve pim uyumludur ve mevcut MCS 51 mikrokontrolör yerine kullanılabilirler, ayrıca çip üstündeki RAM’e 512 bayt ve bir donanım kontrol zamanlayıcısı ekler.

(Bkz http://www.intel.com)

**KAYNAKLAR**

http://www.hc11.demon.nl/thrsim11/68hc11

http://www.motorola.com

Motorola Semiconductor Engineering Bulletin, By John Bodnar Austin, Texas

http://www.intel.com

8051 Architecture and Addressing Modes, Dr. Albert Levi

http://.www.rehn.org/YAM51/51set/instruction.shtml

Bkz http://www.rehn.org/YAM51/51set/regs.shtml

---
*Kaynak: `MİKROKONTROLÖR VE ÇALIŞMA ESASLARI/MİKROKONTROLÖR VE ÇALIŞMA ESASLARI.doc` — ulku — 2004*
