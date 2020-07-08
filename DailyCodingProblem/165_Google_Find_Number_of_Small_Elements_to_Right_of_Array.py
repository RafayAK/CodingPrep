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

if __name__ == '__main__':
    print(count_smaller_on_right([3, 4, 9, 6, 1]))
    print(count_smaller_on_right([3, 2, 4, 9, 6, 1, 0]))





