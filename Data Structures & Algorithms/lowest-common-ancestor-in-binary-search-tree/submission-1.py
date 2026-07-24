class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        # Key Data Structure: Binary Search Tree (Recursive DFS)

        lca = root  # tracks the current best candidate for LCA

        def search(node):
            nonlocal lca  # tells Python to update the outer lca, not create a new local one

            if not node:
                return  # base case — fell off the tree

            lca = node  # update lca to current node before any decision

            if node is p or node is q:
                # found one of the target nodes — it must be the LCA
                return

            elif node.val < p.val and node.val < q.val:
                # both p and q are greater — both are in the right subtree
                search(node.right)

            elif node.val > p.val and node.val > q.val:
                # both p and q are smaller — both are in the left subtree
                search(node.left)

            else:
                # p and q split here — current node is the LCA
                return

        search(root)
        return lca

        # Time Complexity:  O(h) — h is tree height, O(log n) balanced, O(n) worst case skewed
        # Space Complexity: O(h) — recursion stack depth