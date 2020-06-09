"""
This problem was asked by Google.

Given a string, return the first recurring character in it,
or null if there is no recurring character.

For example, given the string "acbbac", return "b".
Given the string "abcdef", return null.
"""


def first_recurring_char(string):
    char_to_freq_map = {}

    for char in string:
        if char not in char_to_freq_map:
            char_to_freq_map[char] = 0

        char_to_freq_map[char] +=1

        if char_to_freq_map[char] > 1:
            return char

    return None

if __name__ == '__main__':
    print(first_recurring_char("acbbac"))
    print(first_recurring_char("abcdef"))