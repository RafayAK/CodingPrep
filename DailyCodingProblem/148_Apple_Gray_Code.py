"""
This problem was asked by Apple.

Gray code is a binary code where each successive value differ in only one bit,
as well as when wrapping around. Gray code is common in hardware so that we don't
see temporary spurious values during transitions.

Given a number of bits n, generate a possible gray code for it.

For example, for n = 2, one gray code would be [00, 01, 11, 10].
"""

# Solution:(Wikipedia)
#
# The binary-reflected Gray code list for n bits can be generated recursively
# from the list for n − 1 bits by reflecting the list (i.e. listing the entries
# in reverse order), prefixing the entries in the original list with a binary 0,
# prefixing the entries in the reflected list with a binary 1, and then concatenating
# the original list with the reversed list.[11] For example, generating the n = 3 list from the n = 2 list:
#
# 2-bit list:	00, 01, 11, 10
# Reflected:	 	10, 11, 01, 00
# Prefix old entries with 0:	000, 001, 011, 010,
# Prefix new entries with 1:	 	110, 111, 101, 100
# Concatenated:	000, 001, 011, 010,	110, 111, 101, 100
#


memo_table = {1: ['0', '1']}


def create_gray_code(n:int):
    if n in memo_table:
        return memo_table[n]

    gray_code_prev_n = create_gray_code(n-1)
    prefix_old = ['0'+entry for entry in gray_code_prev_n]
    prefix_new = ['1'+entry for entry in reversed(gray_code_prev_n)]
    memo_table[n] = prefix_old + prefix_new
    return memo_table[n]


if __name__ == '__main__':
    print(create_gray_code(3))