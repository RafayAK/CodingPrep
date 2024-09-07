'''
There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time.
Given N, write a function that returns the number of unique ways you can climb the staircase.
The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

1, 1, 1, 1
2, 1, 1
1, 2, 1
1, 1, 2
2, 2
What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from
a set of positive integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.
'''

#!/bin/python3

import math
import os
import random
import re
import sys

memo_dict = {}  # store the sum as key with number of ways as value

def stepArbiPrems(n, steps_list): # take steps backed on values in steps list

    if n in memo_dict:
        return memo_dict[n]

    if n < 0:
        return 0
    if n == 0:
        memo_dict[n] =1
        return 1
    memo_dict[n] = 0
    for step in steps_list:
        memo_dict[n]+= stepArbiPrems(n-step, steps_list)

    return memo_dict[n]

def stepPerms(n): # step permutations
    if n in memo_dict:
        return memo_dict[n]
    if n < 0:
        return 0
    if n == 0:
        memo_dict[n] = 1
        return 1

    memo_dict[n] = stepPerms(n-1) + stepPerms(n-2)
    return memo_dict[n]

if __name__ == '__main__':

    N = 4  # steps in a stair case
    step_list = [1, 3, 10]
    # res = stepPerms(N)
    res = stepArbiPrems(N, step_list)
    print(res)

