"""
This problem was asked by Microsoft.

Given an array of numbers, find the length of the longest increasing subsequence in the array.
The subsequence does not necessarily have to be contiguous.

For example, given the array [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15],
the longest increasing subsequence has length 6: it is 0, 2, 6, 9, 11, 15.
"""

memo_dict = None
def helper(arr, seq=[], recur_depth = 0):
    if len(arr) == 0:
        memo_dict[seq[recur_depth]] = seq[recur_depth:]
        return seq

    longest_seq = []

    for i in range(len(arr)):
        if arr[i] > seq[-1]:
            res = helper(arr[i+1:], seq+[arr[i]], recur_depth+1)
            if len(res) >= len(longest_seq):
                longest_seq = res

    memo_dict[seq[recur_depth]] = longest_seq[recur_depth:]
    return longest_seq


def long_subsequence(arr):
    longest = []
    global memo_dict
    memo_dict = {}
    for i in range(len(arr)):
        if arr[i] in memo_dict:
            res = memo_dict[arr[i]]
        else:
            res = helper(arr[i+1:], [arr[i]])
        # print("->>>> res: {}".format(res))
        if len(res) > len(longest):
            longest = res

    return longest

if __name__ == '__main__':
    print(long_subsequence([0, 4, 6, 2, 3, 5, 9]))
    print(long_subsequence([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]))