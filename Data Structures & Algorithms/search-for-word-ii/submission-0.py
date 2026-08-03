class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        # Key Data Structure: Trie + Backtracking

        # build trie from all words
        trie = {}
        for word in words:
            node = trie
            for letter in word:
                node = node.setdefault(letter, {})
            node['.'] = word  # store word at end node for easy retrieval

        rowNum = len(board)
        colNum = len(board[0])
        matchedWords = []

        def backtracking(row, col, parent):
            letter = board[row][col]
            currNode = parent[letter]

            # pop '.' marker — removes it to prevent duplicate matches
            word_match = currNode.pop('.', False)
            if word_match:
                matchedWords.append(word_match)

            board[row][col] = '#'  # mark cell as visited

            for rowOffset, colOffset in [(-1,0), (1,0), (0,-1), (0,1)]:
                newRow, newCol = row + rowOffset, col + colOffset
                if 0 <= newRow < rowNum and 0 <= newCol < colNum:
                    if board[newRow][newCol] in currNode:
                        backtracking(newRow, newCol, currNode)

            board[row][col] = letter  # restore cell (backtrack)

            # prune trie — remove empty nodes to speed up future searches
            if not currNode:
                parent.pop(letter)

        for row in range(rowNum):
            for col in range(colNum):
                if board[row][col] in trie:
                    backtracking(row, col, trie)

        return matchedWords

        # Time Complexity:  O(M × 4 × 3^(L-1)) — M=board cells, L=max word length
        # Space Complexity: O(N) — N=total characters across all words in trie