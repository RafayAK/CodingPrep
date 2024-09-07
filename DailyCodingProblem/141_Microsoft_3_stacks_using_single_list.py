"""
This problem was asked by Microsoft.

Implement 3 stacks using a single list:

class Stack:
    def __init__(self):
        self.list = []

    def pop(self, stack_number):
        pass

    def push(self, item, stack_number):
        pass
"""


class Stack:
    """
    This class creates a triple stack using a single list

    >>> triple_stacks = Stack()
    >>> print(triple_stacks)
    S_1: []
    S_2: []
    S_3: []
    >>> triple_stacks.push(1, 2)
    >>> print(triple_stacks)
    S_1: []
    S_2: []
    S_3 : [1]
    >>> triple_stacks.push(1, 0)
    >>> print(triple_stacks)
    S_1 : [1]
    S_2: []
    S_3 : [1]
    >>> triple_stacks.push(2, 1)
    >>> print(triple_stacks)
    S_1 : [1]
    S_2 : [2]
    S_3 : [1]
    >>> print(triple_stacks.pop(0))
    1
    >>> triple_stacks.pop(0)
    Traceback (most recent call last):
    ...
    IndexError: Stack#0 is empty!
    >>> print(triple_stacks.pop(2))
    1
    >>> triple_stacks.pop(2)
    Traceback (most recent call last):
    ...
    IndexError: Stack#2 is empty!
    >>> print(triple_stacks.pop(1))
    2
    >>> triple_stacks.pop(1)
    Traceback (most recent call last):
    ...
    IndexError: Stack#1 is empty!
    >>> triple_stacks.push(1, 3)
    Traceback (most recent call last):
    ...
    IndexError: Stack#3 does not exist!
    >>> triple_stacks.push(1, stack_number=0)
    >>> triple_stacks.push(1, stack_number=1)
    >>> triple_stacks.push(1, stack_number=2)
    >>> print(triple_stacks)
    S_1 : [1]
    S_2 : [1]
    S_3 : [1]
    >>> triple_stacks.push(2, stack_number=2)
    >>> triple_stacks.push(2, stack_number=1)
    >>> triple_stacks.push(2, stack_number=0)
    >>> print(triple_stacks)
    S_1 : [1, 2]
    S_2 : [1, 2]
    S_3 : [1, 2]
    >>> triple_stacks.push(4, stack_number=1)
    >>> triple_stacks.push(3, stack_number=0)
    >>> triple_stacks.push(5, stack_number=2)
    >>> print(triple_stacks)
    S_1 : [1, 2, 3]
    S_2 : [1, 2, 4]
    S_3 : [1, 2, 5]
    """


    def __init__(self):
        self.list = []
        self.stack_markers = [[0, 0], [0, 0], [0, 0]]

    def pop(self, stack_number):
        if not self._is_empty(stack_number):
            item = self.list[self.stack_markers[stack_number][1]-1]
            del self.list[self.stack_markers[stack_number][1]-1]
            self.stack_markers[stack_number][1] -= 1
            self._update_stack_pointers(stack_number, -1)
            return item
        else:
            raise IndexError("Stack#{} is empty!".format(stack_number))

    def push(self, item, stack_number):
        if stack_number > 2:
            raise IndexError("Stack#{} does not exist!".format(stack_number))

        where_to_push = self._get_stack_top_idx(stack_number)

        self.list.insert(where_to_push, item)
        self.stack_markers[stack_number][1] = self.stack_markers[stack_number][1] +1
        self._update_stack_pointers(stack_number, 1)

    def _get_stack_top_idx(self, stack_number):
        return self.stack_markers[stack_number][1]

    def _update_stack_pointers(self, stack_number, shift):
        for i in range(stack_number+1, 3):
            self.stack_markers[i] = [self.stack_markers[i][0]+shift, self.stack_markers[i][1]+shift]

    def _is_empty(self, stack_number):
        return self.stack_markers[stack_number][0] == self.stack_markers[stack_number][1]

    def __str__(self):
        stacks = ""

        for i in range(3):
            if not self._is_empty(stack_number=i):
                stacks = stacks + "S_{} : {}".format(i+1, self.list[self.stack_markers[i][0]: self.stack_markers[i][1]])
            else:
                stacks = stacks + "S_{}: []".format(i+1)

            if i < 2:
                stacks = stacks + "\n"

        return stacks


if __name__ == '__main__':
    import doctest
    doctest.testmod()





