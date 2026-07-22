class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        # Key Data Structure: Binary Tree (Recursive DFS)

        def balanced(p, q):
            # base case: both nodes are null — same empty spot in both trees
            if not p and not q:
                return True

            # one node exists, the other doesn't — structure mismatch
            if (p and not q) or (q and not p):
                return False

            # both nodes exist but have different values
            if p.val != q.val:
                return False

            # values match — recursively check left and right subtrees
            # both must match for the trees to be the same
            return balanced(p.left, q.left) and balanced(p.right, q.right)

        return balanced(p, q)

        # Time Complexity:  O(n) — visit every node pair once
        # Space Complexity: O(n) — recursion stack depth, O(log n) balanced, O(n) worst case skewed