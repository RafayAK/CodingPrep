'''
Starting with a 1-indexed array of zeros and a list of operations, for each operation add a value to each of the array element between two given indices, inclusive. Once all operations have been performed, return the maximum value in your array.

For example, the length of your array of zeros . Your list of queries is as follows:

    a b k
    1 5 3
    4 8 7
    6 9 1
Add the values of  between the indices  and  inclusive:

index->	 1 2 3  4  5 6 7 8 9 10
	[0,0,0, 0, 0,0,0,0,0, 0]
	[3,3,3, 3, 3,0,0,0,0, 0]
	[3,3,3,10,10,7,7,7,0, 0]
	[3,3,3,10,10,8,8,8,1, 0]
The largest value is  after all operations are performed.

Function Description

Complete the function arrayManipulation in the editor below. It must return an integer, the maximum value in the resulting array.

arrayManipulation has the following parameters:

n - the number of elements in your array
queries - a two dimensional array of queries where each queries[i] contains three integers, a, b, and k.
Input Format

The first line contains two space-separated integers  and , the size of the array and the number of operations.
Each of the next  lines contains three space-separated integers ,  and , the left index, right index and summand.

Constraints

Output Format

Return the integer maximum value in the finished array.

Sample Input

5 3
1 2 100
2 5 100
3 4 100
Sample Output

200
Explanation

After the first update list will be 100 100 0 0 0.
After the second update list will be 100 200 100 100 100.
After the third update list will be 100 200 200 200 100.
The required answer will be 200.
'''





#!/bin/python3

import math
import os
import random
import re
import sys

'''
What this algo does is to register the slopes only, so we just need 2 entry, with O(1) complexity.

We just need to know that we are upping from k at the beginning and decreasing at the end.

Finally, the maximum would be...


      ___
    _/   \
  _/      \__
_/           \


The addition of all the slopes, that is why it's max(sum) of the tables, because the tables itself registers the slopes

O(n) runtime
'''
def arrrayManipluation_linear(n, queries):

    # arrays start at index 1 in the question
    arr = [0] * (n + 1)  # create zeros-array of size n+1

    # run through the queries
    # query -> [start_idx, end_idx, num_to_add]
    # indices are inclusive
    for q in queries:
        arr[q[0]] += q[2]

        if q[1] +1 <= n: # check in range
            arr[q[1] +1] -= q[2]

    arr = arr[1:]

    max_sum = float('-inf')  # to store max value in the arr
    x = 0 # temp variable
    for val in arr:
        x += val
        if x > max_sum:
            max_sum = x

    #print(arr)
    return max_sum

# Complete the arrayManipulation function below.
# O(n^2) implementation
def arrayManipulation(n, queries):

    # arrays start at index 1 in the question
    arr = [0] * (n+1)  # create zeros-array of size n+1

    # run through the queries
    # query -> [start_idx, end_idx, num_to_add]
    # indices are inclusive
    for q in queries:
        temp = arr[q[0]: q[1]+1]  # q[1]+1 because inclusive
        temp = [i+q[2] for i in temp]
        arr[q[0] : q[1]+1] = temp
    arr = arr[1:]
    print(arr)
    return max(arr)



if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    # result = arrayManipulation(n, queries)
    # print(result)

    result = arrrayManipluation_linear(n, queries)
    print(result)
    # fptr.write(str(result) + '\n')

    # fptr.close()
