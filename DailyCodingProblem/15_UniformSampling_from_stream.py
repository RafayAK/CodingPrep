'''
This problem was asked by Facebook.

Given a stream of elements too large to store in memory, pick a random element from the stream with
uniform probability.


SOLUTION: Reservoir Sampling:
    probability of selecting the 1st element after seeing only one element 100%
    probability of selecting the 2nd element after seeing only two elements 1/2
    probability of selecting the 3rd element after seeing only three elements 1/3
    probability of selecting the 4th element after seeing only four elements 1/4
    probability of selecting the 5th element after seeing only five elements 1/5

    Proof uniform sampling
    so probability of selecting the 1st element after seeing five elements is:
    1 * (1 - 1/2) * (1 - 1/3) * (1 - 1/4) * (1 - 1/5)
  = 1 * 1/2 * 2/3 * 3/4 * 4/5 = 1/5
'''

import random
import matplotlib.pyplot as plt
import numpy as np

def uniform_sample(big_stream, printAction=True):
    random_element = None

    for index, element in enumerate(big_stream):

        if index == 0:
            if printAction:
                print("picked element {} from stream of {} elements".format(element, index + 1))
            random_element = element
        elif random.randint(1, index+1) == 1:
            if printAction:
                print("picked element {} from stream of {} elements".format(element, index + 1))
            random_element = element

    return random_element

def create_hist(big_stream, no_of_samples = 5000):
    hist = []

    for i in range(no_of_samples):
        hist.append(uniform_sample(big_stream, printAction=False))

    plt.hist(np.array(hist), align='left')
    plt.ylabel('Probability')
    plt.show()


if __name__ == '__main__':
    random.seed(1)
    big_stream = [1, 2, 3, 4, 5, 6]
    #print(uniform_sample(big_stream))
    create_hist(big_stream, no_of_samples=10000)