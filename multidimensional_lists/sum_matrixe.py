def read_matrix(istest=False):
    mat = []
    if not istest:
        (rows, coulmns) = map(int, input().split(', '))
        for i in range(rows):
            row = list(map(int, input().split(', ')))
            mat.append(row)
    else:
        mat = [
            [1,2,3],
            [3,4,5],
            [6,7,8],
        ]
    return mat


matrix = read_matrix(istest=True)
matrix_sum = 0
for i in range(len(matrix)):
    row = matrix[i]
    for j in range(len(row)):
        matrix_sum += row[j]
print(matrix_sum)
print(matrix)
