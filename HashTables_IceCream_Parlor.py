'''
Each time Sunny and Johnny take a trip to the Ice Cream Parlor, they pool their money to buy ice cream.
On any given day, the parlor offers a line of flavors. Each flavor has a cost associated with it.

Given the value of  and the  of each flavor for  trips to the Ice Cream Parlor, help Sunny and Johnny
choose two distinct flavors such that they spend their entire pool of money during each visit. ID numbers
are the 1- based index number associated with a . For each trip to the parlor, print the ID numbers for
the two types of ice cream that Sunny and Johnny purchase as two space-separated integers on a new line.
You must print the smaller ID first and the larger ID second.

For example, there are  flavors having . Together they have  to spend. They would purchase flavor ID's
and  for a cost of . Use  based indexing for your response.

Note:

Two ice creams having unique IDs  and  may have the same cost (i.e., ).
There will always be a unique solution.
Function Description

Complete the function whatFlavors in the editor below. It must determine the two flavors they
 will purchase and print them as two space-separated integers on a line.

whatFlavors has the following parameter(s):

cost: an array of integers representing price for a flavor
money: an integer representing the amount of money they have to spend
Input Format

The first line contains an integer, , the number of trips to the ice cream parlor.

Each of the next  sets of  lines is as follows:

The first line contains .
The second line contains an integer, , the size of the array .
The third line contains  space-separated integers denoting the .
Constraints

Output Format

Print two space-separated integers denoting the respective indices for the two distinct flavors
they choose to purchase in ascending order. Recall that each ice cream flavor has a unique ID
number in the inclusive range from  to .

Sample Input

2
4
5
1 4 5 3 2
4
4
2 2 4 3
Sample Output

1 4
1 2
Explanation

Sunny and Johnny make the following two trips to the parlor:

1- The first time, they pool together 4 dollars. There are five flavors available that
day and flavors  and  have a total cost of  1 + 3 =5 dollars.

2- The second time, they pool together  dollars. There are four flavors available that
day and flavors  and  have a total cost of 2 + 2= 4 dollars.
'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the whatFlavors function below.
def whatFlavors(cost, money):
    # ------------ New Implementation using python dictionary for constant time look ups => O(n) ----------
    icecream_seen = {}  # dictinary to store ice cream costs as key & index as value
    budget = money
    number_of_elements = len(cost)
    for index in range(number_of_elements):
        if icecream_seen.get(budget - cost[index]) is not None:  # found ice cream in budget
            print('{} {}'.format(icecream_seen[budget - cost[index]] + 1, index + 1 ))
            break
        else:  # corresponding ice cream not found
            icecream_seen[cost[index]] = index

    # ------------ Slow implementation => O(n^2) ---------------
    #     number_of_elements = len(cost)
    #     for item_idx in range(number_of_elements):
    #         to_find = money - cost[item_idx]
    #
    #         small_list = cost[item_idx+1:]
    #         if to_find in small_list:
    #             # small_list.index(to_find)+item_idx+2 gives the correct 1 based index for smaller list
    #             print('{} {}'.format(item_idx+1, small_list.index(to_find)+item_idx+2))
    #             break



if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        money = int(input())

        n = int(input())

        cost = list(map(int, input().rstrip().split()))

        whatFlavors(cost, money)
