# rows, cols = list(map(int, input().split()))
rows = int(input())
matrix = [list(map(int, input().split(', '))) for row in range(rows)]
flattened_matrix = [matrix[row][col] for row in range(rows) for col in range(len(matrix[row]))]
print(flattened_matrix)