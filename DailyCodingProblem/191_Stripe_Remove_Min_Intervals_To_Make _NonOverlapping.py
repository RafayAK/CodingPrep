"""
This problem was asked by Stripe.

Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the
intervals non-overlapping.

Intervals can "touch", such as [0, 1] and [1, 2], but they won't be considered overlapping.

For example, given the intervals (7, 9), (2, 4), (5, 8), return 1 as the last interval can be removed and the
first two won't overlap.

The intervals are not necessarily sorted in any order.
"""


def generate_time_periods(interval):
    return [i for i in range(*interval)]


def min_intervals_removed(intervals:list):
    # generate time periods that the intervals occupy
    list_of_time_periods = []
    for i in intervals:
        list_of_time_periods.append(generate_time_periods(i))

    # find the min number of intervals that can be removed
    num_intervals = len(list_of_time_periods)
    min_removed = num_intervals
    for j in range(num_intervals, 0, -1):
        flattened = []
        list(flattened.extend(x) for x in list_of_time_periods[0:j])
        set_of_intervals = set(tuple(flattened))
        if len(set_of_intervals) == sum([len(x) for x in list_of_time_periods[0:j]]):
            removed = num_intervals - j
            if removed < min_removed:
                min_removed = removed

    return min_removed





if __name__ == "__main__":
    intervals = [(7, 9), (2, 4), (5, 8)]
    print(min_intervals_removed(intervals))
    print(min_intervals_removed([(1,2),(0,1)]))
