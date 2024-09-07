'''
Mark and Jane are very happy after having their first child. Their son loves toys, so Mark wants to buy some. There are a number of different toys lying in front of him, tagged with their prices. Mark has only a certain amount to spend, and he wants to maximize the number of toys he buys with this money.

Given a list of prices and an amount to spend, what is the maximum number of toys Mark can buy? For example, if  and Mark has  to spend, he can buy items  for , or  for  units of currency. He would choose the first group of  items.

Function Description

Complete the function maximumToys in the editor below. It should return an integer representing the maximum number of toys Mark can purchase.

maximumToys has the following parameter(s):

prices: an array of integers representing toy prices
k: an integer, Mark's budget
Input Format

The first line contains two integers,  and , the number of priced toys and the amount Mark has to spend.
The next line contains  space-separated integers

Constraints




A toy can't be bought multiple times.

Output Format

An integer that denotes the maximum number of toys Mark can buy for his son.

Sample Input

7 50
1 12 5 111 200 1000 10
Sample Output

4
Explanation

He can buy only 4 toys at most. These toys have the following prices: 1 12 5 10.
'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maximumToys function below.
def maximumToys(prices, k):
    sorted_prices = sorted(prices)  # sort the prices

    cart = [] # list to store toys
    budget = k
    for toy_price in sorted_prices:
        if toy_price < budget:
            cart.append(toy_price)
            budget-=toy_price
        if budget==0 or toy_price > budget:
            break

    #print('toys : {}'.format(cart))
    return len(cart)



if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0]) # number of toys on the shelf

    k = int(nk[1]) # an integer, Mark's budget

    prices = list(map(int, input().rstrip().split())) # an array of integers representing toy prices

    result = maximumToys(prices, k)

    print('Mark can buy: {}'.format(result))
    # fptr.write(str(result) + '\n')

    # fptr.close()