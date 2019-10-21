"""
This problem was asked by Google.

You are given an N by M 2D matrix of lowercase letters.
Determine the minimum number of columns that can be removed to ensure
that each row is ordered from top to bottom lexicographically.
That is, the letter at each column is lexicographically later as you go down each row.
 It does not matter whether each row itself is ordered lexicographically.

For example, given the following table:

cba
daf
ghi
This is not ordered because of the a in the center. We can remove the second column to make it ordered:

ca
df
gi
So your function should return 1, since we only needed to remove 1 column.

As another example, given the following table:

abcdef
Your function should return 0, since the rows are already ordered (there's only one row).

As another example, given the following table:

zyx
wvu
tsr
Your function should return 3, since we would need to remove all the columns to order it.
"""

def num_of_cols_to_remove(mat):
    n = len(mat)  # rows
    if n == 0 or n == 1:
        return 0
    m = len(mat[0])  # cols

    cols_removed = 0
    for col in range(m):
        prev_letter = None
        for row in range(n):
            if prev_letter is None:
                prev_letter = mat[row][col]
            elif prev_letter > mat[row][col]:
                cols_removed += 1
                break  # move on to the next col
            else:
                prev_letter = mat[row][col]

    return cols_removed

if __name__ == '__main__':
    print(num_of_cols_to_remove(["cba", "daf", "ghi"]))  # 1
    print(num_of_cols_to_remove(["abcdefg"]))  # 0
    print(num_of_cols_to_remove(["zyx", "wvu", "tsr"]))  # 3
    print(num_of_cols_to_remove([]))  # 0