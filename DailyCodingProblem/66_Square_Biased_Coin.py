"""
This problem was asked by Square.

Assume you have access to a function toss_biased() which returns 0 or 1
with a probability that's not 50-50 (but also not 0-100 or 100-0).
You do not know the bias of the coin.

Write a function to simulate an unbiased coin toss.
"""

import random


# biased_coin produces:
# 1 -> 70%
# 0 -> 30%
def biased_coin_flip():

    flip = 1 if random.random() <= 0.7 else 0
    return flip

def unbiased_coin_flip():

    coin_1 = biased_coin_flip()
    coin_2 = biased_coin_flip()

    if coin_1 == 0 and coin_2 == 1:
        return 0
    elif coin_1 == 1 and coin_2 == 0:
        return 1
    else:
        return unbiased_coin_flip()


def simulate(n=10000):

    biased_coin = {0 : 0, 1 : 0}
    unbiased_coin = {0 : 0, 1 : 0}

    # run simulation n times
    for _ in range(n):
        biased_coin[biased_coin_flip()]+=1
        unbiased_coin[unbiased_coin_flip()]+=1

    print("Probability of Biased coin:")
    print("\t P(T): {} \n\tP(H): {}".format(biased_coin[0]/n, biased_coin[1]/n))
    print("--------------------------------")

    print("Probability of Unbiased coin:")
    print("\t P(T): {} \n\tP(H): {}".format(unbiased_coin[0] / n, unbiased_coin[1] / n))


if __name__ == '__main__':
    simulate(n=10000)

