''''
Gary is an avid hiker. He tracks his hikes meticulously, paying close attention to small details like topography. During his last hike he took exactly  steps. For every step he took, he noted if it was an uphill, , or a downhill,  step. Gary's hikes start and end at sea level and each step up or down represents a  unit change in altitude. We define the following terms:

A mountain is a sequence of consecutive steps above sea level, starting with a step up from sea level and ending with a step down to sea level.
A valley is a sequence of consecutive steps below sea level, starting with a step down from sea level and ending with a step up to sea level.
Given Gary's sequence of up and down steps during his last hike, find and print the number of valleys he walked through.

For example, if Gary's path is , he first enters a valley  units deep. Then he climbs out an up onto a mountain  units high. Finally, he returns to sea level and ends his hike.

Function Description

Complete the countingValleys function in the editor below. It must return an integer that denotes the number of valleys Gary traversed.

countingValleys has the following parameter(s):

n: the number of steps Gary takes
s: a string describing his path
Input Format

The first line contains an integer , the number of steps in Gary's hike.
The second line contains a single string , of  characters that describe his path.

Constraints

Output Format

Print a single integer that denotes the number of valleys Gary walked through during his hike.

Sample Input

8
UDDDUDUU
Sample Output

1
Explanation

If we represent _ as sea level, a step up as /, and a step down as \, Gary's hike can be drawn as:

_/\      _
   \    /
    \/\/
He enters and leaves one valley.
'''


# ----------- My Implementation ------------------


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    # stack = []  # keeps track of the U and D movements
    # in_mountain = False
    # in_valley = False
    #
    # count_valleys, count_mountains = 0, 0
    #
    # for step in s:
    #     if in_mountain==False and in_valley==False:  # sea level
    #         if step=='U':
    #             in_mountain=True
    #             stack.append(step)
    #             count_mountains+=1
    #
    #         elif step=='D':
    #             in_valley=True
    #             stack.append(step)
    #             count_valleys+=1
    #
    #     elif in_mountain == True: # still in a mountain
    #         if step=='U':
    #             stack.append(step)
    #         elif step=='D':
    #             stack.pop()
    #
    #         if not stack: # stack empty! stepped over mountain onto sea-level
    #             in_mountain = False
    #
    #     elif in_valley == True:  # still in a valley
    #         if step == 'D':
    #             stack.append(step)
    #         elif step == 'U':
    #             stack.pop()
    #
    #         if not stack:  # stack empty! stepped out of valley onto sea-level
    #             in_valley = False
    #
    # return count_valleys

    # --------------- better implementation ---------------------
    level = 0  # 0 => sealevel
    valleys = 0  # counts number of valleys

    for step in s:
        if level == 0 and step == 'D':  # about to enter valley
            valleys += 1

        if step == 'U':
            level+=1
        else:
            level-=1

    return valleys

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    print('Number of valleys traversed: {}'.format(result))

    #fptr.write(str(result) + '\n')

    #fptr.close()
