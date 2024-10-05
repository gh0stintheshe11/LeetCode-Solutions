# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        def in_order_traversal(node):
            nonlocal prev, min_diff
            if not node:
                return
            in_order_traversal(node.left)
            if prev is not None:
                min_diff = min(min_diff, node.val - prev)
            prev = node.val
            in_order_traversal(node.right)
        
        prev = None
        min_diff = float('inf')
        in_order_traversal(root)
        return min_diff