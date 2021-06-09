file = open('numbers.txt')
result = 0
# directly iterates trough the rows in the file as a list of strings
for line in file:
    result += int(line)
print(result)
# print(sum([int(line) for ele in open('numbers.txt')]))
