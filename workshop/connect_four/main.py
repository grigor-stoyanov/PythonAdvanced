from collections import deque

from connect_four.core.logic import play


def start_game():
    board = [['0'] * 7 for _ in range(6)]
    players = deque(['Player 1', 'Player 2'])
    while True:
        current_player = players.popleft()
        players.append(current_player)
        column = input(f'{current_player}, please choose a column\n')
        if play(board, column, current_player, players):
            break
    if input('Play again? Y\\N\n').upper() in 'Y':
        start_game()


if __name__ == '__main__':
    start_game()
