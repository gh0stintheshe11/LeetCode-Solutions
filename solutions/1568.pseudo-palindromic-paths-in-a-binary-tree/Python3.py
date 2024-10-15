# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        def dfs(node, path):
            if not node:
                return 0
            
            # toggle the bit corresponding to node.val
            path ^= (1 << node.val)
            
            # If it's a leaf, check if the path is pseudo-palindromic
            if not node.left and not node.right:
                # Check if at most one bit is set in path
                # (path & (path - 1)) == 0 if path is a power of two or zero
                return int(path & (path - 1) == 0)
            
            # Continue the DFS
            return dfs(node.left, path) + dfs(node.right, path)
        
        return dfs(root, 0)