"""
This problem was asked by Coursera.

Given a 2D board of characters and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally
or vertically neighboring. The same letter cell may not be used more than once.

For example, given the following board:

[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
exists(board, "ABCCED") returns true, exists(board, "SEE") returns true, exists(board, "ABCB") returns false.
"""

def get_valid_moves(curr_row, curr_col, prev):
    valid_moves = []
    if prev!= (curr_row+1, curr_col):
        valid_moves.append((curr_row+1, curr_col))

    if prev!= (curr_row-1, curr_col):
        valid_moves.append((curr_row-1, curr_col))

    if prev!= (curr_row, curr_col+1):
        valid_moves.append((curr_row, curr_col+1))

    if prev!= (curr_row, curr_col-1):
        valid_moves.append((curr_row, curr_col-1))

def find_word(grid, word):
    def helper(grid, word, curr_row, curr_col, prev=None):
        if len(word) == 0:
            return True

        if curr_row >= len(grid) or curr_row < 0 or curr_col >= len(grid[0]) or curr_col < 0:
            return False

        if grid[curr_row][curr_col] == word[0]:
            up, down, left, right = False, False, False, False
            if prev != (curr_row+1, curr_col):  # try going up if not visited previously
                up = helper(grid, word[1:], curr_row+1, curr_col, prev=(curr_row, curr_col))
            if prev != (curr_row-1, curr_col):  # try going down if not visited previously
                down = helper(grid, word[1:], curr_row-1, curr_col, prev=(curr_row, curr_col))
            if prev != (curr_row, curr_col+1):  # try going right if not visited previously
                left = helper(grid, word[1:], curr_row, curr_col+1, prev=(curr_row, curr_col))
            if prev != (curr_row, curr_col-1):  # try going left if not visited previously
                right = helper(grid, word[1:], curr_row, curr_col-1, prev=(curr_row, curr_col))

            return up or down or left or right

        return False

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == word[0]:
                if helper(grid, word, row, col, prev=(row, col)):
                    return True

    return False


if __name__ == '__main__':
    grid = [
      ['A','B','C','E'],
      ['S','F','C','S'],
      ['A','D','E','E']
    ]
    print(find_word(grid, 'SEE'))
    print(find_word(grid, 'ABCB'))
    print(find_word(grid, 'ABCES'))
    print(find_word(grid, 'ABCCED'))