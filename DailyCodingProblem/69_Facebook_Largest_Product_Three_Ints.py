"""
Problem 69
This problem was asked by Facebook.

Given a list of integers, return the largest product that can be made by multiplying any three integers.

For example, if the list is [-10, -10, 5, 2], we should return 500, since that's -10 * -10 * 5.

You can assume the list has at least three integers.
"""


# def helper(arr, product=1, recursion_depth=0):
#     if len(arr) <= 2:
#         return max(product * arr[0], product * arr[1])
#     if recursion_depth == max_recursion_depth:
#         return product
#
#     list_of_products = []
#
#     for i in range(0, len(arr)):
#         list_of_products += [helper(arr[i + 1:], product * arr[i], recursion_depth + 1)]
#
#     return max(list_of_products)



def largest_product(numbers:list):
    memo_dict = {}
    max_recursion_depth = 3

    def helper(arr, product=1, recursion_depth=0):
        if tuple(arr) in memo_dict:
            return memo_dict

        if recursion_depth == max_recursion_depth:
            return arr[0]

        if len(arr) == 0:
            return 0

        list_of_products = []

        for i in range(0, len(arr)):
            list_of_products += [helper(arr[i + 1:], product * arr[i], recursion_depth + 1)]

        memo_dict[tuple(arr)] = max(list_of_products)

        return memo_dict[tuple(arr)]


    max_product = float('-inf')
    for i in range(len(numbers)):
        res = helper(numbers[i:])
        max_product = max(res, max_product)

    return max_product





if __name__ == '__main__':

    print(largest_product([-10, -10, 5, 2]))