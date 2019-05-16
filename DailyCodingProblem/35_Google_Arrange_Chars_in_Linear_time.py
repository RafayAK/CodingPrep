"""
This problem was asked by Google.

Given an array of strictly the characters 'R', 'G', and 'B', segregate the
values of the array so that all the Rs come first, the Gs come second,
and the Bs come last. You can only swap elements of the array.

Do this in linear time and in-place.

For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'],
it should become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].
"""



# idea : Keep two pointer at either end of the list.
#        The left pointer is used to place 'R's
#        The right end pointer is used to place 'B's
#        if at any point the right pointer and the iterator
#        over the list intersect, the list is sorted
def arrange(array: list):
    def swap(i, j):
        arr[i], arr[j] = arr[j], arr[i]

    R_ptr = 0  # pointer at left end of array
    B_ptr = len(arr) -1  # pointer at the right end of the array

    # set up an iterator 'it' to go over list and place A's and B's
    # according to where R_ptr and B_ptr are pointing at the moment
    # G's will be automatically end up at the right spots
    it = 0
    while it < len(arr):

        if it > B_ptr:
            break  # sorted the list

        if arr[it] == 'R' and it != R_ptr:
            # 'R' not in its correct spot
            swap(it, R_ptr)
            R_ptr+=1

            # continue to not update 'it', keep it in same spot just in case we need to swap again
            continue

        elif arr[it] == 'B' and it != B_ptr:
            # 'B' not in its correct spot
            swap(it, B_ptr)
            B_ptr-=1

            # continue to not update 'it', keep it in same spot just in case we need to swap again
            continue

        # update only when none of the above conditions are met
        it += 1

    return arr
if __name__ == '__main__':
    # arr = ['G', 'B', 'R', 'R', 'B', 'R', 'G']
    # arr = ['B','G', 'R']
    # arr = ['R', 'G', 'B']
    # arr = ['R', 'R', 'R']
    # arr = ['B', 'G', 'G']
    arr = ['G', 'G', 'R']
    print("Unsorted array: {}".format(arr))
    print("Sorted array: {}".format(arrange(arr)))
