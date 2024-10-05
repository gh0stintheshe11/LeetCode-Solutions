# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        def dfs(node, parent, depth, target):
            if not node:
                return None
            if node.val == target:
                return (parent, depth)
            left = dfs(node.left, node, depth + 1, target)
            right = dfs(node.right, node, depth + 1, target)
            return left if left else right
        
        x_info = dfs(root, None, 0, x)
        y_info = dfs(root, None, 0, y)
        
        return x_info[0] != y_info[0] and x_info[1] == y_info[1]