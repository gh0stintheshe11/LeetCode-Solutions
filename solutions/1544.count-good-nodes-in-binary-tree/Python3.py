# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_so_far):
            if not node:
                return 0
            is_good = node.val >= max_so_far
            max_so_far = max(max_so_far, node.val)
            return (1 if is_good else 0) + dfs(node.left, max_so_far) + dfs(node.right, max_so_far)
        
        return dfs(root, root.val)