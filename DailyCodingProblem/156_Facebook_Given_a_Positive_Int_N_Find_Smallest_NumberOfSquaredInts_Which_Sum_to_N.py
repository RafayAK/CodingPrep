"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Given a positive integer n, find the smallest number of squared integers which sum to n.

For example, given n = 13, return 2 since 13 = 3^2 + 2^2 = 9 + 4.

Given n = 27, return 3 since 27 = 3^2 + 3^2 + 3^2 = 9 + 9 + 9.
"""

# exponential time algo, O(n^n), pretty poor Rafay boy!
def squared_sum_to_n(n:int, curr_ele=None):
    if curr_ele is None:
        curr_ele = []

    if n == 0:
        return len(curr_ele), curr_ele

    min_sum_squares = float("inf")
    min_elements = []
    num = 1

    while num**2 <= n:
        new_min, new_min_elements = squared_sum_to_n(n - num**2, curr_ele + [num])

        if new_min < min_sum_squares:
            min_sum_squares = new_min
            min_elements = new_min_elements

        num += 1
    return min_sum_squares, min_elements

# aah much better using dynamic programming
# O(n^2)
def squared_sum_to_n_redux(n:int):
    # create cache map for all the min sum from 0 to n inclusive
    # initially set all to inf
    min_sum_map = [float("inf") for i in range(n+1)]

    # the min sum for the 0th element to 0
    min_sum_map[0] = 0

    # iterate over nums from 1 to n and compute the min sum required for each
    for num in range(1, n+1):
        # start building min sum by removing squares starting form 1
        j = 1
        while j**2 <= num:
            # iteratively check of new min by removing a squared number form num
            min_sum_map[num] = min(min_sum_map[num], min_sum_map[num-j**2]+1)
            j += 1
    return min_sum_map[n]


if __name__ == "__main__":
    # print("3: {}".format(squared_sum_to_n(3)))
    # print("4: {}".format(squared_sum_to_n(4)))
    # print("7: {}".format(squared_sum_to_n(7)))
    # print("13: {}".format(squared_sum_to_n(13)))
    # print("9: {}".format(squared_sum_to_n(9)))
    # print("27: {}".format(squared_sum_to_n(27)))

    print("3: {}".format(squared_sum_to_n_redux(3)))
    print("4: {}".format(squared_sum_to_n_redux(4)))
    print("7: {}".format(squared_sum_to_n_redux(7)))
    print("13: {}".format(squared_sum_to_n_redux(13)))
    print("9: {}".format(squared_sum_to_n_redux(9)))
    print("27: {}".format(squared_sum_to_n_redux(27)))