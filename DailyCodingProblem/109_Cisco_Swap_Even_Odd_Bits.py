"""
This problem was asked by Cisco.

Given an unsigned 8-bit integer, swap its even and odd bits. The 1st and 2nd bit should be swapped, the 3rd and 4th bit should be swapped, and so on.

For example, 10101010 should be 01010101. 11100010 should be 11010001.
"""

# even bits are 0101 0101 -> 85

# solution:
# extract even bits of the number and shift them right
# extract odd bits of the number and shift them left
# combine both even and odd bits with and OR

def swap_bits(number):
    return ((number & 85) << 1) | ((number & (85 << 1)) >> 1)


if __name__ == '__main__':
    assert swap_bits(170) == 85  # 107 =  10101010 , 85 = 01010101
    assert swap_bits(int('0b11100010', 2)) == int('0b11010001', 2)
    assert swap_bits(210) == 225
    assert swap_bits(170) == 85
    assert swap_bits(226) == 209
    assert swap_bits(0) == 0
