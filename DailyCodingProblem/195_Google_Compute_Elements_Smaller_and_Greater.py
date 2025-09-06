"""
This problem was asked by Google.

Let A be an N by M matrix in which every row and every column is sorted.

Given i1, j1, i2, and j2, compute the number of elements of M smaller than M[i1, j1] and larger than M[i2, j2].

For example, given the following matrix:

       0  1  2  3    4  5

0 -  [[1, 3, 7, 10, 15, 20],
1 -   [2, 6, 9, 14, 22, 25],
2 -   [3, 8, 10, 15, 25, 30],
3 -   [10, 11, 12, 23, 30, 35],
4 -   [20, 25, 30, 35, 40, 45]]

And i1 = 1, j1 = 1, i2 = 3, j2 = 3, return 15 as there are 15 numbers in the matrix smaller than 6 or greater than 23.


NOTE: Typo is question there are only 14 elements in the matrix smaller than 6 or greater than 23

"""
from math import ceil


def count_outside_range(matrix, i1, j1, i2, j2):

    def count_smaller_in_row(row, value):
        if row[0] > value:
            # if the smallest is bigger than the value, then there are None
            return 0
        if row[-1] < value:
            # if the largest is smaller than the value, then the entire row is eligible
            return len(row)

        mid = len(row) // 2

        if row[mid] >= value:
            # if the mid of the row is greater or equal than the value,
            # we need to look only on the left of the mid-point
            return count_smaller_in_row(row[:mid], value)
        else:
           # Count up till the mid of the row and see if anything is left still to the right of the mid-point
            return (mid + 1) + count_smaller_in_row(row[mid+1:], value)

    def count_larger_in_row(row, value):
        if row[0] > value:
            # if the smallest value in the row is larger than the value, then all the values in the row are eligible
            return len(row)
        if row[-1] < value:
            # if the largest value in the row is smaller than or equal to the value, then none are eligible
            return 0

        mid = len(row) // 2

        if row[mid] <= value:
            # we only need to look at the right of the mid-point
            return count_larger_in_row(row[mid + 1: ], value)
        else:
            # count up everything to the right of the mid-pint and see if anything is still left
            # to the right of it.
            return (len(row) - mid) + count_larger_in_row(row[:mid], value)

    total = 0
    lower_than = matrix[i1][j1]
    greater_than = matrix[i2][j2]
    for row in matrix:
        total += count_smaller_in_row(row, lower_than)
        total += count_larger_in_row(row, greater_than)

    return total




if __name__ == '__main__':
    matrix = [[1, 3, 7, 10, 15, 20],
              [2, 6, 9, 14, 22, 25],
              [3, 8, 10, 15, 25, 30],
              [10, 11, 12, 23, 30, 35],
              [20, 25, 30, 35, 40, 45]]

    print(count_outside_range(matrix, 1, 1, 3, 3))
    assert count_outside_range(matrix, 1, 1, 3, 3) == 14
