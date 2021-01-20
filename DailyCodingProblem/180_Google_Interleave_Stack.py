"""
This problem was asked by Google.

Given a stack of N elements, interleave the first half of the stack with the second half reversed
using only one other queue. This should be done in-place.

Recall that you can only push or pop from a stack, and enqueue or dequeue from a queue.

For example, if the stack is [1, 2, 3, 4, 5], it should become [1, 5, 2, 4, 3].
If the stack is [1, 2, 3, 4], it should become [1, 4, 2, 3].

Hint: Try working backwards from the end state.
"""
from queue import SimpleQueue


class Stack:
    def __init__(self):
        self._stack = []  # top of stack will be the end of the list.

    def push(self, value):
        self._stack.append(value)

    def pop(self):
        return self._stack.pop()

    def size(self):
        return len(self._stack)

    def push_from_list(self, l):
        for val in l:
            self.push(val)

    def reverse(self):
        self._stack.reverse()

    def interleave_stack(self):

        def pop_from_stack_to_queue(num_of_times):
            for _ in range(num_of_times):
                queue.put(self.pop())

        def push_from_queue_to_stack(num_of_times):
            for _ in range(num_of_times):
                self.push(queue.get())

        # create queue
        queue = SimpleQueue()
        # reverse stack
        self.reverse()

        size_of_stack = self.size()

        for i in range(size_of_stack, 1, -1):
            pop_from_stack_to_queue(num_of_times=i)
            push_from_queue_to_stack(num_of_times=i)


    def __repr__(self):
        stack_str = ""

        # using stack s a list here
        for val in self._stack[::-1]:
            stack_str = stack_str + "| " + str(val) + " |\n"

        stack_str += "|===|"

        return stack_str

if __name__ == '__main__':
    stack_1 = Stack()
    stack_1.push_from_list([1, 2, 3, 4, 5])

    print(stack_1)

    print("\nAfter interleaving:")
    stack_1.interleave_stack()
    print(stack_1)

    print("\n-----------\n")

    stack_2 = Stack()
    stack_2.push_from_list([1, 2, 3, 4])

    print(stack_2)

    print("\nAfter interleaving:")
    stack_2.interleave_stack()
    print(stack_2)


