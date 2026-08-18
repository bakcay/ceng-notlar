# Dairede Poisson

!Bu program poisson denkleminin Gauss Seidel metodu ile sayısal çözümünü yapmaktadır.

!Programda çözüm birim boyutlardaki kare esas alınarak yapılmıştır.

!Programda kullanılan karakterlerler şunları ifade etmektedir:

! a= karenin başlangıç noktası

! b= karenin bitiş noktası

! m= aralık sayısı

! h= adım uzunluğu(aralık uzunluğu)

!f(x,y)=k\*(x(i)\*\*p)+l\*(y(j)\*\*r) şeklinde tanımlanmıştır. burada x ve y değişkenlerinin katasayıları ve üs değerleri istenildiği gibi seçilebilir.

! başlangıç şartları 'baslangic\_sartlari' adındaki alt programda tanımlanmıştır.

!problemde verilen başlangıç şartları x=0 için u=0, y=0 için u=0, y=1 için u=x\*\*2 ve x=1 için u=y\*\*2'dir.

PROGRAM GAUSS\_SEIDEL

dimension::u(200,200),x(200),y(200),xs(200),ys(200),c(200,200),e(200,200)

REAL::h,r,k,l,p,a1,a2,b1,b2,a(200,200),b(200,200)

integer::m,f,g,v,q,w,z,t,d

integer::n

print\*,' Kac adim araliginde islem yapmak istiyorsunuz?'

read\*,m

call baslangic\_sartlari(u,m)

!b karenin bitiş noktası , birbaşka deyişle karenin kenar uzunlığu olmak üzere:

!y=b noktasındaki sınır şartı u= (e\*y(j)\*\*f)+(g\*x(i)\*\*s)+v şeklinde tanımlanmıştır.

!x=b noktasındaki sınır şartı u= (q\*x(i)\*\*w)+(z\*y(j)\*\*t)+d şeklinde tanımlanmıştır.

call sinir\_sartlari(m,e,h,a,b,x,y,u,c,r,xs,ys)

print\*

print\*

print\*,'f(x,y)= (k\*x\*\*p)+(l\*y\*\*r)'

print\*

print\*,'x degiskeninin katsayisini giriniz...(k)='

read\*,k

print\*,'x degiskeninin us degerini giriniz...(p)='

read\*,p

print\*,'y degiskeninin katsayisini giriniz...(l)='

read\*,l

print\*,'y degiskeninin us degerini giriniz...(z)='

read\*,z

print\*,'Kac iterasyon yapmak istiyorsunuz?'

read\*,n

print\*,' 1. iterasyon= '

DO 10 j=2,m

DO 20 i=2, abs (floor((((r\*\*2)-(y(j)\*\*2))\*\*(0.5))/(-h)))

if (c(i,j).gt.h) then

if (e(i,j).gt.h) then

u(i,j)=(((u(i+1,j)+u(i-1,j)+u(i,j+1)+u(i,j-1))/4.0)-((k\*(x(i)\*\*p)+l\*(y(j)\*\*z))\*(h\*\*2))/4.0)

print\*,'u(',i,',',j,')=',u(i,j)

else if (e(i,j).lt.h) then

u(i,j)=( (u(i-1,j)/(2.0))+(u(i+1,j)/(2.0))+(u(i,abs (floor((((r\*\*2)-(x(i)\*\*2))\*\*(0.5))/(-h)))+1)/((b(i,j)\*(b(i,j)+1))))+(u(i,j-1)/((b(i,j)+1))-((h\*\*2)\*((x(i)\*\*p)+(y(j)\*\*z)))))/((1+b(i,j))/(b(i,j)))

print\*,'u(',i,',',j,')=',u(i,j)

end if

else if (c(i,j).lt.h) then

if (e(i,j).gt.h) then

u(i,j)=( (u(i-1,j)/(1+a(i,j)))+(u(abs (floor((((r\*\*2)-(y(j)\*\*2))\*\*(0.5))/(-h)))+1,j)/(a(i,j)\*(1+a(i,j))))+(u(i,j+1)/(2.0))+(u(i,j-1)/(2.0))-((h\*\*2)\*((x(i)\*\*p)+(y(j)\*\*z))))/((a(i,j)+1)/(a(i,j)))

