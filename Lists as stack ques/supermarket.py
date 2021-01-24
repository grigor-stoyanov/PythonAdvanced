from collections import deque

cmd = input()
que = deque()
while not cmd == 'end':
    if not cmd == 'paid':
        que.append(cmd)
    else:
        for name in que:
            print(name.popleft())
    cmd = input()
print(f'{len(que)} people still in que')
