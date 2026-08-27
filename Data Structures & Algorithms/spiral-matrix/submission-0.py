class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        # Key Data Structure: 2D Matrix (Boundary Tracking)

        m, n = len(matrix), len(matrix[0])
        ans = []
        i, j = 0, 0  # current position in the matrix

        UP, DOWN, RIGHT, LEFT = 0, 1, 2, 3
        direction = RIGHT  # spiral always starts by moving right

        # boundaries — shrink inward every time a full side is traversed
        UP_WALL = 0       # topmost row not yet fully visited
        RIGHT_WALL = n    # rightmost column boundary (exclusive)
        DOWN_WALL = m     # bottommost row boundary (exclusive)
        LEFT_WALL = -1    # leftmost column not yet fully visited

        while len(ans) != m * n:  # keep going until every cell has been collected

            if direction == RIGHT:
                while j < RIGHT_WALL:
                    ans.append(matrix[i][j])
                    j += 1
                i, j = i + 1, j - 1   # step down one row, back up one column (undo overshoot)
                RIGHT_WALL -= 1        # this row is done — shrink the right boundary
                direction = DOWN       # turn to go down next

            elif direction == DOWN:
                while i < DOWN_WALL:
                    ans.append(matrix[i][j])
                    i += 1
                i, j = i - 1, j - 1   # step left one column, back up one row (undo overshoot)
                DOWN_WALL -= 1         # this column is done — shrink the bottom boundary
                direction = LEFT       # turn to go left next

            elif direction == LEFT:
                while j > LEFT_WALL:
                    ans.append(matrix[i][j])
                    j -= 1
                i, j = i - 1, j + 1   # step up one row, back up one column (undo overshoot)
                LEFT_WALL += 1         # this row is done — shrink the left boundary
                direction = UP         # turn to go up next

            else:  # direction == UP
                while i > UP_WALL:
                    ans.append(matrix[i][j])
                    i -= 1
                i, j = i + 1, j + 1   # step right one column, back up one row (undo overshoot)
                UP_WALL += 1           # this column is done — shrink the top boundary
                direction = RIGHT      # turn to go right next

        return ans

        # Time Complexity:  O(m*n) — every cell visited exactly once
        # Space Complexity: O(1) — excluding the output array