class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        d = self.trie

        for c in word:
            if c not in d:
                d[c] = {}
            d = d[c]
        d['.'] = '.'

    def search(self, word: str) -> bool:

        def dfs(node, i):
            if i == len(word):
                return '.' in node

            c = word[i]

            if c == '.':
                for child in node:
                    if child != '.' and dfs(node[child], i + 1):
                        return True
                return False

            else:
                if c not in node:
                    return False
                return dfs(node[c], i + 1)

        return dfs(self.trie, 0)