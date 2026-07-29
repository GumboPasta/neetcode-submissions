class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        # Key Data Structure: Binary Tree + HashMap

        # build hashmap for O(1) inorder index lookup
        inorder_map = {}
        for i, val in enumerate(inorder):
            inorder_map[val] = i

        self.idx = 0  # walks forward through preorder (root → left → right)

        def build(left, right):
            if left > right:
                return None  # no nodes in this range

            # next value in preorder is always the current root
            val = preorder[self.idx]
            root = TreeNode(val)
            self.idx += 1  # advance to next node

            # find root in inorder — left of mid = left subtree, right of mid = right subtree
            mid = inorder_map[val]  # O(1) lookup

            # build left before right — preorder visits left subtree first
            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)

            return root

        return build(0, len(inorder) - 1)

        # Time Complexity:  O(n) — each node processed once, O(1) hashmap lookup
        # Space Complexity: O(n) — hashmap + O(h) recursion stack