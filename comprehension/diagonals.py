n = int(input())
matrix = [list(map(int, input().split(', '))) for i in range(n)]
first_diagonal = [matrix[i][i] for i in range(n)]
second_diagonal = [matrix[i][n-i-1] for i in range(n)]
print(f'First diagonal: {", ".join(list(map(str,first_diagonal)))}. Sum: {sum(first_diagonal)}')
print(f'Second diagonal: {", ".join(list(map(str,second_diagonal)))}. Sum: {sum(second_diagonal)}')