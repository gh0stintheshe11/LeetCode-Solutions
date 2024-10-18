# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional, List

class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        def inorderTraversal(node):
            if not node:
                return []
            stack, result = [], []
            current = node
            while stack or current:
                while current:
                    stack.append(current)
                    current = current.left
                current = stack.pop()
                result.append(current.val)
                current = current.right
            return result
        
        sorted_vals = inorderTraversal(root)
        result = []
        
        for q in queries:
            left = -1
            right = -1
            
            # Finding the largest value in the tree that is smaller than or equal to q
            low, high = 0, len(sorted_vals) - 1
            while low <= high:
                mid = (low + high) // 2
                if sorted_vals[mid] <= q:
                    left = sorted_vals[mid]
                    low = mid + 1
                else:
                    high = mid - 1

            # Finding the smallest value in the tree that is greater than or equal to q
            low, high = 0, len(sorted_vals) - 1
            while low <= high:
                mid = (low + high) // 2
                if sorted_vals[mid] >= q:
                    right = sorted_vals[mid]
                    high = mid - 1
                else:
                    low = mid + 1
            
            result.append([left, right])
        
        return result