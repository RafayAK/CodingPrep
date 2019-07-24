"""
This problem was asked by Apple.

Implement a queue using two stacks.

Recall that a queue is a FIFO (first-in, first-out) data
structure with the following methods:
- enqueue, which inserts an element into the queue, and
- dequeue, which removes it.
"""
from queue import LifoQueue

class stack_queue:
    def __init__(self):
        self._stack_1 = LifoQueue()
        self._stack_2 = LifoQueue()

    def get_total_lenght(self):
        return self._stack_1.qsize() + self._stack_2.qsize()

    def enqueue(self, data):
       self._stack_1.put(data)

    def dequeue(self):
        if self._stack_2.empty():
            for _ in range(self._stack_1.qsize()):
                self._stack_2.put(self._stack_1.get())

        return self._stack_2.get()

if __name__ == '__main__':
    q = stack_queue()

    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)

    assert q.dequeue() == 1
    assert q.dequeue() == 2
    assert q.dequeue() == 3
    assert q.dequeue() == 4
    assert q.dequeue() == 5

