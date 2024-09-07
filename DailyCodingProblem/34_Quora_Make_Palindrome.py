"""
Given a string, find the palindrome that can be made by inserting the fewest number of
characters as possible anywhere in the word. If there is more than one palindrome of
 minimum length that can be made, return the lexicographically earliest one (the first one alphabetically).

For example, given the string "race", you should return "ecarace", since we
can add three letters to it (which is the smallest amount to make a palindrome).
There are seven other palindromes that can be made from "race" by adding three letters,
 but "ecarace" comes first alphabetically.

As another example, given the string "google", you should return "elgoogle".
"""


def check_palindrome(string:str):
    len_str = len(string)

    # to check palindrome only need to
    # check:
    # 1- for even length string (len_str/2)  the string
    # 2- for odd length string (len_str//2)

    str_end_idx = -1
    for i in range(0, len_str//2):
        # now check for matching char at corresponding ends of string
        if string[i] != string[str_end_idx - i]:
            return False

    return True


def make_palindrome(string, add_chars="", list_end=-1):
    if check_palindrome(add_chars+string):
        return add_chars+string

    # not palindrome so append chars to the start of the list to make
    # palindrome
    return make_palindrome(string, add_chars+string[list_end], list_end-1)




if __name__ == '__main__':
    # print(check_palindrome('aba'))  # True
    # print(check_palindrome('race'))  # False
    # print(check_palindrome('abba'))  # True

    # print(make_palindrome('race'))
    # print(make_palindrome('google'))
    print(make_palindrome('quora'))