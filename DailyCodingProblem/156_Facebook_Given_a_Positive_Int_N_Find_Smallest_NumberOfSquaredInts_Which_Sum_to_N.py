"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Given a positive integer n, find the smallest number of squared integers which sum to n.

For example, given n = 13, return 2 since 13 = 3^2 + 2^2 = 9 + 4.

Given n = 27, return 3 since 27 = 3^2 + 3^2 + 3^2 = 9 + 9 + 9.
"""


def squared_sum_to_n(n:int, curr_ele=None):
    if curr_ele is None:
        curr_ele = []
    if n == 0:
        return 0, curr_ele

    min_num_squares = float('inf')
    min_elements = []
    i = 1
    while n - i**2 >=0:
        new_min, min_elements = squared_sum_to_n(n-i**2, curr_ele+[i])
        if new_min < min_num_squares:
            min_num_squares = new_min+1
            min_elements = min_elements

        i +=1

    return min_num_squares, min_elements

if __name__ == "__main__":
    print(squared_sum_to_n(13))
    # print(squared_sum_to_n(3))
    print(squared_sum_to_n(27))