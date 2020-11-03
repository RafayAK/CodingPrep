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


if __name__ == '__main__':
    print(transform_sequence("dog", "cat", {"dog", "dot", "dat", "cat"}))
    print(transform_sequence("dog", "cat", {"tod", "dot", "dat", "dar"}))