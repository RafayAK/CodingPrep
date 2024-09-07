"""
This problem was asked by Facebook.

Given a circular array, compute its maximum subarray sum in O(n) time. A subarray can be empty,
and in this case the sum is 0.

For example, given [8, -1, 3, 4], return 15 as we choose the numbers 3, 4, and 8 where the 8
is obtained from wrapping around.

Given [-4, 5, 1, 0], return 6 as we choose the numbers 5 and 1.
"""

# Idea: Use Kadane's algo from DCP # 49 to first find max sum of contiguous sub-array unwrapped. Then min sum of
#       contiguous sub-array also unwrapped. Subtracting sum of array from min-sum of subarray will give max sum of sub-
#       array wrapped. Return max of either wrapped or unwrapped sub array


def max_subarray_sum(l):
    if len(l) == 0:
        return 0

    curr_max_sum = l[0]
    global_max_sum = l[0]

    for num in l[1:]:
        curr_max_sum = max(num, curr_max_sum+num)
        global_max_sum = max(curr_max_sum, global_max_sum)

    return global_max_sum


def min_subarray_sum(l):
    if len(l) == 0:
        return 0

    curr_min_sum = l[0]
    global_min_sum = l[0]

    for num in l[1:]:
        curr_min_sum = min(num, curr_min_sum + num)
        global_min_sum = min(curr_min_sum, global_min_sum)

    return global_min_sum


def max_circular_sum(l):
    max_sum_wrapped_subarray = sum(l) - min_subarray_sum(l)
    return max(max_subarray_sum(l), max_sum_wrapped_subarray)


if __name__ == '__main__':
    assert max_circular_sum([8, -1, 3, 4]) == 15
    assert max_circular_sum([-4, 5, 1, 0]) == 6