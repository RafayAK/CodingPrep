#!/bin/python3

import math
import os
import random
import re
import sys

memo_dict = {} # store the sum as key with number of ways as value

def countWays(n,steps):
    global memo_dict
    current_sum = sum(steps)
    if current_sum == n:
        return 1
    if current_sum > n:
        return 0

    if n-current_sum in memo_dict:
        return memo_dict[n-current_sum]

    memo_dict[n-current_sum] = countWays(n, steps + [1]) + countWays(n, steps+[2]) + countWays(n, steps+[3])
    return memo_dict[n-current_sum]

# Complete the stepPerms function below.
def stepPerms(n):
    steps = []
    global memo_dict
    memo_dict[1] = 1
    memo_dict[2] = 2
    return countWays(n, steps)

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = int(input())

    for s_itr in range(s):
        n = int(input())

        res = stepPerms(n)
        print(res)
        #fptr.write(str(res) + '\n')

    #fptr.close()
