"""
Problem 69
This problem was asked by Facebook.

Given a list of integers, return the largest product that can be made by multiplying any three integers.

For example, if the list is [-10, -10, 5, 2], we should return 500, since that's -10 * -10 * 5.

You can assume the list has at least three integers.
"""

def largest_product(numbers:list):
    max_recursion_depth = 3

    def helper(arr, product=1, recursion_depth=0):
        if recursion_depth < 3  and len(arr) == 0:  # invalid case -> not enough number to compute product of threes
            return float('-inf')  # return -inf in this case


        if len(arr) == 0 or recursion_depth==max_recursion_depth:
            return product

        list_products = []

        for i in range(len(arr)):
            list_products+=[helper(arr[i+1:], product*arr[i], recursion_depth+1)]

        return max(list_products)


    max_product = float('-inf')
    for i in range(len(numbers)):
        if len(numbers[i:]) > 2:  # perform this iff there are at least 3 numbers in the list
            res = helper(numbers[i:])
        max_product = max(res, max_product)

    return max_product





if __name__ == '__main__':

    print(largest_product([-10, -10, 5, 2]))  # ans 500
    print(largest_product([-10, -10, -5, -2]))  # ans -100