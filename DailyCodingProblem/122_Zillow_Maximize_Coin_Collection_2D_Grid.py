"""
This question was asked by Zillow.

You are given a 2-d matrix where each cell represents number of coins in that cell.
Assuming we start at matrix[0][0], and can only move right or down,
find the maximum number of coins you can collect by the bottom right corner.

For example, in this matrix

0 3 1 1
2 0 0 4
1 5 3 1
The most we can collect is 0 + 2 + 1 + 5 + 3 + 1 = 12 coins.
"""

def collect_max_coins(matrix):
    def helper(row=0, col=0, curr_sum=0):
        if row>=len(matrix) or col>=len(matrix[0]):
            return 0

        if row==len(matrix)-1 and col == len(matrix[0])-1:
            return curr_sum+matrix[row][col]

        return max(helper(row+1, col, curr_sum+matrix[row][col]), helper(row, col+1, curr_sum+matrix[row][col]))

    return helper()

if __name__ == '__main__':
    matrix = [
        [0, 3, 1, 1],
        [2, 0, 0, 4],
        [1, 5, 3, 1]
    ]

    print(collect_max_coins(matrix))