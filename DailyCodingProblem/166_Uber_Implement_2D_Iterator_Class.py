"""
This problem was asked by Uber.

Implement a 2D iterator class. It will be initialized with an array of arrays,
and should implement the following methods:

    - `next()`: returns the next element in the array of arrays. If there are no more elements, raise an exception.
    - `has_next()`: returns whether or not the iterator still has elements left.

For example, given the input [[1, 2], [3], [], [4, 5, 6]], calling next() repeatedly should output 1, 2, 3, 4, 5, 6.

Do not use flatten or otherwise clone the arrays. Some of the arrays can be empty.
"""

class ArrayIterator:
    def __init__(self, matrix):
        self.matrix = matrix
        self._curr_row = 0
        self._curr_col = 0

    def next(self):
        if self.has_next():
            return_val = self.matrix[self._curr_row][self._curr_col]
            self._curr_col+=1
            if self._curr_col == len(self.matrix[self._curr_row]):
                self._curr_row+=1
                self._curr_col=0
            return return_val
        else:
            raise Exception(IndexError)

    def has_next(self):
        if self._curr_row < len(self.matrix) and len(self.matrix[self._curr_row]) == 0:
            self._curr_row += 1  # skip this row
        return self._curr_row < len(self.matrix) and self._curr_col < len(self.matrix[self._curr_row])



if __name__ == '__main__':
    test = ArrayIterator([[1, 2], [3], [], [4, 5, 6]])

    while test.has_next():
        print(test.next())



