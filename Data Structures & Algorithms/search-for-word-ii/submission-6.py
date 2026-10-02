class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        m, n = len(board), len(board[0])
        word_map = {}
        res = []

        # populate the trie
        for word in words:
            # start from the root
            d = word_map
            for c in word:
                if c not in d:
                    d[c] = {}
                d = d[c]
            d['.'] = word

        def backtrack(i, j, node):

            # obtain the current character and go down the trie
            character = board[i][j]
            currNode = node[character]

            # check if its the word
            word_match = currNode.pop('.', False)
            if word_match:
                res.append(word_match)

            # invalidate current cell
            temp = board[i][j]
            board[i][j] = "#"

            # check the neighbors
            for i_offset, j_offset in [(0,1),(1,0),(0,-1),(-1,0)]:
                row, col = i + i_offset, j + j_offset
                # apply border constraints
                if 0 <= row < m and 0 <= col < n and board[row][col] in currNode:
                    backtrack(row, col, currNode)

            
            # undue the decision
            board[i][j] = temp


        for i in range(m):
            for j in range(n):
                if board[i][j] in word_map:
                    backtrack(i, j, word_map)


        return res