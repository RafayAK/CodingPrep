'''
This problem was asked by Airbnb.

Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
'''

memo_dict = {}

def max_sum(arr):
    if tuple(arr) in memo_dict:
        return memo_dict[tuple(arr)]

    if len(arr)==0:
        return 0
    if len(arr)==1:
        memo_dict[tuple(arr)] = arr[0]
        return arr[0]
    if len(arr) == 2:
        memo_dict[tuple(arr)] = max(arr[0], arr[1])
        return max(arr[0], arr[1])

    memo_dict[tuple(arr)] = max(arr[0],max_sum(arr[2:])+arr[0], max_sum(arr[1:]))
    return memo_dict[tuple(arr)]


def max_sum_const_space(arr):
    # prevOne -> max from one step back
    # prevTwo -> max from two steps back
    # res -> current max
    prevOne, prevTwo, res = 0, 0, 0

    for i in range(arr.__len__()):
        if i == 0:
            res = arr[0]
        elif i ==1:
            res = max(arr[0], arr[1])
        else:
            res = max(arr[i], prevOne, prevTwo + arr[i])

        prevTwo= prevOne
        prevOne = res

    return res
if __name__ == '__main__':

    arr = [2, 4, 6, 2, 5]
    # arr = [10,-1,-1,-1,]
    res = max_sum_const_space(arr)

    print(res)
