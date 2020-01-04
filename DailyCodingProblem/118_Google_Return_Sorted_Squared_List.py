"""
This problem was asked by Google.

Given a sorted list of integers, square the elements and give the output in sorted order.

For example, given [-9, -2, 0, 2, 3], return [0, 4, 4, 9, 81].
"""


def sorted_squared_list(sorted_numbers):
    stack = []
    res = []
    for num in reversed(sorted_numbers):
        if num > 0:
            stack.insert(0, num**2)
        else:
            while len(stack) > 0 and num**2 >= stack[0]:
                res.append(stack.pop(0))

            res.append(num**2)

    while stack:
        res.append(stack.pop(0))

    return res



if __name__ == '__main__':
    print(sorted_squared_list([-9, -2, 0, 2, 3]))
    print(sorted_squared_list([-9, -2, 0, 2, 3, 3, 4, 5,10, 11]))
    print(sorted_squared_list([-10,-9, -2, 0, 2, 3, 10]))

