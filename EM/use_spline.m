%Cubic spline interpolation
%date:1013-10-9
clear all;clc;
X=[1 2 3 4 5 6 7 8 9 10 11 12];%the given interpolation point
f=inline('sin(x)');%the function can be modified
[~,col]=size(X);
Y=zeros(1,col);
for i=1:col
    Y(1,i)=f(X(i));
end
xi=min(X):0.01:max(X);
yi=interp1(X,Y,xi,'spline');%Cubic spline interpolation
fplot(f,[min(X),max(X)],'r');
hold on;
plot(X,Y,'ro');
plot(xi,yi,'g');
hold off;