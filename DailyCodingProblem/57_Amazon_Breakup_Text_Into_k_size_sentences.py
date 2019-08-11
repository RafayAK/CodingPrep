"""
This problem was asked by Amazon.

Given a string s and an integer k,
break up the string into multiple texts such that each text has a length of k or less.
You must break it up so that words don't break across lines.
If there's no way to break the text up, then return null.

You can assume that there are no spaces at the ends of the
 string and that there is exactly one space between each word.

For example, given the string "the quick brown fox jumps over the lazy dog" and k = 10,
you should return: ["the quick", "brown fox", "jumps over", "the lazy", "dog"].
No string in the list has a length of more than 10.
"""
def breakup_words(string:str):
    return string.split()

def check_valid_string(s, word, k):
    if len(s + word) > k:
        return False
    return True

def breakup_string(string, k):
    words = breakup_words(string)

    broken_text = []

    current_string = ""
    while words:
        w = words[0]
        if len(current_string) == 0:
            # empty sentence "current_string"
            if check_valid_string(current_string, w, k):
                current_string += w
                words = words[1:]
                # check if the string we added was the last one
                if not words:
                    broken_text.append(current_string)
            else:
                return None
        else:
            # sentence already contains a word
            if check_valid_string(current_string+" ", w, k):
                current_string += " " + w
                words = words[1:]
            else:
                # sentence length too long
                broken_text.append(current_string)
                current_string = ""  # reset current_string


    if len(words)>0:
        return None

    return broken_text


if __name__ == '__main__':
    string = "the quick brown fox jumps over the lazy dog"
    k = 10

    print(breakup_string(string, k))
    print(breakup_string("phantasmagoria", k))