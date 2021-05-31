# check number of attacks of knight
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


# generate matrix
n = int(input())
mat = [list(input()) for i in range(n)]
knights_dic = {}
to_remove = 0
knights_dic = {}
for i in range(0, n):
    for j in range(0, n):
        if mat[i][j] == 'K':
            attacks = check_attacks(mat, i, j)
            if attacks > 0:
                knights_dic[(i, j)] = attacks
# sort knights in a dictionary by number of attacks and save their positions as key
knights_dic = dict(sorted(knights_dic.items(), key=lambda x: -x[1]))


# start removing knights on the matrix by order of dictionary and update number of attacks
for knight_pos in knights_dic:
    x, y = knight_pos
    if check_attacks(mat, x, y) > 0:
        mat[x][y] = '0'
        to_remove += 1
print(to_remove)
