from collections import deque

kids = deque(input().split())
n = int(input())
while not len(kids) == 1:
    # for i in range(0, n-1):
    #     kids.append(kids.popleft())
    kids.rotate(-(n-1))
    print(f'Removed {kids.popleft()}')
print(f'Last is {kids[0]}')
