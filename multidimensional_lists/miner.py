from collections import deque


def move(mat, cmd, pos, mined):
    x, y = pos
    escaped = False
    movement = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
    x_off, y_off = movement.get(cmd, (0, 0))
    x += x_off
    y += y_off
    if not 0 <= x < n or not 0 <= y < n:
        return mat, pos, mined, escaped
    else:
        if mat[x][y] == 'c':
            mat[x][y] = '*'
            mined += 1
        elif mat[x][y] == 'e':
            escaped = True
        pos = (x, y)
        return mat, pos, mined, escaped


n = int(input())
commands = deque(input().split())
field = []
start = tuple()
escapes = []
coals = 0
for i in range(n):
    field.append(input().split())
    for j in range(n):
        if field[i][j] == 'c':
            coals += 1
        elif field[i][j] == 's':
            start = (i, j)
position = start
mined = 0
while commands:
    field, position, mined, escaped = move(field, commands.popleft(), position, mined)
    if mined == coals:
        print(f"You collected all coals! ({position[0]}, {position[1]})")
        exit(0)
    elif escaped:
        print(f"Game over! ({position[0]}, {position[1]})")
        exit(0)
print(f"{coals - mined} coals left. ({position[0]}, {position[1]})")
