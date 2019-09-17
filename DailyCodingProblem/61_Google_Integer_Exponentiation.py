"""
This problem was asked by Google.

Implement integer exponentiation.
That is, implement the pow(x, y) function, where x and y are integers and returns x^y.

Do this faster than the naive method of repeated multiplication.

For example, pow(2, 10) should return 1024.
"""

memo_table = {}  # dictionary for memoization


def pow(number, exponent):

    # if we've already calculated this exponent then just return that
    if (number, exponent) in memo_table:
        return memo_table[(number, exponent)]

    if exponent == 1:
        memo_table[(number, exponent)] = number
        return memo_table[number, exponent]
    if exponent == 0:
        memo_table[(number, exponent)] = 1
        return memo_table[(number, exponent)]

    if exponent == 2:
        # just a square of the number
        memo_table[(number, exponent)] = number*number
        return memo_table[(number, exponent)]

    if exponent % 2 == 0:
        # divisible by 2 so can be separated into equal sized groups
        memo_table[(number, exponent)] = pow(number, exponent//2) * pow(number, exponent//2)
        return memo_table[(number, exponent)]
    else:
        # can't be equally divided into groups
        memo_table[(number, exponent)] = pow(number, exponent//2) * pow(number, exponent//2) * number
        return memo_table[(number, exponent)]

    


if __name__ == '__main__':
    print(pow(2, 10))
    print(pow(3, 20))
    print(pow(15, 15))
    print(pow(15,0))