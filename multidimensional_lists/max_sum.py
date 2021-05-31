import sys

row, col = tuple(map(int, input().split()))
mat = []
max_sum = -sys.maxsize
mat_sum = 0
for i in range(row):
    line = input().split()
    mat.append([int(line[j]) for j in range(col)])
for i in range(2, row):
    for j in range(2, col):
        mat_sum = mat[i][j] + mat[i - 1][j] + mat[i - 2][j] \
                  + mat[i][j - 1] + mat[i - 1][j - 1] + mat[i - 2][j - 1] \
                  + mat[i][j - 2] + mat[i - 1][j - 2] + mat[i - 2][j - 2]
        if mat_sum > max_sum:
            max_sum = mat_sum
            max_cords = (i, j)
print(f"Sum = {max_sum}")
for i in range(max_cords[0] - 2, max_cords[0] + 1):
    for j in range(max_cords[1] - 2, max_cords[1] + 1):
        print(mat[i][j], end=' ')
    print()