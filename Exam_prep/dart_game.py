player_1, player_2 = input().split(', ')
dartboard = [[int(ele) if ele.isdigit() else ele for ele in input().split()] for i in range(7)]
score = {player_1: 501, player_2: 501}

turns = {0: player_1, 1: player_2}


def check_hit(x, y):
    if not 0 <= x < 7 or not 0 <= y < 7:
        return 0
    elif isinstance(dartboard[x][y], int):
        return dartboard[x][y]
    else:
        return mapper.get(dartboard[x][y], error)(x, y)


def error():
    return 0


def double(x, y):
    result = dartboard[-1][y] + dartboard[0][y] + dartboard[x][-1] + dartboard[x][0]
    result *= 2
    return result


def triple(x, y):
    result = dartboard[-1][y] + dartboard[0][y] + dartboard[x][-1] + dartboard[x][0]
    result *= 3
    return result


def bullseye(x, y):
    return 501


mapper = {'D': double, 'T': triple, 'B': bullseye}
turn = 0
while score[player_1] > 0 and score[player_2] > 0:
    x, y = map(int, input().strip('()').split(','))
    score[turns[turn % 2]] -= check_hit(x, y)
    turn += 1

if score[player_1] <= 0:
    print(f"{player_2} won the game with {(turn + 1) // 2} throws!")
else:
    print(f"{player_1} won the game with {(turn // 2) + 1} throws!")
