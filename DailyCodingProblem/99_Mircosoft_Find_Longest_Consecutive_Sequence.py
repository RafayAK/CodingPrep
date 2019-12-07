"""
This problem was asked by Microsoft.

Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example, given [100, 4, 200, 1, 3, 2], the longest consecutive element sequence is [1, 2, 3, 4].
Return its length: 4.

Your algorithm should run in O(n) complexity.
"""
class range_storer:
    def __init__(self, min_val, max_val):
        self.min_val = min_val
        self.max_val = max_val
        self.sequence = []

    def __repr__(self):
        return "({}, {}): {}".format(self.min_val, self.max_val, self.sequence)


def add_number_to_dict(min_dict, max_dict, num):
    if num+1 in min_dict and num+2 in max_dict:
        min_elements = min_dict[num+1]
        max_elements = max_dict[num-1]
        new_elements = range_storer(max_elements.min_val, min_elements.max_val)
        new_elements.sequence = max_elements.sequence + [num] + min_elements.sequence
        min_dict[new_elements.min_val] = new_elements
        max_dict[new_elements.max_val] = new_elements
        del min_dict[min_elements.min_val]
        del max_dict[max_elements.max_val]
        return
    elif num+1 in min_dict:
        elements = min_dict[num+1]
        elements.sequence = [num] + elements.sequence
        elements.min_val = num
        min_dict[num] = elements
        del min_dict[num+1]
        return
    elif num-1 in max_dict:
        elements = max_dict[num - 1]
        elements.sequence = elements.sequence + [num]
        elements.max_val = num
        max_dict[num] = elements
        del max_dict[num - 1]
        return



    elements = range_storer(num, num)
    elements.sequence.append(num)
    min_dict[num] = elements
    max_dict[num] = elements


def longest_consecutive(arr):
    # these two dicts store the seen maximum and minimum for a sequence of values
    min_dict = {}
    max_dict = {}

    for num in arr:
        add_number_to_dict(min_dict, max_dict, num)

    sequences = [s.sequence for s in min_dict.values()]

    return len(max(sequences, key=lambda array:len(array)))


if __name__ == '__main__':
    print(longest_consecutive([100, 4, 200, 1, 3, 2]))   # 4
    print(longest_consecutive([100, 4, 200, 1, 3, 2, 5]))  # 5
    print(longest_consecutive([100, 8, 2, 4, 10, 101, 102, 12, 15, 99]))  #  4