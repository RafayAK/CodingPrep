"""
You are given an array of length n + 1 whose elements belong to the set {1, 2, ..., n}.
By the pigeonhole principle, there must be a duplicate. Find it in linear time and space.
"""
# O(n) time but also O(n) space
def get_duplicate(arr):
    element_set = set()
    for num in arr:

        # a duplicate will already exist in the set
        if num in element_set:
            return num

        element_set.add(num)

    return None

# O(n) time and O(1) space
# sum of values from 1-n = (n*(n+1))/2, the Gauss' formula
# so sum all the array and subtract from it the sum from 1-n
# result will be the number that is duplicate
def get_duplicate_redux(arr):
    n = len(arr) - 1  # -1 because the elements in the array would 1 greater due to duplicate
    # print(n)
    return sum(arr) - (n * (n+1))//2


if __name__ == "__main__":

    print("Duplicate value: {}".format(get_duplicate_redux([1, 2, 3, 1])))

    print("Duplicate value: {}".format(get_duplicate_redux([1, 2, 3, 4, 5, 6, 6])))
