"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Given a positive integer n, find the smallest number of squared integers which sum to n.

For example, given n = 13, return 2 since 13 = 3^2 + 2^2 = 9 + 4.

Given n = 27, return 3 since 27 = 3^2 + 3^2 + 3^2 = 9 + 9 + 9.
"""


def squared_sum_to_n(n:int):
    num_list = []
    def helper(num, upto=None):
        guess = 0

        for guess in range(1, upto):
            if num - guess**2 < 0:
                break

        if guess - 1 == 0:
            num_list.clear()
            helper(num, upto-1)
        else:
            new_num = num - (guess -1)**2
            if new_num == 0:
                return
            num_list.append(guess-1)
            helper(new_num, new_num)

    helper(n, n)
    return num_list

if __name__ == "__main__":
    print(squared_sum_to_n(13))
    # print(squared_sum_to_n(3))
    print(squared_sum_to_n(27))