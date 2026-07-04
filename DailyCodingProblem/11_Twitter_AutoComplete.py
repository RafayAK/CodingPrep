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
        return self._wordDict.get("de")


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.word = None



class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for character in word:
            if character not in node.children:
                node.children[character] = TrieNode()
            node = node.children[character]
        node.is_end = True
        node.word = word

    def _collect_words(self, node: TrieNode, result: list[str]):
        if node.is_end:
            result.append(node.word)

        for child in node.children.values():
            self._collect_words(child, result)


    def search_prefix(self, prefix: str) -> list[str]:
        node = self.root
        for character in prefix:
            node = node.children[character]

        result = []
        self._collect_words(node, result)
        return result




def get_autocomplete(s: str, a: list[str]) -> list[str]:
    """Auto complete function
    Args:
        s (str): query string
        a (list[str]): all possible query strings

    Returns:
        list[str]: set of all possible query strings
    """

    trie = Trie()
    for word in a:
        trie.insert(word)
    return trie.search_prefix(s)


if __name__ == '__main__':
    auto = autocomplete()
    auto.addWord('dog')
    auto.addWord('deer')
    auto.addWord('deal')

    res = auto.query('de')
    print(res)


    print(get_autocomplete("de", ["dog", "deer", "deal"]))