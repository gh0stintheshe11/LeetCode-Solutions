# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def dfs(node, parent, grandparent):
            if not node:
                return 0
            sum_val = 0
            if grandparent and grandparent.val % 2 == 0:
                sum_val += node.val
            sum_val += dfs(node.left, node, parent)
            sum_val += dfs(node.right, node, parent)
            return sum_val
        
        return dfs(root, None, None)