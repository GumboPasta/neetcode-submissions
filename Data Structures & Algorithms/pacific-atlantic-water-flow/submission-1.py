from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        pacific_que = deque()
        pacific_seen = set()

        atlantic_que = deque()
        atlantic_seen = set()

        m, n = len(heights), len(heights[0])

        # add each of the borders
        # top row
        for j in range(n):
            pacific_que.append((0, j))
            pacific_seen.add((0, j))

        # left column (skip top left)
        for i in range(1, m):
            pacific_que.append((i, 0))
            pacific_seen.add((i, 0))

        # right column
        for i in range(m):
            atlantic_que.append((i, n - 1))
            atlantic_seen.add((i, n - 1))

        # bottom row (skip bottom right)
        for j in range(0, n - 1):
            atlantic_que.append((m - 1, j))
            atlantic_seen.add((m - 1, j))
 
        # run bfs and check neighbors
        def get_coords(que, visited):
            while que:
                i, j = que.popleft()
                for i_offset, j_offset in [(0,1),(1,0),(0,-1),(-1,0)]:
                    row, col = i + i_offset, j + j_offset
                    # make sure inside borders
                    if (0 <= row < m and 0 <= col < n
                    and heights[row][col] >= heights[i][j] 
                    and (row, col) not in visited):
                        que.append((row, col))
                        visited.add((row, col))


        # check for both pacific and atlantic
        get_coords(pacific_que, pacific_seen)
        get_coords(atlantic_que, atlantic_seen)

        # return the coords that are both present in the pacific and atlantic set
        return list(pacific_seen.intersection(atlantic_seen))
