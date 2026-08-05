class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        # Key Data Structure: Graph DFS (iterative) + HashMap

        if not node:
            return None  # empty graph — nothing to clone

        start = node
        o_to_n = {}       # maps original node → its cloned copy
        stk = [start]      # stack for iterative DFS
        visited = set()    # tracks nodes already discovered (added to stack)
        visited.add(start)

        # Phase 1: discover every node and create a clone (without connecting neighbors yet)
        while stk:
            node = stk.pop()
            o_to_n[node] = Node(val=node.val)  # create clone with same value, empty neighbors

            for nei in node.neighbors:
                if nei not in visited:
                    visited.add(nei)   # mark discovered so we don't re-add to stack
                    stk.append(nei)

        # Phase 2: reconnect all clones with their corresponding neighbor clones
        for old_node, new_node in o_to_n.items():
            for nei in old_node.neighbors:
                new_nei = o_to_n[nei]           # find the clone of this neighbor
                new_node.neighbors.append(new_nei)  # link clone to clone

        return o_to_n[start]  # return the clone of the original starting node

        # Time Complexity:  O(V + E) — visit every node once, every edge once
        # Space Complexity: O(V) — hashmap + visited set store one entry per node