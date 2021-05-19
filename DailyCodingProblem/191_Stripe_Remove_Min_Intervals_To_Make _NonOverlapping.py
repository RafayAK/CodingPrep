"""
This problem was asked by Stripe.

Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the
intervals non-overlapping.

Intervals can "touch", such as [0, 1] and [1, 2], but they won't be considered overlapping.

For example, given the intervals (7, 9), (2, 4), (5, 8), return 1 as the last interval can be removed and the
first two won't overlap.

The intervals are not necessarily sorted in any order.
"""


def non_overlapping_intervals(intervals):
    current_end = float("-inf")
    overlapping = 0

    for start, end in sorted(intervals, key=lambda i: i[1]):
        if start >= current_end:
            current_end = end
        else:
            overlapping += 1

    return overlapping


if __name__ == "__main__":
    print(non_overlapping_intervals([(1,2),(0,1)]))
    print(non_overlapping_intervals([(7, 9), (2, 4), (5, 8)]))
