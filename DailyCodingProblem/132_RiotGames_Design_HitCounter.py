"""
This question was asked by Riot Games.

Design and implement a HitCounter class that keeps track of requests (or hits). It should support the following operations:

    -> record(timestamp): records a hit that happened at timestamp
    -> total(): returns the total number of hits recorded
    -> range(lower, upper): returns the number of hits that occurred between timestamps lower and upper (inclusive)

Follow-up: What if our system has limited memory?
"""

import time

class HitCounter:
    def __init__(self):
        self.hit_time_stamp = {}  #  dict to store time_stamp: hit_list_index
        self.hit_list = []  # to store hits for each time_stamp

    def record(self, timestamp):
        self.hit_time_stamp[timestamp] = len(self.hit_list)
        self.hit_list.append(1)

    def total(self):
        return sum(self.hit_list)

    def range(self, lower, upper):
        return sum(self.hit_list[self.hit_time_stamp[lower]:self.hit_time_stamp[upper]+1])


# improved HitCounter, uses less memory

class HitCounterRedux:
    def __init__(self):
        self.hit_time_stamp = {}  # dict to store time_stamp: total hits up till that point
        # self.hit_list = []  # to store hits for each time_stamp
        self.hit_counter = 0

    def record(self, timestamp):
        self.hit_counter += 1
        self.hit_time_stamp[timestamp] = self.hit_counter

    def total(self):
        return self.hit_counter

    def range(self, lower, upper):
        return self.hit_time_stamp[upper] - self.hit_time_stamp[lower] + 1


if __name__ == '__main__':
    player = HitCounterRedux() # HitCounter()

    first = time.time()
    last = None
    player.record(first)

    for i in range(5):
        temp_time = time.time()
        if i== 3:
            last = temp_time
        player.record(temp_time)

    assert player.total() == 6
    assert player.range(lower=first, upper=last) == 5

