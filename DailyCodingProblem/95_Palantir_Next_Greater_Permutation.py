"""
This problem was asked by Palantir.

Given a number represented by a list of digits, find the next greater permutation of a number,
in terms of lexicographic ordering.
If there is not greater permutation possible, return the permutation with the lowest value/ordering.

For example, the list [1,2,3] should return [1,3,2]. The list [1,3,2] should return [2,1,3].
The list [3,2,1] should return [1,2,3].

Can you perform the operation without allocating extra memory (disregarding the input memory)?
"""

def next_permutation(arr):
    descending = True
    d = None  # index of number
    for i in range(1, len(arr)):
        if arr[i-1] > arr[i]:
            descending = False
            d = i - 1
            break


    if descending:
        arr[-1], arr[-2] = arr[-2], arr[-1]
        return arr





if __name__ == '__main__':
    print(next_permutation([1, 3, 2]))

