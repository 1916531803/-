%Harrison 生成epi 
anNum=7 %角度分辨率
isFlag=1 %0代表取水平EPI，1代表取垂直EPI
pixValue=250 %取像素点的值
anValue=2 %取第几
h=368
w=536
img_path = 'C:/Users/Harrison/Desktop/GroupMeeting/Stanford/sampleReorder'; 

dataset = 'img';
listname = sprintf('Test_%s.txt',dataset);
f = fopen(listname);
if( f == -1 )
    error('%s does not exist!', listname);
end
C = textscan(f, '%s', 'CommentStyle', '#');
list = C{1};
fclose(f); 

for k = 1:length(list)
    lfname = list{k};
              
    if (isFlag==0)
        for ky=anValue
                for kx=1:anNum       
%                     I = imread(['C:/Users/Harrison/Desktop/GroupMeeting/Stanford/sampleReorder/Aloe/f_b_' sprintf('%03d',(ky-1)*anNum+kx) '.png']);
                    lf_path = sprintf('%s/%s/f_b_%03d.png',img_path,lfname,(ky-1)*anNum+kx);
                    disp(lf_path)
                    I = imread(lf_path);
                    TT(kx,ky,:,:,:) = I;

                end
        end
        Epi_map=zeros(anNum,w,3);
        for u=1:anNum
            for v=anValue
             Epi_map(u,1:w,:)=TT(u,v,pixValue,:,:);

            end
        end
    end

    if (isFlag==1)
        for ky=1:anNum 
                for kx=anValue       
%                     I = imread(['C:/Users/Harrison/Desktop/GroupMeeting/Stanford/sampleReorder/Aloe/f_b_' sprintf('%03d',(ky-1)*anNum+kx) '.png']);
                    lf_path = sprintf('%s/%s/f_b_%03d.png',img_path,lfname,(ky-1)*anNum+kx);
                    disp(lf_path)
                    I = imread(lf_path);
                    TT(kx,ky,:,:,:) = I;
                end
        end
        Epi_map=zeros(anNum,h,3);
        for u=anValue 
            for v=1:anNum
             Epi_map(v,1:h,:)=TT(u,v,:,pixValue,:);

            end
        end
    end
    Epi_map=uint8(squeeze(Epi_map));
    figure(1)%green
    epi_path=sprintf('C:/Users/Harrison/Desktop/GroupMeeting/Stanford/EPI/%s',lfname)
    if exist(epi_path)==0
        mkdir(epi_path);
    end
    savepath=sprintf('%s/%s_Epi.png',epi_path,lfname)
    imwrite(Epi_map,savepath)
    imshow(Epi_map);
    axis on
    xticks([])
    yticks([])
end
