def check_attacks(board, x, y):
    x_offset = [2, 1, -2, -1, 2, 1, -2, -1]
    y_offset = [1, 2, -1, -2, -1, -2, 1, 2]
    attacks = 0
    for i in range(8):
        x_pos = x + x_offset[i]
        y_pos = y + y_offset[i]
        if 0 <= x_pos < len(board) and 0 <= y_pos < len(board) and board[x_pos][y_pos] == 'K':
            attacks += 1
    return attacks


def redo_board(board):
    dic = {}
    for i in range(0, n):
        for j in range(0, n):
            if board[i][j] == 'K':
                attacks = check_attacks(mat, i, j)
                if attacks > 0:
                    dic[(i, j)] = attacks
    dic = dict(sorted(dic.items(), key=lambda x: -x[1]))
    return dic


n = int(input())
mat = [list(input()) for i in range(n)]
knights_dic = {}
to_remove = 0
for i in range(0, n):
    for j in range(0, n):
        if mat[i][j] == 'K':
            attacks = check_attacks(mat, i, j)
            if attacks > 0:
                knights_dic[(i, j)] = attacks
knights_dic = dict(sorted(knights_dic.items(), key=lambda x: -x[1]))

while knights_dic:
    x, y = list(knights_dic.keys())[0]
    mat[x][y] = '0'
    to_remove += 1
    knights_dic = redo_board(mat)
print(to_remove)