dirs = {
    'right': lambda x, y: (x, y + 1),
    'left': lambda x, y: (x, y - 1),
    'up': lambda x, y: (x - 1, y),
    'down': lambda x, y: (x + 1, y)
}


def moving(field, dir, steps, pos):
    x, y = pos
    for i in range(steps):
        x, y = dirs[dir](x, y)
        if 0 <= x < len(field) and 0 <= y < len(field):
            continue
        else:
            return field, pos
    if field[x][y] == '.':
        field[pos[0]][pos[1]] = '.'
        field[x][y] = 'A'
        pos = (x, y)
    return field, pos


def shooting(field, dir, tar, pos):
    x, y = pos
    while True:
        x, y = dirs[dir](x, y)
        if 0 <= x < len(field) and 0 <= y < len(field):
            if field[x][y] == 'x':
                field[x][y] = '.'
                tar.append([x, y])
                break
        else:
            break
    return field, tar


field = [input().split() for i in range(5)]
num = int(input())
tars = []
tars_count = len(['x' for i in range(5) for j in range(5) if field[i][j] == 'x'])
my_pos = [(i, j) for i in range(5) for j in range(5) if field[i][j] == 'A']
for _ in range(num):
    cmd, *attr = input().split()
    if cmd == 'move':
        dir, steps = attr
        steps = int(steps)
        field, *my_pos = moving(field, dir, steps, *my_pos)
    elif cmd == 'shoot':
        dir = attr[0]
        field, tars = shooting(field, dir, tars, *my_pos)
        if tars_count == len(tars):
            print(f"Training completed! All {tars_count} targets hit.")
            break
if tars_count - len(tars) > 0:
    print(f"Training not completed! {tars_count - len(tars)} targets left.")
if tars:
    print(*tars, sep='\n')
