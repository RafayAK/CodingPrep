"""
This problem was asked by Microsoft.

Given an array of positive integers, divide the array into two subsets such that the difference between the
sum of the subsets is as small as possible.

For example, given [5, 10, 15, 20, 25], return the sets {10, 25}
and {5, 15, 20}, which has a difference of 5, which is the smallest possible difference.
"""


# idea:
# 1. Sort the array split into two, down the middle.
# 2. Figure out the subset with max sum, mark it "l" for larger and mark the other one "s" for smaller
# 3. Put the smallest element from "l" into "s" until sum of "s" is greater than sum of "l"
# 4. Then put smallest element from "s" ito "l" until sum of "l" is greater than or equal to sum of "s"
# 5. return result
# O(nlogn) due to sorting
# Greedy Algo does not work on  [16, 14, 13, 13, 12, 10, 9, 3]
#   Correct Ans: 0
#     # 16 13 13 3
#     # 14 12 10 9
# returns diff of 2 instead.
# # https://stackoverflow.com/questions/6597180/how-to-divide-a-set-into-two-subsets-such-that-difference-between-the-sum-of-num

# def smallest_diff_subsets(nums):
#     nums.sort()
#     length = len(nums)
#     l1 = nums[:length//2]
#     l2 = nums[length//2:]
#
#     def helper(s:list, l:list):
#         while sum(s) < sum(l):
#             s.append(l[0])
#             l = l[1:]
#
#         iter = 0
#         while sum(l) < sum(s):
#             l.insert(iter, s[0])
#             s = s[1:]
#             iter+=1
#
#         return (abs(sum(l)-sum(s)), s, l)
#
#     if sum(l1) == sum(l2):
#         return (0, l1, l2)
#     if sum(l1) < sum(l2):
#         return helper(s=l1, l=l2)
#     else:
#         return helper(s=l2, l=l1)

# idea: need to iterate over all possible combination of subsets
from itertools import combinations
def smallest_diff_subsets(nums):
    min_diff = None
    best_candidates = None

    for sub1, sub2 in subset_pairs(nums):
        diff = abs(sum(sub1) - sum(sub2))

        if min_diff is None:
            min_diff = diff
            best_candidates = (sub1, sub2)
            continue

        if diff < min_diff:
            min_diff = diff
            best_candidates = (sub1, sub2)


    return min_diff, best_candidates

def subset_pairs(nums):
    n = len(nums)

    # iterate of all sizes of combinations
    for r in range(n+1):
        # generate indices of all combinations42
        for indices in combinations(range(n), r):
            subset1 = [nums[i] for i in indices]  # generate subset by picking numbers according to index
            subset2 = [nums[i] for i in set(range(n)) - set(indices)]

            yield subset1, subset2



if __name__ == '__main__':
    print(smallest_diff_subsets([5, 10, 15, 20, 25]))
    print(smallest_diff_subsets([5, 10, 15, 20]))
    print(smallest_diff_subsets([2,4,5,10,1]))
    print(smallest_diff_subsets([2, 4, 5, 10, 1, 12]))
    print(smallest_diff_subsets([1,5,11,5]))
    print(smallest_diff_subsets([1,2,3,4,5]))
    print(smallest_diff_subsets([0,1,5,6]))
    print(smallest_diff_subsets([16, 14, 13, 13, 12, 10, 9, 3]))
