"""
This problem was asked by Amazon.

Implement a bit array.

A bit array is a space efficient array that holds a value of 1 or 0 at each index.

    -> init(size): initialize the array with size
    -> set(i, val): updates index at i with val where val is either 1 or 0.
    -> get(i): gets the value at index i.
"""

# Note: implementation taken from Daily Coding Problem # 134
# Tracking index of only 1s

class BitArray:
    """
    >>> arr = BitArray(5)
    >>> arr.get(5)
    Traceback (most recent call last):
        ...
    IndexError: Index out of bounds
    >>> arr.set(1,1)
    >>> arr.set(2,1)
    >>> arr.set(3,1)
    >>> arr.get(3)
    1
    >>> arr.get(1)
    1
    >>> arr.set(3, 4)
    Traceback (most recent call last):
        ...
    ValueError: Values can only be either 0 or 1
    """

    def __init__(self, size):
        # initially only contains zeros
        self.tracked_index = set()
        self.size = size

    def _check_bounds(self, i):
        if i < 0 or i >= self.size:
            raise IndexError("Index out of bounds")

    def set(self, i, val):
        self._check_bounds(i)
        # if val not zero track it

        if val == 0 or val == 1:
            if val:
                self.tracked_index.add(i)
            elif i in self.tracked_index:
                # stop tracking indices that go to zero
                self.tracked_index.remove(i)
        else:
            raise ValueError("Values can only be either 0 or 1")

    def get(self, i):
        self._check_bounds(i)

        return 1 if i in self.tracked_index else 0

    def __repr__(self):

        return "".format(self.tracked_index)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
