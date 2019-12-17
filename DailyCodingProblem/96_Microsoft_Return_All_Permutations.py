"""
This problem was asked by Microsoft.

Given a number in the form of a list of digits, return all possible permutations.

For example, given [1,2,3], return [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]].
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


# this uses the solution from DCP # 95
def all_permutations(arr):
    result = []

    result.append(arr)
    next_perm = next_permutation(arr.copy())
    while next_perm != arr:
        result.append(next_perm)
        next_perm = next_permutation(next_perm.copy())

    return result

# better than the previous sol, simpler
def all_permutations_redux(arr):
    perms = []
    def helper(arr, start=0):
        len_arr = len(arr)
        if len_arr - 1 == start:
            perms.append(arr)
            return

        for i in range(start, len_arr):
            new_arr = arr.copy()
            new_arr[start], new_arr[i] = new_arr[i], new_arr[start]
            helper(new_arr, start+1)

    helper(arr)
    return perms


if __name__ == '__main__':
    print(all_permutations([1,2,3]))
    print(all_permutations([3,2,1]))

    print("\n ---- \n")

    print(all_permutations_redux([1,2,3]))
    print(all_permutations_redux([3,2,1]))