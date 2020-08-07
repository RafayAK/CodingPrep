"""
This problem was asked by Airbnb.

Given a list of words, find all pairs of unique indices such that the concatenation of the two words is a palindrome.

For example, given the list ["code", "edoc", "da", "d"], return [(0, 1), (1, 0), (2, 3)].
"""

# This is a O(n^2*c) solution, where c is the length of the work to be reversed

is_palindrome = lambda word: word == word[::-1]


def find_pairs_of_palindrome(arr):
    indices = []
    for i in range(len(arr)):
        for j in range(len(arr)):
            if j == i:
                continue  # don't try to match the word with itself
            if is_palindrome(arr[i]+arr[j]):
                indices.append((i, j))

    return indices


# O(n*c^2) solution, so no longer dependent on number of words for performance
def find_pairs_of_palindromes_redux(arr):
    word_dict = {}
    for i, word in enumerate(arr):
        word_dict[word] = i

    result = []

    for i, word in enumerate(arr):
        for j in range(len(word)):
            prefix, postfix = word[:j], word[j:]

            reversed_prefix, reversed_postfix = prefix[::-1], postfix[::-1]

            if is_palindrome(prefix) and reversed_postfix in word_dict:
                if i != word_dict[reversed_postfix]:  # make sure not matching with the word itself
                    result.append((i, word_dict[reversed_postfix]))

            if is_palindrome(postfix) and reversed_prefix in word_dict:
                if i != word_dict[reversed_prefix]:  # make sure not matching with the word itself
                    result.append((i, word_dict[reversed_prefix]))

    return result


if __name__ == '__main__':
    print(find_pairs_of_palindrome(["code", "edoc", "da", "d"]))

    print(find_pairs_of_palindromes_redux(["code", "edoc", "da", "d"]))
