def read_matrix(istest=False):
    mat = []
    if not istest:
        (rows, coulmns) = map(int, input().split(', '))
        for i in range(rows):
            row = [int(x) for x in input().split(', ')]
            mat.append(row)
    else:
        mat = [
            [1, 2, 3],
            [3, 4, 5],
            [6, 7, 8],
        ]
    return mat


matrix = read_matrix(istest=True)
column_sum = 0
rows_count = len(matrix)
column_count = len(matrix[0])
# for column_i in range(column_count):
#     for row_i in range(rows_count):
#         column_sum += matrix[row_i][column_i]
#     print(column_sum)
#     column_sum = 0
column_sums = [0] * column_count
for row_i in range(rows_count):
    for column_i in range(column_count):
        column_sums[column_i] += matrix[row_i][column_i]
print(*column_sums, sep='\n')

