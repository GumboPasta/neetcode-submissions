from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        # Key Data Structure: Multi-source BFS

        p_que = deque()   # BFS queue starting from Pacific-touching cells
        p_seen = set()    # cells that can reach the Pacific

        a_que = deque()   # BFS queue starting from Atlantic-touching cells
        a_seen = set()    # cells that can reach the Atlantic

        m, n = len(heights), len(heights[0])

        # Pacific touches the top row and left column
        for j in range(n):
            p_que.append((0, j))       # top row
            p_seen.add((0, j))

        for i in range(1, m):
            p_que.append((i, 0))       # left column (skip row 0, already added)
            p_seen.add((i, 0))

        # Atlantic touches the bottom row and right column
        for i in range(m):
            a_que.append((i, n - 1))   # right column
            a_seen.add((i, n - 1))

        for j in range(n - 1):
            a_que.append((m - 1, j))   # bottom row (skip last col, already added)
            a_seen.add((m - 1, j))

        def get_coords(que, seen):
            # BFS OUTWARD from the ocean, moving to higher or equal ground
            # (water flows downhill, so reversing the flow means going uphill)
            while que:
                i, j = que.popleft()
                for i_off, j_off in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    r, c = i + i_off, j + j_off
                    if (0 <= r < m and 0 <= c < n
                        and heights[r][c] >= heights[i][j]  # can flow from (r,c) down to (i,j)
                        and (r, c) not in seen):
                        seen.add((r, c))
                        que.append((r, c))

        get_coords(p_que, p_seen)  # find every cell that can reach Pacific
        get_coords(a_que, a_seen)  # find every cell that can reach Atlantic

        # cells that can reach BOTH oceans
        return list(p_seen.intersection(a_seen))

        # Time Complexity:  O(m*n) — each cell visited at most once per BFS, two BFS passes
        # Space Complexity: O(m*n) — seen sets + queues store up to all cells