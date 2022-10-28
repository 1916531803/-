%Harrison test Bjontegaard metric
clc; close all;
%%
%BD-rate����Ϊ����RD-cost���ߵ�ƽ������ƽ�����ֶ���Ϊ�����ߵ�������ֳ��Ի��������������ߵ�������ֳ��Ի�������֮�
%BD-rate��ʾ��ͬһ��Ƶ�͹�����������£����Ż����㷨��ԭʼ�㷨��ȵ�������������RD-cost��ˮƽ�ߣ���
%BD-rateΪ�����ʾ�Ż����㷨�ı������ܵõ�����ߡ�
%%
% ��������
%Aloe
R1 =[0.070353692;0.034234187;0.018423507;0.010005805];
R2 =[0.072462078;0.034586536;0.018799303;0.010414554];
R3 =[0.035142207;0.021952;0.01340133;0.006605749];
R4 =[0.03845968;0.02262144;0.0135033;0.006744028];
R5 =[0.052073223;0.02731475;0.014178167;0.007022231];
PSNR1 =[41.7629;39.1583;36.4319;33.6509];
PSNR2 =[42.3583;39.9379;37.4362;34.8009];
PSNR3 =[39.59443773;38.07888893;36.65291051;34.50818549];

PSNR4 =[40.49443773;38.67888893;37.085291051;34.40818549];
PSNR5 =[41.79443773;40.07888893;37.85291051;34.70818549];


%%
[row,col] = size(R1);%-------------------------------
%Ԥ����ռ�
rate1=zeros(1,row);
psnr1=zeros(1,row);
rate2=zeros(1,row);
psnr2=zeros(1,row);
rate3=zeros(1,row);
psnr3=zeros(1,row);
rate4=zeros(1,row);
psnr4=zeros(1,row);
rate5=zeros(1,row);
psnr5=zeros(1,row);
% ��������1
for i=1:row          
        rate1(:,i) = R1(i,1);%------------------------------------------
        psnr1(:,i) = PSNR1(i,1);%======================================
end
plot(rate1,psnr1,'c-o');
xlabel('bpp(bit per pixel)');
ylabel('Y-PSNR(dB)');
grid on;
hold on;
% ��������2
for i=1:row          
    rate2(:,i)=R2(i,1);%------------------------------------
    psnr2(:,i)=PSNR2(i,1);%=================================
end
plot(rate2,psnr2,'b-+');
grid on;
hold on;
% ��������3
for i=1:row          
    rate3(:,i)=R3(i,1);%------------------------------------
    psnr3(:,i)=PSNR3(i,1);%=================================
end
plot(rate3,psnr3,'g-s');


grid on;
hold on;

% ��������4
for i=1:row          
    rate4(:,i)=R4(i,1);%------------------------------------
    psnr4(:,i)=PSNR4(i,1);%=================================
end
plot(rate4,psnr4,'r-*');
% % ��������5
for i=1:row          
    rate5(:,i)=R5(i,1);%------------------------------------
    psnr5(:,i)=PSNR5(i,1);%=================================
end
plot(rate5,psnr5,'m-x');

% title('bickcle')

% title('dino')


% legend('Liu et al.','Chen et al.','Jia et al.','Proposed');    %���һ��������1~4��ʾλ��
hleg1=legend('PSC-Z','VVCALL','FLFRNet','LF-GAN','Proposed');

set(hleg1,'Location','SouthEast') 
% ����BDPSNR��
% Bj?ntegaard delta bit rate (BDBR) ��ʾ����ͬ���Ŀ͹������£�
% ���ַ��������ʽ�ʡ���(Rate/distortion curves ��һ��ˮƽ��)


% ����BDBR��(ע�����Ǳ仯�ٷֱ�)
% Bj?ntegaard delta peak signal-to-noise rate (BD-PSNR)��ʾ����
% ������ͬ�������£����ַ�����PSNR-Y�Ĳ���(Rate/distortion curves ��һ����ֱ��)��
BDPSNR_1 = bjontegaard(R1,PSNR1,R2,PSNR2,'dsnr');
BDBR_1 = bjontegaard(R1,PSNR1,R2,PSNR2,'rate');

BDPSNR_2 = bjontegaard(R1,PSNR1,R3,PSNR3,'dsnr');
BDBR_2 = bjontegaard(R1,PSNR1,R3,PSNR3,'rate');

BDPSNR_3 = bjontegaard(R1,PSNR1,R4,PSNR4,'dsnr');
BDBR_3 = bjontegaard(R1,PSNR1,R4,PSNR4,'rate');

BDPSNR_4 = bjontegaard(R1,PSNR1,R5,PSNR5,'dsnr');
BDBR_4 = bjontegaard(R1,PSNR1,R5,PSNR5,'rate');

