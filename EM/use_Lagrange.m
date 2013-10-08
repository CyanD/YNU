%lagrange interpolation
%author:HYC
%date:2013-10-8
clear all;clc;
%input data
X=input('x1,x2,...,xn=?(n-dimensional transverse vector):');
Y=input('y1,y2,...,yn=?(n-dimensional transerse vector):');
x0=input('the interpolation point:');%the interpolation point x0
[~,col1]=size(X);[~,col2]=size(Y);
if(col1~=col2)
    disp('Input Error! Try again please.');
    return;
end
n=col1;
syms t;
p=0;
for k=1:n
    l=1;
    for j=1:k-1
        l=l*(t-X(j))/(X(k)-X(j));
    end
    for j=k+1:n
        l=l*(t-X(j))/(X(k)-X(j));
    end
    p=p+l*Y(k);
end
p=inline(p);%to convert the sybolic variables p to a function
fplot(p,[min(min(X),x0)-1,max(max(X),x0)+1]);
hold on
plot(X,Y,'o',x0,p(x0),'r*');
hold off
disp('The value in the point x0 is:');
disp(p(x0));