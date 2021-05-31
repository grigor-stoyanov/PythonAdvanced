def player_move(mat, psn, command):
    x, y = psn
    moves = {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)}
    x_off, y_off = moves.get(command, (0, 0))
    x += x_off
    y += y_off
    if 0 <= x < n and 0 <= y < m:
        mat[x, y] = 'P'
        mat[x - x_off][y - y_off] = '.'
        psn = (x, y)
        return lair, psn
    else:
        return lair, psn


def bunnies_move(mat):
    x_off = [0, 0, 1, -1]
    y_off = [1, -1, 0, 0]
    for i in range(n):
        for j in range(m):
            if mat[i][j] == 'B':
                for k in range(4):
                    if 0 <= i + x_off[k] < n and 0 <= j + y_off[k] < m:
                        mat[i+x_off][j+y_off] = 'B'
    return lair


n, m = list(map(int, input().split()))
lair = []
for i in range(n):
    lair.append(list(input()))
    for j in lair[i]:
        if lair[i][j] == 'P':
            position = (i, j)
commands = input()
for command in commands:
    lair, position = player_move(lair, position, command)
    lair = bunnies_move(lair)
    if player_dead():
        print(f"dead: {position[0],position[1]}")
        exit(0)
while not player_dead()