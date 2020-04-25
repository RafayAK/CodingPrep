"""
This problem was asked by Triplebyte.

You are given n numbers as well as n probabilities that sum up to 1.
Write a function to generate one of the numbers with its corresponding probability.

For example, given the numbers [1, 2, 3, 4] and probabilities [0.1, 0.5, 0.2, 0.2],
your function should return 1 10% of the time, 2 50% of the time, and 3 and 4 20% of the time.

You can generate random numbers between 0 and 1 uniformly.
"""
# Idea:
#   1.Sort numbers in descending order according to probability:
#       eg [1, 2, 3, 4], [0.1, 0.5, 0.2, 0.2] ---sort---> [2, 3, 4, 1], [0.5, 0.2, 0.2, 0.1]
#   2. Since we can generate uniform random numbers b/w 0 and 1, use this to define when to output which number
#      eg After sorting:  1.0 - 0.5 = 0.5   --so--> if rand uniform > 0.5 output 2
#                         0.5 - 0.2 = 0.3   --so--> elif rand uniform > 0.3 output 3
#                         0.3 - 0.2 = 0.1    --so--> elif rand uniform > 0.1 output 4
#                         else output 1
#

import random
class NumGenerator:
    def __init__(self, numbers:list, probs:list):
        # first check sum of probs due to python number representation sum to 1.0 can hardly ever match so using
        # rounding of number s upto 5 decimal places to check.
        if round(sum(probs), 5) != 1.0:
            raise ValueError("Probabilities do not add up to 1.0!")

        numbers = [n for n, _ in sorted(zip(numbers, probs), key= lambda pair : pair[1], reverse=True)]
        probs = sorted(probs, reverse=True)
        # # create mapping_thresholds
        temp = 1.0
        self.mapping = {}
        for i in range(len(probs)):
            self.mapping[temp-probs[i]] = numbers[i]
            temp-=probs[i]



    def generate(self):
        uni_rand_num = random.uniform(0.0, 1.0)
        for thres in self.mapping:
            if uni_rand_num > thres:
                return self.mapping[thres]


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    probs =  [0.1, 0.5, 0.2, 0.2]
    test = NumGenerator(nums, probs)

    num_iterations = 100000

    values = {i:0 for i in nums}

    for j in range(num_iterations):
        values[test.generate()]+=1

    for k, v in values.items():
        print("{}: {:.2f}".format(k, v/num_iterations))

    print("---------")

    nums = [1, 2, 3, 4, 6]
    probs = [0.1, 0.3, 0.2, 0.2, 0.2]
    test = NumGenerator(nums, probs)

    num_iterations = 100000

    values = {i: 0 for i in nums}

    for j in range(num_iterations):
        a = test.generate()
        values[a] += 1

    for k, v in values.items():
        print("{}: {:.2f}".format(k, v / num_iterations))

    print("---------")

    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    probs = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
    test = NumGenerator(nums, probs)

    num_iterations = 100000

    values = {i: 0 for i in nums}

    for j in range(num_iterations):
        a = test.generate()
        values[a] += 1

    for k, v in values.items():
        print("{}: {:.2f}".format(k, v / num_iterations))
