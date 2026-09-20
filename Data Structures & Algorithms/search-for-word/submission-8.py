class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        m = len(board)
        n = len(board[0])
        W = len(word)

        # base case: if cell is size 1
        if m == 1 and n == 1:
            return board[0][0] == word

        # run back track algorithm on current cell
        def backtrack(pos, index):
            i, j = pos

            # check if its match
            if W == index:
                return True

            # letter is not valid
            if board[i][j] != word[index]:
                return False

            temp = board[i][j]
            board[i][j] = "#"

            # check all adjacent cells (right, down, left, up)
            for i_off, j_off in [(0,1),(1,0),(0,-1),(-1,0)]:
                r, c = i + i_off, j + j_off
                if 0 <= r < m and 0 <= c < n:
                    if backtrack((r, c), index + 1):
                        return True

            # undo the action
            board[i][j] = temp
            return False



        for i in range(m):
            for j in range(n):
                if backtrack((i, j), 0):
                    return True

        return False