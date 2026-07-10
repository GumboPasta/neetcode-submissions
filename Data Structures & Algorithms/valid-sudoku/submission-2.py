class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Key Data Structure: Hash Set

        rows = len(board)
        columns = len(board[0])

        # Check Each Row
        for i in range(rows):
            s = set()
            for j in range(columns):
                item = board[i][j]
                if item in s:
                    return False
                if item != '.':
                    s.add(item)

        # Check Each Column
        for i in range(rows):
            s = set()
            for j in range(columns):
                item = board[j][i]
                if item in s:
                    return False
                if item != '.':
                    s.add(item)

         # Validate Squares (Top Left of Each of Square)
        starts = [(0,0),(0,3),(0,6),
                  (3,0),(3,3),(3,6),
                  (6,0),(6,3),(6,6)]

        # Check Each Square
        for i,j in starts:
            s = set()
            for row in range(i,i+3):
                for col in range(j,j+3):
                    item = board[row][col]
                    if item in s:
                        return False
                    if item != '.':
                        s.add(item)

        return True

        # Time Complexity: O(n^2) 
        # Space Complexity: O(n) 


        