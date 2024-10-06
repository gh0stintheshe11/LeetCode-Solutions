# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import List, Optional

class Solution:
    def getAllElements(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> List[int]:
        def inorder_traversal(root: Optional[TreeNode]) -> List[int]:
            if not root:
                return []
            return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)
        
        list1 = inorder_traversal(root1)
        list2 = inorder_traversal(root2)
        
        # Merge two sorted lists
        result = []
        i, j = 0, 0
        while i < len(list1) and j < len(list2):
            if list1[i] < list2[j]:
                result.append(list1[i])
                i += 1
            else:
                result.append(list2[j])
                j += 1
        
        while i < len(list1):
            result.append(list1[i])
            i += 1
        
        while j < len(list2):
            result.append(list2[j])
            j += 1
        
        return result