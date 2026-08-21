class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        # Key Data Structure: Dynamic Programming (Bottom-Up, 2D Grid)

        # build an m x n grid, all starting at 0
        dp = []
        for _ in range(m):
            dp.append([0] * n)

        dp[0][0] = 1  # starting cell — there's exactly 1 way to "arrive" here (you start here)

        for i in range(m):
            for j in range(n):
                if i == j == 0:
                    continue  # already set the starting cell above, skip recomputing it

                val = 0
                if i > 0:
                    val += dp[i-1][j]  # ways to arrive from directly above
                if j > 0:
                    val += dp[i][j-1]  # ways to arrive from directly to the left

                dp[i][j] = val  # total ways to reach this cell = sum of ways from above + left

        return dp[m-1][n-1]  # bottom-right corner holds the total unique paths

        # Time Complexity:  O(m*n) — visit every cell once
        # Space Complexity: O(m*n) — full 2D grid stored

        # Top-Down DP (Memoization) — alternate approach, kept as reference below
        # memo = {(0,0): 1}
        # def paths(i, j):
        #     if (i, j) in memo:
        #         return memo[(i,j)]           # already computed, return cached result
        #     elif i < 0 or j < 0 or i == m or j == n:
        #         return 0                      # out of bounds — invalid path
        #     else:
        #         val = paths(i, j-1) + paths(i-1, j)  # ways from left + ways from above
        #         memo[(i,j)] = val
        #         return val
        #
        # return paths(m-1, n-1)