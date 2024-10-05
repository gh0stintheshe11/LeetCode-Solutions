# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        def inorder_traverse(node):
            if not node:
                return []
            return inorder_traverse(node.left) + [node.val] + inorder_traverse(node.right)
        
        nums1 = inorder_traverse(root1)
        nums2 = inorder_traverse(root2)
        
        set_nums2 = set(nums2)
        
        for num in nums1:
            if target - num in set_nums2:
                return True
                
        return False