"""
This problem was asked by Amazon.

Given a N by M matrix of numbers, print out the matrix in a clockwise spiral.

For example, given the following matrix:

[[1,  2,  3,  4,  5],
 [6,  7,  8,  9,  10],
 [11, 12, 13, 14, 15],
 [16, 17, 18, 19, 20]]
You should print out the following:

1, 2, 3, 4, 5, 10, 15, 20, 19, 18, 17, 16, 11, 6, 7, 8, 9, 14, 13, 12
"""


def rm_last_col(arr):
    col = []
    for row in arr:
        col+=[row[-1]]
        del row[-1]

    return col, arr


def rm_first_col(arr):
    col = []
    for row in arr:
        col += [row[0]]
        del row[0]

    return col, arr

def spiral_print(arr):

    result = []
    mode = 'l'
    while arr:
        if mode is 'l':
            result+= arr[0]
            del(arr[0])
            mode = 'd'
        elif mode is 'd':
            col, arr = rm_last_col(arr)
            result+= col
            mode = 'r'
        elif mode is 'r':
            result+= arr[-1][::-1]  # reversed
            del(arr[-1])
            mode = 'u'
        elif mode is 'u':
            col, arr = rm_first_col(arr)
            result += col[::-1]  # reversed
            mode = 'l'

    print(*result, sep=', ')  # *->unpacks the list


if __name__ == '__main__':
    arr = [[1,  2,  3,  4,  5],
           [6,  7,  8,  9,  10],
           [11, 12, 13, 14, 15],
           [16, 17, 18, 19, 20]]

    spiral_print(arr)

