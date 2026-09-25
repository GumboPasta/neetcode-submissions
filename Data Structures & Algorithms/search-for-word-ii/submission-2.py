class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        trie = {}
        for word in words:
            node = trie
            for letter in word:
                if letter not in node:
                    node[letter] = {}
                node = node[letter]
            node['.'] = word

        rowNum = len(board)
        colNum = len(board[0])
        matchedWords = []

        def backtrack(row, col, parent):
            letter = board[row][col]
            currNode = parent[letter]

            word_match = currNode.pop('.', False)
            if word_match:
                matchedWords.append(word_match)

            board[row][col] = '#'

            for rowOffset, colOffset in [(0,1),(1,0),(0,-1),(-1,0)]:
                newRow, newCol = row + rowOffset, col + colOffset
                if 0 <= newRow < rowNum and 0 <= newCol < colNum:
                    if board[newRow][newCol] in currNode:
                        backtrack(newRow, newCol, currNode)

            board[row][col] = letter

            if not currNode:
                parent.pop(letter)

        for i in range(rowNum):
            for j in range(colNum):
                if board[i][j] in trie:
                    backtrack(i, j, trie)

        return matchedWords