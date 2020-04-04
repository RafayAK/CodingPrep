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


# A more elegant O(n) solution
def index_of_nearest_larger_num_redux(arr, index):
    for i in range(1, len(arr)):
        left = index - i
        right = index + i

        if left >= 0 and arr[left] > arr[index]:
            return arr[left], left
        if right < len(arr) and arr[right] > arr[index]:
            return arr[right], right

    return None


def preprocess(arr):
    cache = [None for _ in range(len(arr))]

    for j in range(len(arr) -1):
        if arr[j] > arr[j +1]:
            cache[j + 1] =j
        elif arr[j +1] > arr[j]:
            cache[j] = j+1

    return cache

def get_mapping_indices(arr):
    nl_indices = dict()
    sorted_tuples = [(x, i) for i, x in enumerate(arr)]
    sorted_tuples.sort(key=lambda x: x[0])

    for k, (_, i) in enumerate(sorted_tuples[:-1]):
        min_dist = len(arr)
        for m in range(k + 1, len(sorted_tuples)):
            dist = abs(i - sorted_tuples[m][1])
            if dist < min_dist:
                min_dist = dist
                nl_indices[i] = sorted_tuples[m][1]

    return nl_indices


if __name__ == '__main__':
    # print(index_of_nearest_larger_num([4, 1, 3, 5, 6], 0))
    # print(index_of_nearest_larger_num([4, 1, 3, 5, 6], 1))
    # print(index_of_nearest_larger_num([4, 1, 3, 5, 6], 4))

    print(index_of_nearest_larger_num_redux([4, 1, 3, 5, 6], 0))
    print(index_of_nearest_larger_num_redux([4, 1, 3, 5, 6], 1))
    print(index_of_nearest_larger_num_redux([4, 1, 3, 5, 6], 4))

    # print(preprocess([4, 1, 3, 5, 6]))
    # print(preprocess([1, 1, 1, 4, 3, 3]))
    print(get_mapping_indices([4, 1, 3, 5, 6]))