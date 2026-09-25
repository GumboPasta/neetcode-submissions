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

        def dfs(node, index):

            if index == len(word):
                return True if '.' in node else False

            

            c = word[index]

            if c == '.':
                for child in node:
                    if child != '.' and dfs(node[child], index + 1):
                        return True
                return False
            else:
                if c not in node:
                    return False
                return dfs(node[c], index + 1)

        return dfs(self.trie, 0)
        
