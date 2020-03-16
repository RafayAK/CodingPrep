"""
This problem was asked by Facebook.

Given an array of integers in which two elements appear exactly once and
all other elements appear exactly twice, find the two elements that appear only once.

For example, given the array [2, 4, 6, 8, 10, 2, 6, 10], return 4 and 8. The order does not matter.

Follow-up: Can you do this in linear time and constant space?
"""


def occur_once(array):
    xored_sum = array[0]

    for num in array[1:]:
        xored_sum = xored_sum ^ num

    # make this O(n) currently O(n^2)
    # for num in array:
    #     if xored_sum ^ num in array:
    #         return xored_sum ^ num, num

    # Now we have to find xored_sum is the sum of which two numbers?
    # idea: the numbers in xored_sum can be divided into two groups:
    #       1. the number with the most significant bit(MSB) => 1
    #       2. the number with the MSB => 0
    #
    # find the MSB from the right:
    msb = xored_sum & (xored_sum-1)

    # res_1 by the end will contain the number from group 2 that satisfies the condition,
    # similarly res_2 will contain the number from group 1
    res_1, res_2 = 0, 0
    for num in array:
        if num & msb == 0:
            res_1 ^= num
        else:
            res_2 ^= num

    return res_1, res_2


if __name__ == '__main__':
    assert occur_once([2, 4, 6, 8, 10, 2, 6, 10]) == (4, 8)
    assert occur_once([12 , 2, 4, 6, 8, 10, 2, 6, 10, 12]) == (4, 8)