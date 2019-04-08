'''
A bracket is considered to be any one of the following characters: (, ), {, }, [, or ].

Two brackets are considered to be a matched pair if the an opening bracket (i.e., (, [, or {) occurs to the left of a closing bracket (i.e., ), ], or }) of the exact same type. There are three types of matched pairs of brackets: [], {}, and ().

A matching pair of brackets is not balanced if the set of brackets it encloses are not matched. For example, {[(])} is not balanced because the contents in between { and } are not balanced. The pair of square brackets encloses a single, unbalanced opening bracket, (, and the pair of parentheses encloses a single, unbalanced closing square bracket, ].

By this logic, we say a sequence of brackets is balanced if the following conditions are met:

It contains no unmatched brackets.
The subset of brackets enclosed within the confines of a matched pair of brackets is also a matched pair of brackets.
Given  strings of brackets, determine whether each sequence of brackets is balanced. If a string is balanced, return YES. Otherwise, return NO.

Function Description

Complete the function isBalanced in the editor below. It must return a string: YES if the sequence is balanced or NO if it is not.

isBalanced has the following parameter(s):

s: a string of brackets
Input Format

The first line contains a single integer , the number of strings.
Each of the next  lines contains a single string , a sequence of brackets.

Constraints

, where  is the length of the sequence.
All chracters in the sequences ∈ { {, }, (, ), [, ] }.
Output Format

For each string, return YES or NO.

Sample Input

3
{[()]}
{[(])}
{{[[(())]]}}
Sample Output

YES
NO
YES
Explanation

The string {[()]} meets both criteria for being a balanced string, so we print YES on a new line.
The string {[(])} is not balanced because the brackets enclosed by the matched pair { and } are not balanced: [(]).
The string {{[[(())]]}} meets both criteria for being a balanced string, so we print YES on a new line.

'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.

bracket_vocab = {'(': 1,
                 ')': 2,
                 '[': 3,
                 ']': 4,
                 '{': 5,
                 '}': 6}

def isBalanced(s):
    stack = []  # our stack to check if brackets are balances

    for bracket in s:
        if stack.__len__() == 0: # stack empty
            # add to the stack
            stack.append(bracket_vocab[bracket])
        elif bracket_vocab[bracket] -1 == stack[stack.__len__() -1]:
            # found matching bracket, pop
            del(stack[stack.__len__() -1])
        else:
            stack.append(bracket_vocab[bracket])

    if stack.__len__() == 0: # empty stack all brackets matched
        return 'YES'

    return 'NO'

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)
        print(result)
        #fptr.write(result + '\n')

   #fptr.close()

