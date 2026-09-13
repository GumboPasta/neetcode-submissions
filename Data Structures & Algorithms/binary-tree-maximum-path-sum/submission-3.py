class Solution:

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        # default: the root is going to be the default max maxPathSum
        res = root.val

        # helper function: DFS to interate through each TreeNode
        def dfs(node):
            nonlocal res
            # base case: if the node is null
            if not node:
                return 0

            # find max of left and right subtree
            leftMax = dfs(node.left)
            rightMax = dfs(node.right)

            # make sure negative values are disregarded
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)
            # obtain the result of the path through the node
            res = max(res, node.val + leftMax + rightMax)

            # obtain the max of the trees, can only return the one subtree (right or left)
            return node.val + max(leftMax, rightMax)

        dfs(root)
        return res