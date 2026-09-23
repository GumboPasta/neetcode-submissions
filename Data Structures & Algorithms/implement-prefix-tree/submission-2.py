class PrefixTree:

    def __init__(self):
        self.trie = {}
        

    def insert(self, word: str) -> None:
        d = self.trie

        for character in word:
            # check current level
            if character not in d:
                d[character] = {}
            d = d[character]

        # need to label the last with a indicator to show its a word
        d['.'] = '.'

    def search(self, word: str) -> bool:
        d = self.trie

        for character in word:
            if character not in d:
                return False
            d = d[character]

        return True if '.' in d else False
        

    def startsWith(self, prefix: str) -> bool:
        d = self.trie

        for character in prefix:
            if character not in d:
                return False
            d = d[character]

        return True
        
        