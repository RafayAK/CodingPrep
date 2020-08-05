"""
This problem was asked by Airbnb.

Given a list of words, find all pairs of unique indices such that the concatenation of the two words is a palindrome.

For example, given the list ["code", "edoc", "da", "d"], return [(0, 1), (1, 0), (2, 3)].
"""

# This is a O(n^2) solution
def find_pairs_of_palindrome(arr):
    indices = []
    for i in range(len(arr)):
        for j in range(len(arr)):
            if j == i:
                continue  # don't try to match the word with itsef
            word = arr[i] + arr[j]
            if word == word[::-1]:
                indices.append((i, j))

    return indices


if __name__ == '__main__':
    print(find_pairs_of_palindrome(["code", "edoc", "da", "d"]))
