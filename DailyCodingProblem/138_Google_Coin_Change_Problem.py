"""
This problem was asked by Google.

Find the minimum number of coins required to make n cents.

You can use standard American denominations, that is, 1¢, 5¢, 10¢, and 25¢.

For example, given n = 16, return 3 since we can make it with a 10¢, a 5¢, and a 1¢.
"""

# classic memoization problem

memo_table = {1:1, 5:1, 10:1, 25:1}

def min_coins_required(n):
