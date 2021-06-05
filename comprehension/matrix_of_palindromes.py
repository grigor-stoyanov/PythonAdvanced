r, c = list(map(int, input().split()))
palindromes = [[f'{chr(row + 97)}{chr(col + 97 + row)}{chr(row + 97)}' for col in range(c)] for row in range(r)]
print(*[' '.join(palindromes[row]) for row in range(r)], sep='\n')
