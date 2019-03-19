'''
This problem was asked by Twitter.

Implement an autocomplete system. That is, given a query string s and a set of all possible query strings,
return all strings in the set that have s as a prefix.

For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.
'''


class autocomplete:
    def __init__(self):
        self._wordDict = dict()

    def addWord(self, word):
        for i in range(len(word)):
            if word[:i+1] in self._wordDict:
                self._wordDict[word[:i+1]].append(word)
            else:
                self._wordDict[word[:i+1]] = [word]
    def query(self,word):
        if word in self._wordDict:
            return self._wordDict[word]


if __name__ == '__main__':
    auto = autocomplete()
    auto.addWord('dog')
    auto.addWord('deer')
    auto.addWord('deal')

    res = auto.query('de')
    print(res)
