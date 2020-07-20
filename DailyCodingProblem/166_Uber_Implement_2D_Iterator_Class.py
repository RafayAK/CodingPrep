"""
This problem was asked by Uber.

Implement a 2D iterator class. It will be initialized with an array of arrays,
and should implement the following methods:

    - `next()`: returns the next element in the array of arrays. If there are no more elements, raise an exception.
    - `has_next()`: returns whether or not the iterator still has elements left.

For example, given the input [[1, 2], [3], [], [4, 5, 6]], calling next() repeatedly should output 1, 2, 3, 4, 5, 6.

Do not use flatten or otherwise clone the arrays. Some of the arrays can be empty.
"""


# class ArrayIterator:
#     def __init__(self, matrix):
#         self.matrix = matrix
#         self._curr_row = 0
#         self._curr_col = 0
#
#     def next(self):
#         if self.has_next():
#             return_val = self.matrix[self._curr_row][self._curr_col]
#             self._curr_col+=1
#             if self._curr_col == len(self.matrix[self._curr_row]):
#                 self._curr_row+=1
#                 self._curr_col=0
#             return return_val
#         else:
#             raise Exception(IndexError)
#
#     def has_next(self):
#         if self._curr_row < len(self.matrix) and len(self.matrix[self._curr_row]) == 0:
#             self._curr_row += 1  # skip this row
#         return self._curr_row < len(self.matrix) and self._curr_col < len(self.matrix[self._curr_row])


# Cleaner implementation
class ArrayIterator:
    def __init__(self, matrix):
        self.matrix = matrix
        self._curr_row = None
        self._curr_col = None

    def _get_next_coord(self, row, col):
        if self.matrix is None or len(self.matrix) == 0:
            return None

        if row is None or col is None:
            return (0, 0)

        # set next_row and next_col to the currently passed row and col
        next_row, next_col = row, col

        # now find the next row and col
        while next_row < len(self.matrix):
            # if next_col exists in this row, set next_col+=1 i.e next_col+=1 ->> next_col = curr_row + 1
            if next_col + 1 < len(self.matrix[next_row]):
                next_col += 1
                return next_row, next_col
            else:
                # move  on to the next row otherwise and set next_col to -1 so that the cols the checking can
                # start from zero i.e next_col=-1, next_col+1 = -1 + 1 = 0th col
                next_row += 1
                next_col = -1

        return None  # coordinates could not be found

    def next(self):
        # get next coordinates from the curr_row and curr_col
        coord = self._get_next_coord(self._curr_row, self._curr_col)
        if coord:
            self._curr_row, self._curr_col = coord[0], coord[1]
            return self.matrix[coord[0]][coord[1]]
        else:
            raise Exception("Next item doesn't not exist")

    def has_next(self):
        # has_next returns true when the next coordinates exist, looking from the curr_row and curr_col
        if self._get_next_coord(self._curr_row, self._curr_col):
            return True
        else:
            return False


if __name__ == '__main__':
    test = ArrayIterator([[1, 2], [3], [], [4, 5, 6]])

    while test.has_next():
        print(test.next())


