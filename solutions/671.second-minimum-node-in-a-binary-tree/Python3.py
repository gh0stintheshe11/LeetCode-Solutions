# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return set()
            left_vals = dfs(node.left)
            right_vals = dfs(node.right)
            return {node.val} | left_vals | right_vals
        
        if not root:
            return -1
        
        node_values = dfs(root)
        min_val = root.val
        second_min = float('inf')
        
        for val in node_values:
            if min_val < val < second_min:
                second_min = val
        
        return second_min if second_min < float('inf') else -1