% run this function directly on console to render all sequences
function generate_all_sequences()

%% list sequence folders
seqs = dir('datasets/depth/');
dirFlags = [seqs.isdir];
seq_folders = seqs(dirFlags);

n_elem = numel(seq_folders);
seq_names = cell(1, n_elem-2);
start_idx = 3;

for i=start_idx:n_elem
    seq_names{i-2} = seq_folders(i).name;
end 


%% generate sequences
n_seqs = numel(seq_names);
for i=1:n_seqs
    name = char(seq_names(i));
    data_augmentation_batch(name, 512)
end


%% end function
end



