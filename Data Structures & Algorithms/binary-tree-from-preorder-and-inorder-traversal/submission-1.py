# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        inorder_map = {}
        n = len(preorder)
        
        # add inorder values in hashmap
        for i, node in enumerate(inorder):
            inorder_map[node] = i

        # track our position in the preorder
        self.index = 0

        # helper function to build the tree
        def buildTree(left, right):

            # base case: if we our out of bounds
            if left > right:
                return None

            # obtain the node
            val = preorder[self.index]
            
            # increment next root
            self.index += 1

            # create the node
            node = TreeNode(int(val))

            # obtain the mid position
            mid = inorder_map[val]

            node.left = buildTree(left, mid - 1)
            node.right = buildTree(mid + 1, right)

            return node

           
        tree = buildTree(0, n - 1)
        return tree

