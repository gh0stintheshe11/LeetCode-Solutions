# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        def dfs(node, path):
            if not node:
                return
            path.append(chr(node.val + ord('a')))
            if not node.left and not node.right:
                paths.append("".join(reversed(path)))
            dfs(node.left, path)
            dfs(node.right, path)
            path.pop()
            
        paths = []
        dfs(root, [])
        return min(paths)