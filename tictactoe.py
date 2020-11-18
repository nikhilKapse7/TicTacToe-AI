"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def player(board):
    """
    Returns player who has the next turn on a board.
    """

    filled_cell_number = 0
    for row in board:  # iterate through rows
        for cell in row:
            if not cell == EMPTY:
                filled_cell_number += 1

    if filled_cell_number % 2 == 0:
        return 'X'
    elif filled_cell_number % 2 == 1:
        return 'O'

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()

    row_index = -1
    for row in board:
        row_index += 1
        cell_index = -1
        for cell in row:
            cell_index += 1
            if cell == EMPTY:
                row_cell_tuple = (row_index, cell_index)
                actions.add(row_cell_tuple)
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    if not action in actions(board): # accounts for if action is not possible on the inputted board
        raise Exception

    new_board = [[EMPTY, EMPTY, EMPTY],
                 [EMPTY, EMPTY, EMPTY],
                 [EMPTY, EMPTY, EMPTY]]
    row_index = -1
    for row in board:
        row_index += 1
        cell_index = -1
        for cell in row:
            cell_index += 1

            if action == (row_index, cell_index):
                new_board[row_index][cell_index] = player(board)
            else:
                new_board[row_index][cell_index] = board[row_index][cell_index]
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    first_row_X = board[0][0] == board[0][1] == board[0][2] == 'X'
    second_row_X = board[1][0] == board[1][1] == board[1][2] == 'X'
    third_row_X = board[2][0] == board[2][1] == board[2][2] == 'X'
    first_column_X = board[0][0] == board[1][0] == board[2][0] == 'X'
    second_column_X = board[0][1] == board[1][1] == board[2][1] == 'X'
    third_column_X = board[0][2] == board[1][2] == board[2][2] == 'X'
    first_diagonal_X = board[0][0] == board[1][1] == board[2][2] == 'X'
    second_diagonal_X = board[0][2] == board[1][1] == board[2][0] == 'X'

    first_row_O = board[0][0] == board[0][1] == board[0][2] == 'O'
    second_row_O = board[1][0] == board[1][1] == board[1][2] == 'O'
    third_row_O = board[2][0] == board[2][1] == board[2][2] == 'O'
    first_column_O = board[0][0] == board[1][0] == board[2][0] == 'O'
    second_column_O = board[0][1] == board[1][1] == board[2][1] == 'O'
    third_column_O = board[0][2] == board[1][2] == board[2][2] == 'O'
    first_diagonal_O = board[0][0] == board[1][1] == board[2][2] == 'O'
    second_diagonal_O = board[0][2] == board[1][1] == board[2][0] == 'O'

    if first_row_X or second_row_X or third_row_X or first_column_X or second_column_X or third_column_X or first_diagonal_X or second_diagonal_X:
        return 'X'
    elif first_row_O or second_row_O or third_row_O or first_column_O or second_column_O or third_column_O or first_diagonal_O or second_diagonal_O:
        return 'O'
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    all_spaces_taken = True

    for row in board:
        for cell in row:
            if cell == EMPTY:
                all_spaces_taken = False

    winner_player = winner(board)
    if winner_player == 'X' or winner_player == 'O' or all_spaces_taken:
        return True

    return False

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winner_value = winner(board)

    if winner_value == 'X':
        return 1
    elif winner_value == 'O':
        return -1
    else:
        return 0  # draw

# Takes in board and returns optimal action for whoever's turn it is
def minimax_helper(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if (player(board) == 'X'):
        comparator = lambda x, y : x > y
        optimal_tuple = (-math.inf, (None, None))
    else:
        comparator = lambda x, y : x < y
        optimal_tuple = (math.inf, (None, None))

    possible_actions = actions(board)

    for action in possible_actions:
        board_after_current = result(board, action)
        if terminal(board_after_current):
            return (utility(board_after_current), action)
        else:
            (value_after_opponent, opponent_action) = minimax_helper(board_after_current) 
            if comparator(value_after_opponent, optimal_tuple[0]):
                optimal_tuple = (value_after_opponent, action)
    return optimal_tuple

# Takes in board and returns optimal action for whoever's turn it is
def minimax(board):
    return minimax_helper(board)[1]
