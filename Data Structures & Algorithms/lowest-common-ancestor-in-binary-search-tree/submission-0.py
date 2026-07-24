class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        # Key Data Structure: Binary Search Tree (Recursive DFS)

        lca = [root]  # store in a list so the inner function can update it (Python closure workaround)

        def search(root):
            if not root:
                return  # base case — fell off the tree

            lca[0] = root  # update lca to current node before any decision

            if root is p or root is q:
                # found one of the target nodes — it must be the LCA
                # (the other node is guaranteed to be in its subtree in a BST)
                return

            elif root.val < p.val and root.val < q.val:
                # both p and q are greater than root — both are in the right subtree
                search(root.right)

            elif root.val > p.val and root.val > q.val:
                # both p and q are less than root — both are in the left subtree
                search(root.left)

            else:
                # p and q are on different sides of root (or one equals root)
                # current root is the split point — it is the LCA
                return

        search(root)
        return lca[0]

        # Time Complexity:  O(h) — h is tree height, O(log n) balanced, O(n) worst case skewed
        # Space Complexity: O(h) — recursion stack depth