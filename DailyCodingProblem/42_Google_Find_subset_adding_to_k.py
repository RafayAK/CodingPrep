"""
This problem was asked by Google.

Given a list of integers S and a target number k,
write a function that returns a subset of S that adds up to k.
If such a subset cannot be made, then return null.

Integers can appear more than once in the list.
You may assume all numbers in the list are positive.

For example, given S = [12, 1, 61, 5, 9, 2] and k = 24, return [12, 9, 2, 1] since it sums up to 24.
"""




def find_subset(S,k):
    def recursive_helper(S, k, valid_list=[]):
        if k == 0:
            return valid_list
        if k < 0:
            return None
        if len(S) == 0 and k > 0:
            return None

        return recursive_helper(S[1:], k - S[0], valid_list + [S[0]]) or recursive_helper(S[1:], k, valid_list)

    valid_subset = recursive_helper(S, k)
    return valid_subset


def find_valid_subset_2(S, k):

    def recursive_helper(S, k, valid_list=[]):
        if k == 0:
            return valid_list
        if len(S) == 0:
            return None

        with_first = recursive_helper(S[1:], k - S[0], valid_list + [S[0]])
        if with_first:
            return with_first
        else:
            return recursive_helper(S[1:], k, valid_list)



    valid_subset = recursive_helper(S, k)
    return valid_subset


if __name__ == '__main__':
    print(find_subset(S=[12, 1, 61, 5, 9, 2], k =24))
    print(find_subset(S=[12, 11, 2], k=13))
    # print(find_subset(S=[13, 11, 2], k=13))
    # print(find_subset(S=[14, 12, 2], k=13))
    print(find_valid_subset_2(S=[12, 11, 2], k=13))
    print(find_valid_subset_2(S=[12, 1, 61, 5, 9, 2], k =24))
