"""
Find an efficient algorithm to find the smallest distance
(measured in number of words) between any two given words in a string.

For example, given words "hello", and "world" and a text content of
"dog cat hello cat dog dog hello cat world", return 1 because there's only one word "cat" in between the two words.
"""

def find_distance(string:str, key_word_1, key_word_2):
    """
    This works as follows:
    eg. key_word_1 = hello; key_word_1 = world
                     "dog     cat    hello    cat     dog     dog     hello       cat         world"
                     -------------------------------------------------------------------------------
               count|  0       0       0       1       2       3        0         1             0
    ending_key_word |  None  None    world    world  world   world    world     world          hello
          min_count |  inf    inf     inf     inf    inf     inf      inf       inf             1
    Args:
        string:
        key_word_1:
        key_word_2:

    Returns:

    """
    min_count = float('inf')
    count = 0
    ending_key_word = None  # initially we don't know which keyword we are looking to end the count
    for word in string.split():
        if ending_key_word is None and word == key_word_1:  # check if we should start counting
            ending_key_word = key_word_2  # look for key_word_2 to stop count
        elif ending_key_word is None and word == key_word_2:
            ending_key_word = key_word_1  # look for key_word_1 to stop the count
        elif ending_key_word == word: # when the ending keyword has been found
            min_count = min(count, min_count)  # store the min count
            # now we if the the ending_key_word was:
            #  a - key_word_1 we will now set ending_key_word=key_word_2
            #  b - key_word_2 we will now set ending_key_word=key_word_1
            ending_key_word = key_word_2 if key_word_1 == word else key_word_1
            count = 0  # reset count
        elif word == key_word_1 or word == key_word_2:
            count = 0  # reset count found a word that is possibly closer
        elif ending_key_word:
            count += 1  # while we are looking for end_key_word keep counting words

    return min_count


if __name__ == '__main__':
    test_string = "dog cat hello cat dog dog hello cat world"
    print(find_distance(test_string, 'hello', 'world'))  # ans 1

    test_string = "dog cat hello cat dog dog dog cat world cat world dog dog hello"
    print(find_distance(test_string, 'hello', 'world'))  # ans 2