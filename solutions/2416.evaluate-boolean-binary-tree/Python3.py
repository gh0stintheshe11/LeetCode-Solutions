# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if root.val in [0, 1]:
            return root.val == 1
        left_eval = self.evaluateTree(root.left)
        right_eval = self.evaluateTree(root.right)
        if root.val == 2:
            return left_eval or right_eval
        elif root.val == 3:
            return left_eval and right_eval