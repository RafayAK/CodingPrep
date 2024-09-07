"""
This question was asked by Google.

Given an N by M matrix consisting only of 1's and 0's, find the largest rectangle containing only 1's
and return its area.

For example, given the following matrix:

[[1, 0, 0, 0],
 [1, 0, 1, 1],
 [1, 0, 1, 1],
 [0, 1, 0, 0]]
Return 4.
"""

# idea: use the idea of 4 connected components to figure our the largest rect
# mark visited cells with 2

def find_first_one(arr2d):
    for row in range(len(arr2d)):
        if 1 in arr2d[row]:
            return row, arr2d[row].index(1)

    return None

def find_largest_rectangle(arr:list):

    h, w = 0,0

    temp_h, temp_w = 1, 1
    def perform_4_connected_comps(arr, row, col, max_rows, max_cols):
        nonlocal temp_h, temp_w

        # go right and increase width
        if col+1 < max_cols and arr[row][col+1] == 1:
            arr[row][col + 1] = 2
            temp_w += 1
            perform_4_connected_comps(arr, row, col+1, max_rows, max_cols)

        # go left don't increase width
        if col-1 > -1 and arr[row][col - 1] == 1:
            arr[row][col - 1] = 2
            perform_4_connected_comps(arr, row, col - 1, max_rows, max_cols)

        # go down increase length
        if row+1 < max_rows and arr[row+1][col] == 1:
            arr[row+1][col] = 2
            temp_h += 1
            perform_4_connected_comps(arr, row+1, col, max_rows, max_cols)

        # go up and don't length
        if row-1 < -1 and arr[row-1][col] == 1:
            arr[row-1][col] = 2
            perform_4_connected_comps(arr, row-1, col, max_rows, max_cols)

    max_rows, max_cols = len(arr), len(arr[0])
    index_of_one = find_first_one(arr)
    while index_of_one:
        temp_h, temp_w = 1, 1
        arr[index_of_one[0]][index_of_one[1]] = 2

        perform_4_connected_comps(arr, index_of_one[0], index_of_one[1], max_rows, max_cols)

        if temp_w*temp_h > w*h:
            w = temp_w
            h = temp_h

        index_of_one = find_first_one(arr)

    return w*h

if __name__ == '__main__':
    arr = [[1, 0, 0, 0],
          [1, 0, 1, 1],
          [1, 0, 1, 1],
          [0, 1, 0, 0]]

    print(find_largest_rectangle(arr))