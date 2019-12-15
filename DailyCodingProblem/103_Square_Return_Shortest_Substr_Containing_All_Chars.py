"""
This problem was asked by Square.

Given a string and a set of characters, return the shortest substring containing all the characters in the set.

For example, given the string "figehaeci" and the set of characters {a, e, i}, you should return "aeci".

If there is no substring containing all the characters in the set, return null.
"""

def get_shortest_str_with_all_chars(string, chars):
    # add all the chars to a set

    start, end = 0, len(string)

    while chars.issubset(set(string[start: end])):
        temp = set(string[start: end])
        start += 1

    while chars.issubset(set(string[start: end])):
        temp = set(string[start: end])
        end += -1



    return string[start-1: end]


if __name__ == '__main__':
    print(get_shortest_str_with_all_chars("figehaeci", {'a', 'e', 'i'}))
    print(get_shortest_str_with_all_chars("abccbbbccbcb", {'a', 'b', 'c'}))