"""
This problem was asked by Google.

Given a word W and a string S, find all starting indices in S which are anagrams of W.

For example, given that W is "ab", and S is "abxaba", return 0, 3, and 4.
"""
# check by looking against all valid permutations of the target string
def valid_perm(list_target, pattern, index=0):
    if "".join(list_target) == pattern:
        return True

    for i in range(index, len(list_target)):
        temp_list = list_target.copy()
        temp_list[index], temp_list[i] = temp_list[i], temp_list[index]
        if temp_list[0] == pattern[0] and valid_perm(temp_list, pattern, index+1):
            return True

    return False


def get_index_of_pattern(target, pattern):
    pattern_len = len(pattern)

    for i in range(0, len(target)):
        if len(target[i:i+pattern_len])==pattern_len and valid_perm(list(target[i:i+pattern_len]), pattern):
            print('Pattern found at index {}'.format(i))


# Better implementation
# idea: use a window size of the pattern length. Store a sum of ascii values of the pattern
# slide the window across the target string calculating the window ascii sum.

def get_index_of_pattern_redux(target, pattern):
    if len(target) < len(pattern):
        return 'Not Possible'

    pattern_ascii_sum = 0
    window_ascii_sum = 0
    pattern_len = len(pattern)

    # calculate the ascii sum of all chars in the pattern and the first window
    for i in range(pattern_len):
        pattern_ascii_sum += ord(pattern[i])
        window_ascii_sum += ord(target[i])

    #  check first window
    if window_ascii_sum == pattern_ascii_sum:
        print('Pattern found at index {}'.format(0))

    for i in range(1, len(target)):
        if len(target[i: i+pattern_len]) == pattern_len:
            # move window forward by subtracting last ascii value of last
            # element and adding ascii value of new leading element
            window_ascii_sum -= ord(target[i-1])
            window_ascii_sum += ord(target[i+pattern_len-1])
            if window_ascii_sum == pattern_ascii_sum:
                print('Pattern found at index {}'.format(i))


if __name__ == '__main__':
    get_index_of_pattern_redux('abxaba', 'ab')

