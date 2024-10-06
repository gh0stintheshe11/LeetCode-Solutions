# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional
from collections import deque

class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        q = deque([root])
        level = 0
        
        while q:
            level_size = len(q)
            prev_val = None  # No previous value on this level yet
            
            for _ in range(level_size):
                node = q.popleft()
                
                if (level % 2 == 0 and node.val % 2 == 0) or (level % 2 == 1 and node.val % 2 == 1):
                    return False
                
                if prev_val is not None:
                    if (level % 2 == 0 and node.val <= prev_val) or (level % 2 == 1 and node.val >= prev_val):
                        return False
                
                prev_val = node.val
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            level += 1
        
        return True