"""
This problem was asked by Amazon.

Implement a stack API using only a heap. A stack implements the following methods:

push(item), which adds an element to the stack
pop(), which removes and returns the most recently added element (or throws an error if there is nothing on the stack)
Recall that a heap has the following operations:

push(item), which adds a new key to the heap
pop(), which removes and returns the max value of the heap
"""

from heapq import heapify, heappop, heappush
import datetime

class HeapStack:
    def __init__(self):
        self.heap = []
        heapify(self.heap)

    def _get_current_utc_timestamp(self):
        dt = datetime.datetime.now()
        utc_time = dt.replace(tzinfo=datetime.timezone.utc)
        utc_timestamp = utc_time.timestamp()
        # print(utc_timestamp)
        return utc_timestamp

    def push(self, item):
        # get UTC timestamp
        ts = self._get_current_utc_timestamp()

        # since heapq by default creates a min heap to create max heap
        # multiply timestamp by -1. items are stored as (key, value),
        # where key is the timestamp
        heappush(self.heap, (-1 * ts, item))

    def pop(self):
        return heappop(self.heap)[1]



if __name__ == '__main__':
    my_stack = HeapStack()
    # add items to stack
    for num in [5, 4, 3, 1, 2]:
        my_stack.push(num)

    # remove items from heap
    for num in [5, 4, 3, 1, 2][::-1]:
        assert num == my_stack.pop()
