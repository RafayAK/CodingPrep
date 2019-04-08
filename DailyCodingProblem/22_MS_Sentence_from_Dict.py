'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Microsoft.

Given a dictionary of words and a string made up of those words (no spaces),
return the original sentence in a list. If there is more than one possible reconstruction,
return any of them. If there is no possible reconstruction, then return null.

For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox",
you should return ['the', 'quick', 'brown', 'fox'].

Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string "bedbathandbeyond",
return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].
'''




def helper(vocab, string, sentence_list):

    if len(string) == 0:  # string empty => successfully created a sentence
        return sentence_list

    result = None

    for word in vocab:
        if string.startswith(word):
            result = helper(vocab, string[len(word):], sentence_list + [word])
            if result: # found a sentence so no need to check further
                break

    return result



def createSentence(vocab, string):
    return helper(vocab, string, [])





if __name__ == '__main__':
    print(createSentence(vocab=['quickly','quick', 'brown', 'the', 'fox'], string='thequicklybrownfox'))

    print(createSentence(vocab=['bed', 'bath', 'bedbath', 'and', 'beyond'], string='bedbathandbeyond'))

    print(createSentence(vocab=['Riccardo', 'Brigittie', 'and', 'lollipop'], string='RiccardoandBrigittie'))

    v = ["mobile", "samsung", "sam", "sung", "man", "mango","icecream", "and", "go", "i", "like", "ice", "cream"]
    print(createSentence(vocab=v, string='ilikesamsung'))
    print(createSentence(vocab=v, string='iiiiiiii'))
    print(createSentence(vocab=v, string='ilikelikeimangoiii'))
    print(createSentence(vocab=v, string='samsungandmango'))
    print(createSentence(vocab=v, string='samsungandmangok'))