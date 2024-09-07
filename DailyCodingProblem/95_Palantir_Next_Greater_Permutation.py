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
    for i in range(len(arr)-1, -1, -1):
        if arr[i] > arr[i-1]:
            break

    if i == 0:
        return arr[::-1]
    else:
        # get the index smallest value to the right of i-1 larger then
        # the value at index i-1 and swap them
        smallest_idx = arr[i:].index(min(filter(lambda x:x>arr[i-1], arr[i:]))) + i
        arr[smallest_idx], arr[i-1] = arr[i-1], arr[smallest_idx]
        arr[i:] = sorted(arr[i:])

        return arr


if __name__ == '__main__':
    arr1 = [1,2,3]
    print("Starting permutation: {}".format(arr1))

    next_perm = next_permutation(arr1.copy())
    while next_perm != arr1:
        print(next_perm)
        next_perm = next_permutation(next_perm)
    print(next_perm)

    print("\n ----------- \n")
    arr1 = [1,2,3,4]
    print("Starting permutation: {}".format(arr1))

    next_perm = next_permutation(arr1.copy())
    while next_perm != arr1:
        print(next_perm)
        next_perm = next_permutation(next_perm)
    print(next_perm)