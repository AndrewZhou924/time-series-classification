% get jpg: gasf, gadf, mtf and gafs-mtf
% get txt: name.txt eg: Coffee_test.txt Coffee_train.txt

mat_dir = 'mat3d';
f = dir(mat_dir);
image_rgb = [];         % jpg image: R-gasf,G-gadf,B-mtf

for n =1:length(f)
    if(~f(n).isdir)
        mat_name = f(n).name;
        mat_fn = fullfile(mat_dir,mat_name);
        fprintf('%03d: %d\t%s\n',length(f)-2,n-2,mat_fn);
        
        load(mat_fn);
        [row,~] = size(data);
        %row = 5; % debug
        for i=1:row
            data_3d = data(i,:);
            
            gasf = data_3d(1:64*64);
            gadf = data_3d(64*64+1:64*64*2);
            mtf = data_3d(64*64*2+1:64*64*3);
            
            gasf = reshape(gasf,64,64);
            gadf = reshape(gadf,64,64);
            mtf = reshape(mtf,64,64);
            
            image_rgb(:,:,1) = gasf;
            image_rgb(:,:,2) = gadf;
            image_rgb(:,:,3) = mtf;
            
            jpg_name = strcat(sprintf('%06d',i),'.jpg');
            num_dot = strfind(mat_name,'.');
            jpg_file = mat_name(1:num_dot-1);
            
            jpg_dir = fullfile('JPG',jpg_file);
            if ~exist(jpg_dir)
                mkdir(jpg_dir);
            end
            
            imwrite(image_rgb,fullfile(jpg_dir,jpg_name));
            
            %figure('visible','off');
            %imshow(image_rgb,'border','tight');
            %saveas(gcf,fullfile(jpg_dir,jpg_name),'jpg');
            
            fprintf('\toutput: %s %s\n',jpg_dir,jpg_name);
            
        end
        
    end
    
end



