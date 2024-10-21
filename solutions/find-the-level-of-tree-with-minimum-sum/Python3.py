# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def minimumLevel(self, root: 'Optional[TreeNode]') -> int:
        if not root:
            return 0
        
        min_sum = float('inf')
        min_level = 0
        level = 1
        queue = deque([root])
        
        while queue:
            level_sum = 0
            num_nodes = len(queue)
            
            for _ in range(num_nodes):
                node = queue.popleft()
                level_sum += node.val
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            if level_sum < min_sum:
                min_sum = level_sum
                min_level = level
            
            level += 1
        
        return min_level