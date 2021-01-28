row_column = int(input())
matrix = []
for row in range(row_column):
    matrix.append(list(input()))
symbol = input()
for row in range(row_column):
    if symbol in matrix[row]:
        print((row, matrix[row].index(symbol)))
        exit()
    # for column in range(row_column):
    #     if symbol in matrix[row][column]:
    #         print((row, column))
    #         exit()
print(f'{symbol} does not occur in the matrix')
