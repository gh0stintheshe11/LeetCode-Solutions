# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def flip(node):
            if not node or not node.left:
                return node
            newRoot = flip(node.left)
            node.left.left = node.right
            node.left.right = node
            node.left = None
            node.right = None
            return newRoot
        
        return flip(root)