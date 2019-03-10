"""
Given an array of ints, return a new array such that each element at index i
of the new array is the product of all the number in the array except the one at i

E.g. if our input was:
 [1,2,3,4,5],
the expected output would be:
[120, 60, 40, 30, 24]

if input was :
[3,2,1]
output:
[2,3,6]

**** Follow up question: What if you cant use division

"""

import sys

# Complete the abbreviation function below.
sys.setrecursionlimit(2000)

def product_arr(arr):
    total_product = 1
    for i in arr:
        total_product *= i

    result_arr = [int(total_product/x) for x in arr]
    return result_arr

memo_dict = {}

def helper(arr):
    global memo_dict
    if tuple(arr) in memo_dict:
        return memo_dict[tuple(arr)]

    if len(arr) == 1:
        memo_dict[tuple(arr)]= arr[0]
        return arr[0]

    memo_dict[tuple(arr)]= arr[0] * helper(arr[1:])
    return memo_dict[tuple(arr)]




def dp_product(arr):
    len_arr = len(arr)
    if len_arr == 0:
        return None
    result_arr = []
    for idx in range(len_arr):
        result_arr.append(helper([arr[element] for element in range(len_arr) if element != idx]))

    return result_arr

# with O(n) time and O(n) space complexity
def n_product(arr):
    len_arr = len(arr)
    result_arr = []
    temp_left = [None] * len_arr
    temp_right = [None] * len_arr

    # first fill up left
    temp_left[0] = 1
    for i in range(1,len_arr):
        temp_left[i]= temp_left[i-1] * arr[i-1]

    # fill up right
    temp_right[len_arr-1] = 1
    for i in range(len_arr-2, -1, -1):
        temp_right[i] = temp_right[i+1] * arr[i+1]

    for i in range(len_arr):
        result_arr.append(temp_right[i]* temp_left[i])


    return result_arr

#O(n) time O(1) space
def constSpace_product(arr):
    len_arr = len(arr)
    result_arr = [1] * len_arr
    temp = 1

    # first fill up left
    for i in range(0,len_arr):
        result_arr[i] *= temp
        temp*= arr[i]

    # reset temp
    temp =1
    # fill up right
    for i in range(len_arr-1, -1, -1):
        result_arr[i] *= temp
        temp*=arr[i]

    # for i in range(len_arr):
    #     result_arr.append(temp_right[i]* temp_left[i])

    return result_arr

def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    arr = [1]
    for num in nums[:-1]:
        arr.append(num*arr[-1])
    tmp = 1
    for i in range(len(nums)-1, -1, -1):
        arr[i] = arr[i]*tmp
        tmp = tmp*nums[i]
    return arr

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split(',')))
    # print(product_arr(arr))
    # print(dp_product(arr))
    print(n_product(arr))
    # print(constSpace_product(arr))
    #print(productExceptSelf(arr,))