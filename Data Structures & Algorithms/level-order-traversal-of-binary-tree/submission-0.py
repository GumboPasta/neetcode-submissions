from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        # Key Data Structure: Binary Tree (BFS with Queue)

        if root is None:
            return []  # empty tree — no levels to return

        queue = deque()
        queue.append(root)  # seed the queue with the root
        ans = []

        while queue:  # keep processing until all nodes are visited
            level = []
            n = len(queue)  # snapshot how many nodes are on this level
                            # queue will grow as we add children, so we capture size first

            for i in range(n):  # process exactly n nodes — one full level
                node = queue.popleft()
                level.append(node.val)

                # add children for the next level
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)

            ans.append(level)  # finished this level, add to result

        return ans

        # Time Complexity:  O(n) — visit every node exactly once
        # Space Complexity: O(n) — queue holds at most one full level at a time