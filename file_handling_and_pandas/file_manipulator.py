import os
from os import path

while not (command := input()) == 'End':
    cmd, *file_properties = command.split('-')
    file_name = file_properties[0]
    if cmd == 'Create':
        file = open(file_name, 'w')
        file.close()
    elif cmd == 'Add':
        file_name, content = file_properties
        with open(file_name, 'a+') as file:
            file.write(content + '\n')
    elif cmd == 'Replace':
        file_name, old_string, new_string = file_properties
        if path.exists(file_name):
            with open(file_name) as file:
                content = file.read()
                content = content.replace(old_string, new_string)
                # lines = []
                # for line in file:
                #     lines.append(line.replace(old_string, new_string))
            with open(file_name, 'w') as file:
                file.write('\n'.join(content))
        else:
            print('An error has occurred')
    elif cmd == 'Delete':
        try:
            os.remove(file_name)
        except FileNotFoundError:
            print('An error has occurred')
