'''
This problem was asked by Google.

You are given an M by N matrix consisting of booleans that represents a board.
Each True boolean represents a wall.
Each False boolean represents a tile you can walk on.

Given this matrix, a start coordinate, and an end coordinate, return the minimum
number of steps required to reach the end coordinate from the start. If there is no
possible path, then return null.
You can move up, left, down, and right. You cannot move through walls. You cannot wrap around the edges of the board.

For example, given the following board:

[[f, f, f, f],
[t, t, f, t],
[f, f, f, f],
[f, f, f, f]]
and start = (3, 0) (bottom left) and end = (0, 0) (top left), the minimum number of steps required to reach the end is 7, since we would need to go through (1, 2) because there is a wall everywhere else on the second row.
'''

from collections import deque

neighbour_cells = deque()


# lee's algorithm
# a- mark the starting position as 0, because no steps are required to reach it
# b- append the starting cell to a queue
# Main algo:
#   1- pop element from from of queue
#   2- Find all its potential neighbours
#   3- mark all the valid neighbours origin_cell_value+1 (if neighbours already marked, mark as invalid neighbour)
#   4- add all the valid neighbours to a queue to be processed
#   5- repeat until queue is empty



def mark_neighbour(board, cell, board_rows, board_cols, cell_value):

    if cell[0] <0 or cell[0] > board_rows-1: # out of bounds vertically
        return board, False

    if cell[1] < 0 or cell[1] > board_cols - 1:  # out of bounds horizontally
        return board, False

    if board[cell[0]][cell[1]] is True:  # wall -> ignore
        return board, False

    row, col = cell[0], cell[1]

    if board[row][col] is not False:
        # board[row][col] = min(curr_value + 1, board[row][col])
        return board, False

    board[row][col] = cell_value + 1

    return board, True


def mark(board, start, board_rows, board_cols, cell_value):
    global neighbour_cells
    row, col = start[0], start[1]
    potential_neighbours = {
        (row+1, col): False,
        (row-1, col): False,
        (row, col+1): False,
        (row, col-1): False,
    }

    for n in potential_neighbours:  # try to mark potential neighbours, if they can be marked => True else =>False
        board, potential_neighbours[n] = mark_neighbour(board, n, board_rows, board_cols, cell_value)

    for n in potential_neighbours:  # append valid neighbours
        if potential_neighbours[n]:
            neighbour_cells.append(n)

    return board


def find_min_path(board, start, end):
    global neighbour_cells

    board[start[0]][start[1]] = 0 # mark staring point to 0
    neighbour_cells.append(start)
    board_rows = len(board)
    board_cols = len(board[0])

    while len(neighbour_cells) != 0:
        # pop  element from front and mark all its neighbours add them to queue
        cell = neighbour_cells.popleft()

        # optimization if cell == end-cell, then break no need to process rest
        if cell == end:
            break

        # mark all the neighbouring points (cell_value+1)
        board = mark(board, cell, board_rows, board_cols, cell_value = board[cell[0]][cell[1]])

    return board, board[end[0]][end[1]] if board[end[0]][end[1]] else 'Cannot reach end point :('


if __name__ == '__main__':
    board = [[False, False, False, False],
             [True, True, False, True],
             [False, False, False, False],
             [False, False, False, False]]




    for i in board:
        print(i)

    print("\n\n")

    res, steps = find_min_path(board, start=(3,0), end=(0,0))

    for i in res:
        print(i)

    print("\n\n")

    print("Min number of steps required: {}".format(steps))