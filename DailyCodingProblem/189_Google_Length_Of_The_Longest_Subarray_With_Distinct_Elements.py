"""
This problem was asked by Google.

Given an array of elements, return the length of the longest subarray where all its elements are distinct.

For example, given the array [5, 1, 3, 5, 2, 3, 4, 1], return 5 as the longest
subarray of distinct elements is [5, 2, 3, 4, 1].
"""

# using the snail method

def long_distinct_subarray(array):
    tail, head = 0, 1

    longest_subarray_len = 0
    while head <= len(array) and tail != head:
        elements = array[tail:head]
        s = set(elements)
        if len(elements) == len(s):  # distinct only if len(elements) == len(set(elements)
            if len(s) > longest_subarray_len:
                longest_subarray_len = len(s)
            head+=1
        else:
            tail+=1

    return longest_subarray_len


if __name__ == "__main__":
    assert long_distinct_subarray([5, 1, 3, 5, 2, 3, 4, 1]) == 5