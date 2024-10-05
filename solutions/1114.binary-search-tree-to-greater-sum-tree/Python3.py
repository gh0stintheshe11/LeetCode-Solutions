# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.sum = 0
        
        def reverse_inorder(node):
            if not node:
                return
            
            reverse_inorder(node.right)
            
            self.sum += node.val
            node.val = self.sum
            
            reverse_inorder(node.left)
        
        reverse_inorder(root)
        return root