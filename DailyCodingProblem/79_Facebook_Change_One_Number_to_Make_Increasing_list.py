"""
This problem was asked by Facebook.

Given an array of integers, write a function to determine whether
the array could become non-decreasing by modifying at most 1 element.

For example, given the array [10, 5, 7], you should return true,
since we can modify the 10 into a 1 to make the array non-decreasing.

Given the array [10, 5, 1], you should return false,
since we can't modify any one element to get a non-decreasing array.
"""


def is_non_decreasing(arr):
    num_of_decreasing = 0

    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            num_of_decreasing += 1

    return num_of_decreasing <= 1


if __name__ == '__main__':
    print(is_non_decreasing([1,2,3]))  # True
    print(is_non_decreasing([10,5,7]))  # True
    print(is_non_decreasing([10, 5, 1]))  # False
    print(is_non_decreasing([1, 2, 3, -1, 4]))  # True
    print(is_non_decreasing([1, 2, 3, -1, 4, -1, 5]))  # False
