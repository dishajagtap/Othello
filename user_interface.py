# Disha Jagtap. 86199478.

import othello_game

def dimensions() -> tuple:
    '''Asks user for input on the dimensions of the game board'''
    try:
        rows = int(input())
        columns = int(input())
        if 4 <= rows <= 16 and rows % 2 == 0 and 4 <= columns <= 16 and columns % 2 == 0:
            return rows, columns
        else:
            raise SystemExit
    except:
        raise SystemExit

def valid_row_col(gamestate: 'Gamestate', row: int, col: int) -> bool:
    '''Determines whether a given row and column move
        lies within the dimensions of the game board
    '''
    if row in range(0, gamestate.rows) and col in range(0, gamestate.columns):
        return True
    raise othello_game.InvalidMove

def print_current_gameboard(gamestate: 'Gamestate'):
    '''Prints the current gameboard of the gamestate object'''
    gamestate.count_tiles()
    print('B: {}  W: {}'.format(gamestate.b_count, gamestate.w_count))
    for i in range(len(gamestate.board)):

        for j in range(len(gamestate.board[i])):

            if gamestate.board[i][j] == othello_game.NONE:
                print('.', end=' ')
            elif gamestate.board[i][j] == othello_game.WHITE:
                print('W', end=' ')
            elif gamestate.board[i][j] == othello_game.BLACK:
                print('B', end=' ')
        print()

def int_to_player(player: int) -> str:
    '''Given the player's integer,
        returns the string representing the player
    '''
    int_dict = {othello_game.NONE: 'NONE', othello_game.WHITE: 'W', othello_game.BLACK: 'B'}
    return int_dict[player]

def player_to_int(player: str) -> int:
    '''Given the player's string,
        returns the integer representing the player
    '''
    player_dict = {'NONE': othello_game.NONE, 'W': othello_game.WHITE, 'B': othello_game.BLACK}
    return player_dict[player]

def print_winner(player: int) -> None:
    '''Prints the winner of the game'''
    print('WINNER: {}'.format(int_to_player(player)))

def print_turn(gamestate: 'Gamestate', invalid_move: bool) -> None:
    '''Prints whose turn it is to play'''
    if invalid_move:
        return
    else:
        print('TURN: {}'.format(int_to_player(gamestate.turn)))

def input_rows(gamestate: 'Gamestate') -> tuple:
    '''Asks user for input on where to place a tile, if error occurs,
        exception is raised
    '''
    try:
        row, col = input().split()
        row = int(row) - 1
        col = int(col) - 1
        valid_row_col(gamestate, row, col)
    except:
        raise othello_game.InvalidMove
    else:
        return row, col

def play_Othello(gamestate: 'Gamestate', winning_method: str) -> None:
    '''Plays the simple version of the game'''
    invalid_move = False
    print_current_gameboard(gamestate)

    while not othello_game.game_over(gamestate):
        print_turn(gamestate, invalid_move)
        invalid_move = False

        try:
            row, col = input_rows(gamestate)
            gamestate = othello_game.make_move(gamestate, row, col)
        except othello_game.InvalidMove:
            print('INVALID')
            invalid_move = True
        else:
            othello_game.flip_turn(gamestate)
            print_current_gameboard(gamestate)

    print_winner(othello_game.winner(gamestate, winning_method))

def user_interface() -> None:
    '''Main module which initiates the game and then calls the function to play Othello'''
    print('FULL')
    gamestate = othello_game.new_game()

    rows, cols = dimensions()
    othello_game.create_gameboard(gamestate, rows, cols)

    first_player = input()
    try:
        gamestate.init_turn(player_to_int(first_player))
    except:
        raise SystemExit

    top_left = input()
    try:
        othello_game.init_gameboard(gamestate, player_to_int(top_left))
    except:
        raise SystemExit

    winning_method = input()
    if winning_method!='<' and winning_method!='>':
        raise SystemExit

    try:
        play_Othello(gamestate, winning_method)
    except othello_game.StalemateError:
        print_winner(othello_game.winner(gamestate, winning_method))
        raise SystemExit



if __name__ == '__main__':
    user_interface()


