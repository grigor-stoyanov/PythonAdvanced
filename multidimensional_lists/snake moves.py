rows, cols = list(map(int, input().split()))
matrix = [['' for col in range(cols)] for row in range(rows)]
snake = input()
i = 0
for row in range(rows):
    if row % 2 == 0:
        for col in range(cols):
            matrix[row][col] = snake[i]
            i += 1
            if i >= len(snake):
                i = 0
    else:
        for col in range(-1, -cols-1, -1):
            matrix[row][col] = snake[i]
            i += 1
            if i >= len(snake):
                i = 0
for row in matrix:
    print(*row,sep='')