# rows, cols = list(map(int, input().split()))
rows = int(input())
matrix = [list(map(int, input().split(', '))) for row in range(rows)]
matrix2 = [[matrix[row][col] for col in range(len(matrix[row])) if matrix[row][col] % 2 == 0] for row in range(rows)]
print(matrix2)