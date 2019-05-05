"""
This problem was asked by Palantir.

Write an algorithm to justify text. Given a sequence of words and an integer line length k,
return a list of strings which represents each line, fully justified.

More specifically, you should have as many words as possible in each line.
There should be at least one space between each word. Pad extra spaces when necessary
so that each line has exactly length k. Spaces should be distributed as equally as possible,
with the extra spaces, if any, distributed starting from the left.

If you can only fit one word on a line, then you should pad the right-hand side with spaces.

Each word is guaranteed not to be longer than k.

For example, given the list of words ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
and k = 16, you should return the following:

["the  quick brown", # 1 extra space on the left
"fox  jumps  over", # 2 extra spaces distributed evenly
"the   lazy   dog"] # 4 extra spaces distributed evenly
"""


# this helper method find a list of words that fit on to a line
# by costructing sectences with normal spacing i.e 1 space b/w
# two words
# eg. current_sentence = "the quick brown"
# returns :
#   - word_list eg.[the, quick, brown]
#   - counter -> counts how many words we could fit in a line with normal spacing
#
def get_words_for_line(words, word_list, max_line_length, counter=0, current_sentence=""):
    if len(current_sentence) == max_line_length or len(words)==0:
        return word_list, counter

    # counter < len(words) -> make sure we don't access illegal values beyond list length
    # len(current_sentence) + len(words[counter]) + 1 <= max_line_length -> make we are not exceeding line length
    if counter < len(words) and len(current_sentence) + len(words[counter]) + 1 <= max_line_length:
        return get_words_for_line(words, word_list+[words[counter]], max_line_length, counter + 1, " ".join(words[:counter + 1]))
    else:
        return word_list, counter


# this helper method decides how much space to put
# b/w two words when constructing a line
# returns a fully formed sentence with requisite spaces
def put_spaces(words, num_of_words, max_line_length):

    # find number of empty spaces
    # if words =[the, quick, brown]
    # ''.join(words) -> thequickbrown
    num_of_empty_spaces = max_line_length - len(''.join(words))

    # if only one word on the line
    if num_of_words ==1: # simply left justify it and fill remaining spots on the right with spaces
        return words[0]+(num_of_empty_spaces*" ")

    avg_space = num_of_empty_spaces//(num_of_words-1)  # average space b/w two words
    extras = num_of_empty_spaces/float(num_of_words-1)  # extra spot left, shown by decimal overflow

    # create line
    sentence = ""
    for i in range(len(words)-1):
        sentence = sentence + words[i]
        if i == 0 and extras > avg_space:  # only for the first word
            sentence = sentence + " "
        sentence = sentence + (avg_space * " ")

    sentence = sentence+ words[-1]

    return sentence



def justify_text(words, max_line_length):
    sentences = []

    while words:
        sentence, n= get_words_for_line(words, [], max_line_length)
        sentence = put_spaces(sentence, n,max_line_length)
        words = words[n:] # remove words taken up by the sentence just formed
        sentences.append(sentence)

    return sentences


if __name__ == '__main__':
    # words = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
    words = ["the"]
    print(justify_text(words, 16))