"""
This problem was asked by MongoDB.

Given a list of elements, find the majority element, which appears more than half the time (> floor(len(lst) / 2.0)).

You can assume that such element exists.

For example, given [1, 2, 1, 1, 3, 4, 0], return 1.
"""

def majority_element(l):
    counter_dict = {}
    for ele in l:
        if ele not in counter_dict:
            counter_dict[ele] = 0

        counter_dict[ele] += 1

    majority_thresh = len(l) // 2

    for key, value in counter_dict.items():
        if value > majority_thresh:
            return key

    return None


if __name__ == '__main__':
    print(majority_element([1, 2, 1, 1, 3, 4, 0]))