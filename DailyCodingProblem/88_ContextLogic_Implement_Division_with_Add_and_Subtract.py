"""
This question was asked by ContextLogic.

Implement division of two positive integers without using the division, multiplication, or modulus operators.
Return the quotient as an integer, ignoring the remainder.
"""


def division_with_add(divisor, dividend):
    quotient = 0
    s = divisor # sum of divisors
    while s <= dividend:
        s+=divisor
        quotient+=1

    return quotient

if __name__ == "__main__":
    print(division_with_add(2, 4))
    print(division_with_add(2, 7))
    print(division_with_add(1, 1))
    print(division_with_add(7, 49))
    print(division_with_add(7, 45))
    print(division_with_add(7, 50))