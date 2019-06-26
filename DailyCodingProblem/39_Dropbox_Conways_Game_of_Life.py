"""
Conway's Game of Life takes place on an infinite two-dimensional
board of square cells. Each cell is either dead or alive, and at each tick,
the following rules apply:

 - Any live cell with less than two live neighbours dies.
 - Any live cell with two or three live neighbours remains living.
 - Any live cell with more than three live neighbours dies.
 - Any dead cell with exactly three live neighbours becomes a live cell.
 - A cell neighbours another cell if it is horizontally, vertically, or diagonally adjacent.

Implement Conway's Game of Life. It should be able to be initialized with a starting list
of live cell coordinates and the number of steps it should run for. Once initialized,
it should print out the board state at each step. Since it's an infinite board,
print out only the relevant coordinates, i.e. from the top-leftmost live cell to
bottom-rightmost live cell.

You can represent a live cell with an asterisk (*) and a dead cell with a dot (.).
"""

import copy


class GameOfLife:
    def __init__(self, alive_coordinates: list, steps=0):
        # self.board, new_alive_coordinates= self.define_board(alive_coordinates)
        self.board = self.define_board(alive_coordinates)
        self.print_board()
        print('\n------------\n')
        for i in range(steps):
            print("Step number: {}\n".format(i))
            self.board = self.tick()
            self.print_board()
            print('\n------------\n')


    def tick(self):

        # pad the board before simulation
        padded_board = self.pad_board(self.board)
        temp_board = copy.deepcopy(padded_board)

        new_alive_coordinates = list()  # store alive cell coordinates to later prune the no-active areas of the board.

        board_rows = len(padded_board)
        board_cols = len(padded_board[0])

        # make changes in temp board looking at padded board
        for row in range(board_rows):
            for col in range(board_cols):
                neighbours = self.get_neighbours(padded_board, pos=(row, col))
                num_alive_neighbours = sum(neighbours)

                cell = padded_board[row][col] # look at the cell itself
                # check cell state
                if cell == 1:
                    # cell is alive
                    if num_alive_neighbours > 3 or num_alive_neighbours < 2:
                        #cell dies
                        temp_board[row][col] = 0
                    else:
                        # otherwise continue living
                        new_alive_coordinates.append((row,col))
                else:
                    # cell is in dead state
                    if num_alive_neighbours == 3:
                        # cell rises from the dead
                        temp_board[row][col] = 1
                        new_alive_coordinates.append((row,col))

        # prune empty rows and cols by figuring out where alive cells are
        min_row = min(new_alive_coordinates, key=lambda x: x[0])[0]
        max_row = max(new_alive_coordinates, key=lambda x: x[0])[0]

        min_col = min(new_alive_coordinates, key=lambda x: x[1])[1]
        max_col = max(new_alive_coordinates, key=lambda x: x[1])[1]

        temp_board = temp_board[min_row:max_row+1]  # remove non-active rows
        for i in range(len(temp_board)): # remove non-active cols
            temp_board[i] = temp_board[i][min_col:max_col+1]

        return temp_board

    @staticmethod
    def pad_board(board):
        # make changes in temp board looking at padded_board
        padded_board = copy.deepcopy(board)

        # create empty row, same size as the board cols
        empty_row = [0 for _ in range(len(board[0]))]

        # -> add to empty rows before and after the board
        padded_board = [empty_row] + padded_board + [empty_row]
        # -> add empty col before and after row
        for i in range(len(padded_board)):
            padded_board[i] = [0] + padded_board[i] + [0]
        return padded_board

    def define_board(self, alive_coordinates):
        min_row = min(alive_coordinates, key=lambda x: x[0])[0]
        max_row = max(alive_coordinates, key=lambda x: x[0])[0]

        min_col = min(alive_coordinates, key=lambda x: x[1])[1]
        max_col = max(alive_coordinates, key=lambda x: x[1])[1]

        # create board
        board = [[0 for _ in range(max_col-min_col+1)] for _ in range(max_row-min_row+1)]

        # new_coordinates = list()
        # mark the alive coordinates
        for cell in alive_coordinates:
            row, col= cell
            row -=min_row
            col -=min_col
            board[row][col] = 1
            # new_coordinates.append((row, col))  # new alive cell after scaling rows and cols

        return board#, new_coordinates

    @staticmethod
    def get_neighbours(board, pos):
        row, col = pos  # position of target cell

        board_rows = len(board)
        board_cols = len(board[0])

        neighbours = []

        for i in [-1, 0, 1]:
            neighbour_row = row + i

            # check for out of bound rows
            if neighbour_row >= board_rows or neighbour_row < 0:
                continue

            for j in [-1, 0, 1]:
                neighbour_col = col + j

                # check for out of bound cols
                if neighbour_col >= board_cols or neighbour_col < 0:
                    continue

                # ignore the cell it self, only interested in neighbours
                if neighbour_col == col and neighbour_row == row:
                    continue

                neighbours.append(board[neighbour_row][neighbour_col])

        return neighbours

    def print_board(self):
        board_rows = len(self.board)
        board_cols = len(self.board[0])

        for row in range(board_rows):
            for col in range(board_cols):
                if self.board[row][col] == 1:
                    print('*', end=' ')
                else:
                    print('.', end=' ')

            print(end='\n')  # new line



if __name__ == '__main__':
    #Conway = GameOfLife([(5, 0), (6, 1), (1, 2), (1, 1)], steps=3)
    #Conway = GameOfLife(alive_coordinates=[(0,0), (1,0), (2,2)], steps=5)
    # Conway = GameOfLife(alive_coordinates=[(1, 0), (2, 1), (0, 2), (1, 2), (2, 2)], steps=5)
    # Conway = GameOfLife(alive_coordinates=[(0, 0), (1, 0), (1, 1), (1,5)], steps=5)
    # Conway = GameOfLife(alive_coordinates=[(0, 0), (1, 0), (1, 1), (1, 5), (2,5), (2,6)], steps=4)
    Conway = GameOfLife(alive_coordinates=[(0, 0), (1, 0), (1, 1),
                                           (2, 5), (2, 6), (3, 9),
                                           (4, 8), (5, 10)], steps=4)


    # Conway = GameOfLife(alive_coordinates=[(0, 0), (1, 0), (1, 1),
    #                                        (2, 5), (2, 6), (2, 7),
    #                                         (5, 10)], steps=4)

    # https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life#Examples_of_patterns

    # Toad
    # Conway = GameOfLife(alive_coordinates=[(2, 5), (2, 6), (2, 7),
    #                                        (3,6), (3,7),(3,8)], steps=4)

    # blinker
    # Conway = GameOfLife(alive_coordinates=[(2, 5), (2, 6), (2, 7)], steps=4)

    # beacon
    # Conway = GameOfLife(alive_coordinates=[(2, 1), (1, 1), (1, 2),
    #                                        (4, 3), (4, 4), (3, 4)], steps=8)

    # glider
    # Conway = GameOfLife(alive_coordinates=[(1, 3), (2, 3), (3, 3),
    #                                        (2, 1), (3, 2)], steps=11)