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

    for num in array:
        if xored_sum ^ num in array:
            return xored_sum ^ num , num

if __name__ == '__main__':
    print(occur_once([2, 4, 6, 8, 10, 2, 6, 10]))