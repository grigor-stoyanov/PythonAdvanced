import re

with open('input.txt', 'r') as file:
    # symbols = ['-', ',', '.', '!', '?']
    for i, line in enumerate(file.readlines()):
        if i % 2 == 0:
            line = re.sub(r'[-,\.,!,?]', '@', line)
            # for symbol in symbols:
            #     line = line.replace(symbol, '@')
            words = line.split()
            # print(' '.join(reversed(words)))
            print(*words[-1::-1], sep=' ')