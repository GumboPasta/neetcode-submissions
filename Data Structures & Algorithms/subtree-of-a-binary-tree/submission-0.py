class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        # Key Data Structure: Binary Tree (Recursive DFS)

        # helper: checks if two trees are identical (same as isSameTree)
        def sameTree(p, q):
            if not p and not q:
                return True           # both null — same empty spot ✓

            if (p and not q) or (q and not p):
                return False          # one null, one not — structure mismatch ✗

            if p.val != q.val:
                return False          # same position but different values ✗

            # values match — check both subtrees must also match
            return sameTree(p.left, q.left) and sameTree(p.right, q.right)

        # helper: DFS through every node in root, checking if subRoot starts there
        def has_substree(root):
            if not root:
                return False          # ran off the tree, subRoot not found here

            if sameTree(root, subRoot):
                return True           # subRoot matches the tree rooted at this node ✓

            # subRoot not here — try left and right subtrees
            # short circuits: if left finds it, right never runs
            return has_substree(root.left) or has_substree(root.right)

        return has_substree(root)

        # Time Complexity:  O(n * m) — for each of n nodes in root, run sameTree which is O(m)
        # Space Complexity: O(n) — recursion stack depth of has_subtree