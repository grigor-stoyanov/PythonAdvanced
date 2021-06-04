n = int(input())
matrix = [list(map(int, input().split(', '))) for i in range(n)]
first_diagonal = [matrix[i][j] for i in range(n) for j in range(n) if i == j]
second_diagonal = [matrix[i][j] for i in range(n) for j in range(n) if i == n - j - 1]
print(f'First diagonal: {", ".join(list(map(str,first_diagonal)))}. Sum: {sum(first_diagonal)}')
print(f'Second diagonal: {", ".join(list(map(str,second_diagonal)))}. Sum: {sum(second_diagonal)}')