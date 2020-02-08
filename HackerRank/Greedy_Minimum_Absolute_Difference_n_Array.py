'''
Consider an array of integers, . We define the absolute difference between two elements,  and  (where ), to be the absolute value of .

Given an array of integers, find and print the minimum absolute difference between any two elements in the array. For example, given the array  we can create  pairs of numbers:  and . The absolute differences for these pairs are ,  and . The minimum absolute difference is .

Function Description

Complete the minimumAbsoluteDifference function in the editor below. It should return an integer that represents the minimum absolute difference between any pair of elements.

minimumAbsoluteDifference has the following parameter(s):

n: an integer that represents the length of arr
arr: an array of integers
Input Format

The first line contains a single integer , the size of .
The second line contains  space-separated integers .

Constraints

Output Format

Print the minimum absolute difference between any two elements in the array.

Sample Input 0

3
3 -7 0
Sample Output 0

3
Explanation 0

With  integers in our array, we have three possible pairs: , , and . The absolute values of the differences between these pairs are as follows:

Notice that if we were to switch the order of the numbers in these pairs, the resulting absolute values would still be the same. The smallest of these possible absolute differences is .

Sample Input 1

10
-59 -36 -13 1 -53 -92 -2 -96 -54 75
Sample Output 1

1
Explanation 1

The smallest absolute difference is .

Sample Input 2

5
1 -3 71 68 17
Sample Output 2

3
'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):
    abs_min = float('Inf')
    arr_len = len(arr)

    # ------------------- too high runtime
    # for i in range(arr_len-1): # iterate through to the Second-last element
    #     for j in range(i+1, arr_len):
    #         if abs(arr[i] - arr[j]) < abs_min:
    #             abs_min = abs(arr[i] - arr[j])
    #         if abs_min ==0:
    #             break

    # --------------------Better implementation
    # sort the array O(nlog(n))
    arr.sort()

    # now possible solution lies only between adjacent pairs
    for i in range(arr_len-1): # O(n)
        if abs(arr[i] - arr[i+1]) < abs_min:
            abs_min = abs(arr[i] - arr[i+1])
        if abs_min == 0:  # We can break in this case as its the min of the absolute function
            break

    return abs_min

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    print(result)
    #fptr.write(str(result) + '\n')

    #fptr.close()
