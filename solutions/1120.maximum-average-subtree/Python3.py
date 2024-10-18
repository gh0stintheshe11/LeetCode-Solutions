# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        self.max_average = 0.0
        
        def dfs(node):
            if not node:
                return (0, 0)  # (sum, count)
            
            left_sum, left_count = dfs(node.left)
            right_sum, right_count = dfs(node.right)
            
            current_sum = left_sum + right_sum + node.val
            current_count = left_count + right_count + 1
            current_average = current_sum / current_count
            
            self.max_average = max(self.max_average, current_average)
            
            return (current_sum, current_count)
        
        dfs(root)
        return self.max_average