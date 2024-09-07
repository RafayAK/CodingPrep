"""
This problem was asked by Google.

Given an array of integers, return a new array where each element in
the new array is the number of smaller elements to the right of that element in the original input array.

For example, given the array [3, 4, 9, 6, 1], return [1, 1, 2, 1, 0], since:

There is 1 smaller element to the right of 3
There is 1 smaller element to the right of 4
There are 2 smaller elements to the right of 9
There is 1 smaller element to the right of 6
There are no smaller elements to the right of 1

"""
# O(n^2) implementation
def count_smaller_on_right(arr:list):
    new_arr = []

    for i in range(len(arr)):
        count = 0
        curr_number = arr[i]

        for j in range(i+1, len(arr)):
            if arr[j] - curr_number < 0:
                count += 1
        new_arr.append(count)

    return new_arr

import bisect
# the bisect algo runs in O(log(n)) time and is similar to binary search
# the bisect.bisect_left() function returns the index from the left where a given
# element could be inserted, such that the point of insertion results in two halves
# one that is arr_values < x and the other x <= arr_values

# idea: the start from the right most elements and find the index where they would fit
# in a sorted list the index will represent the number of elements smaller to the right
# of the element

# total runtime of redux algo O(nLog(n))
def count_smaller_on_right_redux(arr:list):
    result = []

    sorted_list = []
    for val in reversed(arr):
        index = bisect.bisect_left(sorted_list, val)
        result.append(index)
        sorted_list.insert(index, val)

    result.reverse()
    return result


if __name__ == '__main__':

    print(count_smaller_on_right([3, 4, 9, 6, 1]))
    print(count_smaller_on_right([3, 2, 4, 9, 6, 1, 0, 9]))
    print(count_smaller_on_right([3, 4, 0, 1, 6, 9]))
    print("\n\n")
    print(count_smaller_on_right_redux([3, 4, 0, 1, 6, 9]))
    print(count_smaller_on_right_redux([3, 2, 4, 9, 6, 1, 0, 9]))





