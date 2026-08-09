class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        parent = list(range(n))  # each node starts as its own parent

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]  # path compression
                x = parent[x]
            return x

        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return 0  # already connected, no new merge
            parent[px] = py
            return 1  # merged two components into one

        count = n  # start assuming every node is its own component
        for a, b in edges:
            count -= union(a, b)  # each successful merge reduces count by 1

        return count

        # Time Complexity:  O(E * α(n)) — α is inverse Ackermann, effectively O(1) per operation
        # Space Complexity: O(n) — parent array