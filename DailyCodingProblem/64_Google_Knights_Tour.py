"""
This problem was asked by Google.

A knight's tour is a sequence of moves by a knight on a chessboard such that all squares are visited once.

Given N, write a function to return the number of knight's tours on an N by N chessboard.
"""

import copy

#  vertical, horizontal
moves = [(2, 1),
         (2, -1),
         (1, 2),
         (1, -2),

         (-2, 1),
         (-2, -1),
         (-1, 2),
         (-1, -2)]


def create_board(n):
    return [['O' for _ in range(n)] for _ in range(n)]


def find_tours(board, board_size ,start_row, start_col):
    # move invalid if outside the board or lands on
    # previously visited spot

    if (0 <= start_col < board_size) and (0 <= start_row < board_size) and board[start_row][start_col]!='K':
        board[start_row][start_col] = 'K'
    else:
        return 0

    if check_all_filled(board):
        return 1

    successful_tours = 0
    for x,y in moves:
        successful_tours += find_tours(copy.deepcopy(board), board_size, start_row+x, start_col+y)

    return successful_tours


def check_all_filled(board):
    return all(all(cell == 'K' for cell in row) for row in board)


def num_of_tours(board_size):
    # create board
    board = create_board(board_size)

    num_tours = 0
    # find tours from all spots
    for row in range(board_size):
        for col in range(board_size):
            num_tours += find_tours(copy.deepcopy(board), board_size, start_row=row, start_col=col)

    return num_tours


if __name__ == '__main__':
    print(num_of_tours(board_size=3))