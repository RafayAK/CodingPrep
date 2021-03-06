"""
This problem was asked by Google.

Given a string, split it into as few strings as possible such that each string is a palindrome.

For example, given the input string racecarannakayak, return ["racecar", "anna", "kayak"].

Given the input string abc, return ["a", "b", "c"].
"""


# The max number of palindromes can  would be the length of the
# string itself if no palindromes are found
# Min palindrome can be 1 if th string itself is a palindrome.

# start with all letters are palindrome and try reducing them.


def return_min_palindromes(s):
    palindromes = []

    is_palindrome = lambda x: x == x[::-1]

    def helper(string, left_over=""):

        if len(string) == 0:
            return

        if is_palindrome(string):
            palindromes.append(string)
            helper(left_over, "")
        else:
           helper(string[:-1], string[-1] + left_over)


    helper(s)
    return palindromes


if __name__ == '__main__':
    print(return_min_palindromes('abc'))
    print(return_min_palindromes('racecarannakayak'))
    print(return_min_palindromes('abaana'))
    print(return_min_palindromes('abaaba'))
