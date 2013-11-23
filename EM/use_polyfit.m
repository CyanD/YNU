X=[0 0.9 1.9 3 3.9 5];
Y=[0 10 30 50 80 110];
P=polyfit(X,Y,2);
y=polyval(P,X);
plot(X,Y,'r.','markersize',20);
hold on;
plot(X,y,'-g');
title('using polyfit to fit data');xlabel('x');ylabel('y');
legend('origin data','fit data','location','southeast');