function get_cough_noncougn_mat()
disp('-----------------------------------');
disp('get cough to mat...');
count = 0;
label = 'cough';

cough_dir0 = 'coughReview_0'; % change the dir path
count = get_mat(cough_dir0,label,count);

cough_dir1 = 'coughReview_1'; % change the dir path
count = get_mat(cough_dir1,label,count);
fprintf('\nDone! Get %s: %d\n',label,count);

disp('-----------------------------------');
disp('get noncough to mat...');
count = 0;
label = 'cough';

cough_dir0 = 'coughReview_0'; % change the dir path
count = get_mat(cough_dir0,label,count);

cough_dir1 = 'coughReview_1'; % change the dir path
count = get_mat(cough_dir1,label,count);
fprintf('\nDone! Get %s: %d\n',label,count);

end

function count = get_mat(cough_dir0,label,count)

wav_dir = fullfile(cough_dir0,label);
f = dir(wav_dir);
for i = 1:length(f)
    if(~f(i).isdir)
        wav_name = f(i).name;
        wav_fn = fullfile(wav_dir,wav_name);
        fprintf('%06d: %d\t%s\n',length(f)-2,i-2,wav_fn);
        
        [y,~] = audioread(wav_fn);
        y = y(1:2:end);
        %figure;plot(y);
        mat_dir = strcat(label,'_mat');
        if ~exist(mat_dir,'file')
            mkdir(mat_dir);
        end
        
        count = count + 1;
        mat_name = sprintf('%06d',count);
        save(fullfile(mat_dir,mat_name),'y');
        fprintf('\toutput: %s %s.mat\n',mat_dir,mat_name);

    end
end

end