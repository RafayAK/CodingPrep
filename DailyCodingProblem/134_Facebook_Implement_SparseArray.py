"""
This problem was asked by Facebook.

You have a large array with most of the elements as zero.

Use a more space-efficient data structure, SparseArray, that implements the same interface:

    -> init(arr, size): initialize with the original large array and size.
    -> set(i, val): updates index at i with val.
    -> get(i): gets the value at index i.
"""

# Idea: only note down the positions of non-zero elements

class SparseArray:
    """
    >>> arr = [0, 0, 0, 1, 2, 0, 0, 15, 0, 6]
    >>> sp_arr = SparseArray(arr, len(arr))

    >>> sp_arr.non_zero_vals == {3:1, 4:2, 7:15, 9:6}
    True
    >>> sp_arr.get(0) == 0
    True
    >>> sp_arr.get(4) == 2
    True
    >>> sp_arr.get(8) == 0
    True
    >>> sp_arr.get(-10)
    Traceback (most recent call last):
        ...
    IndexError: Index out of bounds
    >>> sp_arr.get(3)
    1
    >>> sp_arr.set(3,0)
    >>> sp_arr.get(3)
    0
    """

    def __init__(self, arr, size):
        self.non_zero_vals = {}
        self.size = size
        self._create_sparse_arr(arr)

    def _create_sparse_arr(self, arr):
        for i, num in enumerate(arr):
            if num:
                self.non_zero_vals[i] = num

    def _check_bounds(self,i):
        if i < 0 or i >= self.size:
            raise IndexError("Index out of bounds")

    def set(self, i, val):
        self._check_bounds(i)
        # if val not zero track it
        if val:
            self.non_zero_vals[i] = val
        elif i in self.non_zero_vals:
            # stop tracking indices that go to zero
            del self.non_zero_vals[i]

    def get(self, i):
        self._check_bounds(i)

        return self.non_zero_vals.get(i, 0)

    def __repr__(self):

        return "".format(self.non_zero_vals)



if __name__ == '__main__':
    import doctest
    doctest.testmod()





