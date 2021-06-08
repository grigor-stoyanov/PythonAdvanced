command = input()
line = input().split()
count = len(line)
line = map(int, line)
if command == "Odd":
    line = count * sum(filter(lambda x: True if x % 2 == 1 else False, line))
elif command == 'Even':
    line = count * sum(filter(lambda x: True if x % 2 == 0 else False, line))
print(line)
