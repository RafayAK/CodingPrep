"""
This problem was asked by Microsoft.

A number is considered perfect if its digits sum up to exactly 10.

Given a positive integer n, return the n-th perfect number.

For example, given 1, you should return 19. Given 2, you should return 28.
"""

# the first perfect num is 19
# the second perfect num is 28
# the third +ive num is 37

# closer look reveals:
# n=1, 2,  3,  4,  5,  6,  7,  8, 9,  10,  11,   12
# -----------------------------------------------
#  19, 28, 37 46, 64, 46, 73, 82, 91, 100, 109, 118

# so 19+(n*9) eg first th digit is 19 = ((1+1)*9) +1 = 18+1
# i.e all multiples of 9 +1 form 2 onwards

# but there is one problem in this method 10th->100 number if not a perfect num
# 10th number should be the next one then 10th=>109
# so we'll also need to push 11th num to be the 12th num and so on

# note that the outliers of this method exist in form of {100, 199, 299,1000, 10000,etc all nums that don't sum to 10}
# before we return the result we need to adjust for the outliers:

# the result should be
# n= 1, 2,  3,  4,  5,  6,  7,  8, 9,  10,  11,   12
# -----------------------------------------------
#   19, 28, 37 46, 64, 46, 73, 82, 91, 109, 118, 127


def find_perfect_num(n):
    if n ==0:
        return 'nums start from 1'

    n_th_num = 19 # start with 19
    count = 0 # iterator

    while(True):
        curr_sum = sum(list(map(int, str(n_th_num))))

        if curr_sum ==10:
            count+=1

        if count == n:
            return n_th_num

        n_th_num += 9


if __name__ == '__main__':
    # print(find_perfect_num(1))
    # print(find_perfect_num(9))
    # print(find_perfect_num(11))
    # print(find_perfect_num(21))
    # print(find_perfect_num(91))
    # print(find_perfect_num(88))

    for i in range(1, 101):
        print("{}#: {}".format(i, find_perfect_num(i)))
