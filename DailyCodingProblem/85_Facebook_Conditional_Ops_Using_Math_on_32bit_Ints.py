"""
This problem was asked by Facebook.

Given three 32-bit integers x, y, and b, return x if b is 1 and y if b is 0,
using only mathematical or bit operations. You can assume b can only be 1 or 0.
"""

import numpy as np

def conditional_op(x, y, b):
    condition_1 = (b ^ np.uint32(0))
    condition_2 = (b ^ np.uint32(1))
    return (x*condition_1) | (y*condition_2)

if __name__ == '__main__':
    x = np.uint32(44)
    y = np.uint32(5)

    print(conditional_op(x,y, b = np.uint32(1)))  # 44

    print(conditional_op(x, y, b=np.uint32(0)))  # 5



