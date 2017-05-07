# Disha Jagtap. 861994478.
"""
Global Variables used to identify and quantify the users in the game
"""
NONE = 0
WHITE = 1
BLACK = 2

"""CLASSES"""

"""Gamestate Class"""

class Gamestate:
    def __init__(self) -> None:
        '''Creates an empty gameboard and initializing attributes of class'''
        self.board = []
        self.rows = 0
        self.columns = 0
        self.b_count = 0
        self.w_count = 0

    def init_turn(self, first_player: int) -> None:
        '''Assigns gamestate's turn to the specified first player'''
        self.turn = first_player

    def count_tiles(self) -> None:
        '''Counts the black and white tiles in the board'''
        self.b_count = 0
        self.w_count = 0
        for i in self.board:
            self.b_count += i.count(BLACK)
            self.w_count += i.count(WHITE)

"""
Direction Classes
"""

class North:
    def check_validity(self, gs: 'Gamestate', r: int, c: int)->tuple:
        '''Checks whether there lies a tile of the same color as the current player in the North
            direction after finding a tile of the opposite player's color adjacent to a proposed row
                and column input'''
        r -= 1
        valid = False
        while r != -1 and gs.board[r][c] != NONE:
            if gs.board[r][c] == gs.turn:
                valid = True
                break
            r -= 1
        return valid, r, c

    def flip(self, gs: 'Gamestate', r: int, c: int, orig_row: int, orig_col: int)->list:
        '''Flips the tiles in the North direction'''
        for row in range(r, orig_row):
            gs.board[row][c] = gs.turn
        gs.board = _add_tile(gs, orig_row, orig_col)
        return gs.board

class South:
    def check_validity(self, gs: 'Gamestate', r: int, c: int)->tuple:
        '''Checks whether there lies a tile of the same color as the current player in the South
            direction after finding a tile of the opposite player's color adjacent to a proposed row
                and column input'''
        r += 1
        valid = False
        while r != gs.rows and gs.board[r][c] != NONE:
            if gs.board[r][c] == gs.turn:
                valid = True
                break
            r += 1
        return valid, r, c

    def flip(self, gs: 'Gamestate', r: int, c: int, orig_row: int, orig_col: int)->list:
        '''Flips the tiles in the South direction'''
        for row in range(orig_row + 1, r + 1):
            gs.board[row][c] = gs.turn
        gs.board = _add_tile(gs, orig_row, orig_col)
        return gs.board

class West:
    def check_validity(self, gs: 'Gamestate', r: int, c: int)->tuple:
        '''Checks whether there lies a tile of the same color as the current player in the West
            direction after finding a tile of the opposite player's color adjacent to a proposed row
                and column input'''
        c -= 1
        valid = False
        while c != -1 and gs.board[r][c] != NONE:
            if gs.board[r][c] == gs.turn:
                valid = True
                break
            c -= 1
        return valid, r, c

    def flip(self, gs: 'Gamestate', r: int, c: int, orig_row: int, orig_col: int)->list:
        '''Flips the tiles in the West direction'''
        for col in range(c + 1, orig_col + 1):
            gs.board[r][col] = gs.turn
        gs.board = _add_tile(gs, orig_row, orig_col)

        return gs.board

class East:
    def check_validity(self, gs: 'Gamestate', r: int, c: int)->tuple:
        '''Checks whether there lies a tile of the same color as the current player in the East
            direction after finding a tile of the opposite player's color adjacent to a proposed row
                and column input'''
        c += 1
        valid = False
        while c != gs.columns and gs.board[r][c] != NONE:
            if gs.board[r][c] == gs.turn:
                valid = True
                break
            c += 1
        return valid, r, c

    def flip(self, gs: 'Gamestate', r: int, c: int, orig_row: int, orig_col: int):
        '''Flips the files in the East direction'''
        for col in range(orig_col + 1, c + 1):
            gs.board[r][col] = gs.turn
        gs.board = _add_tile(gs, orig_row, orig_col)

        return gs.board

class Northwest:
    def check_validity(self, gs: 'Gamestate', r: int, c: int)->tuple:
        '''Checks whether there lies a tile of the same color as the current player in the Northwest
            direction after finding a tile of the opposite player's color adjacent to a proposed row
                and column input'''
        c -= 1
        r -= 1
        valid = False
        while r != -1 and c != -1 and gs.board[r][c] != NONE:
            if gs.board[r][c] == gs.turn:
                valid = True
                break
            c -= 1
            r -= 1
        return valid, r, c

    def flip(self, gs: 'Gamestate', r: int, c: int, orig_row: int, orig_col: int)->list:
        '''Flips tiles in the Northwest direction'''
        row = orig_row
        col = orig_col
        row -= 1
        col -= 1
        while row != r and col != c:
            gs.board[row][col] = gs.turn
            row -= 1
            col -= 1
        gs.board = _add_tile(gs, orig_row, orig_col)
        return gs.board

