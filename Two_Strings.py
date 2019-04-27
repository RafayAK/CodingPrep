'''
Given two strings, determine if they share a common substring. A substring may be as small as one character.

For example, the words "a", "and", "art" share the common substring . The words "be" and "cat" do not share a substring.

Function Description

Complete the function twoStrings in the editor below. It should return a string, either YES or NO based on whether the strings share a common substring.

twoStrings has the following parameter(s):

s1, s2: two strings to analyze .
Input Format

The first line contains a single integer , the number of test cases.

The following  pairs of lines are as follows:

The first line contains string .
The second line contains string .
Constraints

 and  consist of characters in the range ascii[a-z].
Output Format

For each pair of strings, return YES or NO.

Sample Input

2
hello
world
hi
world
Sample Output

YES
NO
'''
# !/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


# Complete the twoStrings function below.
def twoStrings(s1, s2):
    # only need to satisfy if has any matching letter

    dicty = Counter(s1)

    found = False
    for letter in s2:
        if dicty[letter] != 0:
            found=True
            break

    if found:
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        #fptr.write(result + '\n')

    #fptr.close()