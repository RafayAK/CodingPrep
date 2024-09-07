'''
This problem was asked by Two Sigma.

Alice wants to join her school's Probability Student Club. Membership dues are computed via
one of two simple probabilistic games.

The first game: roll a die repeatedly. Stop rolling once you get a five followed by a six.
Your number of rolls is the amount you pay, in dollars.

The second game: same, except that the stopping condition is a five followed by a five.

Which of the two games should Alice elect to play? Does it even matter? Write a program to simulate the two games
and calculate their expected value.

'''


import random


def game(five_followed_by, trials=1000):

    def simulate_game():
        dice = [1, 2, 3, 4, 5, 6]
        last_roll = None
        amount_to_be_paid = 0
        while True:
            if last_roll is None:
                # means first roll
                last_roll = random.choice(dice)
                amount_to_be_paid+=1

            curr_roll = random.choice(dice)
            amount_to_be_paid+=1

            if last_roll == 5 and curr_roll == five_followed_by:
                break

            last_roll = curr_roll

        return amount_to_be_paid

    total_amount = 0
    for trial in range(trials):
        total_amount += simulate_game()

    return total_amount/trials


def simulate_both_games():
    number_of_trials = 100000
    # first game: 5 followed by 6
    expected_amount_1 = game(6, number_of_trials)

    # second game: 5 followed by 5
    expected_amount_2 = game(5, number_of_trials)

    print("Expected amount for played first game is: ${} based on {} trials".format(expected_amount_1, number_of_trials))
    print("Expected amount for played second game is: ${} based on {} trials".format(expected_amount_2, number_of_trials))


if __name__ == '__main__':
    simulate_both_games()

    # based on simulation of both the games for 100000 trials it seems that the expected value of
    # the first game (5 followed by 6) is lower then the second game (5 followed by 5). So, Alice
    # should elect to play the first game in hopes of a lower membership fee.
    # This mathematically makes sense, too.

    # Each out come 1-6 has a probability of 1/6 on each roll, but how the sequence of winning occurs
    # is different for the two games.

    # GAME ONE (5  followed by 6). Example if we already rolled a 5 in prev attempt
    # -> Prob of rolling a 5 = 1/6 => continue the sequence to hopefully roll a 6
    # -> Prob of rolling a 6 = 1/6 => win, end of game
    # -> Prob of restarting after rolling 1, 2 ,3 , or 4 = 4/6 = 2/3 = 66.7 % => chance we'll need to restart sequence

    # GAME TWO (5  followed by 5). Example if we already rolled a 5 in prev attempt
    # -> Prob of rolling a 5 = 1/6 => win, end of game
    # -> Prob of restarting after rolling 1, 2 ,3 , 4, or 6 = 4/6 = 5/6 = 83.3 % => chance we'll need to restart sequence
