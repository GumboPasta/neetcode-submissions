class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        # track the lengths
        m = len(board)
        n = len(board[0])
        W = len(word)
        res = []

        # edge case: single cell board
        if m == 1 and n == 1:
            return board[0][0] == word

        # helper function: to backtrack the grid
        def backtrack(r, c, index):
            
            # if we met the condition
            if W == index:
                return True

            # base case: if the letter does not match
            if board[r][c] != word[index]:
                return False
    
            res.append(board[r][c])
            temp = board[r][c]
            board[r][c] = "#"

            # recurse in the decision tree
            for i_off, j_off in [(0,1), (1,0), (0,-1), (-1,0)]:
                i = r + i_off
                j = c + j_off
                if 0 <= i < m and 0 <= j < n:
                    if backtrack(i, j, len(res)):
                        return True

            res.pop()
            board[r][c] = temp
            return False


        # run backtrack for each cell
        for i in range(m):
            for j in range(n):
                if backtrack(i, j, 0):
                    return True

        return False