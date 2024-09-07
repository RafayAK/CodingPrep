"""
This problem was asked by Google.

Given a set of closed intervals, find the smallest set of numbers that covers all the intervals.
If there are multiple smallest sets, return any of them.

For example, given the intervals [0, 3], [2, 6], [3, 4], [6, 9], one set of numbers that covers
all these intervals is {3, 6}.
"""

# basicaly we want the smallest set of numbers such that for interval we
# have one number that belongs to that an interval

# 0  1  2  3  4  5  6  7  8  9 10
#    ----
# -------------
#    ^           -------
#    |              ----
#                   ----------
#                    ^   -------
#                    |     ^
#                          |


def numbers_that_cover_intterval(intervals):
    min_range = min(intervals, key=lambda item: item[0])[0]
    max_range = max(intervals, key=lambda item: item[1])[1]

    range_dict = {i: set() for i in range(min_range, max_range + 1)}

    for interval_num, interval in enumerate(intervals):
        for i in range(interval[0], interval[1]+1):
            range_dict[i].add(interval_num)

    numbers_that_cover_range = []
    for key, s in range_dict.items():
        if len(numbers_that_cover_range) == 0:
            numbers_that_cover_range.append(key)
            continue

        elif not s.issubset(range_dict[numbers_that_cover_range[-1]]):
            if range_dict[numbers_that_cover_range[-1]].issubset(s):
                numbers_that_cover_range[-1] = key
            else:
                numbers_that_cover_range.append(key)

    return numbers_that_cover_range


if __name__ == "__main__":
    print(numbers_that_cover_intterval(([0, 3], [2, 6], [3, 4], [6, 9])))
    print(numbers_that_cover_intterval([[0, 3], [2, 6]]))
    print(numbers_that_cover_intterval([[0, 3], [2, 6], [3, 4]]))
    print(numbers_that_cover_intterval([[0, 3], [2, 6], [3, 4], [6, 100]]))
    print(numbers_that_cover_intterval([[1, 2], [0,4], [5,7],[6,7], [6,9], [8,10]]))

