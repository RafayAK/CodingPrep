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


# Basically, creates a window of increasing size to the right until the 'char' set is a subset of the 'temp_set'
# then, succescively reduces the window from the left until the char set is no longer part of temp_set, this is a
# candidate window for the shortest window, store location in "final_start and final_end". Try finding another window
# if possible, by setting "start" to the ending index of the previous window and "end" a step back to reset the window.
def get_shortest_str_redux(string, chars:set):
    final_start= None
    final_end = None

    start, end = 0, 0
    temp_set = set()
    while end < len(string):

        temp_set.add(string[end])

        if chars.issubset(temp_set):
            while chars.issubset(temp_set):
                temp_set.discard(string[start])
                start += 1
            start -= 1
            if final_end is None:
                final_start = start
                final_end = end
            elif final_end - final_start > end-start:
                final_start = start
                final_end = end

            start = end
            end -= 1
            temp_set = set()


        end += 1

    return string[final_start:final_end+1] if final_start is not None else None




if __name__ == '__main__':
    print(get_shortest_str_with_all_chars("figehaeci", {'a', 'e', 'i'}))
    print(get_shortest_str_with_all_chars("abccbbbccbcb", {'a', 'b', 'c'}))
    print(get_shortest_str_with_all_chars("abcdedbc", {'d', 'b', 'b'}))
    print(get_shortest_str_with_all_chars("abcdedbc", {'b', 'c'}))
    print(get_shortest_str_with_all_chars("abcdecdb", {'b', 'c'}))
    print(get_shortest_str_with_all_chars("abcdecdb", {'b', 'c', 'e'}))
    print(get_shortest_str_with_all_chars("abcdecdb", {'x', 'y', 'z'}))

    print('\n ---- \n')

    print(get_shortest_str_redux("figehaeci", {'a', 'e', 'i'}))
    print(get_shortest_str_redux("abccbbbccbcb", {'a', 'b', 'c'}))
    print(get_shortest_str_redux("abcdedbc", {'d', 'b', 'b'}))
    print(get_shortest_str_redux("abcdedbc", {'b', 'c'}))
    print(get_shortest_str_redux("abcdecdb", {'b', 'c'}))
    print(get_shortest_str_redux("abcdecdb", {'b', 'c', 'e'}))
    print(get_shortest_str_redux("abcdecdb", {'x', 'y', 'z'}))