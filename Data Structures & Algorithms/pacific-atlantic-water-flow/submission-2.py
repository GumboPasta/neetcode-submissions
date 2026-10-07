from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        pacif_que = deque()
        pacif_visited = set()

        atlant_que = deque()
        atlant_visited = set()

        m, n = len(heights), len(heights[0])

        # start with top row
        for j in range(0, n):
            pacif_que.append((0, j))
            pacif_visited.add((0, j))

        # start with left column (skip (0,0))
        for i in range(1, m):
            pacif_que.append((i, 0))
            pacif_visited.add((i, 0))

        # start with the right column
        for i in range(0, m):
            atlant_que.append((i, n - 1))
            atlant_visited.add((i, n - 1))

        # start with the last row
        for j in range(0, n - 1):
            atlant_que.append((m - 1, j))
            atlant_visited.add((m - 1, j))

        # run bfs function
        def get_coords(que, visited):

            # check while que is still not null
            while que:
                i, j = que.popleft()

                # check the neighbors
                for i_offset, j_offset in [(0,1),(1,0),(0,-1),(-1,0)]:
                    row, col = i + i_offset, j + j_offset
                    # check if neighbor is greater (if greater add, otherwise skip)
                    if (0 <= row < m and 0 <= col < n 
                    and heights[row][col] >= heights[i][j]
                    and (row, col) not in visited):
                        que.append((row, col))
                        visited.add((row, col))

        # call for both pacific and atlantic 
        get_coords(pacif_que, pacif_visited)
        get_coords(atlant_que, atlant_visited)

        # return the intersection
        return list(pacif_visited.intersection(atlant_visited))

