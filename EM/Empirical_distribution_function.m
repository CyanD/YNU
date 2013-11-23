X=normrnd(0,1,1000,1);%Randomly generat 1000 rows and 1 colums normal numbers
[h,stats]=cdfplot(X);%h:huanbing,stats:min,max,std,mean,median
hold on;
plot(-3:0.01:3,normcdf(-3:0.01:3,0,1),'r');%normcdf:to draw Standard normal distribution function image