"""
This problem was asked by Facebook.

Given a start word, an end word, and a dictionary of valid words,
find the shortest transformation sequence from start to end such that only
one letter is changed at each step of the sequence, and each transformed word exists in the dictionary.
If there is no possible transformation, return null.
Each word in the dictionary have the same length as start and end and is lowercase.

For example, given start = "dog", end = "cat",
and dictionary = {"dot", "dop", "dat", "cat"}, return ["dog", "dot", "dat", "cat"].

Given start = "dog", end = "cat", and dictionary = {"dot", "tod", "dat", "dar"},
return null as there is no possible transformation from dog to cat.
"""

def letter_diff(word_a:str, word_b:str):
    diff = 0
    for i in range(len(word_a)):
        if word_a[i] != word_b[i]:
            diff += 1

    return diff


def transform_sequence(start:str, end:str, dictionary:set):
    sequence = [start]
    dict_iter = 0
    if start in dictionary:
        dictionary.discard(start)
    dict_list = list(dictionary)
    while dictionary:
        if dict_iter == len(dict_list):
            break
        if letter_diff(start, dict_list[dict_iter]) == 1:
            sequence.append(dict_list[dict_iter])
            dict_list.pop(dict_iter)
            start = sequence[-1]
            dict_iter = 0
        else:
            dict_iter +=1

    return sequence if start is end else None


# better solution more robust solution in O(n^2). Using breadth first traversal
from collections import deque
def transform_sequence_redux(start:str, end:str, dictionary:set):
    graph = deque()  # queue for storing breadth first search states
    alphabets = 'abcdefghijklmnopqrstuvwxyz'  # all the alphabets
    graph.append((start, [start]))

    while graph:
        curr_word, path = graph.popleft()
        if curr_word == end:
            return path

        # pick a candidate word and try to find an other candidate in the dictionary
        # by only changing one word
        for i in range(len(curr_word)):
            for alpha in alphabets:
                new_word = curr_word[: i] + alpha + curr_word[i+1:]
                if new_word in dictionary:
                    dictionary.remove(new_word)
                    graph.append((new_word, path+[new_word]))

    return None


if __name__ == '__main__':
    # print(transform_sequence("dog", "cat", {"dot", "dop", "dat", "cat"}))
    print(transform_sequence_redux("dog", "cat", {"dot", "tod", "dat", "dar"}))
    print(transform_sequence_redux("dog", "cat", {"dot", "dbg","dop", "dat", "cat"}))