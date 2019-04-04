'''
Function Description

Complete the function countSwaps in the editor below. It should print the three lines required, then return.

countSwaps has the following parameter(s):

a: an array of integers .
Input Format

The first line contains an integer, , the size of the array .
The second line contains  space-separated integers .

Constraints

Output Format

You must print the following three lines of output:

Array is sorted in numSwaps swaps., where  is the number of swaps that took place.
First Element: firstElement, where  is the first element in the sorted array.
Last Element: lastElement, where  is the last element in the sorted array.
Sample Input 0

3
1 2 3
Sample Output 0

Array is sorted in 0 swaps.
First Element: 1
Last Element: 3
Explanation 0
The array is already sorted, so  swaps take place and we print the necessary three lines of output shown above.

Sample Input 1

3
3 2 1
Sample Output 1

Array is sorted in 3 swaps.
First Element: 1
Last Element: 3

'''
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSwaps function below.
def countSwaps(a):
    num_swaps = 0  # variable to store the number of swaps

    for i in range(0,len(a)):
        ifSwap = False

        for j in range(0, len(a) - (i+1)):
            if a[j] > a[j+1]:  # then swap
                ifSwap = True
                a[j], a[j+1] = a[j+1], a[j]
                num_swaps+=1
        if not ifSwap:
            break
    return a, num_swaps

if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    a, num_swaps = countSwaps(a)

    print('Array is sorted in ' + str(num_swaps) + ' swaps.')
    print('First Element: ' + str(a[0]))
    print('Last Element: '+ str(a[len(a)-1]))
    print(a)