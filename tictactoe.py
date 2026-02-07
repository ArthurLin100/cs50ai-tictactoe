"""
Tic Tac Toe Player
"""

import math
import copy
from turtle import fd

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
    if not board:
        return X
    
    flat = [cell for row in board for cell in row]    
    if flat.count(X) > flat.count(O):
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))

    return possible_actions    


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = copy.deepcopy(board)
    i, j = action
    current_player = player(board)
    if board[i][j] == EMPTY:
        new_board[i][j] = current_player
        return new_board
    else:
        raise ValueError("Invalid action: position is not empty")


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check rows
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return board[i][0]
        
    # Check columns
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] != EMPTY:
            return board[0][j]
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]

    return None    


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None: # there is winner
        return True
    
    for row in board:
        for cell in row:
            if cell == EMPTY:
                return False # game is on going
    return True     


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0    

def max_value(board):
    if terminal(board):
        return utility(board)
    v = -math.inf
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v

def min_value(board):
    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    current_player = player(board)
    if current_player == X: # maximizing player
        best_action = None
        best_value = -math.inf
        for action in actions(board):            
            this_min = min_value(result(board, action)) # oponent's best value
            if (this_min > best_value): # finding the maximum this_min
                best_action = action
                best_value = this_min                        
    else: # current_player == O minimzing player
        best_action = None
        best_value = math.inf
        for action in actions(board):            
            this_max = max_value(result(board, action)) # oponent's best value
            if (this_max < best_value): #finidng the minimum this_max
                best_action = action
                best_value = this_max                                

    return best_action