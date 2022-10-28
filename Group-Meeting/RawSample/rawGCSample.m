%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% generate test data from lytro dataset (30scenes/Occlusions/Reflective)
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% uint8 0-255
% ['LFI_ycbcr']   [3,w,h,aw,ah,N]
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
clear; close all;
%% path
dataset = 'img';
folder = ''; 
listname = sprintf('Test_%s.txt',dataset);
f = fopen(listname);
if( f == -1 )
    error('%s does not exist!', listname);
end
C = textscan(f, '%s', 'CommentStyle', '#');
list = C{1};
fclose(f); 

%% params
H = 368;
W = 536;  

allah = 14;
allaw = 14;

ah = 8;
aw = 8;

%% initialization
LFI_ycbcr = zeros(H, W, 3, ah, aw, 1, 'uint8');
count = 0;

%% generate data
for k = 1:length(list)
    lfname = list{k};
    lf_path = sprintf('%s.png',lfname);
    disp(lf_path)
    savepath = sprintf('C:/Users/Harrison/Desktop/GroupMeeting/Stanford/sample/%s',lfname)
    if exist(savepath)==0
        mkdir(savepath);
    end
    eslf = im2uint8(imread(lf_path));  
    img_ycbcr = zeros(H,W,3,allah,allaw,'uint8');    

    for v = 4 : 10
        for u = 4 : 10            
            sub = eslf(v:allah:end,u:allah:end,:);          
            imwrite(sub(1:H,1:W,:),[savepath,'/','result_',num2str(v),'_',num2str(u),'.png']);                   
        end
    end
end  
