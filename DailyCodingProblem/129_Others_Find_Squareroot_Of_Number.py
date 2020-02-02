"""
Given a real number n, find the square root of n. For example, given n = 9, return 3.

"""


def get_square_root(num, error= 0.00001):
    # binary search over the possible range:
    # -> if guess is high move 'hi' down to guess
    # -> if guess is low move 'lo' up to guess

    lo, hi = 0, num

    guess = (lo + hi) / 2.0

    while abs(guess**2 - num) >= error:
        if guess ** 2 > num:
            hi = guess
        else:
            lo = guess

        guess = (lo + hi) / 2.0

    return guess



if __name__ == '__main__':
    print(get_square_root(9))

