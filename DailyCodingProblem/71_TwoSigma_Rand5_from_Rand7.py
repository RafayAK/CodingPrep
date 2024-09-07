"""
Using a function rand7() that returns an integer from 1 to 7 (inclusive) with uniform probability,
implement a function rand5() that returns an integer from 1 to 5 (inclusive).
"""

# for logic see solution to daily coding problem # 45

import random

def rand7():
    return random.randint(1, 7)


def rand5():
    s = 7*rand7() + rand7() - 7

    if s > 45:
        return rand5()

    return s % 5 + 1


if __name__ == '__main__':
    num_of_experiments = 1000000

    rand7_results = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0}
    rand5_results = {1:0, 2:0, 3:0, 4:0, 5:0}

    for i in range(num_of_experiments):
        rand7_results[rand7()]+=1
        rand5_results[rand5()]+=1

    print("Results of rand7(): ")
    for key,value in rand7_results.items():
        print('{}: {}'.format(key, value/num_of_experiments))

    print('\n\nResults for rand5()')
    for key,value in rand5_results.items():
        print('{}: {}'.format(key, value/num_of_experiments))