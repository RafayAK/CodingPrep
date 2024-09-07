"""
This problem was asked by Microsoft.

You have an N by N board. Write a function that, given N, returns the number of
possible arrangements of the board where N queens can be placed on the board without
threatening each other, i.e. no two queens share the same row, column, or diagonal.
"""

from copy import deepcopy

solved_boards = []  # store list of solved boards


def get_2d_array_col(lists, col):
    return [row[col] for row in lists]


# http://stackoverflow.com/q/3844948/
def checkEqualIvo(lst): # checks if all elements in a list are equal
    return not lst or lst.count(lst[0]) == len(lst)


def is_valid(candidate_pos, queens_pos):
    candi_row, candi_col = candidate_pos

    # check if collisions in row(row only as we are deliberately only putting queens in distinct cols)
    for queen_row, queen_col in queens_pos:

        # if in same row, diff ==0
        # if diagonal, abs(candi_row - queen_row ) == abs(candi_col - queen_col)
        diff = abs(candi_row - queen_row )
        if diff == 0 or diff == abs(candi_col - queen_col):
            return False

    return True

    # check diagonals



def helper(board, n,num_queens, queen_posistions,current_col=1):
    # successfully filled up board with non-threatening queens
    if num_queens == 0:
        solved_boards.append(deepcopy(board))
        return

    # Pruning.
    # stop further execution if:
    # 1- reached end of board, or
    # 2- couldn't fill up last col. i.e. last col is all 'E'
    if current_col == n or checkEqualIvo(get_2d_array_col(board, current_col-1)):
        return

    for i in range(n):
        if is_valid(candidate_pos=(i, current_col), queens_pos=queen_posistions):
            board[i][current_col] = 'Q'
            helper(board, n, num_queens-1, queen_posistions+[(i, current_col)], current_col+1)
            board[i][current_col] = 'E'  # replace


def n_queens(n):
    """

    :type n: int, specifies board size and number of queen to be placed on it

    """

    # create board
    board = [['E']*n for _ in range(n)]
    # initialize queens
    num_of_queens = n

    # temp_board = board.copy()
    for i in range(n):
        # place a queen at the i'th row in the 1st col
        # temp_board[i][0] = 'Q'
        board[i][0] = 'Q'
        helper(board, n,num_of_queens-1, [(i,0)])
        board[i][0] = 'E'  # replace

    printboard(solved_boards)


def printboard(boards):

    print("Found {} solutions".format(len(boards)))

    for board in boards:
        for row in board:
            print(row)
        print('\n')


if __name__ == '__main__':
    n_queens(5)
