"""
Tic Tac Toe Player
"""

import math
import copy

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
    count_x = 0
    count_o = 0
    
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col]== X:
                count_x+=1
            if board[row][col]== O:
                count_o+=1    
    if count_x>count_o:
        return O
    else:
        return X



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    allPossibleActions = set()
    
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col]== EMPTY:
                allPossibleActions.add((row, col))  
    return allPossibleActions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if  action not in actions(board):
        raise Exception("Not valid action")
    
    row , col = action
    board_copy = copy.deepcopy(board)
    board_copy[row][col] = player(board)
    return board_copy

def checkRow(board,player):
    for row in range(len(board)):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player :
            return True
    return False

def checkCol(board,player):
    for col in range(len(board)):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player :
            return True
    return False

def checkFirstDiagonal(board,player):
    count = 0
    for row in range(len(board)):
        for col in range(len(board[row])):
            if row==col and board[row][col] == player:
                count +=1
    if count==3 :
        return True
    else :
        return False

def checkSecDiagonal(board,player):
    count = 0
    for row in range(len(board)):
        for col in range(len(board[row])):
            if (len(board) - row -1)==col and board[row][col] == player:
                count +=1
    if count==3 :
        return True
    else :
        return False


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if checkRow(board,X) or checkCol(board,X) or checkFirstDiagonal(board,X) or checkSecDiagonal(board,X) :
        return X
    elif checkRow(board,O) or checkCol(board,O) or checkFirstDiagonal(board,O) or checkSecDiagonal(board,O) :
        return O
    else :
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board)== X or winner(board)== O :
        return True
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == EMPTY:
                return False
    return True              ## Tie


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board)== X :
        return 1
    elif winner(board)== O :
            return -1
    else:
        return 0
    
def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    if player(board) == X:
        score = -math.inf
        action_to_take = None

        for action in actions(board):
            min_val = minvalue(result(board, action))

            if min_val > score:
                score = min_val
                action_to_take = action

        return action_to_take

    elif player(board) == O:
        score = math.inf
        action_to_take = None
        
        for action in actions(board):
            max_val = maxvalue(result(board, action))
            
            if max_val < score:
                score = max_val
                action_to_take = action
                
        return action_to_take


def minvalue(board):
    """
    Returns the minimum value out of all maximum values
    """

    if terminal(board):  # if game over, just return the utility of state
        return utility(board)

    max_value = math.inf  # iterate over the available actions and return the minimum out of all maximums
    for action in actions(board):
        max_value = min(max_value, maxvalue(result(board, action)))

    return max_value

def maxvalue(board):
    """
    Returns the maximum value out of all minimum values
    """

    if terminal(board):
        return utility(board)

    min_val = -math.inf
    for action in actions(board):
        min_val = max(min_val, minvalue(result(board, action)))

    return min_val


