"""
This problem was asked by Square.

Given a list of words, return the shortest unique prefix of each word. For example, given the list:

    dog
    cat
    apple
    apricot
    fish

Return the list:

    d
    c
    app
    apr
    f
"""


# rough idea
#
#   1st iter     2nd iter    3rd iter
#
#     d             d           d
#     c             c           c
#     a             ap          app
#     a             ap          apr
#     f             f           f
#

import itertools

def get_unique_prefixes(words):

    unique_prefixes = set()

    def all_unique_prefixes(prefix_dict):
        # this function adds unique prefixes to "unique_prefixes" set
        # and non-unique into "non_unique_prefixes" and returns them.
        non_unique_prefixes = {}

        for key, val in prefix_dict.items():
            if len(val) == 1:
                unique_prefixes.add(key)
            else:
                non_unique_prefixes[key] = val

        return non_unique_prefixes

    def helper(word_list, prefix_len=1):
        prefix_dict = {}
        for word in word_list:
            if word[:prefix_len] not in prefix_dict:
                prefix_dict[word[:prefix_len]] = []
            prefix_dict[word[:prefix_len]].append(word)

        non_unique_prefixes = all_unique_prefixes(prefix_dict)

        if len(non_unique_prefixes) > 0:
            # since simple dict.values() will return list of list in this case eg:
            # {a:[apple, apricot], c = [car, cat]}.values () = [[apple, apricot], [car, cat]]
            # we need to flatten this list of list, itertools.chain does that for us if we pass
            # it decompressed/unpacked(*) lists
            helper(list(itertools.chain(*non_unique_prefixes.values())), prefix_len=prefix_len+1)

    helper(words)

    return unique_prefixes


if __name__ == '__main__':
    print(get_unique_prefixes(['dog', 'cat', 'apple', 'apricot', 'fish']))
    print(get_unique_prefixes(['dog', 'cat', 'apple', 'apricot', 'fish', 'car']))

