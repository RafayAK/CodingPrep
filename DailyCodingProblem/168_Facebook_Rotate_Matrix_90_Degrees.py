"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Given an N by N matrix, rotate it by 90 degrees clockwise.

For example, given the following matrix:

    [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
you should return:

    [[7, 4, 1],
     [8, 5, 2],
     [9, 6, 3]]
Follow-up: What if you couldn't use any extra space?
"""
from copy import deepcopy

# naive solution runs in O(n^2) and requires O(n^2) space
# where n is the length of the matrix

def rotate_90(arr_2d:list):
    result = deepcopy(arr_2d)

    # turn rows of input array to col
    for r in range(len(arr_2d)):
        row = arr_2d[r]
        for i in range(len(row)):
            result[i][len(result) -1 - r] = row[i]

    return result

def rotate_90_redux(matrix):
    n = len(matrix)

    for i in range(n //2):
        for j in range(i, n - i -1):
            p1 = matrix[i][j]
            p2 = matrix[j][ n - 1 - i]
            p3 = matrix[n - i - 1][n - j - 1]
            p4 = matrix[n - j - 1][i]

            matrix[j][n-i-1] = p1
            matrix[n - i - 1][n - j -1] = p2

            matrix[n - j - 1][i] = p3
            matrix[i][j] = p4


if __name__ == '__main__':
    print(rotate_90_redux([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]]))