path = 'C:/Users/Harrison/Desktop/GEO';
dataDir = fullfile(path, 'data'); % data目录
files = dir(fullfile(path, '*.png'));
H = 368;
W = 536;  
allah = 14;
allaw = 14;
ah = 7;
aw = 7;
for k = 1:numel(files)
    file = files(k).name;
    if endsWith(file, '.png', 'IgnoreCase', true)
        I = im2uint8(imread(fullfile(path, file)));
        % 这里可以继续处理图像I
        % 创建文件名的目录
        [~, filename, ~] = fileparts(file);
        outputDir = fullfile(dataDir, filename);

        if ~exist(outputDir, 'dir')
            mkdir(outputDir); % 如果目录不存在，则创建它
        end
        for v = 5 : 11
            for u = 5 : 11            
            sub =I(v:allah:end,u:allah:end,:); 
            % 构建输出文件路径
            outputFilePath = fullfile(outputDir, ['result_', num2str(v), '_', num2str(u), '.png']);

        % 保存图像
            imwrite(I(1:H, 1:W, :), outputFilePath);
%             imwrite(sub(1:H,1:W,:),['C:/Users/Harrison/Desktop/几何感知/data','/','occlusions_1_eslf','/','result_',num2str(v),'_',num2str(u),'.png']);            
            end
        end
    end
end


