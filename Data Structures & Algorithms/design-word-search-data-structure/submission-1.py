class WordDictionary:

    # Key Data Structure: Trie + DFS for wildcard matching

    def __init__(self):
        self.trie = {}  # nested dict trie, same as PrefixTree

    def addWord(self, word: str) -> None:
        d = self.trie

        for c in word:
            if c not in d:
                d[c] = {}   # create node if doesn't exist
            d = d[c]

        d['.'] = '.'        # end of word marker

    def search(self, word: str) -> bool:

        def dfs(node, i):
            if i == len(word):
                return '.' in node  # reached end — check for word marker

            c = word[i]

            if c == '.':
                # wildcard — try every child node at this level
                for child in node:
                    if child != '.' and dfs(node[child], i + 1):
                        return True  # found a match through this child
                return False

            else:
                # normal character — follow exact path
                if c not in node:
                    return False    # character not in trie
                return dfs(node[c], i + 1)

        return dfs(self.trie, 0)

        # Time Complexity:
        #   addWord:  O(n)      — n = word length
        #   search:   O(n)      — no wildcards, follows single path
        #             O(26^n)   — all wildcards worst case (tries every branch)
        # Space Complexity: O(total characters inserted)