class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        # Key Data Structure: Trie + Backtracking

        # build trie from all words so we can search multiple words simultaneously
        trie = {}
        for word in words:
            node = trie          # reset pointer to root for each new word
            for letter in word:
                # move down one level, creating node if it doesn't exist
                node = node.setdefault(letter, {})
            node['.'] = word     # store full word string at end node for easy retrieval

        rowNum = len(board)
        colNum = len(board[0])
        matchedWords = []

        def backtracking(row, col, parent):
            letter = board[row][col]
            currNode = parent[letter]  # move into the trie node for this letter

            # check if a word ends here — pop removes it to prevent duplicate matches
            # if no '.' exists, pop returns False (default)
            word_match = currNode.pop('.', False)
            if word_match:
                matchedWords.append(word_match)

            board[row][col] = '#'  # mark cell as visited so we don't reuse it in this path

            # explore all 4 neighbours
            for rowOffset, colOffset in [(-1,0), (1,0), (0,-1), (0,1)]:
                newRow, newCol = row + rowOffset, col + colOffset
                if 0 <= newRow < rowNum and 0 <= newCol < colNum:
                    # only recurse if neighbour's letter exists in current trie node
                    if board[newRow][newCol] in currNode:
                        backtracking(newRow, newCol, currNode)

            board[row][col] = letter  # restore cell (backtrack) so other paths can use it

            # prune trie — if this node is now empty, remove it from parent
            # prevents revisiting dead branches in future searches
            if not currNode:
                parent.pop(letter)

        # try every cell as a potential starting point
        for row in range(rowNum):
            for col in range(colNum):
                # only start backtracking if this cell's letter is in trie root
                if board[row][col] in trie:
                    backtracking(row, col, trie)

        return matchedWords

        # Time Complexity:  O(M × 4 × 3^(L-1)) — M=board cells, L=max word length
        #                   4 directions for first step, 3 for rest (can't go back)
        # Space Complexity: O(N) — N=total characters across all words in trie