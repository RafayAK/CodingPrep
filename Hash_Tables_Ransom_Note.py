'''
Check out the resources on the page's right side to learn more about hashing. The video tutorial is by Gayle Laakmann McDowell, author of the best-selling interview book Cracking the Coding Interview.

Harold is a kidnapper who wrote a ransom note, but now he is worried it will be traced back to him through his handwriting. He found a magazine and wants to know if he can cut out whole words from it and use them to create an untraceable replica of his ransom note. The words in his note are case-sensitive and he must use only whole words available in the magazine. He cannot use substrings or concatenation to create the words he needs.

Given the words in the magazine and the words in the ransom note, print Yes if he can replicate his ransom note exactly using whole words from the magazine; otherwise, print No.

For example, the note is "Attack at dawn". The magazine contains only "attack at dawn". The magazine has all the right words, but there's a case mismatch. The answer is .

Function Description

Complete the checkMagazine function in the editor below. It must print  if the note can be formed using the magazine, or .

checkMagazine has the following parameters:

magazine: an array of strings, each a word in the magazine
note: an array of strings, each a word in the ransom note
Input Format

The first line contains two space-separated integers,  and , the numbers of words in the  and the ..
The second line contains  space-separated strings, each .
The third line contains  space-separated strings, each .

Constraints

.
Each word consists of English alphabetic letters (i.e.,  to  and  to ).
Output Format

Print Yes if he can use the magazine to create an untraceable replica of his ransom note. Otherwise, print No.

Sample Input 0
'''

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict, Counter

# Complete the checkMagazine function below.
# def checkMagazine(magazine, note):
#     #magazine_dict = {}
#     magazine_dict = defaultdict(int)  # ------ for better implementation
#
#     for word in magazine:
#         # if word in magazine_dict: # key already exists
#         #     magazine_dict[word] +=1
#         # else: # initialize
#         #     magazine_dict[word] = 1
#         magazine_dict[word]+=1  # -------> for better implementation, defaultdict returns 0 for missing keys in 'int' state
#
#     # now check if the note can be replicated
#     for word in note:
#         # if word in magazine_dict: # key exists
#         #     if magazine_dict[word] == 0: # not enough words
#         #         print('No')
#         #         return
#         #     else:
#         #         magazine_dict[word]-=1
#         # else:
#         #     print('No')
#         #     return
#
#         #  ------------- better implementation ---------
#
#         if magazine_dict[word] ==0:
#             print('No')
#             return
#         magazine_dict[word] -=1
#     print('Yes')


# even better implementation using COUNTER
def checkMagazine(magazine, note):
    if Counter(note) - Counter(magazine) != {}:
        print('No')
        return
    print('Yes')


if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
