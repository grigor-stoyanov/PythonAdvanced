def read_matrix(istest=False):
    mat = []
    if not istest:
        (rows, coulmns) = map(int, input().split(', '))
        for i in range(rows):
            row = list(map(int, input().split(', ')))
            mat.append(row)
    else:
        mat = [
            [1, 2, 3],
            [3, 4, 5],
            [9, 7, 8],
        ]
    return mat


matrix = read_matrix(istest=True)
prime_diag = 0
for i in range(len(matrix)):
    prime_diag += matrix[i][i]
print(prime_diag)
# we can increment i or j for any other subdiagonal
second_diag = 0
for i in range(1, len(matrix)+1):
    second_diag += matrix[-i][i-1]
print(second_diag)