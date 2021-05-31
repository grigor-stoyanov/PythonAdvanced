n = int(input())
mat = []
prim_diag = 0
second_diag = 0
for _ in range(n):
    mat.append(list(map(int, input().split())))
for i in range(n):
    prim_diag += mat[i][i]
for i in range(1, n + 1):
    second_diag += mat[-i][i - 1]
print(abs(prim_diag - second_diag))
