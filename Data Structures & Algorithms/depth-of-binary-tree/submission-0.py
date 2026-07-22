class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        # Key Data Structure: Binary Tree (Recursive DFS)

        if not root:
            return 0  # base case — empty node contributes 0 depth

        left = self.maxDepth(root.left)   # depth of left subtree
        right = self.maxDepth(root.right)  # depth of right subtree

        return 1 + max(left, right)  # current node adds 1, take the deeper subtree

        # Time Complexity:  O(n) — visit every node once
        # Space Complexity: O(n) — recursion stack, O(log n) balanced, O(n) worst case (skewed)