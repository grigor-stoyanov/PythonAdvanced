rows = int(input())
matrix = [list(map(int, input().split())) for row in range(rows)]
command = input()
while not command == 'END':
    cmd, *args = command.split()
    x, y, value = list(map(int, args))
    if 0 <= x < rows and 0 <= y < len(matrix):
        if cmd == 'Add':
            matrix[x][y] += value
        elif cmd == 'Subtract':
            matrix[x][y] -= value
    else:
        print('Invalid coordinates')
    command = input()
print(*[' '.join(list(map(str, matrix[row]))) for row in range(rows)], sep='\n')
