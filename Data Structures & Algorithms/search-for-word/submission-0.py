class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        # Key Data Structure: Backtracking (DFS on grid)

        m = len(board)
        n = len(board[0])
        W = len(word)

        # edge case: single cell board
        if m == 1 and n == 1:
            return board[0][0] == word

        def backtrack(pos, index):
            i, j = pos

            if index == W:
                return True  # matched all characters in word — found it!

            if board[i][j] != word[index]:
                return False  # current cell doesn't match current character — dead end

            # temporarily mark cell as visited so we don't reuse it in this path
            char = board[i][j]
            board[i][j] = '#'

            # explore all 4 neighbours (right, down, left, up)
            for i_off, j_off in [(0,1), (1,0), (0,-1), (-1,0)]:
                r, c = i + i_off, j + j_off
                if 0 <= r < m and 0 <= c < n:  # stay within grid bounds
                    if backtrack((r, c), index + 1):
                        return True  # found the word — propagate True up immediately

            # restore cell (backtrack) — unmark so other paths can use this cell
            board[i][j] = char
            return False

        # try starting the word from every cell in the grid
        for i in range(m):
            for j in range(n):
                if backtrack((i, j), 0):
                    return True

        return False  # word not found starting from any cell

        # Time Complexity:  O(m * n * 4^W) — try each cell as start, explore 4 directions W times
        # Space Complexity: O(W) — recursion stack depth equals word length