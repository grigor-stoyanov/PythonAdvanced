# def get_magic_triangle(n):
#     triangle = [[1], [1, 1]]
#     if n == 1:
#         return [[1]]
#     elif n == 2:
#         return triangle
#     else:
#         for i in range(2, n):
#             triangle.append([
#                 triangle[i - 1][j - 1] + triangle[i - 1][j]
#                 if 0 <= j - 1 and j < len(triangle[i - 1])
#                 else triangle[i - 1][j - 1] for j in range(i + 1)
#             ])
#         return triangle

def get_magic_triangle(n, lol=None):
    if lol is None: lol = [[1]]
    if n == 1:
        return lol
    last_row = lol[-1]
    new_row = [x + y for x, y in zip([0] + last_row, last_row + [0])]
    return get_magic_triangle(n - 1, lol + [new_row])


print(get_magic_triangle(5))
