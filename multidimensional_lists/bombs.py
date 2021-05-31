def explode(pos, field):
    x, y = pos
    if field[x][y] <= 0:
        return field
    x_offset = [1, -1, 1, -1, 0, 1, -1, 0]
    y_offset = [1, -1, -1, 1, 1, 0, 0, -1]
    for i in range(8):
        x_pos = x + x_offset[i]
        y_pos = y + y_offset[i]
        if 0 <= x_pos < len(field) and 0 <= y_pos < len(field):
            if field[x_pos][y_pos] > 0:
                field[x_pos][y_pos] -= field[x][y]
    field[x][y] = 0
    return field


n = int(input())
mat = [list(map(int, input().split())) for i in range(n)]
bombs = [tuple(map(int, ele.split(','))) for ele in input().split()]
aliveCells = 0
sumofCells = 0
for bomb in bombs:
    mat = explode(bomb, mat)
for i in range(n):
    for j in range(n):
        if mat[i][j] > 0:
            aliveCells += 1
            sumofCells += mat[i][j]
print(f'Alive cells: {aliveCells}')
print(f'Sum: {sumofCells}')
for i in range(n):
    for j in range(n):
        print(mat[i][j], end=" ")
    print()
