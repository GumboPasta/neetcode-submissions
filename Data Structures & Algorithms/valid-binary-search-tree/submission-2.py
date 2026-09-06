# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        # helper function
        def search(node, minn, maxx):

            # base case: we fell of the tree
            if not node:
                return True

            # check if current node obeys our condition
            if node.val <= minn or node.val >= maxx:
                return False

            # check left and right subtrees
            return search(node.left, minn, node.val) and search(node.right, node.val, maxx)

        return search(root, float("-inf"), float("inf"))

