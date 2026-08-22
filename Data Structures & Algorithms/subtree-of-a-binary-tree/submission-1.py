# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        # helper function to determine if its same tree
        def isSameTree(p, q):
            # base case: if root is null
            if not p and not q:
                return True

            # check case: if one node is empty
            if (p and not q) or (q and not p):
                return False

            # check case: if values are not equal
            if p.val != q.val:
                return False
            print(p.val, q.val)
            # keep check left and right subtrees
            return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

        # helper function to preform dfs
        def dfs(root):
            # base case: if root is null
            if not root:
                return False
            
            # check current root node and check if it is the subtrees
            result = isSameTree(root, subRoot)
            if result:
                return True
            # check left and right subtrees
            return dfs(root.left) or dfs(root.right)

        return dfs(root)