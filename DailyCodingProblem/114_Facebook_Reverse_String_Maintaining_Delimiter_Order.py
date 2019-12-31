"""
This problem was asked by Facebook.

Given a string and a set of delimiters,
reverse the words in the string while maintaining the relative order of the delimiters.
For example, given "hello/world:here", return "here/world:hello"

Follow-up: Does your solution work for the following cases: "hello/world:here/", "hello//world:here"
"""

import re

def reverse_str_maintain_delimiter(string):
    pattern = "[a-z]+"  # pattern to match all chars

    words = re.findall(pattern, string, flags=re.IGNORECASE)
    special_chars = re.split(pattern, string, flags=re.IGNORECASE)

    word_iter= len(words)-1
    new_string = ""

    for char in special_chars:
        new_string += char
        if word_iter >= 0:
            new_string+=words[word_iter]

        word_iter-=1

    return new_string

if __name__ == '__main__':
    print(reverse_str_maintain_delimiter("here/world:hello"))
    print(reverse_str_maintain_delimiter("hello/world:here/"))
    print(reverse_str_maintain_delimiter("hello//world:here"))
    print(reverse_str_maintain_delimiter("hello//world:hereJohn"))
