"""
This problem was asked by Google.

On our special chessboard, two bishops attack each other if they share the same diagonal.
This includes bishops that have another bishop located between them, i.e. bishops can attack through pieces.

You are given N bishops, represented as (row, column) tuples on a M by M chessboard.
Write a function to count the number of pairs of bishops that attack each other.
The ordering of the pair doesn't matter: (1, 2) is considered the same as (2, 1).

For example, given M = 5 and the list of bishops:

(0, 0)
(1, 2)
(2, 2)
(4, 0)
The board would look like this:

[b 0 0 0 0]
[0 0 b 0 0]
[0 0 b 0 0]
[0 0 0 0 0]
[b 0 0 0 0]
You should return 2, since bishops 1 and 3 attack each other, as well as bishops 3 and 4.
"""
memo_attacking_pair = {}

#diag_moves->row_iter, col_iter
moves = [
            (-1, -1),
            (-1, +1),
            (+1, -1),
            (+1, +1)
        ]


def find_attacking_bishops(start_row, start_col, board):
    global memo_attacking_pair, moves
    size_of_board = len(board)

    def helper(row, col, move, attackers=0):
        # if out of bounds of the board return number of attackers found up till now
        if row < 0 or col<0 or row == size_of_board or col == size_of_board:
            return attackers

        # if a bishop is found increment num of attackers by 1
        if board[row][col] == 'b':
            # check if we've seen this pair before
            if (row, col) in memo_attacking_pair and memo_attacking_pair[(row, col)] == (start_row, start_col):
                pass
            else:
                attackers = +1
                # store attacking pairs so that next time we dont count it
                memo_attacking_pair[(start_row, start_col)] = (row, col)

        return helper(row+move[0], col+move[1], move, attackers)

    num_attackers = 0
    for row_iter, col_iter in moves:
        # check if this diagonal has already been visited
        num_attackers += helper(start_row+row_iter, start_col+col_iter, move=(row_iter, col_iter))

    return num_attackers


def create_board(size_of_board, bishop_positions):
    board = [[0 for _ in range(size_of_board)] for _ in range(size_of_board)]
    for row,col in bishop_positions:
        board[row][col] = 'b'

    return board


def num_attacking_bishops(M, list_of_bishops):
    # create board
    board = create_board(M, list_of_bishops)  # don't really need the board, added just for debugging

    num_of_attacking_bishops = 0
    # loop over all the positions in list
    for row, col in list_of_bishops:
        num_of_attacking_bishops += find_attacking_bishops(start_row=row, start_col=col, board=board)

    return num_of_attacking_bishops



if __name__ == '__main__':
    print(num_attacking_bishops(5, [(0, 0), (1, 2), (2, 2), (4, 0)])) # ans = 2
    print(num_attacking_bishops(5,[(0, 0), (1, 2), (2, 2)])) # ans =1