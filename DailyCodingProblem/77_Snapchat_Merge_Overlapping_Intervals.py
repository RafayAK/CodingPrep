"""
This problem was asked by Snapchat.

Given a list of possibly overlapping intervals,
return a new list of intervals where all overlapping intervals have been merged.

The input list is not necessarily ordered in any way.

For example, given [(1, 3), (5, 8), (4, 10), (20, 25)], you should return [(1, 3), (4, 10), (20, 25)].
"""


# O(n)
def merge_intervals(intervals):
    max_end_time = max(intervals, key=lambda x: x[1])[1]
    # min_end_time = min(intervals, key=lambda x: x[0])[0]

    timeline = [0]*(max_end_time+1)   # create an array of appropriate size to be used as a timeline

    for start, end in intervals:
        if timeline[start] == 'E':  # if time spot is marked end('E') & another time spot starts('S') there then mark 0
            timeline[start] = 0  # ending time == starting time => time interval continues
            timeline[end] = 'E'
            continue

        timeline[start] = 'S'
        timeline[end] = 'E'

    # print(timeline)
    merged_intervals = []
    s, e = None, None
    Es_to_skip = 0  # keep count of num of end_times to skip so that we pick the last time point in overlapping times.
    for i in range(len(timeline)):
        if timeline[i] == 'S' and s is None:
            s = i
        elif timeline[i] == 'S' and s is not None:
            Es_to_skip += 1
        elif timeline[i] == 'E' and Es_to_skip > 0:
            Es_to_skip -= 1
        elif timeline[i] == 'E' and Es_to_skip == 0:
            e = i

        if s and e and Es_to_skip == 0:
            merged_intervals.append((s, e))
            s, e = None, None

    return merged_intervals


if __name__ == '__main__':
    print(merge_intervals([(1, 3), (5, 8), (4, 10), (20, 25)]))  # [(1, 3), (4, 10), (20, 25)]
