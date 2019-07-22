"""
This problem was asked by Facebook.

Given a function that generates perfectly random numbers between 1 and k (inclusive),
where k is an input, write a function that shuffles a deck of cards represented as an array using only swaps.

It should run in O(N) time.

Hint: Make sure each one of the 52! permutations of the deck is equally likely.
"""


from random import randint


def generate_random_num(k):
    return randint(1, k)


def shuffle_deck():
    cards = [i for i in range(52)]

    # shuffle
    for old_card_pos in range(52):
        new_card_position = generate_random_num(52 - old_card_pos) -1  # now the range is [0, k-1],
        # need to change the range as the array of cards starts from zero and goes to 51
        #swap
        cards[old_card_pos], cards[new_card_position] = cards[new_card_position], cards[old_card_pos]

    return cards


if __name__ == '__main__':
    # cards = shuffle_deck()
    # print(cards)
    # print(len(cards))

    # check all the cards are present in 52 shuffles
    assert all(x in shuffle_deck() for x in range(52))



