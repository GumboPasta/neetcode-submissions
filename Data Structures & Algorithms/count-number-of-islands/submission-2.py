class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        m, n = len(grid), len(grid[0])
        num_islands = 0
        
        def sink_islands(i, j):
            # base case: if 
            if grid[i][j] == '0':
                return

            # set current cell to water
            grid[i][j] = '0'

            # check neighbors
            for i_off, j_off in [(0,1),(1,0),(0,-1),(-1,0)]:
                row, col = i + i_off, j + j_off
                # if new indexes are inside our grid
                if 0 <= row < m and 0 <= col < n:
                    sink_islands(row, col)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    # found a island, now sink it 
                    num_islands += 1
                    sink_islands(i, j)

        return num_islands






