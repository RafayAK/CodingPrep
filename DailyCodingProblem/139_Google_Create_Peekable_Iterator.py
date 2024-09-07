"""
Given an iterator with methods next() and hasNext(), create a wrapper iterator, PeekableInterface,
which also implements peek(). peek shows the next element that would be returned on next().

Here is the interface:

class PeekableInterface(object):
    def __init__(self, iterator):
        pass

    def peek(self):
        pass

    def next(self):
        pass

    def hasNext(self):
        pass
"""

class PeekableInterface(object):
    def __init__(self, iterator):
        self.iterator = iterator
        self._next = next(iterator)

    def peek(self):
        return self._next

    def next(self):
        result = self._next
        try:
            self._next = next(self.iterator)
        except StopIteration:
            self._next = None
        return result

    def hasNext(self):
        return self._next is not None


if __name__ == '__main__':
    lst = [1, 2, 3, 4, 5]

    peekable_lst = PeekableInterface(iter(lst))

    assert peekable_lst.peek() == 1
    assert peekable_lst.hasNext()
    assert peekable_lst.next() == 1

    assert peekable_lst.next() == 2
    assert peekable_lst.next() == 3
    assert peekable_lst.next() == 4
    assert peekable_lst.next() == 5

    assert not peekable_lst.hasNext()
