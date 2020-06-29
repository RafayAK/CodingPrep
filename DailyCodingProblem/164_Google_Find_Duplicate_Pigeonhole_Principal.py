"""
You are given an array of length n + 1 whose elements belong to the set {1, 2, ..., n}.
By the pigeonhole principle, there must be a duplicate. Find it in linear time and space.
"""

def get_duplicate(arr):
    element_set = set()
    for num in arr:

        # a duplicate will already exist in the set
        if num in element_set:
            return num

        element_set.add(num)

    return None


if __name__ == "__main__":

    print("Duplicate value: {}".format(get_duplicate([1, 2, 3, 1])))

    print("Duplicate value: {}".format(get_duplicate([1, 2, 3, 4, 5, 6, 6])))

    print("Duplicate value: {}".format(get_duplicate([1, 2, 3, 4, 5, 6, 7])))