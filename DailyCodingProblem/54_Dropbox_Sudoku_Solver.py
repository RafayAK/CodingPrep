"""
This problem was asked by Dropbox.

Sudoku is a puzzle where you're given a partially-filled 9 by 9 grid with digits.
The objective is to fill the grid with the constraint that every row, column, and box (3 by 3 subgrid)
must contain all of the digits from 1 to 9.

Implement an efficient sudoku solver.
"""

def get_col(matrix, col):
    return [row[col] for row in matrix]


def check_row_valid(num, row):
    if num in row:
        return False
    return True


def check_col_valid(num, col):
    if num in col:
        return False
    return True


def get_block(row, col, puzzle):
    block_row_start = 3*(row//3)
    block_col_start = 3*(col // 3)

    block_vals = []
    for i in range(block_row_start, block_row_start+3):
        for j in range(block_col_start, block_col_start+3):
            block_vals.append(puzzle[i][j])

    return block_vals


def check_3x3_box(num, box):
    if num in box:
        return False
    return True


def check_board_filled(puzzle):
    # return True when all elements are filled
    return all(all(val is not 'O' for val in row) for row in puzzle)


def get_first_empty_cell(puzzle):
    for row in range(9):
        for col in range(9):
            if puzzle[row][col] == 'O':
                return row, col


def check_valid(row, col, num):
    if check_col_valid(num, get_col(puzzle, col)) is False:
        return False
    if check_row_valid(num, puzzle[row]) is False:
        return False
    if check_3x3_box(num, get_block(row, col, puzzle)) is False:
        return False

    return True


def solve_puzzle(puzzle):
    # check if puzzle is solved
    if check_board_filled(puzzle):
        return puzzle

    # get and empty cell row
    cell_row, cell_col = get_first_empty_cell(puzzle)

    # try numbers 1-9
    for num in range(1, 10):
        if check_valid(cell_row, cell_col, num):
            puzzle[cell_row][cell_col] = num

            result = solve_puzzle(puzzle)
            if check_board_filled(result):
                return result

        puzzle[cell_row][cell_col] = 'O'

    return puzzle

def print_puzzle(puzzle):
    coliter =0
    row_iter=0

    for row_iter in range(0, 9):
        if row_iter %3 ==0 and row_iter !=0:
            print('-----------------------')
        for coliter in range(0,9):
            if coliter % 3 ==0:
                print('|', end=' ')
            print(puzzle[row_iter][coliter], end=' ')

        print() # simply moves cursor to next line

if __name__ == '__main__':
    puzzle = [
        ['O', 'O', 'O', 'O', 2, 'O', 'O', 9, 'O'],
        [3, 'O', 'O', 8, 'O', 'O', 'O', 'O', 'O'],
        ['O', 5, 'O', 'O', 'O', 'O', 'O', 'O', 6],
        ['O', 2, 'O', 'O', 'O', 'O', 'O', 1, 'O'],
        ['O', 'O', 'O', 4, 1, 'O', 'O', 7, 'O'],
        ['O', 'O', 9, 'O', 7, 'O', 4, 'O', 3],
        ['O', 'O', 'O', 5, 'O', 'O', 'O', 'O', 'O'],
        [5, 'O', 7, 'O', 'O', 'O', 'O', 3, 'O'],
        [6, 'O', 'O', 'O', 'O', 'O', 'O', 8, 'O']
    ]

    print_puzzle(puzzle)

    print("\n Solved Puzzle: \n")

    print_puzzle(solve_puzzle(puzzle))


