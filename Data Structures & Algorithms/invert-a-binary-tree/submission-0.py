class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        # Key Data Structure: Binary Tree (Recursive DFS)

        if not root:
            return None  # base case — empty node, nothing to invert

        # swap left and right children at the current node
        root.left, root.right = root.right, root.left

        # recursively invert the left and right subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root  # return the root with all children inverted

        # Time:  O(n) — visit every node exactly once
        # Space: O(n) — recursion stack depth, O(log n) for balanced tree, O(n) worst case (skewed)