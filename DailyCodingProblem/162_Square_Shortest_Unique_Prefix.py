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


# better implementation using Trie data structures
class Node:
    def __init__(self, val=None):
        self.value = val  # Node value
        self.children = {}  # all children of this node, with letters as keys
        self.count = 0  # count of the number of times this letter appeared , root node's None implicitly part of every word's start
        self.is_complete = False  # denotes if the node represents a complete word

    def add_child(self, val):
        # First update counter of this node
        self.count += 1

        # then check if val does not exist as a child:
        if val not in self.children:
            # create it if it does not exist
            self.children[val] = Node(val)

        # return the child node
        return self.children[val]

    def __repr__(self):
        return "{}:{}".format(self.value, list(self.children.keys()))

class Trie:
    def __init__(self):
        self.root = Node()  # root node is empty

    def add_word(self, word):
        curr_node = self.root
        for letter in word:
            curr_node = curr_node.add_child(letter)

        curr_node.is_complete = True
        curr_node.count+=1 #

    def number_of_words(self):
        return self.root.count

    def unique_prefixes(self, word_list):
        unique_prefixes = []
        for word in word_list:
            prefix = ""
            curr_node = self.root
            for letter in word:
                prefix = prefix + letter
                curr_node = curr_node.children[letter]
                if curr_node.count == 1:
                    unique_prefixes.append(prefix)
                    break



        return unique_prefixes

def get_unique_prefixes_redux(words):
    my_trie = Trie()

    for word in words:
        my_trie.add_word(word)

    return my_trie.unique_prefixes(words)

if __name__ == '__main__':
    print(get_unique_prefixes(['dog', 'cat', 'apple', 'apricot', 'fish']))
    print(get_unique_prefixes(['dog', 'cat', 'apple', 'apricot', 'fish', 'car']))

    print(get_unique_prefixes_redux(['dog', 'cat', 'apple', 'apricot', 'fish']))
    print(get_unique_prefixes_redux(['dog', 'cat', 'apple', 'apricot', 'fish', 'car']))
