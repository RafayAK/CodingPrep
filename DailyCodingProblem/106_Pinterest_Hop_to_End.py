"""
This problem was asked by Pinterest.

Given an integer list where each number represents the number of hops you can make,
determine whether you can reach to the last index starting at index 0.

For example, [2, 0, 1, 0] returns True while [1, 1, 0, 1] returns False.
"""


def can_hop_to_end(arr:list, curr_idx=0):
    if curr_idx == len(arr)-1:
        return True

    hops = arr[curr_idx]

    if hops == 0:
        return False

    for h in range(1,hops+1):
        if can_hop_to_end(arr, curr_idx+h):
            return True

    return False

if __name__ == '__main__':
    # arr = [2, 0, 1, 0]
    # arr = [1,1, 0, 1]
    arr = [5, 0]
    print(can_hop_to_end(arr))