% get jpg: gasf, gadf, mtf and gafs-mtf
% get txt: name.txt eg: Coffee_test.txt Coffee_train.txt

%change this part ------------------------------------
mat_dir = 'cough_mat';
out_dir = 'cough_jpg'
%change this part -----------------------------------#

f = dir(mat_dir);
image_rgb = [];         % jpg image: R-gasf,G-gadf,B-mtf

for n = 1:length(f)
    if(~f(n).isdir)
        mat_name = f(n).name;
        mat_fn = fullfile(mat_dir,mat_name);
        fprintf('%06d: %d\t%s\n',length(f)-2,n-2,mat_fn);
        
        load(mat_fn);
        [row,~] = size(data);
        
        %row = 5; % debug
        for i=1:row
            data_3d = data(i,:);
            m = sqrt(length(data_3d)/3);
            gasf = data_3d(1:m*m);
            gadf = data_3d(m*m+1:m*m*2);
            mtf = data_3d(m*m*2+1:m*m*3);
            
            
            gasf = reshape(gasf,m,m);
            gadf = reshape(gadf,m,m);
            mtf = reshape(mtf,m,m);
            figure;imshow(mtf,'colormap',jet);
            
            image_rgb(:,:,1) = gasf;
            image_rgb(:,:,2) = gadf;
            image_rgb(:,:,3) = mtf;
            
            %jpg_name = strcat(sprintf('%06d',i),'.jpg');
            num_dot = strfind(mat_name,'.');
            %jpg_file = mat_name(1:num_dot-1);
            jpg_name = strcat(mat_name(1:num_dot-1),'.jpg');
            
            %jpg_dir = fullfile(out_dir,jpg_file);
            if ~exist(out_dir)
                mkdir(out_dir);
            end
            
            imwrite(image_rgb,fullfile(out_dir,jpg_name));
            
            %figure('visible','off');
            %imshow(image_rgb,'border','tight');
            %saveas(gcf,fullfile(jpg_dir,jpg_name),'jpg');
            
            fprintf('\toutput: %s %s\n',out_dir,jpg_name);
            
        end
        
    end
    
end



