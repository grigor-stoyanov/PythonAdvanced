# def check_path(r, c, mat):
#     # check if there is a king on 1 of the queens paths
#     mat[r][c] = 'M'
#     paths = {'horizontal': [mat[r][i] for i in range(len(mat))], 'vertical': [mat[i][c] for i in range(len(mat))]}
#     offset1 = c - r
#     paths['fdiagonal'] = [mat[i][i + offset1] for i in range(len(mat)) if 0 <= i + offset1 < len(mat)]
#     offset2 = len(mat) - r - c - 1
#     paths['bdiagonal'] = [mat[i][len(mat) - i - 1 - offset2] for i in range(len(mat)) if
#                           0 <= len(mat) - i - 1 - offset2 < len(mat)]
#
#     mat[r][c] = 'Q'
#     # Go trough paths available
#     for p_type, path in paths.items():
#         # check for path with a king
#         if 'K' in path:
#             path_stack = []
#             # check if path blocked
#             for i in range(len(path)):
#                 if path[i] == 'K' or path[i] == 'M':
#                     path_stack.append(i)
#             start, end = path_stack
#             if 'Q' in path[start:end+1]:
#                 pass
#             else:
#                 return [r, c]
#     # remove queen if no path with king by default
#     return
#
#
# board = [input().split() for i in range(8)]
# queen_pos = []
# for row in range(len(board)):
#     for col in range(len(board)):
#         if board[row][col] == 'Q':
#             queen_pos.append((row, col))
# checks = []
# for queen in queen_pos:
#     result =check_path(*queen,board)
#     if result:
#         checks.append(result)
#
# if checks:
#     print(*checks, sep='\n')
# else:
#     print("The king is safe!")


def king_move(x, y, mat):
    default_pos = (x, y)
    moves = {
        'up': lambda a, b: (a, b + 1),
        'down': lambda a, b: (a, b - 1),
        'left': lambda a, b: (a + 1, b),
        'right': lambda a, b: (a - 1, b),
        'fdiaup': lambda a, b: (a + 1, b + 1),
        'fdiadown': lambda a, b: (a + 1, b - 1),
        'sdiaup': lambda a, b: (a - 1, b + 1),
        'sdiadown': lambda a, b: (a - 1, b - 1)
    }
    queens = []
    for direction in moves:
        x, y = default_pos
        while 0 <= x < 8 and 0 <= y < 8:
            if mat[x][y] == 'Q':
                queens.append([x, y])
                break
            x, y = moves[direction](x, y)
    return queens


board = [input().split() for i in range(8)]
for row in range(len(board)):
    for col in range(len(board)):
        if board[row][col] == 'K':
            queen_pos = king_move(row, col, board)
            print('\n'.join(list(map(str, queen_pos))) if queen_pos else "The king is safe!")
            exit(0)
