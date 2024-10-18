# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def inorder(node):
            if not node:
                return
            yield from inorder(node.left)
            yield node
            yield from inorder(node.right)
        
        dummy = TreeNode()
        current = dummy
        for node in inorder(root):
            node.left = None
            current.right = node
            current = current.right
        
        return dummy.right