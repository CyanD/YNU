%Newton interpolation
%date: 2013-10-8
clear all;clc;
X=input('x1,x2,...,xn=? vector:');
Y=input('y1,y2,...,yn=? vector:');
[~,col1]=size(X);[~,col2]=size(Y);
if col1~=col2
    disp('Input data Error!');
    return;
end
x0=input('The interpolation point x0 : ');
n=col1;
F=Y;
for i=1:n-1
    for k=n:-1:i+1
        F(k)=(F(k)-F(k-1))/(X(k)-X(k-i));
    end
end
syms t;
p=Y(1);
for i=2:n
    l=1;
    for j=1:i-1
        l=l*(t-X(j));
    end
    p=p+l*F(i);
end
p=inline(p);
fplot(p,[min(min(X),x0)-1,max(max(X),x0)+1]);
hold on;
plot(X,Y,'o',x0,p(x0),'r*');
hold off;
disp('The value in the point x0 is:');
disp(p(x0));