class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        # Key Data Structure: Grid DFS

        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            # base case — out of bounds or not land, stop exploring
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != '1':
                return
            else:
                grid[i][j] = '0'  # mark as visited (sink the land) to avoid recounting

                # explore all 4 directions
                dfs(i, j+1)   # right
                dfs(i+1, j)   # down
                dfs(i, j-1)   # left
                dfs(i-1, j)   # up

        num_islands = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    num_islands += 1  # found a new island — count it
                    dfs(i, j)          # sink the entire island so it's not counted again

        return num_islands

        # Time Complexity:  O(m * n) — visit every cell at most once
        # Space Complexity: O(m * n) — worst case recursion stack if entire grid is land