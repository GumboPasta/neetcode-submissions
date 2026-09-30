class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        # populate our trie
        word_map = {}
        res = []

        m, n = len(board), len(board[0])

        for word in words:
            # start at the root
            d = word_map
            for c in word:
                if c not in d:
                    d[c] = {}
                d = d[c]
            d['.'] = word

        def backtrack(i, j, node):

            # we reached our condition
            matched_word = node.pop('.', False)
            if matched_word:
                res.append(matched_word)

            # set current cell to invalid
            temp = board[i][j]
            board[i][j] = '#'
            
            # check the neighbors
            for i_offset, j_offset in [(0,1),(1,0),(0,-1),(-1,0)]:
                row, col = i + i_offset, j + j_offset
                if 0 <= row < m and 0 <= col < n:
                    if board[row][col] in node:
                        backtrack(row, col, node[board[row][col]])

            # undue our decision
            board[i][j] = temp

        for i in range(m):
            for j in range(n):
                if board[i][j] in word_map:
                    character = board[i][j]
                    backtrack(i, j, word_map[character])

        return res
