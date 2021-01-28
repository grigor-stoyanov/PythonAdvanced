def get_max_sum2x2(max_i, max_j, mat):
    max_sum = 0
    for i in range(max_i, max_i + 2):
        for j in range(max_j, max_i + 2):
            max_sum += mat[i][j]
    return max_sum, max_i, max_j


def get_max(mat):
    max_sum = 0
    max_i = 0
    max_j = 0
    for row in range(len(matrix)):
        for column in range(len(mat)):
            curr_max, curr_i, curr_j = get_max_sum2x2(row, column, mat)
            if curr_max > max_sum:
                max_sum = curr_max
                max_i = curr_i
                max_j = curr_j
    return max_sum, max_i, max_j


rows = int(input())
columns = int(input())
matrix = [[int(x) for x in row] for row in input().split(', ')]
sub_matrix = []
best_sum, best_i, best_j = get_max(matrix)
for i in range(best_i, best_i + 2):
    print()
    for j in range(best_j, best_j + 2):
        print(matrix[i][j], end='')
print(best_sum)