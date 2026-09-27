class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        word_map = {}
        matched_words = []
        m, n = len(board), len(board[0])

        # propagate the trie
        for word in words:
            d = word_map
            for c in word:
                if c not in d:
                    d[c] = {}
                d = d[c]
            # store the word, to pop later
            d["."] = word

        # backtrack through the board
        def backtrack(pos, node, index):

            # obtains position and current word index
            i, j = pos
            letter = board[i][j]
            currNode = node[letter]

            # base case: if we found the word
            word_matched = currNode.pop(".", False)
            if word_matched:
                matched_words.append(word_matched)

            # set it visited
            temp = board[i][j]
            board[i][j] = "#"

            # check the neighbors
            for i_off, j_off in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                row, col = i + i_off, j + j_off
                if 0 <= row < m and 0 <= col < n and board[row][col] in currNode:
                    backtrack((row, col), currNode, index + 1)

            # undue our decision
            board[i][j] = temp

        for i in range(m):
            for j in range(n):
                # check if current cell is valid
                if board[i][j] in word_map:
                    backtrack((i, j), word_map, i)

        return matched_words
