clear all;clc;
syms n;
y1='4*n^2';
y2='log2(n)';
y3='3^n';
y4='20*n';
y5='2';
y6='n^(2/3)';
color=['y','m','c','r','b','g','k'];
n=10;
N=[1,n];
hold on;
fplot(y2,N,color(2));
fplot(y5,N,color(5));
fplot(y6,N,color(6));
title('Time complexity');xlabel('n');ylabel('f(n)');
legend(y2,y5,y6,'location','Northwest');