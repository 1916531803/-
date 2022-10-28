%Harrison
clear; close all;
%% path
dataset = 'img';
RA='RA37';
folder = 'C:/Users/Harrison/Desktop/GroupMeeting/Stanford/reconstruction'; 
savepath = sprintf('C:/Users/Harrison/Desktop/GroupMeeting/LF-R/LFData/test_%s.h5',RA);

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

ah = 7;
aw = 7;

%% initialization
LFI_ycbcr = zeros(H, W, 3, ah, aw, 1, 'uint8');
count = 0;

%% generate data
 
img_ycbcr = zeros(H,W,3,ah,aw,'uint8');    
for k = 1:length(list)
    lfname = list{k};
    for v = 4 : 10
        for u = 4 : 10   
            lf_path = sprintf('%s/%s/result_%d_%d.png',folder,lfname,v,u);
            disp(lf_path)
    
            eslf = im2uint8(imread(lf_path)); 

            sub = rgb2ycbcr(eslf);  
          
            img_ycbcr(:,:,:,v,u) = sub(1:H,1:W,:);           
        end
    end
        
    img_ycbcr = img_ycbcr(:,:,:,4:10,4:10); %[H,W,3,ah,aw]

    count = count+1;    
    LFI_ycbcr(:, :, :, :, :, count) = img_ycbcr;
end    
%% generate dat
LFI_ycbcr = permute(LFI_ycbcr,[3,2,1,5,4,6]);

%% save data
if exist(savepath,'file')
  fprintf('Warning: replacing existing file %s \n', savepath);
  delete(savepath);
end 

h5create(savepath,'/LFI_ycbcr',size(LFI_ycbcr),'Datatype','uint8');
h5write(savepath, '/LFI_ycbcr', LFI_ycbcr);

h5disp(savepath);