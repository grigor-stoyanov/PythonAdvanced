line = filter(lambda x: True if x % 2 == 0 else False, map(int, input().split()))
print(list(line))
