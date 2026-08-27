class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        # Key Data Structure: 2D Matrix (In-Place Marker Trick)

        ROWS, COLS = len(matrix), len(matrix[0])
        rowZero = False  # tracks whether the FIRST row itself needs to become all zeros
                          # (handled separately since row 0 doubles as a marker row)

        # Phase 1: use the first row and first column as "marker" storage
        # to record which rows/columns contain a zero, without extra space
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0  # mark this column as needing zeros

                    if r > 0:
                        matrix[r][0] = 0  # mark this row as needing zeros
                    else:
                        # this zero IS in row 0 — can't use matrix[0][0] alone to mark it
                        # (since that cell doubles as both row AND column marker)
                        rowZero = True

        # Phase 2: zero out all cells based on the markers,
        # EXCLUDING row 0 and column 0 (processed separately at the end)
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        # Phase 3: handle column 0 based on matrix[0][0]
        # (this marker was set during phase 1 if column 0 needs zeroing)
        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0

        # Phase 4: handle row 0 separately using the rowZero flag
        # (row 0 couldn't reliably use matrix[0][0] as its own marker)
        if rowZero:
            for c in range(COLS):
                matrix[0][c] = 0

        # Time Complexity:  O(m*n) — a few passes over the matrix
        # Space Complexity: O(1) — uses the matrix itself as marker storage, no extra structures