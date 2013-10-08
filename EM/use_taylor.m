%the given function f(x)=x^0.5, solve f(115),if x0=100
%using taylor interpolation
%author:HYC
%date:2013-10-8
f=inline('x^(1/2)');%thie given funcion
p1=inline('5+0.05*x');%Time interpolation
p2=inline('10+1/20*(x-100)-1/4000/2*(x-100)^2');%Quadratic interpolation
X1=[-50,300];X2=[-30,300];
subplot(1,2,1);
fplot(f,X1,'r');
hold on;
fplot(p1,X1);
plot(115,10.75,'*');
line([115,115],[0,10.75]);%caution:line from [115,0] to [115,10.75]
subplot(1,2,2);
fplot(f,X2,'r');
hold on;
fplot(p2,X2);
plot(115,10.72,'*');
line([115,115],[0,10.72]);