"""
This problem was asked by Square.

Given a string and a set of characters, return the shortest substring containing all the characters in the set.

For example, given the string "figehaeci" and the set of characters {a, e, i}, you should return "aeci".

If there is no substring containing all the characters in the set, return null.
"""

def get_shortest_str_with_all_chars(string, chars):
    if chars.issubset(set(string)):
        left = get_shortest_str_with_all_chars(string[1:], chars)
        right = get_shortest_str_with_all_chars(string[:-1], chars)

        if left and right:
            return left if len(left) < len(right) else right
        elif left:
            return left
        elif right:
            return right
        else:
            return string

    return None



if __name__ == '__main__':
    print(get_shortest_str_with_all_chars("figehaeci", {'a', 'e', 'i'}))
    print(get_shortest_str_with_all_chars("abccbbbccbcb", {'a', 'b', 'c'}))
    print(get_shortest_str_with_all_chars("abcdedbc", {'d', 'b', 'b'}))
    print(get_shortest_str_with_all_chars("abcdedbc", {'b', 'c'}))
    print(get_shortest_str_with_all_chars("abcdecdb", {'b', 'c'}))
    print(get_shortest_str_with_all_chars("abcdecdb", {'b', 'c', 'e'}))
    print(get_shortest_str_with_all_chars("abcdecdb", {'x', 'y', 'z'}))