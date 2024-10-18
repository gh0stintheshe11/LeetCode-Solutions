# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional, List

class Solution:
    def kthLargestPerfectSubtree(self, root: Optional[TreeNode], k: int) -> int:
        perfect_sizes = []

        # Helper function to determine if a tree is perfect and return its size
        def dfs(node):
            if not node:
                return 0, True  # Empty tree is perfect with size 0
            left_size, left_perfect = dfs(node.left)
            right_size, right_perfect = dfs(node.right)
            if left_perfect and right_perfect and left_size == right_size:
                current_size = left_size + right_size + 1
                perfect_sizes.append(current_size)
                return current_size, True
            return 0, False
        
        dfs(root)
        perfect_sizes.sort(reverse=True)
        
        if len(perfect_sizes) < k:
            return -1
        
        return perfect_sizes[k - 1]