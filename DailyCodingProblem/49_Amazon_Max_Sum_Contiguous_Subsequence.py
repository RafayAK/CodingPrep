"""
This problem was asked by Amazon.

Given an array of numbers, find the maximum sum of any contiguous subarray of the array.

For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would be 137,
since we would take elements 42, 14, -5, and 86.

Given the array [-5, -1, -8, -9], the maximum sum would be 0, since we would not take any elements.

Do this in O(N) time.
"""

def find_max_sum(arr):  # not optimal the 'sum' function mainly is slowing it down
    if len(arr) == 1:
        return 0 if arr[0] < 0 else arr[0]

    sum_of_arr = sum(arr)

    s1 = find_max_sum(arr[1:])
    s2 = find_max_sum(arr[:-1])

    if sum_of_arr > 0 and sum_of_arr > s1 and sum_of_arr > s2:
        return sum_of_arr
    elif s1 > s2 and s1>0:
        return s1
    elif s2 > s1 and s2>0:
        return s2
    else:
        return 0


def find_max_sum_optimized(arr):
    if not arr or max(arr) < 0:
        return 0

    curr_max_sum = arr[0]
    overall_max_sum = arr[0]

    for num in arr[1:]:
        curr_max_sum = max(curr_max_sum, curr_max_sum+num)
        overall_max_sum = max(curr_max_sum, overall_max_sum)

    return overall_max_sum

if __name__ == '__main__':
    # print(find_max_sum([34, -50, 42, 14, -5, 86]))
    # print(find_max_sum([-5, -1, -8, -9]))
    print(find_max_sum_optimized([34, -50, 42, 14, -5, 86]))
    print(find_max_sum_optimized([-5, -1, -8, -9]))