print\*,'u(',i,',',j,')=',u(i,j)

else if(e(i,j).lt.h) then

u(i,j)=( (u(i-1,j)/((1+a(i,j))))+(u(abs (floor((((r\*\*2)-(y(j)\*\*2))\*\*(0.5))/(-h)))+1,j)/((a(i,j)\*(1+a(i,j )))))+(u(i,abs (floor((((r\*\*2)-(x(i)\*\*2))\*\*(0.5))/(-h)))+1)/((b(i,j)\*(b(i,j)+1))))+(u(i,j-1)/((b(i,j)+1)))-((h\*\*2)\*((x(i)\*\*p)+(y(j)\*\*z))))/((a(i,j)+b(i,j))/(b(i,j)\*a(i,j)))

print\*,'u(',i,',',j,')=',u(i,j)

end if

end if

20 CONTINUE

10 CONTINUE

icount=1

print\*,' 2. iterasyon= '

5 DO 70 j=2,m

DO 80 i=2,abs (floor((((r\*\*2)-(y(j)\*\*2))\*\*(0.5))/(-h)))

if (c(i,j).gt.h) then

if (e(i,j).gt.h) then

u(i,j)=(((u(i+1,j)+u(i-1,j)+u(i,j+1)+u(i,j-1))/4.0)-((k\*(x(i)\*\*p)+l\*(y(j)\*\*z))\*(h\*\*2))/4.0)

print\*,'u(',i,',',j,')=',u(i,j)

else if (e(i,j).lt.h) then

u(i,j)=( (u(i-1,j)/(2.0))+(u(i+1,j)/(2.0))+(u(i,abs (floor((((r\*\*2)-(x(i)\*\*2))\*\*(0.5))/(-h)))+1)/((b(i,j)\*(b(i,j)+1))))+(u(i,j-1)/((b(i,j)+1))-((h\*\*2)\*((x(i)\*\*p)+(y(j)\*\*z)))))/((1+b(i,j))/(b(i,j)))

print\*,'u(',i,',',j,')=',u(i,j)

end if

else if (c(i,j).lt.h) then

if (e(i,j).gt.h) then

u(i,j)=( (u(i-1,j)/(1+a(i,j)))+(u(abs (floor((((r\*\*2)-(y(j)\*\*2))\*\*(0.5))/(-h)))+1,j)/(a(i,j)\*(1+a(i,j))))+(u(i,j+1)/(2.0))+(u(i,j-1)/(2.0))-((h\*\*2)\*((x(i)\*\*p)+(y(j)\*\*z))))/((a(i,j)+1)/(a(i,j)))

print\*,'u(',i,',',j,')=',u(i,j)

else if(e(i,j).lt.h) then

u(i,j)=( (u(i-1,j)/((1+a(i,j))))+(u(abs (floor((((r\*\*2)-(y(j)\*\*2))\*\*(0.5))/(-h)))+1,j)/((a(i,j)\*(1+a(i,j )))))+(u(i,abs (floor((((r\*\*2)-(x(i)\*\*2))\*\*(0.5))/(-h)))+1)/((b(i,j)\*(b(i,j)+1))))+(u(i,j-1)/((b(i,j)+1)))-((h\*\*2)\*((x(i)\*\*p)+(y(j)\*\*z))))/((a(i,j)+b(i,j))/(b(i,j)\*a(i,j)))

print\*,'u(',i,',',j,')=',u(i,j)

end if

end if

80 CONTINUE

70 CONTINUE

icount=icount+1

print\*,'',icount+1,'. iterasyon='

if(icount.lt.n) go to 5

continue

end program gauss\_seidel

subroutine sinir\_sartlari(m,e,h,a,b,x,y,u,c,r,xs,ys)

dimension::u(200,200)

real::h,r,x(200),y(200),c(200,200),e(200,200),a(200,200),b(200,200),xs(200),ys(200)

integer::m

print\*,'dairenin uzunlugunu giriniz....r='

read\*,r

h=(r)/m

print\*,'h=',h

x(1)=0

y(1)=0

do 310 i=1,m+1

do 320 j=1,m+1

x(i+1)=x(i)+h

y(j+1)=y(j)+h

print\*,'x(',i,')=',x(i)

