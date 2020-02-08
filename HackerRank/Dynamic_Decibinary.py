#!/bin/python3

import math
import os
import random
import re
import sys

# 999999999999999999999

def db_value(x):  # takes db_number and return its decimal value
    power = 0
    value = 0
    for i in reversed(str(x)):
        value += int(i) * (2**power)
        power+=1
    return value



def comp(a):  # comparator sorts the db_numbers based on their decimal value
    return db_value(a)



ans_list = list()
def decibinaryNumbers_bruteForce():
    global ans_list
    for i in range(1100):
        ans_list.append(i)

    ans_list = sorted(ans_list, key=comp)

# --------------------------------------------------------
# recursive approach

# d -> number of digits
# s -> required decimal value
# v -> current integer being built
def gen(d, s, v):

    # 9*((1 << (d+1))-1) :
    #       - (1 << (d+1) => right shift its by d+1 bits
    #                        eg. if d=2, then 1<<(2+1)= 1000_b
    #       - (1 << (d+1) -1 => sub one to find the max this binary value can achieve
    #                        => eg 1000_b(8_d) -1 = 111_b(7_d)
    #       - 9*((1 << (d+1))-1) => times 9 to find the max decibinary value these digits can achieve
    #                            => 9*(111_b) = 999_db = 63_d

    # NOTE : at d = 0 => no shift in bits max value = 9
    #        at d = -1 => exhausted digits, max value =1
    if s < 0 or s > 9*((1 << (d+1))-1):  # can't create this number either too big for the
        pass                         # given digits or less than 0
    elif s==0 and d==-1:
        ans_list.append(v)
    else:
        for i in range(10):
            # s - i*(1<<d) => i*(1<<d) creates the db_number and subs it form the required value to
            #                 recurse to a smaller value
            # v*10 + i =>  v*10 add a zero to the current number being built to add a value form 0-9
            #              eg  10_db(2_decimal) -> 2*10 = 20_db
            gen(d-1, s - i*(1<<d), v*10 + i)


memo_dict = {}
memo_dict[0] =1
memo_dict[1] = 1
memo_dict[2] = 2
def my_gen_counter(d, s, v):
    global memo_dict
    # 9*((1 << (d+1))-1) :
    #       - (1 << (d+1) => right shift its by d+1 bits
    #                        eg. if d=2, then 1<<(2+1)= 1000_b
    #       - (1 << (d+1) -1 => sub one to find the max this binary value can achieve
    #                        => eg 1000_b(8_d) -1 = 111_b(7_d)
    #       - 9*((1 << (d+1))-1) => times 9 to find the max decibinary value these digits can achieve
    #                            => 9*(111_b) = 999_db = 63_d

    # NOTE : at d = 0 => no shift in bits max value = 9
    #        at d = -1 => exhausted digits, max value =1
    if s in memo_dict:
        return memo_dict[s]
    if s < 0 or s > 9*((1 << (d+1))-1):  # can't create this number either too big for the
        pass                         # given digits or less than 0
    elif s==0 and d==-1:
        return 1
    else:
        for i in range(10):
            # s - i*(1<<d) => i*(1<<d) creates the db_number and subs it form the required value to
            #                 recurse to a smaller value
            # v*10 + i =>  v*10 add a zero to the current number being built to add a value form 0-9
            #              eg  10_db(2_decimal) -> 2*10 = 20_db
            memo_dict[s] = my_gen_counter(d-1, s - i*(1<<d))

# ----------------------------------------------------------------------------------
# DP method
decimal_value = 270000#285140#285133#300005
digits= 19#25

dp_arr = [[-1 for i in range(decimal_value+1)] for j in range(digits+1)]
nm = [0]*decimal_value
def count(d, s): # count the numbr of intrgers with the decimal value 'val'
    global  dp_arr
    if(d ==-1 and s == 0):
        return 1
    elif (d == -1):
        return 0
    elif(dp_arr[d][s] == -1):
        dp_arr[d][s] = 0
        for i in range(10):
            temp= (1<<d)*i
            if (1<<d)*i > s:
                break
            dp_arr[d][s] += count(d-1, s-((1 << d)*i))
            dp_arr[d][s+1] = dp_arr[d][s]
    return dp_arr[d][s]

# memo_list = []
# def my_gen(decimal_range):
#     global memo_list, ans_list
#     memo_list.append(1) # for 0
#     memo_list.append(1) # for 1
#
#     for i in range(2,decimal_range, 2):
#         gen(20, i, 0)
#         memo_list.append(ans_list.__len__())
#         memo_list.append(ans_list.__len__())
#         ans_list.clear()





if __name__ == '__main__':

    # decibinaryNumbers_bruteForce() # bruteForce to generate numbers and sort them

    # # generate 10^7 db_numbers recursively
    # for i in range(600):  # generating db_numbers up to decimal value of 599 does the trick
    #     gen(20, i, 0)
    #
    q = int(input())

    for i in range(0, decimal_value, 2):
        nm[i] = count(digits, i)
        if i+1!=decimal_value: nm[i+1] = nm[i]
    for i in range(1,decimal_value):
        nm[i] += nm[i-1]

    #print(nm)


    for q_itr in range(q):
        x = int(input())
        if x == 1:
            print(0)
        else:
            lo = 0
            hi = decimal_value - 1
            idx = None
            while lo <= hi:
                mid = int((lo + hi) / 2)
                if nm[mid] >= x:
                    idx = mid
                    hi = mid - 1
                else:
                    lo = mid + 1

            #print(idx)
            ans_list.clear()
            gen(digits, idx, 0)
            index = nm[idx - 1]
            for i in range(ans_list.__len__()):
                index += 1
                if index == x:
                    print(ans_list[i])



    # for q_itr in range(q):
    #     x = int(input())
    #
    #     #result = ans_list[x-1]
    #     if x == 1:
    #         print(1)
    #     else:
    #         lo =0
    #         hi =decimal_value-1
    #         ans = None
    #         while(lo <= hi):
    #             mid = int((lo+hi)/2)
    #             if nm[mid] >= x:
    #                 ans = mid
    #                 hi= mid-1
    #             else:
    #                 lo = mid+1
    #
    #         g = x - nm[ans -1]
    #         s = ans
    #         d =None
    #
    #         i=-1
    #         while count(i,s) < g:
    #             d= i
    #             i+=1
    #         d+=1
    #
    #         while d>=0:
    #             val =0
    #             for i in range(10):
    #                 if s - ((1 << d)*i) >=0:
    #                     val+=count(d-1, s-((1<<d)*i))
    #                 if val >=g:
    #                     print(i)
    #                     g-=val - count(d-1, s-((1<<d)*i))
    #                     s -=(1 << d)*i
    #                     break
    #             d-=1

