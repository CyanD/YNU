%Multidimensional data distribution test
%X=[data], rows: Number of samples, col: Dimension
%QQ image
X=normrnd(0,1,100,4);
[N,P]=size(X);
d=mahal(X,X);
d1=sort(d);
pt=[[1:N]-0.5]/N;
x2=chi2inv(pt,P);
plot(d1,x2','*',[0:max(d1)],[0:max(d1)],'-r');