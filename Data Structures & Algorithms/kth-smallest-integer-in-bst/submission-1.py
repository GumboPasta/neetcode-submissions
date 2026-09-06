# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        # track count
        count = k
        ans = 0

        # helper function
        def dfs(node):
            nonlocal count,ans

            # base case: if we fell of the tree
            if not node:
                return

            # traverse to left subtree
            dfs(node.left)

            # we have met our node
            if count == 1:
                ans = node.val

            # decrement count
            count -= 1

            # check right subtree
            if count > 0:
                dfs(node.right)

        dfs(root)
        return ans
