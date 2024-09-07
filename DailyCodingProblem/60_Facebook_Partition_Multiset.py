"""
This problem was asked by Facebook.

Given a multiset of integers, return whether it can be partitioned into
two subsets whose sums are the same.

For example, given the multiset {15, 5, 20, 10, 35, 15, 10}, it would return true,
since we can split it up into {15, 5, 10, 15, 10} and {20, 35}, which both add up to 55.

Given the multiset {15, 5, 20, 10, 35}, it would return false, since we can't split it up
into two subsets that add up to the same sum.
"""

def can_be_split_into_two(multiset):
    def helper(multiset, start, end, set_1, set_2):
        if start > end:
            return False

        if sum(set_1) == sum(set_2):
            return True

        return helper(multiset, start+1, end, set_1 + [multiset[start]], set_2[1:]) \
               or helper(multiset, start, end-1, set_1 + [multiset[end]], set_2[:-1])

    multiset.sort()

    # give helper function half of the multiset
    return helper(multiset, start=0, end=len(multiset)-1, set_1=[], set_2=multiset)


if __name__ == '__main__':
    assert can_be_split_into_two([15, 5, 20, 10, 35, 15, 10]) is True
    assert can_be_split_into_two([5,5]) is True
    assert can_be_split_into_two([1, 1, 1, 1, 1, 1, 1, 6]) is False
    assert can_be_split_into_two([1, 1, 1, 1, 1, 1, 6]) is True
    assert can_be_split_into_two([1, 4, 4, 4, 5,  6]) is True
    assert can_be_split_into_two([15, 5, 20, 10, 35]) is False


