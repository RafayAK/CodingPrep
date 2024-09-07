"""
This problem was asked by Dropbox.

Given a string s and a list of words words, where each word is the same length,
find all starting indices of substrings in s that is a concatenation of every word in words exactly once.

For example, given s = "dogcatcatcodecatdog" and words = ["cat", "dog"], return [0, 13],
 since "dogcat" starts at index 0 and "catdog" starts at index 13.

Given s = "barfoobazbitbyte" and words = ["dog", "cat"], return [] since there are no
 substrings composed of "dog" and "cat" in s.

The order of the indices does not matter.
"""

def get_indices(s:str, words:list):
    word_len = len(words[0])
    num_of_words = len(words)

    # create index,candidates substring pairs
    candidate_substrings = []
    for i in range(len(s)):
        if i + word_len*num_of_words <= len(s):
            candidate_substrings.append((i, s[i: i+word_len*num_of_words]))

    result = []
    for candidate in candidate_substrings:
        index, substr = candidate
        candi_word_set = set()
        for i in range(num_of_words):
            candi_word_set.add(substr[i*word_len: i*word_len + word_len])

        # skip if the words created are duplicates
        if len(candi_word_set) < num_of_words:
            continue

        # if union of set(words) U set(candi_words_set) == num of words then we've
        # found a match
        if len(set(words).union(candi_word_set)) == num_of_words:
            result.append(index)

    return result


if __name__ == '__main__':
    print(get_indices("barfoobazbitbyte", ['cat', "dog"]))

    print(get_indices("dogcatcatcodecatdog", ['cat', "dog"]))
