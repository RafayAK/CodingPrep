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
    right_index, right_distance = search(index, left=False)  # search right

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
            return left
        if right < len(arr) and arr[right] > arr[index]:
            return right

    return None

"""
Preprocess works by checking the immediate left and right neighbours
For example given the arr=[4, 1, 3, 5, 6] we preprocess as follows:
   1. create cache to store the indices of larger neighbour
        cache = [None, None, None, None, None]
   2. iterate over each index checking only its immediate neighbour
        
        iter 1: 
            if      4 > 1 -->> Yes
                    cache = [None, 0, None, None, None]
        
        iter 2:    
            if      1 > 3 ---> No   
            elif    3 > 1 ---> Yes
                    cache = [None, 2, None, None, None]
        
        iter 3:
            if      3 > 5 ---> No
            elif    5 > 3 ---> Yes
                    cache = [None, 2, 3, None, None]
                    
        iter 4: 
            if      5 > 6 ---> No
            elif    6 > 5 ---> Yes
                    cache = cache = [None, 2, 3, 4, None]      
                    
        Now there the None values need to filled in through the O(n) algo
        After falling back to the O(n) algo the final cache is:
                    cache = cache = [3, 2, 3, 4, None],  
                    Note there is no element greater than 6 so its index remains None
                    
                    
        If there are duplicates than the worst case is O(n^2)
"""
def preprocess(arr):
    cache = [None for _ in range(len(arr))]

    for j in range(len(arr) -1):
        if arr[j] > arr[j +1]:
            cache[j + 1] =j
        elif arr[j +1] > arr[j]:
            cache[j] = j+1

    for i in range(len(cache)):
        if cache[i] is None:
            # fall back to the O(n) algo
            cache[i] = index_of_nearest_larger_num_redux(arr, i)

    return cache


cache = None  # global cache for pre-processing


def return_nearest(arr, i):
    global cache
    if cache is None:
        cache = preprocess(arr)
    return cache[i]

if __name__ == '__main__':
    # print(index_of_nearest_larger_num([4, 1, 3, 5, 6], 0))
    # print(index_of_nearest_larger_num([4, 1, 3, 5, 6], 1))
    # print(index_of_nearest_larger_num([4, 1, 3, 5, 6], 4))

    # print(index_of_nearest_larger_num_redux([4, 1, 3, 5, 6], 0))
    # print(index_of_nearest_larger_num_redux([4, 1, 3, 5, 6], 1))
    # print(index_of_nearest_larger_num_redux([4, 1, 3, 5, 6], 4))

    print(return_nearest([4, 1, 3, 5, 6], 0))
    print(return_nearest([4, 1, 3, 5, 6], 1))
    print(return_nearest([4, 1, 3, 5, 6], 4))
