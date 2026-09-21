class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        trie = {}
        for word in words:
            node = trie
            for letter in word:
                node = node.setdefault(letter, {})
            node['.'] = word

        rowNum = len(board)
        colNum = len(board[0])
        matchedWords = []

        def backtracking(row, col, parent):
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
                        backtracking(newRow, newCol, currNode)

            board[row][col] = letter

            if not currNode:
                parent.pop(letter)

        for row in range(rowNum):
            for col in range(colNum):
                if board[row][col] in trie:
                    backtracking(row, col, trie)

        return matchedWords