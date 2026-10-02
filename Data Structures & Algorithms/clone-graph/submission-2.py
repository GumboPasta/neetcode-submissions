"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        # track old node and new node
        o_to_n = {}

        start = node
        stk = [start]
        visited = set()
        visited.add(start)

        # if node is empty
        if not node:
            return 

        while stk:
            # pop the node and add to map
            curr = stk.pop()
            o_to_n[curr] = Node(val=curr.val)

            # add the nodes neighbors
            for nei in curr.neighbors:
                # check if we visited the node already
                if nei not in visited:
                    visited.add(curr)
                    stk.append(nei)

        # iterate through each node
        for old_node, new_node in o_to_n.items():
            curr = old_node
            # populate all the neighhbors for the new nodes
            for nei in old_node.neighbors:
                # obtain the new neighbor
                new_nei = o_to_n[nei]
                new_node.neighbors.append(new_nei)

        return o_to_n[start]

