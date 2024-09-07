"""
This problem was asked by Google.

Given a string which we can delete at most k, return whether you can make a palindrome.

For example, given 'waterrfetawx' and a k of 2, you could delete f and x to get 'waterretaw'.

"""


def make_palindrome(string, k):
    def helper(s, level=0):
        if s == s[::-1]:
            return s
        if level == k:
            return None

        valid_palindrome = None
        for i in range(len(s)):
            valid_palindrome = helper(s[:i] + s[i + 1:], level + 1)
            if valid_palindrome:
                return valid_palindrome

        return valid_palindrome

    return helper(string)

if __name__ == '__main__':
    print(make_palindrome("abbcda", k=2))
    print(make_palindrome("waterrfetawx", k=2))
    print(make_palindrome("a", 0))
    print(make_palindrome("aaa", 2))
    print(make_palindrome("add", 0))
    print(make_palindrome("waterrfetawx", 2))
    print(make_palindrome("waterrfetawx", 1))
    print(make_palindrome("waterrfetawx", 3))
    print(make_palindrome("malayalam", 0))
    print(make_palindrome("malayalam", 1))
    print(make_palindrome("asdf", 5))
    print(make_palindrome("asdf", 2))
