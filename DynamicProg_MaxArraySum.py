'''Given an array of integers, find the subset of non-adjacent elements with the maximum sum. Calculate the sum of that subset.

For example, given an array arr= [-2, 1, 3, -4, 5]  we have the following possible subsets:

Subset      Sum
[-2, 3, 5]   6
[-2, 3]      1
[-2, -4]    -6
[-2, 5]      3
[1, -4]     -3
[1, 5]       6
[3, 5]       8
Our maximum subset sum is 8.

Function Description

Complete the maxSubsetSum function in the editor below. It should return an integer representing the maximum subset sum for the given array.

maxSubsetSum has the following parameter(s):

arr: an array of integers

Return the maximum sum described in the statement.

Sample Input 0

5
3 7 4 6 5
Sample Output 0

13
Explanation 0

Our possible subsets are  and . The largest subset sum is  from subset

Sample Input 1

5
2 1 5 8 4
Sample Output 1

11
Explanation 1

Our subsets are  and . The maximum subset sum is  from the first subset listed.

Sample Input 2

5
3 5 -7 8 10
Sample Output 2

15
Explanation 2

Our subsets are  and . The maximum subset sum is  from the fifth subset listed.
'''

# !/bin/python3

import math
import os
import random
import re
import sys


# Complete the maxSubsetSum function below.
'''
Intro: Since we know it's DP, we can solve the problem by solving subproblems of smaller size.

Because of the condition. No two adjacent elements can be picked. 
Therefore we can either take one and then skip one, or skip one and run the subroutine.

we can solve this problem in linear time and constant space ;)

Idea: store solutions for problem of size i-2 and i-1, where i is the size of the subproblem. 
The solution for problem of size i is either:
 1- solution for problem i-1, or 
 2- solution for problem i-2, or 
 3- solution of problem i-2 + arr[i],
 4- or ar[i]. 
Iterate for every i. Start with 0, 0 for problems of size - 2 and -1
'''


def maxSubsetSum(arr):
    a = float('-inf') # store solution for set of size i-2
    b = float('-inf') # store solution for set of size i-1

    for value in arr:
        a,b = b, max(a, a+value, b, value)

    return b
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = maxSubsetSum(arr)

    print(res)

    # fptr.write(str(res) + '\n')
    #
    # fptr.close()
