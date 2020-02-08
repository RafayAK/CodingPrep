'''
In computer programming, the XOR swap is an algorithm that uses the XOR bitwise operation to swap values of distinct
variables having the same data type without using a temporary variable. "Distinct" means that the
variables are stored at different, non-overlapping, memory addresses; the actual values of the variables do not have to be different.
'''

x = 1
y = 2

print('before swap: \n x={}, y={}'.format(x,y))

# XOR swap
x = x ^ y
y = x ^ y
x = x ^ y

print('after swap: \n x={}, y={}'.format(x,y))