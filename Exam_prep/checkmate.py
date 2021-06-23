def check_path(r, c, mat):
    # check if there is a king on 1 of the queens paths
    mat[r][c] = 'M'
    paths = {'horizontal': [mat[r][i] for i in range(len(mat))], 'vertical': [mat[i][c] for i in range(len(mat))]}
    offset1 = c - r
    paths['fdiagonal'] = [mat[i][i + offset1] for i in range(len(mat)) if 0 <= i + offset1 < len(mat)]
    offset2 = len(mat) - r - c - 1
    paths['bdiagonal'] = [mat[i][len(mat) - i - 1 - offset2] for i in range(len(mat)) if
                          0 <= len(mat) - i - 1 - offset2 < len(mat)]
    # bdiag = []
    # for i in range(len(mat)):
    #     if 0 <= len(mat) - i - 1 - offset2 < len(mat):
    #         bdiag.append(mat[i][len(mat) - i - 1 - offset2])

    mat[r][c] = 'Q'
    # Go trough paths available
    for p_type, path in paths.items():
        # check for path with a king
        if 'K' in path:
            path_stack = []
            # check if path blocked
            for i in range(len(path)):
                if path[i] == 'K' or path[i] == 'M':
                    path_stack.append(i)
            start, end = path_stack
            if 'Q' in path[start:end+1]:
                pass
            else:
                return [r, c]
    # remove queen if no path with king by default
    return


board = [input().split() for i in range(8)]
queen_pos = []
for row in range(len(board)):
    for col in range(len(board)):
        if board[row][col] == 'Q':
            queen_pos.append((row, col))
checks = []
for queen in queen_pos:
    result =check_path(*queen,board)
    if result:
        checks.append(result)

if checks:
    print(*checks, sep='\n')
else:
    print("The king is safe!")
