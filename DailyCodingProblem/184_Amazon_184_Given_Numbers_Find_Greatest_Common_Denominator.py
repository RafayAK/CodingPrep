"""
This problem was asked by Amazon.

Given n numbers, find the greatest common denominator between them.

For example, given the numbers [42, 56, 14], return 14.
"""

# Idea: for each number in the list generate a multiset of prime factors
# the intersection of all the multi-set of prime factors will be the
# greatest common divisor

# Counter is the closest default data-structure to a multiset in python
from collections import Counter


def generate_prime_factors(n):
    prime_factors = Counter()

    def helper(number, factor=2):
        if number == 1:
            return

        if number % factor == 0:
            prime_factors[factor] += 1
            number = number // factor
        else:
            factor += 1

        helper(number, factor)

    helper(n)
    return prime_factors



def get_greatest_common_divisor(l):
    list_of_multisets = []

    for number in l:
        list_of_multisets.append(generate_prime_factors(number))

    intersection = None
    for m in list_of_multisets:
        if intersection is None:
            intersection = m
        else:
            intersection = intersection & m

    if len(intersection) == 0:
        return 1
    else:
        gce = 1
        for factor, count in intersection.items():
            gce = gce * factor**count

        return gce


if __name__ == '__main__':
    assert get_greatest_common_divisor([14, 56, 42]) == 14
    assert get_greatest_common_divisor([5, 3, 17]) == 1
