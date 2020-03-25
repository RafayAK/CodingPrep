"""
This problem was asked by Google.

Given an array of numbers and an index i, return the index of the nearest
larger number of the number at index i, where distance is measured in array indices.

For example, given [4, 1, 3, 5, 6] and index 0, you should return 3.

If two distances to larger numbers are the equal, then return any one of them.
If the array at i doesn't have a nearest larger integer, then return null.

Follow-up: If you can preprocess the array, can you do this in constant time?
"""

# O(n) implementation
def index_of_nearest_larger_num(arr, index):
    def search(idx, left=False):
        step = 1
        arr_size = len(arr)
        if left:
            step = -1
            arr_size = 0

        larger_index, larger_distance = None, float("inf")
        for i in range(idx, arr_size, step):
            if arr[i] > arr[index]:
                larger_distance = abs(i - index)
                larger_index = i
                break

        return larger_index, larger_distance

    left_index, left_distance = search(index, left=True)  # search left
    right_index, right_distance = search(index, left=False)  # serach right

    if left_distance < right_distance:
        return left_index
    else:
        return right_index


if __name__ == '__main__':
    print(index_of_nearest_larger_num([4, 1, 3, 5, 6], 0))
    print(index_of_nearest_larger_num([4, 1, 3, 5, 6], 1))
    print(index_of_nearest_larger_num([4, 1, 3, 5, 6], 4))