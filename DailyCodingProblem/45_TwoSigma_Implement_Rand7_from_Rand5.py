"""
This problem was asked by Two Sigma.

Using a function rand5() that returns an integer from 1 to 5 (inclusive)
with uniform probability, implement a function rand7() that returns an integer from 1 to 7 (inclusive).
"""
import random

# trying out new way to write a loop
# https://twitter.com/raymondh/status/1144527183341375488
from itertools import repeat
from functools import partial

random.seed(1)

"""

   _1__2__3__4__5__                     _1__2__3__4__5__
5 | 6  7  8  9  10                   5 | 1  2  3  4  5   
10| 11 12 13 14 15       -5          10| 6  7  8  9  10
15| 16 17 18 19 20      =====>       15| 11 12 13 14 15
20| 21 22 23 24 25                   20| 16 17 18 19 20    
25| 26 27 28 29 30                   25| 21 22 23 24 25 

now if we take %7:


             _1__2__3__4__5__
          5 | 1  2  3  4  5   
          10| 6  0  1  2  3
  %7      15| 4  5  6  0  1
 =====>   20| 2  3  4  5  6  
          25| 0  1  2  3  4   # if we remove the last 4 elements form the last rwo than
                                all the remaining number will be of uniform probability

            _1__2__3__4__5__
         5 | 2  3  4  5  6  
+1       10| 7  1  2  3  4      
====>    15| 5  6  7  1  2     ====> Now all the numbers [1-7] with uniform probability
         20| 3  4  5  6  7  
         25| 1  X  X  X  X  


"""


def rand5():
    return random.randint(1, 5)


def rand7():
    sum = 5*rand5() + rand5() - 5  # generates uniform random numbers from [1-25]

    if sum < 22: # ie. remove the last 4 elements
        return sum % 7 + 1
    else:
        return rand7() # try again




if __name__ == '__main__':
    #print([rand5() for _ in repeat(None, 5)])

    times = partial(repeat, None)  # hiding the superfluous None arg
    # experiment
    results_dic = dict()
    num_experiments = 100000
    for _ in times(num_experiments):
        num = rand7()
        if num not in results_dic:
            results_dic[num] = 0

        results_dic[num] += 1

    desired_prob = 1/7
    for number in results_dic:
        results_dic[number] = results_dic[number] / num_experiments
        print("Probability of {0}: {1:.2f} ----- Desired Probability:{2:.2f}".format(number, results_dic[number], desired_prob))
        assert round(desired_prob, 2) == round(results_dic[number],2)