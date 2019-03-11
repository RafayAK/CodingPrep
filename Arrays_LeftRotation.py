'''

A left rotation operation on an array shifts each of the array's elements  unit to the left. For example, if  left rotations are performed on array , then the array would become .

Given an array  of  integers and a number, , perform  left rotations on the array. Return the updated array to be printed as a single line of space-separated integers.

Function Description

Complete the function rotLeft in the editor below. It should return the resulting array of integers.

rotLeft has the following parameter(s):

An array of integers .
An integer , the number of rotations.
Input Format

The first line contains two space-separated integers  and , the size of  and the number of left rotations you must perform.
The second line contains  space-separated integers .

Constraints

Output Format

Print a single line of  space-separated integers denoting the final state of the array after performing  left rotations.

Sample Input

5 4
1 2 3 4 5
Sample Output

5 1 2 3 4

'''

# !/bin/python3

import math
import os
import random
import re
import sys

def rotate_left(n, k, arr):
    # n-> size of array/list 'arr'
    # k-> number of left rotations
    # arr-> list of numbers
    num_of_rotations = k%n

    # # --------------------  Slow implementation -----------------
    # for i in range(num_of_rotations):
    #     temp = arr[0]  # store the first element
    #     for j in range(n -1 ):
    #         arr[j] = arr[j+1]
    #     arr[n-1] = temp

    # Faster implementation O(n)
    # if num_of_rotations >0:
    #     # temp variable to store rotations
    #     for i in range(n):
    #         if(i< num_of_rotations):
    #             temp = arr.pop(0)  # pop first element into to temporarily store it
    #             arr.append(temp)

    # EVEN Better implementation using slicing
    arr = arr[num_of_rotations:] + arr[:num_of_rotations]



    return arr



if __name__ == '__main__':
    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    a = list(map(int, input().rstrip().split()))

    arr = rotate_left(n,k,a)
    print(arr)

