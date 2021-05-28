<<<<<<< HEAD
from collections import deque

kids = deque(input().split())
n = int(input())
while not len(kids) == 1:
    # for i in range(0, n-1):
    #     kids.append(kids.popleft())
    kids.rotate(-(n-1))
    print(f'Removed {kids.popleft()}')
print(f'Last is {kids[0]}')
=======
from collections import deque

kids = deque(input().split())
n = int(input())
while not len(kids) == 1:
    # for i in range(0, n-1):
    #     kids.append(kids.popleft())
    kids.rotate(-(n-1))
    print(f'Removed {kids.popleft()}')
print(f'Last is {kids[0]}')
>>>>>>> 7e8381d627bc725b2be27de4d386243fc039cd29
