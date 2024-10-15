class Solution:
    def flatten(self, root):
        def dfs(node):
            if not node:
                return None
            if not node.left and not node.right:
                return node
            left = dfs(node.left)
            right = dfs(node.right)
            if left:
                left.right = node.right
                node.right = node.left
                node.left = None
            return right if right else left
        dfs(root)