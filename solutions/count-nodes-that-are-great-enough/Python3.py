# Definition for a binary tree node.
from typing import Optional

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def countGreatEnoughNodes(self, root: Optional[TreeNode], k: int) -> int:
        great_enough_count = 0
        
        def dfs(node):
            nonlocal great_enough_count
            if not node:
                return 0, []
            
            left_size, left_values = dfs(node.left)
            right_size, right_values = dfs(node.right)
            
            subtree_size = left_size + right_size + 1
            subtree_values = left_values + right_values + [node.val]
            subtree_values.sort()
            
            if subtree_size >= k and node.val > subtree_values[k-1]:
                great_enough_count += 1
            
            return subtree_size, subtree_values[:k]
        
        dfs(root)
        return great_enough_count