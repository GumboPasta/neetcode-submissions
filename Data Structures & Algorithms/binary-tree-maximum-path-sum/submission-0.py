class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        # Key Data Structure: Binary Tree (Recursive DFS)

        res = root.val  # tracks the global maximum path sum seen so far

        def dfs(node):
            nonlocal res

            if not node:
                return 0  # null node contributes 0 to any path

            leftMax = dfs(node.left)    # max gain from left subtree
            rightMax = dfs(node.right)  # max gain from right subtree

            # if a subtree gives negative gain, ignore it (take 0 instead)
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            # a path through the current node can use BOTH left and right
            # update global max — this path can't be extended further up the tree
            res = max(res, node.val + leftMax + rightMax)

            # but when returning to parent, we can only go ONE direction
            # (a path can't split — returning both sides would create a fork)
            return node.val + max(leftMax, rightMax)

        dfs(root)
        return res

        # Time Complexity:  O(n) — visit every node once
        # Space Complexity: O(n) — recursion stack, O(log n) balanced, O(n) worst case skewed