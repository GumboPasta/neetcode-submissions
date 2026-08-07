from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # Key Data Structure: Graph (Cycle Detection with DFS)

        g = defaultdict(list)  # adjacency list: course a → list of prerequisites
        courses = prerequisites
        for a, b in courses:
            g[a].append(b)      # to take course a, must first take course b

        # 3-state tracking for cycle detection
        UNVISITED = 0  # haven't explored this node yet
        VISITING = 1   # currently in the recursion stack (exploring its neighbors)
        VISITED = 2    # fully explored, confirmed no cycle through here
        states = [UNVISITED] * numCourses

        def dfs(node):
            state = states[node]
            if state == VISITED:
                return True    # already confirmed safe, no cycle
            elif state == VISITING:
                return False   # found node already in current path — CYCLE detected!

            states[node] = VISITING  # mark as currently being explored

            for nei in g[node]:
                if not dfs(nei):
                    return False  # cycle found deeper in the graph — propagate failure up

            states[node] = VISITED  # fully explored this node and all its prerequisites safely
            return True

        # check every course — graph might have disconnected components
        for i in range(numCourses):
            if not dfs(i):
                return False  # found a cycle somewhere — impossible to finish all courses

        return True  # no cycles anywhere — all courses can be completed

        # Time Complexity:  O(V + E) — visit every course and every prerequisite edge once
        # Space Complexity: O(V + E) — adjacency list + states array + recursion stack