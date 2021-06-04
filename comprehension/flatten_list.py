line = input().split(*'|')
flat = [num for ele in reversed(line) for num in ele.split()]
print(*flat)