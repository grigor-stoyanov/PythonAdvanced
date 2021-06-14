import re

with open('input.txt', 'r') as file, open('output.txt', 'a') as output:
    for line_num, line in enumerate(file.readlines()):
        marks = len(re.findall(f"[-,\\.!?']", line))
        # chars = sum([len(word) for word in line.split()])
        # marks = len(list(filter(lambda x: x in "-,.!?'", line)))
        chars = len(''.join(line.split())) - marks
        output.write(f'Line {line_num + 1}: {line} ({chars})({marks})\n')
