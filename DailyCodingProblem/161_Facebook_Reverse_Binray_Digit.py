"""
This problem was asked by Facebook.

Given a 32-bit integer, return the number with its bits reversed.

For example, given the binary number
    1111 0000 1111 0000 1111 0000 1111 0000,
return
    0000 1111 0000 1111 0000 1111 0000 1111.

"""


# take a bit from number one by one add it to the resultant reversed number
# The below implementation check if the right most bit in the number is 1
# buy AND'ing the number with 1 if the result is 1 then it is added as 1 to the
# result otherwise 0, using the OR op.
def reverse_bits(number):
    res = 0  # This variable stores the result from reversed bits

    number_of_bits = 32

    re_bits = bin(res)
    num_bits = bin(number)
    while number > 0:
        res = res << 1
        re_bits = bin(res)

        res = res | (number & 1)
        re_bits = bin(res)
        num_bits = bin(number)

        number = number >> 1
        num_bits = bin(number)

        number_of_bits -= 1

    return res




if __name__ == '__main__':

    assert reverse_bits(int("11110000111100001111000011110000", 2)) == int("00001111000011110000111100001111", 2)

    assert reverse_bits(int("110001", 2)) == int("100011", 2)
