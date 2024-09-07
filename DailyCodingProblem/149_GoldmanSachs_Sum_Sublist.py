"""
This problem was asked by Goldman Sachs.

Given a list of numbers L, implement a method sum(i, j) which returns the sum from the sublist L[i:j]
(including i, excluding j).

For example, given L = [1, 2, 3, 4, 5], sum(1, 3) should return sum([2, 3]), which is 5.

You can assume that you can do some pre-processing. sum() should be optimized over the pre-processing step.
"""
class OptimListSum:
    def __init__(self, l:list):
        self.L = l
        self.sum_dict = None
        self._preprocess()

    def _preprocess(self):
        # Pre-process
        # stores the sums from the index i to the end of the list
        # so given L = [1, 2, 3, 4, 5]
        # sum_dict[0] = sum(L[0:]) = 15
        # sum_dict[1] = sum(L[1:]) = 14
        # sum_dict[2] = sum(L[2:]) = 12
        # ...
        self.sum_dict = {i: sum(self.L[i:]) for i in range(len(self.L))}

    def sum(self, i, j):
        return self.sum_dict[i] - self.sum_dict[j]


if __name__ == '__main__':
    ols = OptimListSum([1, 2, 3, 4, 5])
    print(ols.sum(1, 3))
    print(ols.sum(1, 4))
    print(ols.sum(0, 4))











