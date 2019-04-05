'''
This problem was asked by Snapchat.

Given an array of time intervals (start, end) for classroom lectures (possibly overlapping),
 find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
'''


def minClasses(times_list):
    start_times = [(t[0], 1) for t in times_list]  # [(30, 1), (0, 1), (60, 1)]
    end_times = [(t[1], -1) for t in times_list]  # [(75, -1), (50, -1), (150, -1)]

    # 1 tells room needed , -1 room vacated
    room_state = [i[1] for i in sorted(start_times+end_times, key=lambda x:x[0])] # [1, 1, -1, 1, -1, -1]

    max_classes = 0 # stores the max_num of classes requested following the time-table
    classes = 0
    for i in room_state:
        classes += i  # required or released
        max_classes = max(max_classes, classes)

    return max_classes

if __name__ == '__main__':
    times = [(30, 75), (0, 50), (60, 150)]
    print(minClasses(times))

    
    