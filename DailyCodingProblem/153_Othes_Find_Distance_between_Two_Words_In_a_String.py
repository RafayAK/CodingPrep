"""
Find an efficient algorithm to find the smallest distance
(measured in number of words) between any two given words in a string.

For example, given words "hello", and "world" and a text content of
"dog cat hello cat dog dog hello cat world", return 1 because there's only one word "cat" in between the two words.
"""

def find_distance(string:str, key_word_1, key_word_2):
    min_count = float('inf')
    count = 0
    ending_key_word = None
    for word in string.split():
        if ending_key_word is None and word == key_word_1:
            ending_key_word = key_word_2
        elif ending_key_word is None and word == key_word_2:
            ending_key_word = key_word_1
        elif ending_key_word == word:
            min_count = min(count, min_count)
            ending_key_word = key_word_2 if key_word_1 == word else key_word_1
            count = 0
        elif word == key_word_1 or word == key_word_2:
            count = 0
        elif ending_key_word:
            count+=1

    return min_count


if __name__ == '__main__':
    test_string = "dog cat hello cat dog dog hello cat world"
    print(find_distance(test_string, 'hello', 'world'))  # ans 1

    test_string = "dog cat hello cat dog dog dog cat world cat world dog dog hello"
    print(find_distance(test_string, 'hello', 'world'))  # ans 2