class Southwest:
    def check_validity(self, gs: 'Gamestate', r: int, c: int)->tuple:
        '''Checks whether there lies a tile of the same color as the current player in the Southwest
            direction after finding a tile of the opposite player's color adjacent to a proposed row
                and column input'''
        c -= 1
        r += 1
        valid = False
        while r != gs.rows and c != -1 and gs.board[r][c] != NONE:
            if gs.board[r][c] == gs.turn:
                valid = True
                break
            c -= 1
            r += 1
        return valid, r, c

    def flip(self, gs: 'Gamestate', r: int, c: int, orig_row: int, orig_col: int)->list:
        '''Flips tiles in the Southwest direction'''
        row = orig_row
        col = orig_col
        row += 1
        col -= 1
        while row != r and col != c:
            gs.board[row][col] = gs.turn
            row += 1
            col -= 1
        gs.board = _add_tile(gs, orig_row, orig_col)
        return gs.board

class Northeast:
    def check_validity(self, gs: 'Gamestate', r: int, c: int)->tuple:
        '''Checks whether there lies a tile of the same color as the current player in the Northeast
            direction after finding a tile of the opposite player's color adjacent to a proposed row
                and column input'''
        c += 1
        r -= 1
        valid = False
        while r != -1 and c != gs.columns and gs.board[r][c] != NONE:
            if gs.board[r][c] == gs.turn:
                valid = True
                break
            c += 1
            r -= 1
        return valid, r, c

    def flip(self, gs: 'Gamestate', r: int, c: int, orig_row: int, orig_col: int)->list:
        '''Flips tiles in the Northeast direction'''
        row = orig_row
        col = orig_col
        row -= 1
        col += 1
        while row != r and col != c:
            gs.board[row][col] = gs.turn
            row -= 1
            col += 1
        gs.board = _add_tile(gs, orig_row, orig_col)
        return gs.board

class Southeast:
    def check_validity(self, gs: 'Gamestate', r: int, c: int)->tuple:
        '''Checks whether there lies a tile of the same color as the current player in the Southeast
            direction after finding a tile of the opposite player's color adjacent to a proposed row
                and column input'''
        c += 1
        r += 1
        valid = False
        while r != gs.rows and c != gs.columns and gs.board[r][c] != NONE:
            if gs.board[r][c] == gs.turn:
                valid = True
                break
            c += 1
            r += 1
        return valid, r, c

    def flip(self, gs: 'Gamestate', r: int, c: int, orig_row: int, orig_col: int)->list:
        '''Flips tiles in the Southeast direction'''
        row = orig_row
        col = orig_col
        row += 1
        col += 1
        while row != r and col != c:
            gs.board[row][col] = gs.turn
            row += 1
            col += 1
        gs.board = _add_tile(gs, orig_row, orig_col)
        return gs.board

"""
Exception Classes
"""

class StalemateError(Exception):
    '''raised whenever a stalemate error occurs'''
    pass

class InvalidMove(Exception):
    '''raised whenever an invalid move is made'''
    pass

"""
Initializing Game Methods
"""

def new_game() -> 'Gamestate':
    '''starts new game by creating an object of the Gamestate class'''
    gamestate = Gamestate()
    return gamestate

def create_gameboard(gs, r: int, c: int) -> None:
    '''replacing gameboard with two dimensional array of given parameters'''
    for i in range(r):
        gs.board.append([])
        for j in range(c):
            gs.board[-1].append(NONE)
    gs.rows = len(gs.board)
    gs.columns = len(gs.board[0])

def init_gameboard(gs, top_left: int) -> None:
    '''changing gameboard to simulate a board at the start of the game'''
    rows = gs.rows
    columns = gs.columns

    if top_left == WHITE:
        top_right = BLACK
    elif top_left == BLACK:
        top_right = WHITE
    else:
        raise SystemExit

    gs.board[int(rows / 2) - 1][int(columns / 2) - 1] = top_left
    gs.board[int(rows / 2) - 1][int(columns / 2)] = top_right

    gs.board[int(rows / 2)][int(columns / 2) - 1] = top_right
    gs.board[int(rows / 2)][int(columns / 2)] = top_left

"""
Game Private Methods
"""
def _opposite_player(player: int) -> int:
    '''returns opposite player's integer value'''
    if player == 1:
        return 2
    elif player == 2:
        return 1

