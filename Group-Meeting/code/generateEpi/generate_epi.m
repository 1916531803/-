%Harrison 生成epi 
anNum=7 %角度分辨率
isFlag=0 %0代表取水平EPI，1代表取垂直EPI
pixValue=250 %取像素点的值
anValue=2 %取第几
h=368
w=536

if (isFlag==0)
    for ky=anValue
            for kx=1:anNum       

                I = imread(['C:/Users/Harrison/Desktop/GroupMeeting/Stanford/sampleReorder/Aloe/f_b_' sprintf('%03d',(ky-1)*anNum+kx) '.png']);
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

                I = imread(['C:/Users/Harrison/Desktop/GroupMeeting/Stanford/sampleReorder/Aloe/f_b_' sprintf('%03d',(ky-1)*anNum+kx) '.png']);
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
imshow(Epi_map);
axis on
xticks([])
yticks([])