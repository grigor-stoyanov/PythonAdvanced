import os

dir_path = input('Enter directory: ')
_, _, files = next(os.walk(dir_path))
file_types = {}
for file in files:
    name, ext = file.split('.')
    file_types[ext] = file_types.get(ext, []) + [name]
file_types = dict(sorted(file_types.items(), key=lambda x: x[0]))
file_types = {key: list(sorted(value)) for key, value in file_types.items()}
with open(f'C:\\Users\\{os.getlogin()}\\Desktop\\report.txt', 'w+') as output:
    for ext, names in file_types.items():
        output.write(ext + '\n- - -' + '\n- - -'.join(names) + '\n')