def _get_directions_dict(r:int,c:int)->dict:
    '''returns dictionary of the coordinates adjacent
    to a coordinate of all eight directions
    '''
    return {(r - 1, c): 'North',
            (r + 1, c): 'South',
            (r, c - 1): 'West',
            (r, c + 1): 'East',
            (r - 1, c - 1): 'Northwest',
            (r + 1, c + 1): 'Southeast',
            (r - 1, c + 1): 'Northeast',
            (r + 1, c - 1): 'Southwest'
            }

def _find_empty_coordinates(gs:'Gamestate')->list:
    '''Returns a list of the empty coordinates of the board'''
    empty_coordinates = []
    for i in range(len(gs.board)):
        for j in range(len(gs.board[i])):
            if gs.board[i][j] == NONE:
                empty_coordinates.append([i, j])
    return empty_coordinates

def _check_adjacents(gs: 'Gamestate', directions_dict: dict) -> 'Gamestate':
    '''returns a list of the possible directions in which a tile can be placed
        according to a given row and column and the player
     '''
    player = gs.turn
    directions_found = []
    for coord in directions_dict:
        if coord[0] != -1 and coord[0] != gs.rows and coord[1] != -1 and coord[1] != gs.columns:
            if gs.board[coord[0]][coord[1]] == _opposite_player(player):
                validity, stop_row, stop_col = eval(directions_dict[coord])().check_validity(gs, coord[0], coord[1])
                if validity:
                    directions_found.append((directions_dict[coord], stop_row, stop_col))
    return directions_found

def _flip_tiles(requirements: tuple)->list:
    '''Flips the tiles in the board'''
    gs, direction, stop_row, stop_col, r, c = requirements
    gs.board = eval(direction)().flip(gs, stop_row, stop_col, r, c)
    return gs.board

def _add_tile(gs: 'Gamestate', r:int, c:int) -> list:
    '''Adds a tile of the current player's color in a coordinate'''
    gs.board[r][c] = gs.turn
    return gs.board

def _check_stalemate(gs: 'Gamestate')->bool:
    '''Checks whether each player has a valid move, if either one player does not,
        skips his turn and reverts back a turn,
         boolean is returned representing whether the game has arrive at a stalemate'''
    is_stalemate = False
    orig_player = gs.turn
    empty_coordinates = _find_empty_coordinates(gs)

    orig_directions_found = []
    for i in range(len(empty_coordinates)):
        r = empty_coordinates[i][0]
        c = empty_coordinates[i][1]
        directions_dict = _get_directions_dict(r,c)
        orig_directions_found.extend(_check_adjacents(gs, directions_dict))

    gs.turn = _opposite_player(orig_player)
    opp_directions_found = []
    for i in range(len(empty_coordinates)):
        r = empty_coordinates[i][0]
        c = empty_coordinates[i][1]
        directions_dict = _get_directions_dict(r,c)
        opp_directions_found.extend(_check_adjacents(gs, directions_dict))

    if len(orig_directions_found) == 0 and len(opp_directions_found) == 0:
        raise StalemateError
    elif len(orig_directions_found) == 0:
        gs.turn = _opposite_player(orig_player)
        return is_stalemate
    elif len(opp_directions_found) == 0:
        gs.turn = orig_player
        return is_stalemate

    gs.turn = orig_player
    return is_stalemate

def _board_not_full(gs: 'Gamestate') -> bool:
    '''determines whether the board is full'''
    for i in range(len(gs.board)):
        for j in range(len(gs.board[i])):
            if gs.board[i][j] == NONE:
                return True
    return False

"""Game Public Methods"""

def make_move(gs: 'Gamestate', r: int, c: int) -> 'Gamestate':
    '''Makes a move with given coordinates'''
    directions_dict = _get_directions_dict(r,c)

    directions_found = _check_adjacents(gs, directions_dict)
    if gs.board[r][c] != NONE or len(directions_found) == 0:
        raise InvalidMove()

    for i in directions_found:
        direction, stop_row, stop_col = i
        gs.board = _flip_tiles((gs, direction, stop_row, stop_col, r, c))
    return gs

def flip_turn(gs) -> None:
    '''flips the turn to the opposite player'''
    gs.turn = _opposite_player(gs.turn)

def winner(gs:'Gamestate', method: 'str') -> int:
    '''returns the winner when the game comes to an end'''
    if method == '>':
        if gs.b_count > gs.w_count:
            return BLACK
        elif gs.b_count < gs.w_count:
            return WHITE
        elif gs.b_count == gs.w_count:
            return NONE
    elif method == '<':
        if gs.b_count < gs.w_count:
            return BLACK
        elif gs.b_count > gs.w_count:
            return WHITE
        elif gs.b_count == gs.w_count:
            return NONE

def game_over(gs:'Gamestate')->bool:
    '''determines whether the game is over'''
    if _board_not_full(gs) and not _check_stalemate(gs):
        return False
    return True
