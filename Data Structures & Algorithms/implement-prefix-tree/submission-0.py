class PrefixTree:

    # Key Data Structure: Trie (nested dictionaries)

    def __init__(self):
        self.trie = {}  # root of the trie — each key is a character, value is another dict

    def insert(self, word: str) -> None:
        d = self.trie  # start at root

        for c in word:
            if c not in d:
                d[c] = {}       # create new node for this character if it doesn't exist
            d = d[c]            # move down to the next level

        d['.'] = '.'            # end of word marker — '.' signals a complete word ends here

    def search(self, word: str) -> bool:
        d = self.trie  # start at root

        for c in word:
            if c not in d:
                return False    # character not found — word doesn't exist in trie
            d = d[c]            # move down to the next level

        return '.' in d         # only True if we landed on a complete word (not just a prefix)

    def startsWith(self, prefix: str) -> bool:
        d = self.trie  # start at root

        for c in prefix:
            if c not in d:
                return False    # prefix doesn't exist in trie
            d = d[c]            # move down to the next level

        return True             # reached end of prefix — at least one word starts with it
                                # (don't check for '.' — a prefix doesn't need to be a full word)

        # Time Complexity:  O(n) for all operations — n is the length of the word/prefix
        # Space Complexity: O(n) per insert — n nodes created in worst case (no shared prefix)