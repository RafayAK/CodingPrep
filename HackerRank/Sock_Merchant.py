'''
John works at a clothing store. He has a large pile of socks that he must pair by color for sale. Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.

For example, there are  socks with colors . There is one pair of color  and one of color . There are three odd socks left, one of each color. The number of pairs is .

Function Description

Complete the sockMerchant function in the editor below. It must return an integer representing the number of matching pairs of socks that are available.

sockMerchant has the following parameter(s):

n: the number of socks in the pile
ar: the colors of each sock
Input Format

The first line contains an integer , the number of socks represented in .
The second line contains  space-separated integers describing the colors  of the socks in the pile.

Constraints

 where
Output Format

Print the total number of matching pairs of socks that John can sell.

Sample Input

9
10 20 20 10 10 30 50 10 20

Sample Output

3
'''

# ----------- My Implementation ------------------

# !/bin/python3

import math
import os
import random
import re
import sys


def get_number_of_pairs(socks):  # pass dictionary of socks
    num_of_pairs = 0
    for key in socks:
        num_of_pairs += math.floor(socks[key] / 2)

    return num_of_pairs


# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    socks = {}  # dictionary to store socks of each color

    for i in range(n):  # iterate over all the socks in the array 'ar'
        count = 1  # start from 1, beacuse you've already found one

        if ar[
            i] not in socks:  # create entry in dictionary for the sock color and look for more                                # of that color
            for j in range(i + 1, n):  # iterate over rest of the socks
                if ar[i] == ar[j]: count += 1
            socks[ar[i]] = count

    return get_number_of_pairs(socks)


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    print(result)

    # fptr.write(str(result) + '\n')
    #
    # fptr.close()


'''
Input format:
9
10 20 20 10 10 30 50 10 20

Output:
3

'''