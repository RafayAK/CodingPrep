"""
This problem was asked by Amazon.

Given a string, find the longest palindromic contiguous substring.
If there are more than one with the maximum length, return any one.

For example, the longest palindromic substring of "aabcdcb" is "bcdcb".
The longest palindromic substring of "bananas" is "anana".
"""

def check_palindrome(s):
    if len(s)==1:
        return True

    for i in range(len(s)//2):
        if s[i] != s[-1 - i]:
            return False

    return True


def find_longest_palindromic_substr(s):
    longest_substr = ""

    def recursive_helper(s, substr="", iter=0):
        nonlocal longest_substr  # to access variable from outer scope
        if iter >= len(s):
            return
        if check_palindrome(substr + s[iter]):
            if len(substr + s[iter]) > len(longest_substr):
                longest_substr = substr + s[iter]
            recursive_helper(s, substr+s[iter], iter+1)

        recursive_helper(s, substr + s[iter], iter+1)
        recursive_helper(s, s[iter], iter+1)


    recursive_helper(s)
    return longest_substr


# -----------------------------------------

# A much cleaner and simpler approach
def check_palindrome2(s):
    return s == s[::-1]


def find_longest_palindromic_substr2(s):
    if check_palindrome2(s):
        return s

    s1 = find_longest_palindromic_substr2(s[1:])
    s2 = find_longest_palindromic_substr2(s[:-1])

    return s1 if len(s1) > len(s2) else s2


if __name__ == "__main__":

    # print(find_longest_palindromic_substr('aabcdcb'))
    # print(find_longest_palindromic_substr('bananas'))
    # print(find_longest_palindromic_substr('johanna111222111'))

    # -------------------------
    print(find_longest_palindromic_substr2('aabcdcb'))
    print(find_longest_palindromic_substr2('bananas'))
    print(find_longest_palindromic_substr2('johanna111222111'))
