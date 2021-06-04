r, c = list(map(int, input().split()))
palindromes = [[f'{chr(row + 97)}{chr(col + 97 + row)}{chr(row + 97)}' for col in range(c)] for row in range(r)]
for i in range(r):
    for j in range(c):
        print(palindromes[i][j],end=' ')
    print()