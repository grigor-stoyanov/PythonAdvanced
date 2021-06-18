from tic_tac_toe.core.logic import play


def print_initial_board_positions():
    print('This is the numeration of the board:')
    print("| 1 | 2 | 3 |")
    print("| 4 | 5 | 6 |")
    print("| 7 | 8 | 9 |")


def create_empty_board():
    return [[' ']*3 for _ in range(3)]


def setup():
    player_1 = input('Player 1 name: ')
    player_2 = input('Player 2 name: ')
    player_1_sign = input(f'{player_1}, choose your sign (X or O): ').upper()
    while player_1_sign not in ['X', 'O']:
        player_1_sign = input(f'{player_1}, choose your sign (X or O): ').upper()
    player_2_sign = 'O' if player_1_sign == 'X' else 'X'
    print_initial_board_positions()
    first_player = player_1 if player_1_sign == 'X' else player_2
    second_player = player_1 if first_player == player_2 else player_2
    print(f'{first_player} starts first')
    players = {player_1: player_1_sign, player_2: player_2_sign}
    board = create_empty_board()
    turn_mapper = {0: first_player, 1: second_player}
    play(players, board, turn_mapper)


def start_game():
    setup()


if __name__ == '__main__':
    start_game()
