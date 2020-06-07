"""
This problem was asked by Amazon.

Given a string, determine whether any permutation of it is a palindrome.

For example, "carrace" should return true, since it can be rearranged to
form "racecar", which is a palindrome. "daily" should return false, since there's no rearrangement that can form a palindrome.
"""


def permutes_to_palindrome(string):
    def char_to_frequency():
        freq_map = {}
        for char in string:
            if char not in freq_map:
                freq_map[char] = 0
            freq_map[char] += 1

        return freq_map

    def freq_in_multiples_of_2(freq_map):
        count = 0
        # at most only one char cannot have frequency in multiples of two

        for char, freq in frequency_map.items():
            if freq % 2 != 0:
                count += 1
                if count > 1:
                    return False

        return True

    frequency_map = char_to_frequency()

    return freq_in_multiples_of_2(frequency_map)


if __name__ == '__main__':
    print(permutes_to_palindrome("carrace"))  # True, c:2, a:2, r:2, e:1
    print(permutes_to_palindrome("daily"))   # False  d:1, a:1, i:1, l:1, y:1
    print(permutes_to_palindrome("jjjjje"))  # False j:5, e:5
    print(permutes_to_palindrome("jjjjjeecc"))  # True j:5, e:2, c:2







