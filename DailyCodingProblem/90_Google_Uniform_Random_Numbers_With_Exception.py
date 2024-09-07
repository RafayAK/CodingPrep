"""
This question was asked by Google.

Given an integer n and a list of integers l,
write a function that randomly generates a number from 0 to n-1 that isn't in l (uniform).
"""
import random
def get_random_not_in_list(n, l):
    # create list of acceptable values
    acceptable_list = [i for i in range(n) if i not in l]
    return random.choices(acceptable_list)[0] if len(acceptable_list) > 0 else None# choice by default prints

def run_experiment(n, l,num_times=1000):
    results = dict()

    for _ in range(num_times):
        rand_num = get_random_not_in_list(n, l)
        if rand_num not in results:
            results[rand_num] = 0
        results[rand_num] +=1

    # normalize the results
    for n in results:
        results[n] = results[n]/num_times

    print(results)


if __name__ == '__main__':
    get_random_not_in_list(5, [0, 1, 2, 3, 4])
    run_experiment(7, [0, 1, 5], 100000)

