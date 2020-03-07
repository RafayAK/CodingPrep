"""
This problem was asked by Google.

Find the minimum number of coins required to make n cents.

You can use standard American denominations, that is, 1¢, 5¢, 10¢, and 25¢.

For example, given n = 16, return 3 since we can make it with a 10¢, a 5¢, and a 1¢.
"""

# classic dynamic programming problem

def _get_change_making_matrix(set_of_coins, total:int):
    # create a zeros matrix where rows go from 0->number_of_denominations and
    # cols go from 0->total+1
    mat = [[0 for _ in range(total+1)] for _ in range(len(set_of_coins)+1)]

    # for the zero'th row set all number of coins from sum of 1 to total to "infinity"
    # there is no way of making change with a zero denomination
    for i in range(1, total+1):
        mat[0][i] = float('inf')

    return mat


def _get_coins_from_mat(mat, n, denominations):
    rows = len(mat)
    cols = len(mat[0])
    coins = []
    curr_row, curr_col = rows-1, cols-1
    while n != 0:
        if mat[curr_row][curr_col] == mat[curr_row-1][curr_col]:
            curr_row -=1
        else:
            n = n - denominations[curr_row-1]
            coins.append(denominations[curr_row-1])
            curr_col = n

    return coins




def min_coins_required(coins:list, n:int):
    # first create change making matrix
    mat = _get_change_making_matrix(coins, n)

    for c in range(1, len(coins)+1):
        for s in range(1, n+1):
            # if the current denomination matches the current sum that means only one coin required
            if coins[c-1] == s:
                mat[c][s] = 1

            # if current coin is greater than required sum use the number of coins from the previous coin's row
            # ie. take the value from the above row
            elif coins[c - 1] > s:
                mat[c][s] = mat[c-1][s]

            # Now we have two options, pick te min:
            # 1- use the result from the previous row to make this current sum, we will not use the current coin then
            #    i.e mat[c-1][s]
            # 2- Use the current coin and solution required to make current_sum - current_coin in the current matrix row
            #   i.e mat[c][s - coins[c-1]]
            else:
                mat[c][s] = min(mat[c-1][s], 1 + mat[c][s-coins[c-1]])

    print(_get_coins_from_mat(mat, n, coins))
    return mat[-1][-1]


if __name__ == '__main__':
    print(min_coins_required([1,5,10,25], 26))