class Codec:

    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:

        # Key Data Structure: Binary Tree (Preorder DFS)
        res = []

        def dfs(node):
            if not node:
                res.append("N")   # null marker so we can reconstruct structure later
                return
            res.append(str(node.val))  # record current node first (preorder)
            dfs(node.left)             # then left subtree
            dfs(node.right)            # then right subtree

        dfs(root)
        return ",".join(res)  # join into single string e.g. "1,2,N,N,3,N,N"

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:

        vals = data.split(",")  # split back into list of tokens
        self.i = 0              # global index walks forward through vals (same trick as buildTree)

        def dfs():
            if vals[self.i] == "N":
                self.i += 1     # consume the null marker
                return None     # null node — no children

            node = TreeNode(int(vals[self.i]))  # create node from current token
            self.i += 1                          # advance to next token

            node.left  = dfs()  # reconstruct left subtree
            node.right = dfs()  # reconstruct right subtree
            return node

        return dfs()

        # Time Complexity:  O(n) — visit every node once in both serialize and deserialize
        # Space Complexity: O(n) — res list / vals list store n nodes + O(h) recursion stack