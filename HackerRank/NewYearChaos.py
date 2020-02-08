'''
It's New Year's Day and everyone's in line for the Wonderland rollercoaster ride! There are a number of people queued up, and each person wears a sticker indicating their initial position in the queue. Initial positions increment by  from  at the front of the line to  at the back.

Any person in the queue can bribe the person directly in front of them to swap positions. If two people swap positions, they still wear the same sticker denoting their original places in line. One person can bribe at most two others. For example, if and  bribes , the queue will look like this: .

Fascinated by this chaotic queue, you decide you must know the minimum number of bribes that took place to get the queue into its current state!

Function Description

Complete the function minimumBribes in the editor below. It must print an integer representing the minimum number of bribes necessary, or Too chaotic if the line configuration is not possible.

minimumBribes has the following parameter(s):

q: an array of integers
Input Format

The first line contains an integer , the number of test cases.

Each of the next  pairs of lines are as follows:
- The first line contains an integer , the number of people in the queue
- The second line has  space-separated integers describing the final state of the queue.

Constraints

Subtasks

For  score
For  score

Output Format

Print an integer denoting the minimum number of bribes needed to get the queue into its final state. Print Too chaotic if the state is invalid, i.e. it requires a person to have bribed more than  people.

Sample Input

2
5
2 1 5 3 4
5
2 5 1 3 4
Sample Output

3
Too chaotic

Test Case 2

No person can bribe more than two people, so its not possible to achieve the input state.
'''

import math
import os
import random
import re
import sys

# # Complete the minimumBribes function below.
# def minimumBribes(q):
#     bribes = 0
#     size_of_line = len(q)
#
#     # check if the queue is too chaotic
#     for i, v in enumerate(q):
#         if (v - 1) - i > 2: # nothing can be positively too far away from its original spot
#             print("Too chaotic")
#             return
#
#
#     # bubble sort
#     for i in range(size_of_line):
#         swap_happened = False
#
#         for j in range(size_of_line-1):
#             if q[j] > q[j+1]:
#                 q[j],q[j+1] = q[j+1], q[j] # swap
#                 swap_happened = True
#                 bribes+=1
#
#         if swap_happened is False:
#             break
#
#     print(bribes)


# better implementation -> just count the number of people who overtake some one

def minimumBribes(q):
    bribes = 0
    for i in range(len(q)-1,-1,-1):
        if (q[i]-1) - i > 2:
            print('Too chaotic')
            return
        current = q[i]
        range_start = max(0, q[i] - 2)
    #     if q[i] - (i + 1) > 2:
    #         print('Too chaotic')
    #         return
        for j in range(max(0, q[i] - 2),i):
            looking_at = q[j]
            if q[j] > q[i]:
                bribes+=1
    print(bribes)


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)