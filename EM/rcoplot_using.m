clear all;clc;
Y=[143 145 146 147 149 150 153 154 155 156 157 158 159 160 162 164];
X=[88 85 88 91 92 93 93 95 96 98 97 96 98 99 100 102];
plot(X,Y,'*-');figure
[~,n]=size(X);
XX=[ones(n,1),X'];
%b=regress(Y',XX);
[b,bint,r,rint,s]=regress(Y',XX);
b,bint,s,
rcoplot(r,rint)

