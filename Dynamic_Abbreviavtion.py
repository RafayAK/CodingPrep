'''
You can perform the following operations on the string, :

Capitalize zero or more of 's lowercase letters.
Delete all of the remaining lowercase letters in .
Given two strings,  and , determine if it's possible to make  equal to  as described. If so, print YES on a new line. Otherwise, print NO.

For example, given  and , in  we can convert  and delete  to match . If  and , matching is not possible because letters may only be capitalized or discarded, not changed.

Function Description

Complete the function  in the editor below. It must return either  or .

abbreviation has the following parameter(s):

a: the string to modify
b: the string to match
Input Format

The first line contains a single integer , the number of queries.

Each of the next  pairs of lines is as follows:
- The first line of each query contains a single string, .
- The second line of each query contains a single string, .

Constraints

String  consists only of uppercase and lowercase English letters, ascii[A-Za-z].
String  consists only of uppercase English letters, ascii[A-Z].
Output Format

For each query, print YES on a new line if it's possible to make string  equal to string . Otherwise, print NO.

Sample Input

1
daBcd
ABC
Sample Output

YES
Explanation

image

We have  daBcd and  ABC. We perform the following operation:

Capitalize the letters a and c in  so that  dABCd.
Delete all the remaining lowercase letters in  so that  ABC.
Because we were able to successfully convert  to , we print YES on a new line.
'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the abbreviation function below.
sys.setrecursionlimit(2000)
memo_dict = {}  # key is stored as a tuple of a's strings first then b's strings ('string_a', 'string_b') = TRUE/FALSE
dic_access = 0
def abbreviation(a, b):
    global dic_access
    if len(a) < len(b):
        return False

    if (a,b) in memo_dict:
        dic_access=+1
        return memo_dict[(a,b)]

    if a=='' and b!='':
        memo_dict[(a, b)] = False
        return False

    if a =='' and b=='':
        memo_dict[(a, b)] = True
        return True

    if b == '':
        if a[0].islower():
            memo_dict[(a,b)]= abbreviation(a[1:], b)
            return memo_dict[(a,b)]
        else:
            memo_dict[(a,b)]=False
            return False

    if a[0] == b[0]:
        memo_dict[(a,b)]= abbreviation(a[1:], b[1:])
        return memo_dict[(a,b)]
    elif a[0].isupper() and b[0].isupper():
        memo_dict[(a, b)] = False
        return False
    else: #a[0] != b[0]:
        memo_dict[(a,b)] = abbreviation(a[0].upper()+a[1:], b[0:]) or abbreviation(a[1:], b[0:])
        return memo_dict[(a,b)]




def output(result):
    if result:
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        a = input()

        b = input()

        result = abbreviation(a, b)
        #result = abbreviation_bottomUP(a, b)
        output(result)
        memo_dict.clear()
        print(dic_access)
        dic_access=0
        #fptr.write(result + '\n')

    #fptr.close()
