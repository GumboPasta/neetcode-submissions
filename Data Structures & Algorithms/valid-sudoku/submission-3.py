class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # Key Data Structure: Hash Set

        rows = len(board)
        columns = len(board[0])

        # Check the rows
        for i in range(rows):
            s = set()
            for j in range(columns):
                item = board[i][j]
                if item in s:
                    return False
                if item != '.':
                    s.add(item)

        # Check the columns
        for i in range(rows):
            s = set()
            for j in range(columns):
                item = board[j][i]
                if item in s:
                    return False
                if item != '.':
                    s.add(item)

        # Create a starts array with tuples (Left Corner of Board) (Row,Column)
        starts = [(0,0),(0,3),(0,6),
                 (3,0),(3,3),(3,6),
                 (6,0),(6,3),(6,6)]

        # Check each square
        for i,j in starts:
            s = set()
            # Iterate through each square
            for row in range(i,i+3):
                for col in range(j,j+3):
                    item = board[row][col]
                    if item in s:
                        return False
                    if item != '.':
                        s.add(item)
        
        return True
        