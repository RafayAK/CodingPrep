"""
This problem was asked by Microsoft.

You have n fair coins and you flip them all at the same time. Any that come up tails you set aside. The ones that come
up heads you flip again. How many rounds do you expect to play before only one coin remains?

Write a function that, given n, returns the number of rounds you'd expect to play until one coin remains.
"""


# There is a probability that after each round the number of conis remainning will be halved

def rounds_until_one(coins):
    if coins <= 0:
        return None

    if coins == 1:
        print("     {0} coins on round {1}".format(coins, 0))
        return 0

    round_number = rounds_until_one(coins//2) + 1
    print("     {0} coins on round {1}".format(coins, round_number))
    return round_number



if __name__ == '__main__':
    coins = [4, 100, 50, 25, 0, -1]

    for c in coins:
        print("Number of rounds played: {}".format(rounds_until_one(c)))

