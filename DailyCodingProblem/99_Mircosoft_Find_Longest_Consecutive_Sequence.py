"""
This problem was asked by Microsoft.

Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example, given [100, 4, 200, 1, 3, 2], the longest consecutive element sequence is [1, 2, 3, 4].
Return its length: 4.

Your algorithm should run in O(n) complexity.
"""

def add_number_to_dict(lookup_dict, num):
    if num+1 in lookup_dict and num-1 in lookup_dict:
        elements_greater = lookup_dict[num+1]
        elements_lesser = lookup_dict[num-1]
        new_elements = elements_lesser + [num] + elements_greater
        # store these elements in the entry of the lesser key
        lookup_dict[num-1] = new_elements
        lookup_dict[new_elements[-1]] = new_elements
        #
        del lookup_dict[num+1]
        return
    if num+1 in lookup_dict:
        elements = lookup_dict[num+1]
        elements = [num] + elements
        # create new entry in lookup_dict
        lookup_dict[num] = elements
        # delete old entry
        del lookup_dict[num+1]
        return
    elif num-1 in lookup_dict:
        elements = lookup_dict[num-1]
        elements = elements + [num]
        # create new entry in lookup_dict
        lookup_dict[num-1] = elements
        return

    lookup_dict[num] = [num]

def longest_consecutive(arr):
    lookup_dict = {}

    for num in arr:
        add_number_to_dict(lookup_dict, num)

    return max(lookup_dict.values(), key=lambda x: len(x))


if __name__ == '__main__':
    # print(longest_consecutive([100, 4, 200, 1, 3, 2]))
    print(longest_consecutive([100, 4, 200, 1, 3, 2, 5]))