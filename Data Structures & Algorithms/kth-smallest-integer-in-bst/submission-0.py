class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        # Key Data Structure: Binary Search Tree (Inorder DFS)

        count = k   # countdown — decrements each time we visit a node inorder
        ans = 0     # stores the answer once we hit the kth node

        def dfs(node):
            nonlocal count, ans  # allow inner function to update outer variables

            if not node:
                return

            dfs(node.left)  # visit left subtree first (smallest values)

            if count == 1:
                ans = node.val  # this is the kth smallest — record it

            count -= 1
            if count > 0:
                dfs(node.right)  # only recurse right if we haven't found it yet

        dfs(root)
        return ans

        # Time Complexity:  O(h + k) — go down to leftmost node O(h), then k steps inorder
        # Space Complexity: O(h) — recursion stack depth