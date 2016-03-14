function my_get_txt()
%disp(' ----------------------------');
%disp('Get txt: "_TRAIN"');
%backend = '_TRAIN';
%txt_backend = '_train';
%get_txt(backend,txt_backend)
disp(' ----------------------------');
disp('Get txt: "_TEST"');
backend = '_TEST';
txt_backend = '_test';
get_txt(backend,txt_backend)

end

function get_txt(backend,txt_backend)

data_table = {'Lighting2', 'Lighting7', 'Coffee','Beef','ECG200','50words', ...
            'Adiac','FaceAll', 'OliveOil', 'OSULeaf','SwedishLeaf', 'CBF', ...
            'FaceFour', 'FISH', 'Gun_Point',  'Trace', 'Two_Patterns', 'wafer', 'yoga'};
%data_table = {'CBF','Coffee'};

data_file = 'UCRdata';



for i=1:length(data_table)
    data_name = strcat(data_table{i},backend);
    data_dir = fullfile(data_file,data_table{i},data_name);
    
    fprintf('%03d: %d\n\t%s\t%s\n',length(data_table),i,data_dir,data_name);
    
    data = load(data_dir);
    label = data(:,1);
    % label begin with 0
    if min(label)
        label = label-min(label);
    end
    
    data_name1 = strcat(data_table{i},txt_backend);
    txt_name = strcat(data_name1,'.txt');
    txt_dir = fullfile('JPG',data_name1);
    
    % if txt exist, delete it
    if exist(fullfile(txt_dir,txt_name),'file')
        %disp('yes');
        delete(fullfile(txt_dir,txt_name));
    end
        
    fid = fopen(fullfile(txt_dir,txt_name),'a');
    
    for j=1:length(label)
        fprintf(fid,'/%06d.jpg %d\n',j,label(j));
    end
    fclose(fid);
    
end

end
