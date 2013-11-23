%Normality test methods
is_norm_small_data=normrnd(0,1,100,1);
is_norm_big_data=normrnd(0,1,100000,1);
isnot_norm_small_data=rand(100,1);
isnot_norm_big_data=rand(100000,1);
%(1).Jarque-Bera test:jbtest, use for big data
alpha=0.05;
H1=jbtest(isnot_norm_big_data,alpha);
H2=jbtest(is_norm_big_data,alpha);
disp(H1);disp(H2);%1:no,0:yes

%(2).Kolmogorov-Smirnov test:kstest, just for standard norm
H1=kstest(isnot_norm_big_data);
H2=kstest(is_norm_big_data);
disp(H1);disp(H2);%1:no,0:yes

%(3).Lilliefors test:lillietest, use for small data(<10000)
alpha=0.05;
H1=lillietest(isnot_norm_small_data,alpha);
H2=lillietest(is_norm_small_data,alpha);
disp(H1);disp(H2);%1:no,0:yes