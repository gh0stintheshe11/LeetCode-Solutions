from collections import deque
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = deque([(root, 1)])
        level_sums = {}
        
        while queue:
            node, level = queue.popleft()
            
            if level not in level_sums:
                level_sums[level] = 0
            level_sums[level] += node.val
            
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
        
        max_level, max_sum = 1, level_sums[1]
        for level in level_sums:
            if level_sums[level] > max_sum:
                max_level = level
                max_sum = level_sums[level]
        
        return max_level