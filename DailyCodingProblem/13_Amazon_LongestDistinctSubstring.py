'''
This problem was asked by Amazon.

Given an integer k and a string s, find the length of the longest substring that
contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".

longest_substring('abcba', 2)  # longest substring with at most 2 distinct characters is 'bcb'
    3
longest_substring('edabccccdccba', 3)  # 'bccccdccb'
    9
'''

from collections import deque
# caterpillar method better implementation
def longest_substring(string, k):
    substring = deque()
    len_longest_substr = 0
    idx = 0

    if k == 0:
        return 0
    else:
        while idx < len(string):
            substring.append(string[idx])
            if len(set(substring)) == k:
                if len(substring) > len_longest_substr:
                    len_longest_substr = len(substring)
            elif len(set(substring)) > k:
                while len(set(substring)) > k:
                    substring.popleft()
            idx+=1
    return len_longest_substr

# recursive implementation pretty poor run-time though
def longest_substring_redux(string, k):
    def helper(char_list):
        if len(set(char_list)) == k:
            return char_list

        return max(helper(char_list[1:]), helper(char_list[:len(char_list)-1]), key=len)

    return "".join(helper([s for s in string]))


if __name__ == '__main__':
    string = 'edabccccdccba'
    print(longest_substring(string,3))
    print(longest_substring_redux(string, 3))