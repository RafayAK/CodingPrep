"""
This problem was asked by Alibaba.

Given an even number (greater than 2), return two prime numbers whose sum will be equal to the given number.

A solution will always exist. See Goldbach’s conjecture.(https://en.wikipedia.org/wiki/Goldbach%27s_conjecture)

Example:

Input: 4
Output: 2 + 2 = 4
If there are more than one solution possible, return the lexicographically smaller solution.

If [a, b] is one solution with a <= b, and [c, d] is another solution with c <= d, then

[a, b] < [c, d]
If a < c OR a==c AND b < d.
"""


def primes(n):
    numbers = [True for _ in range(n+1)]

    p = 2
    while p*p < n:
        if numbers[p] == True:
            for i in range(p*p, n+1, p):
                numbers[i] = False

        p+=1

    list_of_primes = [i for i in range(2, n+1) if numbers[i] is True]
    return list_of_primes


def get_prime_sum(k):
    list_of_primes = primes(k)  # get a list of prime numbers

    # create two pointers at either end of the list
    left = 0
    right = len(list_of_primes) -1

    while list_of_primes[left] + list_of_primes[right] != k:
        if list_of_primes[left] + list_of_primes[right] > k:
            right-=1
        elif list_of_primes[left] + list_of_primes[right] < k:
            left+=1

    return list_of_primes[left], list_of_primes[right]


if __name__ == '__main__':
    print(get_prime_sum(30))
