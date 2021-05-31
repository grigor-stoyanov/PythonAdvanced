row, col = tuple(map(int, input().split()))
mat = []
counter = 0
mat_set = set()
for i in range(row):
    line = input().split()
    mat.append([line[j] for j in range(col)])
for i in range(1, row):
    for j in range(1, col):
        mat_set = {mat[i][j], mat[i - 1][j - 1], mat[i][j - 1], mat[i - 1][j]}
        if len(mat_set) == 1:
            counter += 1
        mat_set.clear()
print(counter)
