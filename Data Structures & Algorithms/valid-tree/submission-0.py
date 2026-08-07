from collections import defaultdict

class Solution:
    def validTree(self, n, edges):

        # Key Data Structure: Graph (Cycle Detection with DFS)

        if not n:
            return True  # edge case: 0 nodes is trivially a valid tree

        # build adjacency list — undirected, so add both directions per edge
        adj = defaultdict(list)
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visit = set()  # tracks all nodes visited during DFS

        def dfs(i, prev):
            if i in visit:
                return False  # already visited this node — cycle detected!

            visit.add(i)

            for j in adj[i]:
                if j == prev:
                    continue  # skip going back the way we came (not a real cycle)
                if not dfs(j, i):
                    return False  # cycle found deeper — propagate failure up

            return True  # no cycle found through this node's subtree

        # start DFS from node 0:
        #   dfs(0,-1) → True only if no cycles exist
        #   n == len(visit) → True only if every node was reached (fully connected)
        return dfs(0, -1) and n == len(visit)

        # Time Complexity:  O(V + E) — visit every node and edge once
        # Space Complexity: O(V + E) — adjacency list + visited set + recursion stack