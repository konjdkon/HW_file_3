import pathlib

file_size_dict = {}
currentDirectory = pathlib.Path(f'{pathlib.Path.cwd()}\\files')
total_file_path = f'{pathlib.Path.cwd()}\\total\\total.txt'
open(total_file_path, 'w').close()

for currentFile in currentDirectory.iterdir():
    with open(currentFile, 'r', encoding='utf8') as f:
        file_size_dict[currentFile] = sum(1 for line in f)

s = [file_size_dict[i] for i in sorted(file_size_dict, key=file_size_dict.__getitem__)]
key_list = list(file_size_dict.keys())
val_list = list(file_size_dict.values())

total_f = open(total_file_path, 'a', encoding='utf8')
for i in range(len(s)):
    filename = key_list[val_list.index(s[i])]
    with open(filename, 'r', encoding='utf8') as f:
        total_f.write(str(filename.name) + '\n' + str(s[i]) + '\n')
        for line in f:
            total_f.write(line.strip() + '\n')
total_f.close()