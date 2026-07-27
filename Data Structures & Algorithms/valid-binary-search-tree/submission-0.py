class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        # Key Data Structure: Binary Tree (Recursive DFS with bounds)

        def is_valid(node, minn, maxx):
            if not node:
                return True  # base case — empty node is valid

            # every node must be strictly within its allowed range (minn, maxx)
            if node.val <= minn or node.val >= maxx:
                return False  # node violates its bounds — not a valid BST

            # recurse into subtrees with updated bounds:
            # left child must be less than current node → update maxx to node.val
            # right child must be greater than current node → update minn to node.val
            return is_valid(node.left, minn, node.val) and is_valid(node.right, node.val, maxx)

        # start with infinite bounds — root can be any value
        return is_valid(root, float('-inf'), float('inf'))

        # Time Complexity:  O(n) — visit every node once
        # Space Complexity: O(n) — recursion stack, O(log n) balanced, O(n) worst case skewed