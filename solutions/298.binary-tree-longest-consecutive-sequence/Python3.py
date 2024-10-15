# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        def dfs(node, parent_val, length):
            if not node:
                return length
            
            current_length = length + 1 if node.val == parent_val + 1 else 1
            left_length = dfs(node.left, node.val, current_length)
            right_length = dfs(node.right, node.val, current_length)
            
            return max(current_length, left_length, right_length)
        
        return dfs(root, root.val - 1, 0)