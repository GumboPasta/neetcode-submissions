from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        # base case: if root is null
        if not root:
            return []
            
        # intialize our deque, set first value to root
        queue = deque()
        queue.append(root)
        res = []

        # execute until all nodes are processed
        while queue:
            # track each level and number of nodes in queue
            level = []
            n = len(queue)

            # iterate each level
            for i in range(n):
                # pop each node and add to level
                node = queue.popleft()
                level.append(node.val)

                # if node had children
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # add to our res
            res.append(level)

        return res