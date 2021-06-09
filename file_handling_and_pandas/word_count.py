import re

result = {}
with open('words.txt', 'r') as key_words, open('input.txt', 'r') as text:
    keys = key_words.read().split()
    lines = text.readlines()
    for word in keys:
        result[word] = len(re.findall(r'(?i)\b%s\b' % word, '\n'.join(lines)))
with open('output.txt', 'w') as output:
    result = {k: v for k, v in sorted(result.items(), key=lambda x: -x[1])}
    for key,value in result.items():
        output.write(f'{key} - {value}\n')