"""
This problem was asked by Facebook.

There is an N by M matrix of zeroes.
Given N and M, write a function to count the number of ways of starting
at the top-left corner and getting to the bottom-right corner.
You can only move right or down.

For example, given a 2 by 2 matrix, you should return 2, since there are two ways to get to the bottom-right:

Right, then down
Down, then right
Given a 5 by 5 matrix, there are 70 ways to get to the bottom-right
"""

def count_ways(N, M, start_row=0, start_col=0):
    if start_row==N-1 and start_col==M-1:
        return 1

    if start_row<N-1 and start_col<M-1:
        # can go either Right or Down
        return count_ways(N,M,start_row+1, start_col) + count_ways(N,M,start_row, start_col+1)
    elif start_row<N-1:
        # can only go only Down
        return count_ways(N,M,start_row+1, start_col)
    else:
        # can only Right
        return count_ways(N, M, start_row, start_col+1)

if __name__ == '__main__':
    print(count_ways(5,5))