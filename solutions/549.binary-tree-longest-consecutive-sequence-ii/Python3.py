# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return (0, 0, 0) # (inc, dec, max_len)
            
            inc, dec, max_len = 1, 1, 1
            
            if node.left:
                left_inc, left_dec, left_len = dfs(node.left)
                if node.val == node.left.val + 1:
                    inc = left_inc + 1
                elif node.val == node.left.val - 1:
                    dec = left_dec + 1
                max_len = max(max_len, left_len)
            
            if node.right:
                right_inc, right_dec, right_len = dfs(node.right)
                if node.val == node.right.val + 1:
                    inc = max(inc, right_inc + 1)
                elif node.val == node.right.val - 1:
                    dec = max(dec, right_dec + 1)
                max_len = max(max_len, right_len)
            
            max_len = max(max_len, inc + dec - 1)
            return (inc, dec, max_len)
        
        return dfs(root)[2]