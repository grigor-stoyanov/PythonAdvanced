# multidimensional lists are essentually a matrix of data
# such as a list of lists or a grid with columns and rows
matrix = []
for i in range(3):
    matrix.append([])
    for j in range(2):
        matrix[i].append(0)
print(matrix)
# because in python lists are dynamic we can keep adding elements to the matrix regardless of columns
# in other languages a column specifier must be added
rows = int(input())
matrix = [[ele for ele in input().split()] for ele in range(rows)]
print(matrix)
# to access elements in the matrix we need the row and coulmns
# depending of the number of dimensions to go trough each element we need apropriate number of nested cycles
# its bad practice to use comprehension for multi dimensional lists
