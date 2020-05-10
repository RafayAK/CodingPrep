"""
This problem was asked by MongoDB.

Given a list of elements, find the majority element, which appears more than half the time (> floor(len(lst) / 2.0)).

You can assume that such element exists.

For example, given [1, 2, 1, 1, 3, 4, 0], return 1.
"""

# The example provided is WORNG!
# according to the second requirement of the majority element > floor(len(lst) / 2.0) = floor(7 /2.0) = floor(3.5) = 3
# and the frequency of element "1" = 3 not > 3

def majority_element(l):
    frequency_map = {}
    for ele in l:
        if ele not in frequency_map:
            frequency_map[ele] = 0

        frequency_map[ele] += 1

    majority_thresh = len(l) // 2
    
    for key, value in frequency_map.items():
        if value > majority_thresh:
            return key

    return None


if __name__ == '__main__':
    print(majority_element([1, 2, 1, 1, 3, 4, 0]))
    print(majority_element([1, 2, 1, 1, 3, 4, 1]))
    print(majority_element([0]))
