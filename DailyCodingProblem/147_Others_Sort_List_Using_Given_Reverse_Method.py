"""
Given a list, sort it using this method: reverse(lst, i, j), which reverses lst from i to j.
"""


def reverse(lst, i, j):
    lst[i: j] = lst[i: j][::-1]


def sort_with_reverse(lst:list):
    iterator = 0

    while iterator < len(lst)-1:
        smallest_value = min(lst[iterator:])
        index_smallest = lst.index(smallest_value, iterator, len(lst))

        reverse(lst, iterator, index_smallest+1)

        iterator += 1

    return lst


if __name__ == '__main__':
    l = [3, 2, 4, 1]
    assert sort_with_reverse(l) == [1, 2, 3, 4]

    l = [5, 2, 3, 4, 5, 6, 2]
    assert sort_with_reverse(l) == [2, 2, 3, 4, 5, 5, 6]