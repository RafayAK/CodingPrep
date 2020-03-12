"""
This problem was asked by Facebook.

Given an array of integers in which two elements appear exactly once and
all other elements appear exactly twice, find the two elements that appear only once.

For example, given the array [2, 4, 6, 8, 10, 2, 6, 10], return 4 and 8. The order does not matter.

Follow-up: Can you do this in linear time and constant space?
"""


def occur_once(array):

    for i in range(len(array)):
        if i % 2 != 0:
            array[i] = - array[i]

    s = sum(array)
    b = 0
    for i in array:
        b += i

    for num in array:
        if s - num in array:
            return num, s-num

    return None

if __name__ == '__main__':
    print(occur_once([2, 4, 6, 8, 10, 2, 6, 10]))