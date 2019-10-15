"""
This problem was asked by Apple.

Suppose you have a multiplication table that is N by N.
That is, a 2D array where the value at the
i-th row and j-th column is (i + 1) * (j + 1) (if 0-indexed) or i * j (if 1-indexed).

Given integers N and X, write a function that returns the number of times X
appears as a value in an N by N multiplication table.

For example, given N = 6 and X = 12, you should return 4, since the multiplication table looks like this:

| 1 | 2  |  3   |  4   | 5  | 6 |

| 2 | 4  |  6   |  8   | 10 | 12 |

| 3 | 6  |  9   |  12  | 15 | 18 |

| 4 | 8  |  12  |  16  | 20 | 24 |

| 5 | 10 |  15  |  20  | 25 | 30 |

| 6 | 12 |  18  |  24  | 30 | 36 |

And there are 4 12's in the table.
"""


def count_in_table(table_size, X):
    factors_found = set()
    count = 0

    if X == 1 or X == table_size*table_size:  # corner cases
        return 1

    for i in range(1, table_size+1):
        if i in factors_found:  # if already looked factors this number move on to the next number
            continue

        if X % i == 0 and X/i <= table_size:
            if i == X/i:  # if same factor eg 25 =5 *
                count += 1
            else:
                count += 2
            factors_found.add(i)
            factors_found.add(X/i)

    return count


if __name__ == '__main__':
    assert count_in_table(table_size=6, X=12) == 4
    assert count_in_table(table_size=6, X=2) == 2
    assert count_in_table(table_size=6, X=15) == 2
    assert count_in_table(table_size=6, X=36) == 1
    assert count_in_table(table_size=6, X=1) == 1
    assert count_in_table(table_size=6, X=25) == 1
    assert count_in_table(table_size=6, X=20) == 2
