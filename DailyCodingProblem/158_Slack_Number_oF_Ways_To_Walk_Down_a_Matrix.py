"""
This problem was asked by Slack.

You are given an N by M matrix of 0s and 1s. Starting from the top left corner,
how many ways are there to reach the bottom right corner?

You can only move right and down. 0 represents an empty space while 1 represents a wall you cannot walk through.

For example, given the following matrix:

[[0, 0, 1],
 [0, 0, 1],
 [1, 0, 0]]
Return two, as there are only two ways to get to the bottom right:

Right, down, down, right
Down, right, down, right
The top left corner and bottom right corner will always be 0.
"""


def num_of_ways_to_traverse(map):
    successful_paths = []
    successes = 0

    num_of_rows = len(map)
    num_of_cols = len(map[0])

    def helper(curr_row=0, curr_col=0, path=None):
        nonlocal successes
        nonlocal successful_paths
        nonlocal num_of_rows
        nonlocal num_of_cols

        if path is None:
            path = []

        if curr_col == num_of_cols-1 and curr_row == num_of_rows -1:
            successes += 1
            successful_paths.append(path)

        # see if you can move right i.e in bounds and not wall
        if curr_col+1 < num_of_cols and map[curr_row][curr_col+1] !=1:
            helper(curr_row, curr_col+1, path+["Right"])

        # see if you can move down i.e in bounds and not wall
        if curr_row + 1 < num_of_rows and map[curr_row + 1][curr_col] != 1:
            helper(curr_row + 1, curr_col, path + ["Down"])

    helper()
    print(successful_paths)
    return successes if successes >0 else 0


if __name__ == '__main__':
    map = [[0, 0, 1],
           [0, 0, 1],
           [1, 0, 0]]

    print(num_of_ways_to_traverse(map))