print\*,'y(',j,')=',y(j)

320 continue

310 continue

do 230 i=2,m

do 140 j=2,m

ys(i)=(((r\*\*2)-(x(i)\*\*2))\*\*(0.5))

xs(j)=(((r\*\*2)-(y(j)\*\*2))\*\*(0.5))

print\*,'xs(',j,')=',xs(j)

print\*,'ys(',i,')=',ys(i)

140 continue

230 continue

do 150 i=2,m

do 160 j=2,m

u(i,abs (floor((((r\*\*2)-(x(i)\*\*2))\*\*(0.5))/(-h)))+1)=x(i)\*ys(i)

u(abs (floor((((r\*\*2)-(y(j)\*\*2))\*\*(0.5))/(-h)))+1,j)=xs(j)\*y(j)

print\*,'u(',i,',sinir)=',u(i,abs (floor((((r\*\*2)-(x(i)\*\*2))\*\*(0.5))/(-h)))+1)

print\*,'u(sinir,',j,')=',u(abs (floor((((r\*\*2)-(y(j)\*\*2))\*\*(0.5))/(-h)))+1,j)

160 continue

150 continue

do 200 i=1,m

do 210 j=1,m

u(i,1)=0

u(1,j)=0

print\*,'u(',i,',1)=0',u(i,j)

print\*,'u(1,',j,')=0',u(i,j)

210 continue

200 continue

do 30 j=2,m

do 40 i= abs (floor((((r\*\*2)-(y(j)\*\*2))\*\*(0.5))/(-h))),abs (floor((((r\*\*2)-(y(j)\*\*2))\*\*(0.5))/(-h)))

if ((ys(i)-y(j)).lt.h) then

a(i,j)=(xs(j)-x(i))/h

b(i,j)=(ys(i)-y(j))/h

print\*,'a(',i,',',j,')=',a(i,j)

print\*,'b(',i,',',j,')=',b(i,j)

else

b(i,j)=1

a(i,j)=(xs(j)-x(i))/h

print\*,'a(',i,',',j,')=',a(i,j)

print\*,'b(',i,',',j,')=',b(i,j)

end if

40 continue

30 continue

do 130 i=2,m

do 240 j= abs (floor((((r\*\*2)-(x(i)\*\*2))\*\*(0.5))/(-h))),abs (floor((((r\*\*2)-(x(i)\*\*2))\*\*(0.5))/(-h)))

if ((xs(j)-x(i)).lt.h) then

a(i,j)=(xs(j)-x(i))/h

b(i,j)=(ys(i)-y(j))/h

print\*,'a(',i,',',j,')=',a(i,j)

print\*,'b(',i,',',j,')=',b(i,j)

else

a(i,j)=1

b(i,j)=(ys(i)-y(j))/h

print\*,'a(',i,',',j,')=',a(i,j)

print\*,'b(',i,',',j,')=',b(i,j)

end if

240 continue

130 continue

do 115 i=2,abs (floor((((r\*\*2)-(y(m)\*\*2))\*\*(0.5))/(-h)))-1

do 125 j=m,m

b(i,j)=(ys(i)-y(j))/h

print\*,'b(',i,',',j,')=',b(i,j)

125 continue

115 continue

do 440 j=2,m

do 450 i=2,abs (floor((((r\*\*2)-(y(j)\*\*2))\*\*(0.5))/(-h)))

c(i,j)=xs(j)-x(i)

print\*,'c(',i,',',j,')=',c(i,j)

450 continue

440 continue

do 540 i=2,m

do 550 j=2,abs (floor((((r\*\*2)-(x(i)\*\*2))\*\*(0.5))/(-h)))

e(i,j)=ys(i)-y(j)

print\*,'e(',i,',',j,')=',e(i,j)

550 continue

540 continue

return

end

subroutine baslangic\_sartlari(u,m)

dimension::u(200,200)

integer::m

do 50 i=2,m

do 60 j=2,m-i+3

u(i,j+i-3)=0

print\*,'u(',i,',',j,')=',u(i,j)

60 continue

50 continue

return

end

---
*Kaynak: `DAİREDE POİSSON/DAİREDE POİSSON/dairede poisson.doc` — BERK AYVAZ — 2004*
