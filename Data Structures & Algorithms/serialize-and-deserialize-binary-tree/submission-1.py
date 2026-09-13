class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        
        res = []

        # helper function: preform preorder traversal via DFS
        def dfs(node):
            # base case: if node is null
            if not node:
                res.append("N")
                return

            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(res)

    def deserialize(self, data: str) -> Optional[TreeNode]:

        vals = data.split(",")
        self.i = 0

        # helpfunction: preform dfs
        def dfs():
            
            # base case: if node is "N"
            if vals[self.i] == "N":
                self.i += 1
                return None

            # create new node
            node = TreeNode(int(vals[self.i]))
            self.i += 1

            # obtain the left and right subtrees
            node.left = dfs()
            node.right = dfs()

            return node

        return dfs()