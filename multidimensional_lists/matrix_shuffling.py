rows, cols = map(int, input().split())
mat = []
temp = 0
for i in range(rows):
    mat.append(input().split())
command = input()
while not command == 'END':
    cmd, *cords = command.split()
    if cmd == 'swap' and len(cords) == 4:
        x1, y1, x2, y2 = list(map(int, cords))
        if (x1 and x2) <= rows - 1 and (y1 and y2) <= cols -1:
            mat[x1][y1], mat[x2][y2] = mat[x2][y2], mat[x1][y1]
            for i in range(rows):
                for j in range(cols):
                    print(mat[i][j], end=" ")
                print()
            command = input()
            continue
    print('Invalid input!')
    command = input()
