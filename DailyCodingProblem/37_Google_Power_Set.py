"""
This problem was asked by Google.

The power set of a set is the set of all its subsets. Write a function that, given a set, generates its power set.

For example, given the set {1, 2, 3}, it should return {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}.

You may also use a list or array to represent a set.
"""


'''
Idea: Recall that the 'empty set' is part of every set, so start with that
eg given [1,2,3]

SOL : start ->{{}}
    -   take first element, 1
    -> {{}} + ({}+{1}) => {{}, {1}}
    - second element, 2
    -> {{}, {1}} + ({}+{2}) + {{1}+{2}} => {{}, {1}, {2}, {1,2}}
    - third element, 3
    -> {{}, {1}, {2}, {1,2}} + ({}+{3}) + ({1}+{3}) + ({2}+{3}) + ({1, 2}+{3}) => {{{}, {1}, {2}, {3}, {1,2}}, {1,2,3}} 

'''



def create_power_set(arr):
    power_set = [[]]  # empty set part of all sets

    for num in arr:
        temp_power_set = power_set.copy()
        for j in range(len(power_set)):
            temp_power_set.append(power_set[j]+[num])

        power_set = temp_power_set

    return power_set


if __name__ == '__main__':
    s = [1,2,3]
    print(create_power_set(s))