# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def equalToDescendants(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0, 0
            
            left_sum, left_count = dfs(node.left)
            right_sum, right_count = dfs(node.right)
            
            current_sum = left_sum + right_sum
            current_count = left_count + right_count
            
            if node.val == current_sum:
                current_count += 1
            
            return current_sum + node.val, current_count

        _, count = dfs(root)
        return count