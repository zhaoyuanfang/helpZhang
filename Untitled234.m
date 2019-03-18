clear
K_left=xlsread('K_left.csv');
hc=xlsread('hc.csv');



K=hc'*K_left*hc;


Kaa=K(253:378,253:378);
Ktt=K(127:252,127:252);
Kta=K(127:252,253:378);
Kat=K(253:378,127:252);

K1=(Kaa^-1*Kat-Kta^-1*Ktt)^-1;
